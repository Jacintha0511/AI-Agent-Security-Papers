# 分类方法 / Classification Method

本仓库使用“一个主分类 + 多个标签”。主分类对应最直接的研究对象，标签描述攻击方式、威胁模型、评测或防御属性。

The repository uses one primary category plus multiple tags. The primary category identifies the main system component; tags retain cross-cutting attack, threat-model, benchmark, and defense attributes.

## 为什么不完全自动分类

标题中出现 `memory` 的论文可能研究攻击、基准或防御；出现 `tool` 也不能说明论文重点是工具选择、执行隔离还是间接注入。因此正则只能生成候选分类，最终结果必须人工阅读摘要、威胁模型和方法后确认。

## 正则优先级

规则位于 [`regex_rules.json`](regex_rules.json)，按以下顺序处理：

1. 综述与分类
2. RAG 与记忆
3. 多 Agent 通信
4. 工具与行动
5. 规划与长时程
6. 防御架构
7. 提示注入
8. 进攻能力
9. 综合基准

更具体的模块规则放在更通用的 `benchmark` 前面，避免所有带 “benchmark” 的标题都落入综合评测。

运行示例：

```bash
python scripts/classify.py "Memory poisoning attack against a tool-using LLM agent"
```

输出是带命中次数和优先级的候选列表，不会直接修改论文数据。
