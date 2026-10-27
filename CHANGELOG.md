# Changelog

## [2.2.0] — 2026-10-26

### Added
- **海关贸易数据管道**（SKILL.md 1.0）：产品词搜索 > 裸 HS 码、`{"orList":[...]}` 字符串结构铁律、国别矩阵批量扫描、同行出口客户反查
- **批量补全工程化**（SKILL.md 3.7）：只填空不覆盖 / 断点续传 progress.jsonl / 死链二次验证 / 宁缺毋假 / nohit 不重试 / 吞吐基准（6 秒/家，命中率 70-90%）
- **回复五分类**（SKILL.md 5.8）：兴趣/补信息/异议/拒绝/无效 → 各自动作；分类自动化、承诺人工
- **抑制名单机制**（SKILL.md 5.9）：已回复客户域名后缀级黑名单，双保险持久化
- **统计双口径**（SKILL.md 5.10）：记录口径 + 去重口径；邮箱 × CRM 月度联合核对流程（噪声过滤）
- `references/mcpc-due-diligence.md`：MCPC 四维背调方法论（市场/客户/产品/用户）
- `templates/email-quality-checklist.md`：80 分质量门禁对照表 + 五个致命模式
- `CHANGELOG.md`：本文件

### Changed
- 仪表盘"首次回复率"目标从 ≥5% 修正为 1-5% 健康区间（对齐冷信行业基准）
- Cron 邮件模板：工作日 25 封/天上限 + 前 8 名深研/其余快研节奏 + 抑制名单过滤
- 踩坑记录 20 → 27 条（新增数据核对与批量任务类 7 条）
- README 实战数据刷新（5,400+ 记录 / 256 国家 / 2.5% 回复率）

## [2.1.0] — 2026-08-05

### Added
- 4 个免费技能整合：account-research / facebook-scraper / market-research-agent / serkaion-due-diligence
- CRM 集成通用化（飞书 lark-cli / Notion / Airtable 三种示例）

## [2.0.0] — 2026-08-05

### Added
- Loop Engineering 自循环引擎（4 大核心 Loop + 安全护栏）
- 搜索语法工具箱、稀疏市场发现、竞品分销商页面挖掘
- KYC 合规门禁、注入防护
- 确定性加权打分 + E1-E4 邮箱分级 + 红旗系统
- P7-B 沉睡客户再激活、P12 客户体量分层触达
- 邮件送达率工程、踩坑记录 100+ 条精选 Top 20

## [1.0.0] — 2026-06-04

### Added
- 初始版本：5 阶段 Pipeline + 6 Agent 协作
