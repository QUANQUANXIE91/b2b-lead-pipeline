---
name: b2b-lead-pipeline
description: |
  B2B 外贸客户开发全流程 — 6 Agent 协作 Pipeline。搜索→调研→补全→评分→触达→记忆，适用于任何行业的外贸客户开发。支持多语言、多市场、多渠道。当用户说"找客户"、"开发信"、"外贸获客"、"B2B lead generation"、"客户开发流程"、"cold email"时使用此 skill。
---

# B2B Lead Pipeline — 外贸客户开发全流程

> 6 Agent 协作，5 阶段 Pipeline，适用于任何行业

## 一句话

**输入你的产品关键词 → Agent 自动搜索全球客户 → 深度调研 → 补全联系方式 → 评分分级 → 生成个性化开发信 → 持续优化**

---

## 快速开始

### 最简配置（2 分钟上手）

告诉 Agent 以下信息即可开始：

```
产品: [你的产品，如 LED lighting / solar panel / textile machine]
目标市场: [国家或地区，如 Southeast Asia / Middle East / Africa]
排除市场: [可选，如 India / Pakistan]
客户类型: [如 distributor / wholesaler / importer / contractor]
```

### 运行方式

```
# 方式 1：一句话触发
帮我开发 [产品] 的 [市场] 客户

# 方式 2：完整指令
执行 B2B 客户开发 Pipeline:
产品: LED lighting
目标市场: Nigeria, Kenya, Ghana, UAE
数量: 30 家
排除: India, Pakistan
```

---

## 5 阶段 Pipeline

### Stage 1: 发现（Scout）

多渠道搜索潜在客户线索。

**搜索引擎选择**：
| 市场 | 推荐引擎 | 原因 |
|------|---------|------|
| 非洲/中东/东南亚 | Serper | Google 覆盖好 |
| 欧洲/美洲 | Tavily | LLM 优化结果好 |
| 全球通用 | Brave API | 稳定可靠 |

**搜索策略**：
```
关键词 = 产品词 + 客户类型词 + 国家/地区
示例: "LED bulb distributor Nigeria"
     "textile machine wholesaler Vietnam"
     "solar panel importer Kenya"
```

**多语言关键词**：对非英语市场，同时搜索当地语言：
- 西班牙语市场：distribuidor / mayorista / importador
- 阿拉伯语市场：موزع / تاجر جملة / مستورد
- 葡萄牙语市场：distribuidor / atacadista / importador
- 法语市场：distributeur / grossiste / importateur

**过滤规则（5 层）**：
1. 域名黑名单：社交/电商/内容平台/目录站
2. URL 路径过滤：/blog, /article, /news, /wiki
3. 标题模式过滤：Top N, Best N, list of, wholesale supplier
4. 内容过滤：we have listed, top manufacturers, affiliate
5. 正向信号：排除 IP 地址 URL、超长 URL

**排除规则**：
```python
EXCLUDED_COUNTRIES = []  # 根据业务需要添加，如 ["India", "Pakistan"]
EXCLUDED_INDUSTRIES = [] # 根据业务需要添加，如 ["medical", "vaccine"]
EXCLUDED_PLATFORMS = ["Amazon", "eBay", "Alibaba", "AliExpress", "dropshipping"]
```

### Stage 2: 调研（Researcher）

深度调研每家公司的背景、产品线、购买信号。

**调研维度**：
| 维度 | 内容 | 数据源 |
|------|------|--------|
| 业务类型 | 分销/零售/工程/制造 | 公司网站 |
| 产品线 | 主营产品、品牌代理 | 网站内容 |
| 购买信号 | 扩招/新品/缺货/竞品 | 新闻/社媒 |
| 公司规模 | 员工数/营收/门店数 | LinkedIn/年报 |
| 地理覆盖 | 本地/区域/全国 | 网站/社媒 |

**购买信号检测**：
```python
BUYING_SIGNALS = {
    "expanding": ["expansion", "new branch", "growing", "hiring"],
    "diesel_dependent": ["diesel", "generator", "fuel", "backup power"],
    "grid_unreliable": ["power outage", "load shedding", "blackout"],
    "competitor_gap": ["looking for", "seeking supplier", "importing"],
    "seasonal_need": ["summer", "peak season", "inventory restock"],
}
```

### Stage 3: 补全（Enricher）

补全联系方式：邮箱、电话、联系人、WhatsApp。

**补全策略栈**（按优先级）：
1. **网站联系页** — 抓取 /contact, /about, /team 页面
2. **Hunter.io** — 域名邮箱查找
3. **邮箱格式推断** — {first}@domain, {first}.{last}@domain
4. **LinkedIn 查找** — 公司页 + 决策人搜索
5. **社媒反向查找** — Facebook/Instagram 商业页面

**完整度评分**：
| 字段 | 权重 | 说明 |
|------|------|------|
| 邮箱 | 30% | 有邮箱可发邮件 |
| 电话 | 20% | 有电话可直接联系 |
| 联系人 | 25% | 知道找谁 |
| 网站 | 10% | 有网站可调研 |
| 国家 | 10% | 知道在哪 |
| 社交媒体 | 5% | 多渠道触达 |

### Stage 4: 评分（Qualifier）

100 分制评分，Tier A/B/C 分级。

**评分公式**：
```
总分 = 联系方式(0-25) + 产品相关性(0-25) + 公司规模(0-20) + 决策人(0-15) + 地理优先级(0-15)
```

