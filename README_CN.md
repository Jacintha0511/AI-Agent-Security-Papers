# AI Agent 安全论文精选

30 篇经过逐条核验、值得精读的 LLM / RAG / Agent 安全论文。中文解释为主，保留英文题名、术语、会议与原始链接。

[English](README.md) · [中文](README_CN.md)

> Last verified: 2026-09-30. Publication status is recorded separately from preprints. A missing code link means no official public implementation was found during verification.
> 最后核验：2026-09-30。正式发表与预印本严格分开；代码栏为空表示核验时未找到作者公开实现。

## 如何使用

- 想快速入门：先读综述，再读 AgentDojo、ASB、InjecAgent、ToolEmu。
- 想做 RAG/记忆安全：从 PoisonedRAG、AgentPoison、MINJA 开始。
- 想做系统防御：对照阅读 StruQ、SecAlign、CaMeL 和 *The Attacker Moves Second*。
- 想做多 Agent：先读 Prompt Infection，再读 AiTM。
- 机器可读数据在 [`data/papers.json`](data/papers.json)，正则规则在 [`taxonomy/regex_rules.json`](taxonomy/regex_rules.json)。

## 分类总览

| 主分类 | 数量 | 主要问题 |
|---|---:|---|
| [综述与分类](#survey-taxonomy) | 1 | 这个领域包含哪些资产、攻击面和防御？ |
| [综合基准与评测](#benchmark-evaluation) | 3 | 怎样公平地量化 Agent 安全？ |
| [提示注入](#prompt-injection) | 6 | 不可信文本如何劫持目标？ |
| [防御与安全架构](#defense-architecture) | 5 | 怎样从训练或系统结构上限制注入？ |
| [RAG 与记忆安全](#rag-memory-security) | 6 | 知识库和持久记忆如何被污染？ |
| [工具调用与行动安全](#tool-action-security) | 4 | 工具调用怎样造成真实副作用？ |
| [规划、后门与长时程安全](#planning-long-horizon) | 2 | 攻击如何进入规划并跨多轮累积？ |
| [多 Agent 协作安全](#multi-agent-security) | 2 | 恶意内容如何沿通信链传播？ |
| [Agent 进攻能力](#offensive-capability) | 1 | Agent 本身能否成为自动化攻击者？ |

## 分类原则

每篇论文只有一个**主分类**，防止重复计数；同时保留多个标签表达交叉属性。主分类由人工核验，正则只负责给新增条目提出候选分类，因为仅凭标题无法可靠区分“攻击论文”和“防御论文”。详细规则见 [`taxonomy/README.md`](taxonomy/README.md)。

入选标准：问题重要；威胁模型或方法有代表性；有正式会议、公开代码、基准影响力或明确的新攻击面；结论能够从论文/项目页核验。没有把引用量当作唯一标准。

## 综述与分类
<a id="survey-taxonomy"></a>

### 驶过风险区：LLM Agent 安全与隐私威胁综述

- **英文标题**：Navigating the Risks: A Survey of Security and Privacy Threats in LLM-Based Agents
- **论文**：[Navigating the Risks: A Survey of Security and Privacy Threats in LLM-Based Agents](https://doi.org/10.1145/3807666)
- **会议/状态**：ACM Transactions on Software Engineering and Methodology (TOSEM), accepted 2026 · 正式发表
- **代码**：未找到作者公开代码
- **标签**：`survey` · `taxonomy` · `privacy` · `cross-module`
- **为什么入选**：适合作为第一篇阅读：它从威胁来源、影响和 Agent 特性三个角度整理领域，能先建立完整地图，再进入单点攻击。
- **三点核心贡献**：

  1. 提出能覆盖跨模块、跨阶段风险的分类法。
  2. 归纳六类会改变风险暴露面的 Agent 特性。
  3. 用搜索、游戏、导航和软件开发案例连接分类与真实系统。


## 综合基准与评测
<a id="benchmark-evaluation"></a>

### Agent Security Bench：形式化并评测 LLM Agent 的攻击与防御

- **英文标题**：Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents
- **论文**：[Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://openreview.net/forum?id=V4y0CpX4hK)
- **会议/状态**：ICLR 2025 · 正式发表
- **代码**：[GitHub](https://github.com/agiresearch/ASB)
- **标签**：`benchmark` · `prompt-injection` · `memory-poisoning` · `backdoor` · `defense`
- **为什么入选**：它把用户输入、工具观察、记忆和规划放进同一测试框架，适合横向理解 Agent 各模块的攻击面。
- **三点核心贡献**：

  1. 构建覆盖 10 个场景、10 个 Agent 和 400 多个工具的综合基准。
  2. 统一评测提示注入、记忆投毒、Plan-of-Thought 后门和混合攻击。
  3. 在多种 LLM 骨干上比较攻击、防御与正常任务表现。

### AgentHarm：衡量 LLM Agent 有害行为的基准

- **英文标题**：AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents
- **论文**：[AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://openreview.net/forum?id=AC5n7xHuR1)
- **会议/状态**：ICLR 2025 · 正式发表
- **代码**：[GitHub](https://github.com/epfl-nlp/helpful-to-a-fault/tree/main/agentharm)
- **标签**：`benchmark` · `harmful-actions` · `tool-use` · `jailbreak`
- **为什么入选**：它关注 Agent 是否真正通过工具完成有害多步任务，而不是只检查输出里有没有危险文字。
- **三点核心贡献**：

  1. 设计跨多类危害的多步工具调用任务。
  2. 用可执行行为评分，而不是只靠文本分类。
  3. 配套良性任务，区分“安全拒绝”和“根本不会用工具”。

### AgentDojo：动态评测 LLM Agent 提示注入攻击与防御

- **英文标题**：AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents
- **论文**：[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://openreview.net/forum?id=m1YYAQjO3w)
- **会议/状态**：NeurIPS 2024, Datasets and Benchmarks Track · 正式发表
- **代码**：[GitHub](https://github.com/ethz-spylab/agentdojo)
- **标签**：`benchmark` · `indirect-prompt-injection` · `tool-use` · `defense` · `utility`
- **为什么入选**：这是 Agent 提示注入研究中使用最广的动态环境之一，同时测攻击成功和正常任务效用，不会把“什么都拒绝”误当成安全。
- **三点核心贡献**：

  1. 提供可扩展环境，而不是只发布一组固定攻击字符串。
  2. 包含 97 个真实任务和 629 个安全测试用例。
  3. 把攻击目标、正常任务完成度和防御代价分开计量。


## 提示注入
<a id="prompt-injection"></a>

### 攻击者后出手：自适应攻击绕过越狱与提示注入防御

- **英文标题**：The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections
- **论文**：[The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections](https://www.usenix.org/conference/usenixsecurity26/presentation/nasr)
- **会议/状态**：USENIX Security 2026 · 正式发表
- **代码**：未找到作者公开代码
- **标签**：`adaptive-attack` · `prompt-injection` · `jailbreak` · `defense-evaluation`
- **为什么入选**：它提醒读者不要被静态攻击集上的低成功率迷惑：真正的攻击者会针对防御机制调整策略。
- **三点核心贡献**：

  1. 提出以防御为已知条件的自适应评测原则。
  2. 系统扩展梯度、强化学习、随机搜索和人工探索攻击。
  3. 对 12 种近期防御给出高成功率绕过结果，暴露静态评测缺陷。

### 评测大模型面对提示注入时的指令遵循鲁棒性

- **英文标题**：Evaluating the Instruction-Following Robustness of Large Language Models to Prompt Injection
- **论文**：[Evaluating the Instruction-Following Robustness of Large Language Models to Prompt Injection](https://aclanthology.org/2024.emnlp-main.33/)
- **会议/状态**：EMNLP 2024 · 正式发表
- **代码**：[GitHub](https://github.com/Leezekun/instruction-following-robustness-eval)
- **标签**：`prompt-injection` · `instruction-following` · `benchmark`
- **为什么入选**：这篇论文直指核心矛盾：模型越会遵循指令，不代表越能判断哪条指令有权限被遵循。
- **三点核心贡献**：

  1. 建立面向提示注入的指令鲁棒性基准。
  2. 分析模型错误遵循嵌入指令的行为模式。
  3. 揭示上下文理解能力与抗注入能力之间并非简单正相关。

### 提示注入攻击与防御的形式化和基准评测

- **英文标题**：Formalizing and Benchmarking Prompt Injection Attacks and Defenses
- **论文**：[Formalizing and Benchmarking Prompt Injection Attacks and Defenses](https://www.usenix.org/conference/usenixsecurity24/presentation/liu-yupei)
- **会议/状态**：USENIX Security 2024 · 正式发表
- **代码**：[GitHub](https://github.com/liu00222/Open-Prompt-Injection)
- **标签**：`prompt-injection` · `benchmark` · `attack` · `defense`
- **为什么入选**：它给提示注入一个统一定义和实验平台，适合学习如何做公平、可重复的攻防比较。
- **三点核心贡献**：

  1. 建立统一的提示注入形式化框架。
  2. 系统比较 5 种攻击、10 种防御、10 个模型和 7 类任务。
  3. 公开平台，降低后续研究的复现实验成本。

### InjecAgent：工具型 LLM Agent 的间接提示注入基准

- **英文标题**：InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents
- **论文**：[InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](https://aclanthology.org/2024.findings-acl.624/)
- **会议/状态**：Findings of ACL 2024 · 正式发表
- **代码**：[GitHub](https://github.com/uiuc-kang-lab/InjecAgent)
- **标签**：`indirect-prompt-injection` · `tool-use` · `benchmark` · `data-exfiltration`
- **为什么入选**：它专门研究恶意指令藏在工具返回值里的情况，场景与当前邮件、日历、金融类 Agent 很接近。
- **三点核心贡献**：

  1. 构建 1,054 个测试用例，覆盖 17 个用户工具和 62 个攻击者工具。
  2. 把攻击目标分为直接伤害和私密数据外泄。
  3. 系统比较 30 种 LLM Agent 配置的脆弱性。

### 这不是你同意的事：用间接提示注入攻陷真实 LLM 应用

- **英文标题**：Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection
- **论文**：[Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)
- **会议/状态**：arXiv preprint · 预印本
- **代码**：[GitHub](https://github.com/greshake/llm-security)
- **标签**：`indirect-prompt-injection` · `data-exfiltration` · `tool-use` · `real-world`
- **为什么入选**：这是理解间接提示注入的奠基性案例研究：攻击者不直接和 Agent 对话，只需污染它会读取的网页或文档。
- **三点核心贡献**：

  1. 明确提出并演示远程间接提示注入攻击面。
  2. 给出数据窃取、蠕虫传播和 API 操纵等影响分类。
  3. 在真实系统与合成应用上证明攻击链可行。

### 针对 LLM 集成应用的提示注入攻击

- **英文标题**：Prompt Injection Attack against LLM-Integrated Applications
- **论文**：[Prompt Injection Attack against LLM-Integrated Applications](https://arxiv.org/abs/2306.05499)
- **会议/状态**：arXiv preprint · 预印本
- **代码**：[GitHub](https://github.com/LLMSecurity/HouYi)
- **标签**：`direct-prompt-injection` · `black-box` · `real-world` · `prompt-leakage`
- **为什么入选**：HouYi 把提示注入从零散手工技巧推进为可组合的黑盒攻击框架，并在商业应用上做了大规模实测。
- **三点核心贡献**：

  1. 把攻击拆成预构造提示、上下文分隔和恶意载荷三部分。
  2. 在 36 个真实应用上测试，报告 31 个可被攻击。
  3. 展示任意使用模型和窃取应用提示等实际后果。


## 防御与安全架构
<a id="defense-architecture"></a>

### 从系统设计上击败提示注入（CaMeL）

- **英文标题**：Defeating Prompt Injections by Design
- **论文**：[Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813)
- **会议/状态**：arXiv preprint · 预印本
- **代码**：未找到作者公开代码
- **标签**：`defense` · `capability-security` · `information-flow` · `tool-use` · `prompt-injection`
- **为什么入选**：CaMeL 不依赖模型自己识别恶意文本，而是在系统层分离控制流和不可信数据，并限制敏感数据流向。
- **三点核心贡献**：

  1. 用特权模型生成程序控制流，用隔离模型处理不可信数据。
  2. 引入能力机制追踪数据来源并限制外泄。
  3. 在 AgentDojo 上以可证明安全为条件评估任务完成度。

### SecAlign：用偏好优化防御提示注入

- **英文标题**：SecAlign: Defending Against Prompt Injection with Preference Optimization
- **论文**：[SecAlign: Defending Against Prompt Injection with Preference Optimization](https://arxiv.org/abs/2410.05451)
- **会议/状态**：ACM CCS 2025 · 正式发表
- **代码**：[GitHub](https://github.com/facebookresearch/SecAlign)
- **标签**：`defense` · `prompt-injection` · `preference-optimization` · `fine-tuning`
- **为什么入选**：它把安全回答与被注入后回答做成偏好对，让模型不仅学习正确输出，也主动降低错误指令的偏好。
- **三点核心贡献**：

  1. 构造包含注入输入、安全回答和不安全回答的偏好数据。
  2. 用偏好优化直接拉开安全与不安全输出的概率。
  3. 评估多类未见攻击，并同时检查正常任务效用。

### StruQ：用结构化查询防御提示注入

- **英文标题**：StruQ: Defending Against Prompt Injection with Structured Queries
- **论文**：[StruQ: Defending Against Prompt Injection with Structured Queries](https://www.usenix.org/conference/usenixsecurity25/presentation/chen-sizhe)
- **会议/状态**：USENIX Security 2025 · 正式发表
- **代码**：[GitHub](https://github.com/Sizhe-Chen/StruQ)
- **标签**：`defense` · `prompt-injection` · `instruction-data-separation` · `fine-tuning`
- **为什么入选**：StruQ 把“指令”和“数据”从接口到训练过程明确分开，是理解结构化防御的代表工作。
- **三点核心贡献**：

  1. 提出双通道结构化查询接口。
  2. 设计安全前端，避免应用直接拼接指令和数据。
  3. 训练模型只遵循指令通道内容，并评估安全与效用。

### 用 Spotlighting 防御间接提示注入

- **英文标题**：Defending Against Indirect Prompt Injection Attacks With Spotlighting
- **论文**：[Defending Against Indirect Prompt Injection Attacks With Spotlighting](https://arxiv.org/abs/2403.14720)
- **会议/状态**：arXiv preprint · 预印本
- **代码**：未找到作者公开代码
- **标签**：`defense` · `indirect-prompt-injection` · `provenance` · `prompt-engineering`
- **为什么入选**：它是低改造成本的输入来源标记思路，适合与后续训练型、系统型防御比较，但不能把论文中的静态结果当作绝对安全保证。
- **三点核心贡献**：

  1. 提出用输入变换持续标记不可信数据来源。
  2. 给出多种 Spotlighting 具体实现方式。
  3. 同时测攻击成功率与正常 NLP 任务效用。

### 指令层级：训练大模型优先遵循高权限指令

- **英文标题**：The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions
- **论文**：[The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208)
- **会议/状态**：arXiv preprint · 预印本
- **代码**：未找到作者公开代码
- **标签**：`defense` · `instruction-hierarchy` · `prompt-injection` · `training`
- **为什么入选**：它把 system、user、tool 等来源的优先级变成明确训练目标，是当前 Agent 权限语义的重要基础。
- **三点核心贡献**：

  1. 明确提出按来源权限排序的指令层级。
  2. 构造冲突指令数据，训练模型忽略低权限覆盖。
  3. 验证对未见攻击类型也能提升鲁棒性，同时尽量保持通用能力。


## RAG 与记忆安全
<a id="rag-memory-security"></a>

### 藏在记忆里：LLM Agent 的休眠式记忆投毒

- **英文标题**：Hidden in Memory: Sleeper Memory Poisoning in LLM Agents
- **论文**：[Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/abs/2605.15338)
- **会议/状态**：arXiv preprint · 预印本
- **代码**：[GitHub](https://github.com/ivaxi0s/LLM-agent-memory-poisoning)
- **标签**：`memory-poisoning` · `persistent-memory` · `cross-session` · `sleeper-attack`
- **为什么入选**：它把评测扩展到跨会话：恶意内容先休眠在长期记忆里，之后再触发行为或工具动作。
- **三点核心贡献**：

  1. 定义跨会话休眠式记忆投毒威胁。
  2. 逐段测量写入、检索和行为触发的完整攻击链。
  3. 在多种有状态助手上比较模型与攻击目标差异。

### Machine Against the RAG：用阻断文档让 RAG 拒绝服务

- **英文标题**：Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents
- **论文**：[Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents](https://www.usenix.org/conference/usenixsecurity25/presentation/shafran)
- **会议/状态**：USENIX Security 2025 · 正式发表
- **代码**：未找到作者公开代码
- **标签**：`rag` · `denial-of-service` · `black-box` · `retrieval-poisoning`
- **为什么入选**：它研究的不是让 RAG 胡说，而是让系统看似合理地拒答；这种故障更隐蔽，也不容易靠事实核查发现。
- **三点核心贡献**：

  1. 提出针对 RAG 的 jamming 拒绝服务威胁。
  2. 设计无需知道嵌入模型和生成模型的黑盒优化。
  3. 比较指令注入、辅助模型生成和无辅助模型优化三类阻断文档。

### 仅通过查询交互向 LLM Agent 注入恶意记忆（MINJA）

- **英文标题**：Memory Injection Attacks on LLM Agents via Query-Only Interaction
- **论文**：[Memory Injection Attacks on LLM Agents via Query-Only Interaction](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42a97bbd9844d2bf68596730af80bcdf-Abstract-Conference.html)
- **会议/状态**：NeurIPS 2025 · 正式发表
- **代码**：未找到作者公开代码
- **标签**：`memory-poisoning` · `query-only` · `long-term-memory` · `attack`
- **为什么入选**：MINJA 的威胁模型更现实：攻击者没有数据库权限，只通过普通查询就诱导 Agent 自己写入恶意记忆。
- **三点核心贡献**：

  1. 提出 query-only 记忆注入攻击。
  2. 用桥接步骤把攻击查询与未来受害查询关联起来。
  3. 用提示逐步缩短策略提高恶意记忆的隐蔽性和可检索性。

### PoisonedRAG：针对 RAG 的知识腐化攻击

- **英文标题**：PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models
- **论文**：[PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag)
- **会议/状态**：USENIX Security 2025 · 正式发表
- **代码**：[GitHub](https://github.com/sleeepeer/PoisonedRAG)
- **标签**：`rag` · `knowledge-poisoning` · `retrieval` · `attack`
- **为什么入选**：它清楚展示 RAG 知识库本身就是安全边界：少量恶意文档可同时操纵检索与最终回答。
- **三点核心贡献**：

  1. 把 RAG 知识腐化写成可优化的攻击问题。
  2. 分别设计白盒和黑盒条件下的恶意文本生成方法。
  3. 在百万级语料设置中评估攻击，并测试多种现有防御。

### AgentPoison：通过投毒记忆或知识库红队测试 LLM Agent

- **英文标题**：AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases
- **论文**：[AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://arxiv.org/abs/2407.12784)
- **会议/状态**：NeurIPS 2024 · 正式发表
- **代码**：[GitHub](https://github.com/AI-secure/AgentPoison)
- **标签**：`memory-poisoning` · `rag` · `backdoor` · `retrieval`
- **为什么入选**：它把长期记忆和 RAG 知识库视为同类检索入口，说明无需改模型参数也能植入隐蔽后门。
- **三点核心贡献**：

  1. 提出针对通用 Agent 记忆与 RAG 的检索后门攻击。
  2. 通过约束优化让触发词落入独特嵌入区域。
  3. 在自动驾驶、知识问答和医疗 Agent 上测试迁移性与隐蔽性。

### 胶水披萨与吃石头：利用 RAG 模型的知识库漏洞

- **英文标题**：Glue Pizza and Eat Rocks: Exploiting Vulnerabilities in Retrieval-Augmented Generative Models
- **论文**：[Glue Pizza and Eat Rocks: Exploiting Vulnerabilities in Retrieval-Augmented Generative Models](https://aclanthology.org/2024.emnlp-main.96/)
- **会议/状态**：EMNLP 2024 · 正式发表
- **代码**：未找到作者公开代码
- **标签**：`rag` · `knowledge-poisoning` · `black-box` · `misinformation`
- **为什么入选**：它用攻击者不知道用户问题、知识库内容和模型参数的现实黑盒设定，研究公开语料被投毒后的错误建议。
- **三点核心贡献**：

  1. 定义面向开放知识库的现实黑盒投毒威胁。
  2. 构造能被检索并影响生成的欺骗内容。
  3. 分析投毒对事实回答和系统行为的影响。


## 工具调用与行动安全
<a id="tool-action-security"></a>

### 用语言模型模拟沙箱识别 Agent 风险（ToolEmu）

- **英文标题**：Identifying the Risks of LM Agents with an LM-Emulated Sandbox
- **论文**：[Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://openreview.net/forum?id=GEcwtMk1uA)
- **会议/状态**：ICLR 2024 · 正式发表
- **代码**：[GitHub](https://github.com/ryoungj/ToolEmu)
- **标签**：`tool-use` · `sandbox` · `risk-evaluation` · `simulation`
- **为什么入选**：ToolEmu 用模型模拟工具和环境，低成本寻找长尾高危失败，是学习 Agent 安全测试工程的好入口。
- **三点核心贡献**：

  1. 提出用 LM 模拟工具执行结果的可扩展测试框架。
  2. 构建 36 个高风险工具包和 144 个测试用例。
  3. 用人工评估检查模拟器和自动风险判断的真实性。

### R-Judge：评测 LLM 对 Agent 行为风险的识别能力

- **英文标题**：R-Judge: Benchmarking Safety Risk Awareness for LLM Agents
- **论文**：[R-Judge: Benchmarking Safety Risk Awareness for LLM Agents](https://aclanthology.org/2024.findings-emnlp.79/)
- **会议/状态**：Findings of EMNLP 2024 · 正式发表
- **代码**：[GitHub](https://github.com/Lordog/R-Judge)
- **标签**：`risk-detection` · `trajectory` · `benchmark` · `tool-use`
- **为什么入选**：它研究 Agent 执行轨迹已经产生后，模型能否读懂多轮记录并识别风险，适合作为运行时监控研究起点。
- **三点核心贡献**：

  1. 构建 569 条多轮 Agent 交互记录。
  2. 覆盖 5 类应用、27 个场景和 10 种风险。
  3. 把行为风险识别与一般有害文本判断区分开。

### RedCode：代码 Agent 的危险代码执行与生成基准

- **英文标题**：RedCode: Risky Code Execution and Generation Benchmark for Code Agents
- **论文**：[RedCode: Risky Code Execution and Generation Benchmark for Code Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/bfd082c452dffb450d5a5202b0419205-Abstract-Datasets_and_Benchmarks_Track.html)
- **会议/状态**：NeurIPS 2024, Datasets and Benchmarks Track · 正式发表
- **代码**：[GitHub](https://github.com/AI-secure/RedCode)
- **标签**：`code-agent` · `code-execution` · `sandbox` · `benchmark`
- **为什么入选**：对代码 Agent 来说，危险不止是生成恶意文本，而是真正在解释器或 shell 中执行；RedCode 专门测这条边界。
- **三点核心贡献**：

  1. 把危险代码执行和危险代码生成拆成两个子基准。
  2. 在隔离 Docker 环境中用真实执行结果判定风险。
  3. 建立跨系统、网络和程序逻辑等场景的风险分类。

### ToolSword：揭示工具学习三个阶段的安全问题

- **英文标题**：ToolSword: Unveiling Safety Issues of Large Language Models in Tool Learning Across Three Stages
- **论文**：[ToolSword: Unveiling Safety Issues of Large Language Models in Tool Learning Across Three Stages](https://aclanthology.org/2024.acl-long.119/)
- **会议/状态**：ACL 2024 · 正式发表
- **代码**：[GitHub](https://github.com/Junjie-Ye/ToolSword)
- **标签**：`tool-use` · `benchmark` · `input` · `execution` · `output`
- **为什么入选**：它把工具使用安全按输入、执行和输出三阶段拆开，能看清风险不只发生在工具调用前。
- **三点核心贡献**：

  1. 定义覆盖三阶段的六类工具安全场景。
  2. 评测恶意查询、越狱、误导、风险提示、恶意反馈和错误冲突。
  3. 在 11 个开源与闭源模型上系统比较。


## 规划、后门与长时程安全
<a id="planning-long-horizon"></a>

### AgentLAB：评测 LLM Agent 面对长时程攻击的安全性

- **英文标题**：AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks
- **论文**：[AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks](https://proceedings.mlr.press/v306/jiang26as.html)
- **会议/状态**：ICML 2026 · 正式发表
- **代码**：[GitHub](https://github.com/TanqiuJiang/AgentLAB)
- **标签**：`long-horizon` · `benchmark` · `memory-poisoning` · `tool-chaining` · `objective-drift`
- **为什么入选**：它补上单轮测试的盲区，专门研究攻击如何在多轮交互、工具链和持久状态中逐步累积。
- **三点核心贡献**：

  1. 定义意图劫持、工具链、任务注入、目标漂移和记忆投毒五类长时程攻击。
  2. 覆盖 28 个 Agent 环境和 644 个安全测试用例。
  3. 验证单轮防御难以稳定抵挡多轮自适应攻击。

### 小心你的 Agent：LLM Agent 后门威胁研究

- **英文标题**：Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents
- **论文**：[Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Abstract-Conference.html)
- **会议/状态**：NeurIPS 2024 · 正式发表
- **代码**：[GitHub](https://github.com/lancopku/agent-backdoor-attacks)
- **标签**：`backdoor` · `planning` · `reasoning` · `observation` · `tool-use`
- **为什么入选**：它说明 Agent 后门可以只污染中间思考或工具选择，即使最终答案看起来正确，执行过程仍可能已经越权。
- **三点核心贡献**：

  1. 区分 Query、Observation 和 Thought 三类 Agent 后门。
  2. 把攻击结果扩展到中间步骤与工具行为。
  3. 在 ReAct Agent 上分析隐蔽性、有效性和防御。


## 多 Agent 协作安全
<a id="multi-agent-security"></a>

### 通过通信攻击红队测试 LLM 多 Agent 系统

- **英文标题**：Red-Teaming LLM Multi-Agent Systems via Communication Attacks
- **论文**：[Red-Teaming LLM Multi-Agent Systems via Communication Attacks](https://aclanthology.org/2025.findings-acl.349/)
- **会议/状态**：Findings of ACL 2025 · 正式发表
- **代码**：未找到作者公开代码
- **标签**：`multi-agent` · `communication` · `agent-in-the-middle` · `red-team`
- **为什么入选**：AiTM 不需要控制任何单个 Agent，只篡改 Agent 间消息就能影响整个协作流程，是研究通信完整性的代表工作。
- **三点核心贡献**：

  1. 提出 Agent-in-the-Middle 通信攻击。
  2. 用带反思机制的攻击 Agent 生成符合上下文和角色格式的恶意消息。
  3. 跨多种框架、通信结构和应用评测系统级影响。

### Prompt Infection：多 Agent 系统中的 LLM 到 LLM 提示注入

- **英文标题**：Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems
- **论文**：[Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems](https://arxiv.org/abs/2410.07283)
- **会议/状态**：arXiv preprint · 预印本
- **代码**：未找到作者公开代码
- **标签**：`multi-agent` · `prompt-injection` · `self-replication` · `data-exfiltration`
- **为什么入选**：它把单 Agent 注入扩展成会在 Agent 之间复制传播的感染链，突出消息传递本身就是信任边界。
- **三点核心贡献**：

  1. 提出 LLM-to-LLM 自复制提示感染攻击。
  2. 展示数据窃取、诈骗、错误信息和系统扰乱等跨 Agent 后果。
  3. 提出 LLM Tagging，并与现有防护组合测试。


## Agent 进攻能力
<a id="offensive-capability"></a>

### LLM Agent 可以自主攻击网站

- **英文标题**：LLM Agents Can Autonomously Hack Websites
- **论文**：[LLM Agents Can Autonomously Hack Websites](https://arxiv.org/abs/2402.06664)
- **会议/状态**：arXiv preprint · 预印本
- **代码**：未找到作者公开代码
- **标签**：`cybersecurity` · `autonomous-agent` · `web-security` · `offensive-capability`
- **为什么入选**：它从另一个方向刻画风险：不是 Agent 被攻击，而是 Agent 作为低成本攻击者。阅读时要特别注意实验网站、模型版本和工具权限的限制。
- **三点核心贡献**：

  1. 构建具备浏览器与代码工具的自主网络攻击 Agent。
  2. 在沙箱网站上评估多类常见漏洞利用能力。
  3. 比较模型、工具与规划组件对成功率和成本的影响。

## 维护与纠错

欢迎提交 Issue 或 PR。新增论文必须给出可核验的论文页、准确出版状态、作者公开代码（如有）、入选理由和三点核心贡献。详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。
