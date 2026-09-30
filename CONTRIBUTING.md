# Contributing / 参与贡献

欢迎纠错和新增论文。请不要只提交论文标题。

每个新增条目必须提供：

- 准确英文标题与简洁中文标题；
- DOI、会议页面、ACL Anthology、OpenReview、USENIX 或 arXiv 原始链接；
- 明确的出版状态：`peer-reviewed` 或 `preprint`；
- 作者或机构公开的官方代码链接；若没有则留空，不能用第三方复现冒充官方代码；
- 一个主分类和若干标签；
- 中英文入选理由；
- 中英文各三点核心贡献，内容必须能从论文或项目页核验。

提交前运行：

```bash
python scripts/generate.py
python scripts/validate.py
```

不收录只使用 Agent 做安全任务、但不研究 Agent 自身风险的普通应用论文。进攻型 Agent 能力研究除外，因为它直接刻画 Agent 带来的安全外部性。