**Tier 分级**：
| Tier | 分数 | 占比 | 后续动作 |
|------|------|------|---------|
| Tier 1 高价值 | ≥ 75 | 15-20% | 深度背调 + 8封邮件序列 |
| Tier 2 标准 | 50-74 | 40-50% | 标准邮件 + 补全联系方式 |
| Tier 3 存根 | < 50 | 30-40% | 仅入库，后续按需 |

### Stage 5: 触达（Outreacher）

为高价值客户生成个性化开发信。

**四大邮件框架**：

| 框架 | 结构 | 适用场景 |
|------|------|---------|
| **PAS** | Problem → Agitate → Solve | 客户知道有问题但没行动 |
| **BAB** | Before → After → Bridge | 客户没意识到有问题 |
| **AIDA** | Attention → Interest → Desire → Action | 需要强力吸引注意力 |
| **One-Liner** | 观察+结果+软性请求 | 忙碌高管、后续跟进 |

**PAS 示例**：
```
Subject: Quick question about [Company Name]

Hi [Name],

Noticed [Company] doesn't have [specific thing they're missing].

Most [business type] in [area] lose [X customers/dollars] monthly 
because of this — and it compounds.

We built a [solution] for [similar business] that [specific result].

Worth 10 minutes to see how it works?
```

**邮件质量基准**：
| 指标 | 差 | 一般 | 好 | 优秀 |
|------|-----|------|-----|------|
| 打开率 | <30% | 40-50% | 50-65% | 65%+ |
| 回复率 | <2% | 3-5% | 5-8% | 8%+ |
| 正面回复 | <1% | 1-2% | 2-4% | 4%+ |

**跟进序列**：
| 天数 | 渠道 | 内容 |
|------|------|------|
| Day 0 | Email | 首封价值驱动（PAS/BAB） |
| Day 3 | LinkedIn | 建立关系+互动 |
| Day 5 | Email | 分享洞察/案例 |
| Day 10 | Email | 简短个性化触达 |
| Day 14 | Email | 收尾告别邮件 |

---

## 输出格式

### 标准输出字段

| 字段 | 说明 |
|------|------|
| 公司名 | 公司名称 |
| 国家 | 所在国家 |
| 网站 | 公司网站 |
| 主营内容 | 业务描述 |
| 客户类型 | Distributor/Importer/Contractor/... |
| 邮箱 | 联系邮箱 |
| 电话 | 联系电话 |
| WhatsApp | WhatsApp 号码 |
| 联系人 | 决策人姓名 |
| 职位 | 决策人职位 |
| Tier | Tier 1/2/3 |
| 完整度 | ✅ 完整 / ⏳ 待补全 / ⚠️ 部分 |
| 来源 | 数据来源 |
| 备注 | 背调信息 |

---

## 6 Agent 角色定义

| Agent | 角色 | 职责 |
|-------|------|------|
| Scout | 市场猎手 | 多渠道搜索潜在客户 |
| Researcher | 调研专家 | 深度调研公司背景 |
| Enricher | 补全工匠 | 补全联系方式 |
| Qualifier | 评分裁判 | 评估价值、分配 Tier |
| Outreacher | 触达专家 | 生成个性化邮件 |
| Memory | 记忆管家 | 记录经验、持续优化 |

---

## 踩坑记录

### 排除规则同步
修改排除规则后，必须检查所有搜索脚本中的关键词是否同步更新。

### 电话验证
电话正则容易误匹配日期、坐标、版本号。验证逻辑：
- 7-15 位数字
- 排除纯 8 位数字（日期格式）
- 排除多小数点（坐标格式）
- 排除日期格式 YYYY-MM-DD

### 域名健康度
非洲/中东小公司域名 87% DNS 失败。补全前先做 DNS 预检：
```bash
dig +short +time=3 example.com A
```

### 邮件送达率
- 发送域名用二级域名（保护主品牌域名）
- 每天 <50 封/邮箱
- 预热 2+ 周（从 5 封/天开始）
- 配置 SPF/DKIM/DMARC

---

## 工具依赖

| 工具 | 用途 | 免费额度 |
|------|------|---------|
| Serper | Google 搜索 API | 2,500 次/月 |
| Tavily | AI 优化搜索 | 1,000 次/月 |
| Hunter.io | 域名邮箱查找 | 25 次/月 |
| web_extract | 网页内容提取 | 免费 |
| cold-email | 冷邮件生成 | 免费 |

---

## 进阶用法

### 自定义行业关键词

```yaml
# 配置你的产品关键词
product:
  name: "LED Lighting"
  keywords:
    en: ["LED bulb distributor", "LED strip wholesale"]
    es: ["distribuidor LED", "mayorista iluminación LED"]
    ar: ["موزع LED", "تاجر جملة إضاءة"]
  exclude:
    countries: ["India", "Pakistan"]
    industries: ["medical", "vaccine"]
```

### 多产品并行

```
同时帮我开发两个产品线的客户:
1. LED lighting — 目标 Southeast Asia
2. Solar panel — 目标 Middle East
```

### 飞书集成

如果配置了飞书多维表格，Pipeline 结果可自动写入：
```
lark-cli base +record-upsert \
  --base-token <token> \
  --table-id <table_id> \
  --json '{"客户名称":"ABC","国家":"Nigeria","邮箱":"abc@example.com"}'
```

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.0.0 | 2026-06-04 | 初始版本：从 solar-lead-workflow 通用化 |

---

*基于实战经验提炼，适用于任何行业的 B2B 外贸客户开发*
