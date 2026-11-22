#!/usr/bin/env python3
"""
Google Maps Lead Extractor v2.1 (2026-11-22 重写提取核心)
v2.0 的 data-item-* 选择器是臆造的（真实 DOM 不存在），本版改用真实结构：
  - 结果卡: div[role="feed"] 内 a[href*="/maps/place/"]（name=aria-label）
  - 详情面板: button[data-item-id="phone"|"address"] / a[data-item-id="authority"](网站)
反检测: headless=new + 去自动化标记 + 真实 UA。chromedriver 需与 chrome 同大版本（PATH 前置）。

Usage: python3 get_google_maps_leads.py "keyword" "region" [count] [--proxy URL] [-o out.csv|out.json] [--with-email]
"""

import csv
import json
import time
import random
import re
import sys
import argparse

# Maps 详情面板稳定锚点（data-item-id 由 Google 官方渲染，2026 仍有效）
SEL_FEED = 'div[role="feed"]'
SEL_PLACE_LINKS = 'a[href*="/maps/place/"]'
SEL_PHONE = 'button[data-item-id="phone"]'
SEL_ADDR = 'button[data-item-id="address"]'
SEL_WEB = 'a[data-item-id="authority"]'
SEL_RATING = 'div[role="main"] span[role="img"][aria-label*="star"]'
SEL_CAT = 'button[jsaction*="category"]'

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36')


def setup_driver(proxy=None):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service

    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--lang=en-US')
    options.add_argument(f'user-agent={UA}')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')

    driver = webdriver.Chrome(options=options)
    # navigator.webdriver 抹除
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': "Object.defineProperty(navigator,'webdriver',{get:()=>undefined});"})
    return driver


def _find(driver, sel, attr=None):
    try:
        el = driver.find_element('css selector', sel)
        return (el.get_attribute(attr) or '').strip() if attr else el.text.strip()
    except Exception:
        return ''


def _click_place(driver, href):
    """直接导航到 place 页（比点卡片稳，避开遮挡/粘连）"""
    try:
        driver.get(href if href.startswith('http') else 'https://www.google.com' + href)
        time.sleep(random.uniform(2.0, 3.5))
        return True
    except Exception:
        return False


def search_google_maps(driver, keyword, location, max_results=50):
    search_url = f"https://www.google.com/maps/search/{keyword.replace(' ', '+')}+{location.replace(' ', '+')}"
    print(f"🔍 搜索: {search_url}")
    print(f"📊 目标: {max_results} 条\n")

    driver.get(search_url)
    time.sleep(random.uniform(4, 6))

    # 收集 place 链接（滚动 feed 加载更多）
    seen, links = set(), []
    scrolls, max_scrolls = 0, min(max_results // 5 + 5, 30)
    while len(links) < max_results and scrolls < max_scrolls:
        try:
            feed = driver.find_element('css selector', SEL_FEED)
            driver.execute_script("arguments[0].scrollBy(0, 2000)", feed)
        except Exception:
            pass
        time.sleep(random.uniform(1.5, 2.5))
        scrolls += 1
        for a in driver.find_elements('css selector', SEL_PLACE_LINKS):
            name = (a.get_attribute('aria-label') or '').strip()
            href = (a.get_attribute('href') or '').strip()
            if name and href and name not in seen:
                seen.add(name)
                links.append({'name': name, 'href': href})
        if scrolls % 5 == 0:
            print(f"  📊 进度: {len(links)}/{max_results} 链接 (滚动 {scrolls} 次)")

    print(f"🔗 共收集 {len(links)} 个商家链接，逐个进详情…\n")

    results = []
    for item in links[:max_results]:
        if not _click_place(driver, item['href']):
            continue
        info = {
            'name': item['name'],
            'phone': _find(driver, SEL_PHONE, 'aria-label') or _find(driver, SEL_PHONE),
            'address': _find(driver, SEL_ADDR, 'aria-label') or _find(driver, SEL_ADDR),
            'website': _find(driver, SEL_WEB, 'href'),
            'category': _find(driver, SEL_CAT),
            'rating': _find(driver, SEL_RATING, 'aria-label'),
        }
        # aria-label 常是 "Phone: +234…" 形式，剥前缀
        for k, pre in (('phone', 'Phone:'), ('address', 'Address:')):
            if info[k].startswith(pre):
                info[k] = info[k][len(pre):].strip()
        info['email'] = ''
        info['reviews'] = ''
        results.append(info)
        print(f"  ✅ {len(results)}. {info['name'][:50]} | {info['phone'][:20]} | {info['website'][:35]}")
        time.sleep(random.uniform(1.5, 3.0))

    return results


def try_extract_email(driver, website_url):
    if not website_url:
        return ''
    try:
        driver.get(website_url)
        time.sleep(2)
        src = driver.page_source
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', src)
        bad = ('example.com', 'test.com', 'sentry.io', 'wixpress.com', 'schema.org',
               'googleusercontent.com', 'sentry', '.png', '.jpg', '.webp')
        valid = [e for e in emails if not any(x in e.lower() for x in bad)]
        if valid:
            # 域名匹配优先（邮箱域主干含官网域主干）
            host = re.sub(r'https?://(www\.)?', '', website_url).split('/')[0].lower()
            stem = host.replace('www.', '').split('.')[0]
            match = [e for e in valid if stem in e.lower()]
            return (match or valid)[0]
        return ''
    except Exception:
        return ''


def save_results(results, filename):
    if filename.endswith('.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=1)
    else:
        fieldnames = ['name', 'phone', 'address', 'website', 'email', 'rating', 'reviews', 'category']
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
    print(f"\n💾 已保存 {len(results)} 条到 {filename}")


def main():
    parser = argparse.ArgumentParser(description='Google Maps B2B Lead Extractor v2.1')
    parser.add_argument('keyword', help='搜索关键词 (英文)')
    parser.add_argument('region', help='目标地区')
    parser.add_argument('count', nargs='?', type=int, default=50, help='目标数量 (默认50)')
    parser.add_argument('--proxy', help='代理服务器 URL')
    parser.add_argument('-o', '--output', help='输出文件名 (.csv 或 .json)')
    parser.add_argument('--with-email', action='store_true', help='尝试从网站提取邮箱（较慢）')
    args = parser.parse_args()

    if not args.output:
        args.output = f"leads_{args.keyword.replace(' ', '_')[:20]}_{args.region.replace(' ', '_')[:10]}.csv"

    print("=" * 50)
    print("🗺️  Google Maps Lead Extractor v2.1")
    print("=" * 50)
    print(f"关键词: {args.keyword} | 地区: {args.region} | 目标: {args.count}")
    print(f"代理: {args.proxy or '无'} | 提取邮箱: {'是' if args.with_email else '否'}")
    print("=" * 50 + "\n")

    driver = setup_driver(args.proxy)
    try:
        results = search_google_maps(driver, args.keyword, args.region, args.count)

        if args.with_email and results:
            print("\n📧 尝试从网站提取邮箱（域名匹配优先）...")
            for lead in results:
                if lead.get('website'):
                    email = try_extract_email(driver, lead['website'])
                    if email:
                        lead['email'] = email
                        print(f"  ✅ {lead['name'][:40]}: {email}")
                    time.sleep(1)

        save_results(results, args.output)

        n = max(len(results), 1)
        print(f"\n📊 统计: 总计 {len(results)} | 有电话 {sum(1 for r in results if r.get('phone'))} "
              f"| 有网站 {sum(1 for r in results if r.get('website'))} "
              f"| 有邮箱 {sum(1 for r in results if r.get('email'))}")
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
