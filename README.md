# Hong AI Platform — Document RAG POC

## 项目信息
- 客户: Hong (一亩三分地合同制)
- 行业: 新能源硬件制造业
- Milestone 1: Document RAG + 自定义报告生成
- 时间: 最多3个月
- 预算: $20K-200K
- 数据量: 100-200G

## 分工
- 美国(Guilin): 应用层 — RAG系统、AI Agent、数据pipeline、LLM集成
- 中国本地团队: 基础设施 — 服务器、GPU、运维部署

## 技术方案
- LLM: Qwen3.5/2.5 (本地部署)
- Embedding: BGE-M3 (多语言)
- 向量数据库: Milvus
- 文档解析: MinerU(中英) + PaddleOCR(多语言)
- 语言: 先英文，后续支持中/越/泰等5种

## 文档目录
- `docs/` — Hong分享的样本文档
- `analysis/` — 文档分析结果
- `prototype/` — 原型代码

## 状态
- [x] 第一次meeting (2026-03-26)
- [x] 已发邮件要样本数据
- [ ] 收到样本数据
- [ ] 技术方案 + 架构图
- [ ] 原型开发
