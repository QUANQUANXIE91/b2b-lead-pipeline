# B2B Lead Pipeline

> **B2B 外贸客户开发全流程 — 6 Agent 协作 × 4 大 Loop 自循环引擎**
> 从线索发现到成交的完整自动化系统，适用于任何行业的外贸客户开发。

[![version](https://img.shields.io/badge/version-2.1.0-blue)](./SKILL.md)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![pitfalls](https://img.shields.io/badge/pitfalls-100%2B-orange)](./SKILL.md)
[![industry](https://img.shields.io/badge/industry-any-purple)](./SKILL.md)

---

## 这是什么？

一个经过实战验证的 **AI Agent 客户开发技能（Skill）**。把它装进你的 Agent（Claude Code / Cursor / Hermes / 任何支持 SKILL.md 的环境），你的 Agent 就获得了一套完整的 B2B 外贸获客方法论：

```
输入产品关键词 → 自动搜索全球客户 → 深度调研 → 补全联系方式
→ KYC 合规筛查 → 确定性评分 → 个性化开发信 → 自循环跟进
```

**这不是一个理论框架，而是从真实业务中长出来的系统**：3000+ CRM 记录、65+ 国家覆盖、数百封实战开发信、100+ 条踩坑记录沉淀。

---

## 为什么需要它？

B2B 外贸客户开发的痛点：

| 痛点 | 传统做法 | 本 Skill 的做法 |
|------|---------|----------------|
| 找客户靠运气 | 手动 Google，一天找 10 家 | 多引擎并行搜索 + 稀疏市场扫描，一天 50+ 线索 |
| 客户质量参差不齐 | 发完邮件才发现是竞品 | KYC 门禁 + 确定性评分 + 红旗系统前置过滤 |
| 邮件千篇一律 | 模板群发，回复率 <1% | 4 要素个性化 + ≥80 分质量门禁，回复率目标 5%+ |
| 跟进断链 | 发完就忘 | Loop 自循环：无回复自动进培育池，定期再激活 |
| 经验不沉淀 | 同样的坑反复踩 | Memory Agent：每次执行沉淀 Pitfall |

---

## 核心特性

### 🔁 Loop Engineering（自循环引擎）

从"执行一次就结束"升级为**自循环系统**——每个阶段都有"检查→决定是否继续"的反馈闭环：

| Loop | 目标 | 退出条件 |
|------|------|---------|
| Loop 1 线索发现 | 每天 10+ 新线索 | 去重后 ≥10 条 |
| Loop 2 画像补全 | 关键字段 ≥80% 完整 | 完整度 ≥80% |
| Loop 3 触达回复 | 每客户至少 1 次回复 | 收到回复 |
| Loop 4 质量巡检 | Pipeline 健康 + 邮件质量 | 无异常 + 评分 ≥80 |

配套安全护栏：最大迭代次数、Token 预算、无进展检测、人工兜底、状态持久化。

### 🔍 搜索语法工具箱

- 22 个 Google 高级运算符（10 基础 + 12 外贸专用）
- 30+ 国家公司后缀速查（GmbH / S.R.L. / SDN BHD / FZE…）
- 各国公共邮箱后缀库
- 采购角色关键词库（importer / distributor / wholesaler…）
- 多语言关键词策略（西/阿/葡/法/俄语）

### 🛡️ KYC 合规门禁

OFAC + EU + UN 三大制裁名单强制核查，命中即终止。建立商业关系前的不可跳过步骤。

### 🎯 确定性评分

```
score = 邮箱质量×0.40 + 交叉验证×0.25 + 决策人×0.20 + 规模×0.15 - 疑点×0.20
```

- E1-E4 邮箱分级替代主观判断
- 红旗系统：critical 否决 / minor 扣分
- 相同特征必得相同分数，可复现、可审计

### 📧 邮件工程

- 四大框架：PAS / BAB / AIDA / One-Liner
- P12 客户体量分层（小/中/大企业差异化触达）
- P7-B 沉睡客户再激活三策略（≥3 个月无回复专用）
- 送达率工程：域名预热策略、SPF/DKIM/DMARC、签名铁律

### 💎 高价值渠道发现

- **竞品分销商页面挖掘**：竞品已在卖同类产品的分销商 = 预筛选渠道伙伴（实测单页 17 条线索，71% 转化率）
- **稀疏市场扫描**：CRM 饱和后自动转向低覆盖国家

### 🆕 v2.1 新增能力

| 技能 | 功能 | 成本 |
|------|------|------|
| **account-research** | 公司销售情报（招聘信号/新闻/领导层） | 免费 |
| **facebook-scraper** | Facebook 商业页面/群组爬取 | 免费 |
| **market-research-agent** | 结构化市场调研框架 | 免费 |
| **serkaion-due-diligence** | 投资/合作尽调（Go/No-Go） | 免费 |

---

## 快速开始

### 安装

```bash
git clone https://github.com/QUANQUANXIE91/b2b-lead-pipeline.git
# 将 SKILL.md 放入你的 Agent 技能目录
```

### 使用

```
# 一句话触发
帮我开发 LED lighting 的东南亚客户

# 完整指令
执行 B2B 客户开发 Pipeline:
产品: LED lighting
目标市场: Nigeria, Kenya, Ghana, UAE
数量: 30 家
排除: India, Pakistan

# Loop 模式（持续运营推荐）
为客户开发系统配置每日自动循环引擎
```

---

## 系统架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    🔁 循环引擎（每日自动运行）                     │
│                                                                  │
│  08:05 💓 Pipeline 巡检 ──→ 异常? → 生成修复任务                  │
│                                                                  │
│  09:00 ☀️ Loop 1 线索发现 ──→ 达标(≥10条)? → Loop 2              │
│                                                                  │
│  10:00 🔍 Loop 2 画像补全 ──→ 完整度≥80%? → Loop 3               │
│                                                                  │
│  持续  📧 Loop 3 触达回复 ──→ 收到回复? → 成交流程                 │
│                              无回复? → 培育池                     │
└─────────────────────────────────────────────────────────────────┘
```

**6 个 Agent 角色**：Scout（猎手）→ Researcher（调研）→ Enricher（补全）→ Qualifier（评分）→ Outreacher（触达）→ Memory（记忆）

---

## 实战数据

| 指标 | 数据 |
|------|------|
| CRM 记录 | 3000+ 条，覆盖 65+ 国家 |
| 开发信发送 | 数百封，100% 发送成功率 |
| 竞品分销商渠道 | 单页 17 条线索，71% 转化率 |
| Google 邮箱发现 | `"公司名" email contact` 成功率 43%（非洲市场） |
| Hunter.io 补全 | domain-search 命中率 46% |
| 踩坑沉淀 | 100+ 条 Pitfall |

---

## 踩坑记录精选

每条都是真金白银换来的教训：

2. **双签名 bug** — body 含签名 + 脚本追加签名 = 双签名（发生 4+ 次的经典坑）
3. **邮箱 false positive** — 搜到的邮箱可能属于同名不同公司，必须验证域名匹配
4. **CRM 字段索引漂移** — JSON 字段顺序不稳定，必须动态读取
5. **市场饱和信号** — 筛选转化率 <5% 即判定饱和，转向稀疏市场

完整 100+ 条见 [SKILL.md](./SKILL.md)。

---

## 适用场景

✅ 外贸工厂/贸易公司的海外客户开发
✅ 任何行业：太阳能、制冷、机械、纺织、电子、建材……
✅ 需要批量获客 + 个性化触达的 B2B 销售团队
✅ 想把客户开发从"人工驱动"升级为"系统自循环"的团队

❌ 不适合：B2C 零售、一次性项目、不愿意配置 CRM 的场景

---

## 工具链（免费优先）

| 工具 | 用途 | 成本 |
|------|------|------|
| web_search 多引擎 | 线索搜索 | 免费额度 |
| Crawl4AI | LLM 友好深度爬虫 | 开源免费 |
| Firecrawl CLI | 搜索+抓取一体 | 免费额度 |
| Jina Reader | LinkedIn 公开资料读取 | 免费 |
| Hunter.io | 邮箱查找 | 25 次/月免费 |
| account-research | 公司销售情报 | 免费 |
| facebook-scraper | Facebook 爬取 | 免费 |
| market-research-agent | 市场调研 | 免费 |
| serkaion-due-diligence | 尽调框架 | 免费 |
| Serper / Tavily | 搜索 API（可选） | 免费额度 |

---

## v2.1 更新

**新增 4 个免费技能：**

- 🔍 **account-research** — 公司销售情报（Anthropic 出品，纯 web search）
- 📘 **facebook-scraper** — Facebook 商业页面/群组爬取（反检测）
- 📊 **market-research-agent** — 结构化市场调研框架
- 📋 **serkaion-due-diligence** — 投资/合作尽调（Go/No-Go）

**其他改进：**
- CRM 集成通用化（飞书/Notion/Airtable 示例）
- 内容优化，更易理解

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| **2.1.0** | 2026-08-05 | 新增 4 个免费技能 + CRM 通用化 |
| **2.0.0** | 2026-08-05 | Loop Engineering + 搜索语法工具箱 + KYC + 确定性评分 + 100+ 踩坑 |
| 1.0.0 | 2026-06-04 | 初始版本 |

---

## 贡献

欢迎提 Issue 和 PR：
- 新的踩坑记录（Pitfall）
- 新的搜索语法/渠道
- 新的行业适配经验

## License

MIT

---

*"Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead."*
