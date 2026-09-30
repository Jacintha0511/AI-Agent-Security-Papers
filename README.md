# AI Agent Security Papers

30 verified, high-value papers on LLM, RAG, and agent security. This English index mirrors the Chinese reading guide.

[English](README.md) · [中文](README_CN.md)

> Last verified: 2026-09-30. Publication status is recorded separately from preprints. A missing code link means no official public implementation was found during verification.


## How to use this repository

- Start with the survey, then AgentDojo, ASB, InjecAgent, and ToolEmu.
- For RAG/memory security, begin with PoisonedRAG, AgentPoison, and MINJA.
- For defenses, compare StruQ, SecAlign, CaMeL, and *The Attacker Moves Second*.
- For multi-agent security, read Prompt Infection before AiTM.
- Machine-readable records live in [`data/papers.json`](data/papers.json); regex rules are in [`taxonomy/regex_rules.json`](taxonomy/regex_rules.json).

## Taxonomy overview

| Primary category | Count | Main question |
|---|---:|---|
| [Survey & Taxonomy](#survey-taxonomy) | 1 | What assets, attack surfaces, and defenses define the field? |
| [Benchmarks & Evaluation](#benchmark-evaluation) | 3 | How should agent security be measured fairly? |
| [Prompt Injection](#prompt-injection) | 6 | How can untrusted text hijack an objective? |
| [Defense Architecture](#defense-architecture) | 5 | How can training or system design constrain injection? |
| [RAG & Memory Security](#rag-memory-security) | 6 | How are corpora and persistent memory poisoned? |
| [Tool & Action Security](#tool-action-security) | 4 | How do tool calls produce real side effects? |
| [Planning & Long-Horizon Security](#planning-long-horizon) | 2 | How do attacks enter plans and accumulate over time? |
| [Multi-Agent Security](#multi-agent-security) | 2 | How does malicious content cross communication boundaries? |
| [Offensive Agent Capability](#offensive-capability) | 1 | Can an agent itself become an automated attacker? |

## Classification principles

Each paper has one **primary category** to prevent double counting, plus multiple cross-cutting tags. Primary categories are human-verified; regex rules only suggest categories for new entries because titles alone cannot reliably distinguish attacks from defenses. See [`taxonomy/README.md`](taxonomy/README.md).

Selection favors important problems, representative threat models or methods, peer-reviewed venues, public artifacts, benchmark influence, or a clearly new attack surface. Citation count alone is not a selection rule.

## Survey & Taxonomy
<a id="survey-taxonomy"></a>

### Navigating the Risks: A Survey of Security and Privacy Threats in LLM-Based Agents

- **Chinese title**：驶过风险区：LLM Agent 安全与隐私威胁综述
- **Paper**：[Navigating the Risks: A Survey of Security and Privacy Threats in LLM-Based Agents](https://doi.org/10.1145/3807666)
- **Venue/status**：ACM Transactions on Software Engineering and Methodology (TOSEM), accepted 2026 · peer-reviewed
- **Code**：No official public code found
- **Tags**：`survey` · `taxonomy` · `privacy` · `cross-module`
- **Why selected**：A strong first read: it maps the field by threat source, impact, and agent feature before the reader dives into individual attacks.
- **Three core contributions**：

  1. Builds a taxonomy that captures cross-module and cross-stage threats.
  2. Distills six agent features that shape security exposure.
  3. Connects the taxonomy to search, gaming, navigation, and software-engineering case studies.


## Benchmarks & Evaluation
<a id="benchmark-evaluation"></a>

### Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents

- **Chinese title**：Agent Security Bench：形式化并评测 LLM Agent 的攻击与防御
- **Paper**：[Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://openreview.net/forum?id=V4y0CpX4hK)
- **Venue/status**：ICLR 2025 · peer-reviewed
- **Code**：[GitHub](https://github.com/agiresearch/ASB)
- **Tags**：`benchmark` · `prompt-injection` · `memory-poisoning` · `backdoor` · `defense`
- **Why selected**：It puts user input, tool observations, memory, and planning into one framework, making cross-module comparison possible.
- **Three core contributions**：

  1. Builds a benchmark spanning 10 scenarios, 10 agents, and more than 400 tools.
  2. Evaluates prompt injection, memory poisoning, Plan-of-Thought backdoors, and mixed attacks in one framework.
  3. Compares attacks, defenses, and benign task performance across multiple LLM backbones.

### AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents

- **Chinese title**：AgentHarm：衡量 LLM Agent 有害行为的基准
- **Paper**：[AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://openreview.net/forum?id=AC5n7xHuR1)
- **Venue/status**：ICLR 2025 · peer-reviewed
- **Code**：[GitHub](https://github.com/epfl-nlp/helpful-to-a-fault/tree/main/agentharm)
- **Tags**：`benchmark` · `harmful-actions` · `tool-use` · `jailbreak`
- **Why selected**：It asks whether agents actually complete harmful multi-step tool tasks, not merely whether their text sounds unsafe.
- **Three core contributions**：

  1. Designs multi-step tool-use tasks across diverse harm categories.
  2. Scores executable behavior rather than relying only on text classification.
  3. Adds benign counterparts to separate safe refusal from lack of agent capability.

### AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

- **Chinese title**：AgentDojo：动态评测 LLM Agent 提示注入攻击与防御
- **Paper**：[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://openreview.net/forum?id=m1YYAQjO3w)
- **Venue/status**：NeurIPS 2024, Datasets and Benchmarks Track · peer-reviewed
- **Code**：[GitHub](https://github.com/ethz-spylab/agentdojo)
- **Tags**：`benchmark` · `indirect-prompt-injection` · `tool-use` · `defense` · `utility`
- **Why selected**：A widely used dynamic environment that measures both attack success and benign utility, so blanket refusal is not mistaken for security.
- **Three core contributions**：

  1. Provides an extensible environment rather than a fixed list of attack strings.
  2. Includes 97 realistic tasks and 629 security test cases.
  3. Separates attacker success, benign task utility, and defense cost.


## Prompt Injection
<a id="prompt-injection"></a>

### The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections

- **Chinese title**：攻击者后出手：自适应攻击绕过越狱与提示注入防御
- **Paper**：[The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections](https://www.usenix.org/conference/usenixsecurity26/presentation/nasr)
- **Venue/status**：USENIX Security 2026 · peer-reviewed
- **Code**：No official public code found
- **Tags**：`adaptive-attack` · `prompt-injection` · `jailbreak` · `defense-evaluation`
- **Why selected**：It warns against trusting low attack rates on static test sets: real attackers adapt to the defense being evaluated.
- **Three core contributions**：

  1. Argues for defense-aware adaptive evaluation.
  2. Scales gradient, reinforcement-learning, random-search, and human-guided attacks.
  3. Bypasses 12 recent defenses at high success rates, exposing weaknesses in static evaluation.

### Evaluating the Instruction-Following Robustness of Large Language Models to Prompt Injection

- **Chinese title**：评测大模型面对提示注入时的指令遵循鲁棒性
- **Paper**：[Evaluating the Instruction-Following Robustness of Large Language Models to Prompt Injection](https://aclanthology.org/2024.emnlp-main.33/)
- **Venue/status**：EMNLP 2024 · peer-reviewed
- **Code**：[GitHub](https://github.com/Leezekun/instruction-following-robustness-eval)
- **Tags**：`prompt-injection` · `instruction-following` · `benchmark`
- **Why selected**：It exposes the central tension: better instruction following does not imply better judgment about which instruction is authorized.
- **Three core contributions**：

  1. Creates a benchmark for instruction robustness under prompt injection.
  2. Analyzes patterns in which models follow embedded instructions incorrectly.
  3. Shows that contextual understanding and injection resistance do not have a simple positive relationship.

### Formalizing and Benchmarking Prompt Injection Attacks and Defenses

- **Chinese title**：提示注入攻击与防御的形式化和基准评测
- **Paper**：[Formalizing and Benchmarking Prompt Injection Attacks and Defenses](https://www.usenix.org/conference/usenixsecurity24/presentation/liu-yupei)
- **Venue/status**：USENIX Security 2024 · peer-reviewed
- **Code**：[GitHub](https://github.com/liu00222/Open-Prompt-Injection)
- **Tags**：`prompt-injection` · `benchmark` · `attack` · `defense`
- **Why selected**：It supplies a common formalization and experiment platform for fair, reproducible comparisons of prompt-injection attacks and defenses.
- **Three core contributions**：

  1. Introduces a unified formal framework for prompt injection.
  2. Compares 5 attacks and 10 defenses across 10 models and 7 tasks.
  3. Releases a platform that lowers the cost of reproducible follow-up work.

### InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents

- **Chinese title**：InjecAgent：工具型 LLM Agent 的间接提示注入基准
- **Paper**：[InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](https://aclanthology.org/2024.findings-acl.624/)
- **Venue/status**：Findings of ACL 2024 · peer-reviewed
- **Code**：[GitHub](https://github.com/uiuc-kang-lab/InjecAgent)
- **Tags**：`indirect-prompt-injection` · `tool-use` · `benchmark` · `data-exfiltration`
- **Why selected**：It focuses on malicious instructions hidden in tool outputs, closely matching modern email, calendar, and finance agents.
- **Three core contributions**：

  1. Builds 1,054 cases across 17 user tools and 62 attacker tools.
  2. Separates attack goals into direct harm and private-data exfiltration.
  3. Compares 30 LLM-agent configurations systematically.

### Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection

- **Chinese title**：这不是你同意的事：用间接提示注入攻陷真实 LLM 应用
- **Paper**：[Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)
- **Venue/status**：arXiv preprint · preprint
- **Code**：[GitHub](https://github.com/greshake/llm-security)
- **Tags**：`indirect-prompt-injection` · `data-exfiltration` · `tool-use` · `real-world`
- **Why selected**：A foundational case study of indirect prompt injection: the attacker poisons content the agent will read instead of chatting with it directly.
- **Three core contributions**：

  1. Defines and demonstrates the remote indirect-prompt-injection surface.
  2. Taxonomizes impacts including data theft, worming, and API manipulation.
  3. Shows practical attack chains on real and synthetic applications.

### Prompt Injection Attack against LLM-Integrated Applications

- **Chinese title**：针对 LLM 集成应用的提示注入攻击
- **Paper**：[Prompt Injection Attack against LLM-Integrated Applications](https://arxiv.org/abs/2306.05499)
- **Venue/status**：arXiv preprint · preprint
- **Code**：[GitHub](https://github.com/LLMSecurity/HouYi)
- **Tags**：`direct-prompt-injection` · `black-box` · `real-world` · `prompt-leakage`
- **Why selected**：HouYi turns ad-hoc prompt injection into a composable black-box attack framework and evaluates it on commercial applications.
- **Three core contributions**：

  1. Decomposes attacks into a framework prompt, context separator, and malicious payload.
  2. Tests 36 real applications and reports 31 as vulnerable.
  3. Demonstrates practical outcomes such as unauthorized model use and prompt theft.


## Defense Architecture
<a id="defense-architecture"></a>

### Defeating Prompt Injections by Design

- **Chinese title**：从系统设计上击败提示注入（CaMeL）
- **Paper**：[Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813)
- **Venue/status**：arXiv preprint · preprint
- **Code**：No official public code found
- **Tags**：`defense` · `capability-security` · `information-flow` · `tool-use` · `prompt-injection`
- **Why selected**：CaMeL does not ask the model to recognize malicious text; it separates control from untrusted data and constrains sensitive flows at the system layer.
- **Three core contributions**：

  1. Uses a privileged model for control flow and a quarantined model for untrusted data.
  2. Tracks provenance with capabilities to restrict exfiltration.
  3. Evaluates task completion with provable security conditions on AgentDojo.

### SecAlign: Defending Against Prompt Injection with Preference Optimization

- **Chinese title**：SecAlign：用偏好优化防御提示注入
- **Paper**：[SecAlign: Defending Against Prompt Injection with Preference Optimization](https://arxiv.org/abs/2410.05451)
- **Venue/status**：ACM CCS 2025 · peer-reviewed
- **Code**：[GitHub](https://github.com/facebookresearch/SecAlign)
- **Tags**：`defense` · `prompt-injection` · `preference-optimization` · `fine-tuning`
- **Why selected**：It trains on preferred secure outputs and dispreferred injected outputs, teaching the model both what to do and what not to follow.
- **Three core contributions**：

  1. Builds preference data with injected inputs, secure outputs, and insecure outputs.
  2. Uses preference optimization to separate secure and injected behavior.
  3. Evaluates unseen attacks while monitoring benign utility.

### StruQ: Defending Against Prompt Injection with Structured Queries

- **Chinese title**：StruQ：用结构化查询防御提示注入
- **Paper**：[StruQ: Defending Against Prompt Injection with Structured Queries](https://www.usenix.org/conference/usenixsecurity25/presentation/chen-sizhe)
- **Venue/status**：USENIX Security 2025 · peer-reviewed
- **Code**：[GitHub](https://github.com/Sizhe-Chen/StruQ)
- **Tags**：`defense` · `prompt-injection` · `instruction-data-separation` · `fine-tuning`
- **Why selected**：StruQ separates instructions from data at both the interface and training levels, making it a representative structured defense.
- **Three core contributions**：

  1. Introduces a two-channel structured-query interface.
  2. Adds a secure front end instead of raw prompt-data concatenation.
  3. Trains models to follow only the instruction channel and evaluates security and utility.

### Defending Against Indirect Prompt Injection Attacks With Spotlighting

- **Chinese title**：用 Spotlighting 防御间接提示注入
- **Paper**：[Defending Against Indirect Prompt Injection Attacks With Spotlighting](https://arxiv.org/abs/2403.14720)
- **Venue/status**：arXiv preprint · preprint
- **Code**：No official public code found
- **Tags**：`defense` · `indirect-prompt-injection` · `provenance` · `prompt-engineering`
- **Why selected**：A low-cost provenance-marking idea that is useful to compare with training and system defenses, while not treating static results as a security proof.
- **Three core contributions**：

  1. Uses input transformations to continuously mark untrusted provenance.
  2. Presents multiple concrete spotlighting variants.
  3. Measures both attack success and benign NLP utility.

### The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions

- **Chinese title**：指令层级：训练大模型优先遵循高权限指令
- **Paper**：[The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208)
- **Venue/status**：arXiv preprint · preprint
- **Code**：No official public code found
- **Tags**：`defense` · `instruction-hierarchy` · `prompt-injection` · `training`
- **Why selected**：It turns the priority of system, user, and tool instructions into an explicit training objective, foundational for agent authority semantics.
- **Three core contributions**：

  1. Defines an instruction hierarchy ordered by source privilege.
  2. Generates conflicting-instruction data that teaches models to ignore lower-privilege overrides.
  3. Tests generalization to unseen attacks while monitoring general capability.


## RAG & Memory Security
<a id="rag-memory-security"></a>

### Hidden in Memory: Sleeper Memory Poisoning in LLM Agents

- **Chinese title**：藏在记忆里：LLM Agent 的休眠式记忆投毒
- **Paper**：[Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/abs/2605.15338)
- **Venue/status**：arXiv preprint · preprint
- **Code**：[GitHub](https://github.com/ivaxi0s/LLM-agent-memory-poisoning)
- **Tags**：`memory-poisoning` · `persistent-memory` · `cross-session` · `sleeper-attack`
- **Why selected**：It extends evaluation across sessions: malicious content sleeps in persistent memory and activates during later behavior or tool use.
- **Three core contributions**：

  1. Defines cross-session sleeper memory poisoning.
  2. Measures the full chain from write to retrieval to behavioral activation.
  3. Compares models and attack goals across stateful assistants.

### Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents

- **Chinese title**：Machine Against the RAG：用阻断文档让 RAG 拒绝服务
- **Paper**：[Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents](https://www.usenix.org/conference/usenixsecurity25/presentation/shafran)
- **Venue/status**：USENIX Security 2025 · peer-reviewed
- **Code**：No official public code found
- **Tags**：`rag` · `denial-of-service` · `black-box` · `retrieval-poisoning`
- **Why selected**：Instead of forcing false answers, it makes RAG plausibly refuse to answer—a stealthier failure that fact-checking may miss.
- **Three core contributions**：

  1. Defines a jamming denial-of-service threat against RAG.
  2. Develops black-box optimization without knowing the retriever or generator.
  3. Compares instruction injection, oracle-LLM generation, and optimization-only blocker documents.

### Memory Injection Attacks on LLM Agents via Query-Only Interaction

- **Chinese title**：仅通过查询交互向 LLM Agent 注入恶意记忆（MINJA）
- **Paper**：[Memory Injection Attacks on LLM Agents via Query-Only Interaction](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42a97bbd9844d2bf68596730af80bcdf-Abstract-Conference.html)
- **Venue/status**：NeurIPS 2025 · peer-reviewed
- **Code**：No official public code found
- **Tags**：`memory-poisoning` · `query-only` · `long-term-memory` · `attack`
- **Why selected**：MINJA uses a stronger real-world threat model: the attacker has no database access and induces the agent to write malicious memory through normal queries.
- **Three core contributions**：

  1. Introduces query-only memory injection.
  2. Uses bridging steps to connect attacker queries to future victim queries.
  3. Progressively removes explicit cues to improve stealth and later retrieval.

### PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models

- **Chinese title**：PoisonedRAG：针对 RAG 的知识腐化攻击
- **Paper**：[PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag)
- **Venue/status**：USENIX Security 2025 · peer-reviewed
- **Code**：[GitHub](https://github.com/sleeepeer/PoisonedRAG)
- **Tags**：`rag` · `knowledge-poisoning` · `retrieval` · `attack`
- **Why selected**：It shows that the RAG corpus is itself a security boundary: a few malicious documents can manipulate retrieval and final answers.
- **Three core contributions**：

  1. Formulates RAG knowledge corruption as an optimization problem.
  2. Designs malicious-document methods for white-box and black-box settings.
  3. Evaluates attacks at million-document scale and tests existing defenses.

### AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases

- **Chinese title**：AgentPoison：通过投毒记忆或知识库红队测试 LLM Agent
- **Paper**：[AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://arxiv.org/abs/2407.12784)
- **Venue/status**：NeurIPS 2024 · peer-reviewed
- **Code**：[GitHub](https://github.com/AI-secure/AgentPoison)
- **Tags**：`memory-poisoning` · `rag` · `backdoor` · `retrieval`
- **Why selected**：It treats long-term memory and RAG stores as retrieval surfaces where stealthy backdoors can be planted without changing model weights.
- **Three core contributions**：

  1. Introduces retrieval backdoors for generic agent memory and RAG.
  2. Optimizes triggers into distinctive embedding regions.
  3. Tests transferability and stealth across driving, QA, and healthcare agents.

### Glue Pizza and Eat Rocks: Exploiting Vulnerabilities in Retrieval-Augmented Generative Models

- **Chinese title**：胶水披萨与吃石头：利用 RAG 模型的知识库漏洞
- **Paper**：[Glue Pizza and Eat Rocks: Exploiting Vulnerabilities in Retrieval-Augmented Generative Models](https://aclanthology.org/2024.emnlp-main.96/)
- **Venue/status**：EMNLP 2024 · peer-reviewed
- **Code**：No official public code found
- **Tags**：`rag` · `knowledge-poisoning` · `black-box` · `misinformation`
- **Why selected**：It studies public-corpus poisoning under a realistic black-box setting where the attacker lacks queries, corpus contents, and model parameters.
- **Three core contributions**：

  1. Defines a realistic black-box poisoning threat for open knowledge bases.
  2. Constructs deceptive content that is retrieved and influences generation.
  3. Analyzes the effect of poisoning on factual answers and system behavior.


## Tool & Action Security
<a id="tool-action-security"></a>

### Identifying the Risks of LM Agents with an LM-Emulated Sandbox

- **Chinese title**：用语言模型模拟沙箱识别 Agent 风险（ToolEmu）
- **Paper**：[Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://openreview.net/forum?id=GEcwtMk1uA)
- **Venue/status**：ICLR 2024 · peer-reviewed
- **Code**：[GitHub](https://github.com/ryoungj/ToolEmu)
- **Tags**：`tool-use` · `sandbox` · `risk-evaluation` · `simulation`
- **Why selected**：ToolEmu emulates tools and environments with an LM to search for rare high-impact failures at lower engineering cost.
- **Three core contributions**：

  1. Introduces scalable LM-based tool emulation.
  2. Builds 36 high-stakes toolkits and 144 test cases.
  3. Uses human evaluation to validate emulator and risk-evaluator realism.

### R-Judge: Benchmarking Safety Risk Awareness for LLM Agents

- **Chinese title**：R-Judge：评测 LLM 对 Agent 行为风险的识别能力
- **Paper**：[R-Judge: Benchmarking Safety Risk Awareness for LLM Agents](https://aclanthology.org/2024.findings-emnlp.79/)
- **Venue/status**：Findings of EMNLP 2024 · peer-reviewed
- **Code**：[GitHub](https://github.com/Lordog/R-Judge)
- **Tags**：`risk-detection` · `trajectory` · `benchmark` · `tool-use`
- **Why selected**：It tests whether a model can read multi-turn agent traces and recognize risk, a useful starting point for runtime monitoring.
- **Three core contributions**：

  1. Builds 569 multi-turn agent interaction records.
  2. Covers 5 application classes, 27 scenarios, and 10 risk types.
  3. Separates behavioral risk awareness from generic harmful-text detection.

### RedCode: Risky Code Execution and Generation Benchmark for Code Agents

- **Chinese title**：RedCode：代码 Agent 的危险代码执行与生成基准
- **Paper**：[RedCode: Risky Code Execution and Generation Benchmark for Code Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/bfd082c452dffb450d5a5202b0419205-Abstract-Datasets_and_Benchmarks_Track.html)
- **Venue/status**：NeurIPS 2024, Datasets and Benchmarks Track · peer-reviewed
- **Code**：[GitHub](https://github.com/AI-secure/RedCode)
- **Tags**：`code-agent` · `code-execution` · `sandbox` · `benchmark`
- **Why selected**：For code agents, the danger is actual interpreter or shell execution, not merely unsafe text; RedCode evaluates that boundary directly.
- **Three core contributions**：

  1. Separates risky execution from risky code generation.
  2. Scores real execution outcomes inside isolated Docker environments.
  3. Builds a taxonomy spanning system, network, and program-logic risks.

### ToolSword: Unveiling Safety Issues of Large Language Models in Tool Learning Across Three Stages

- **Chinese title**：ToolSword：揭示工具学习三个阶段的安全问题
- **Paper**：[ToolSword: Unveiling Safety Issues of Large Language Models in Tool Learning Across Three Stages](https://aclanthology.org/2024.acl-long.119/)
- **Venue/status**：ACL 2024 · peer-reviewed
- **Code**：[GitHub](https://github.com/Junjie-Ye/ToolSword)
- **Tags**：`tool-use` · `benchmark` · `input` · `execution` · `output`
- **Why selected**：It splits tool-use safety into input, execution, and output stages, showing that risk is not limited to pre-call filtering.
- **Three core contributions**：

  1. Defines six tool-safety scenarios across three stages.
  2. Covers malicious queries, jailbreaks, misdirection, risky cues, harmful feedback, and error conflicts.
  3. Compares 11 open and closed models.


## Planning & Long-Horizon Security
<a id="planning-long-horizon"></a>

### AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks

- **Chinese title**：AgentLAB：评测 LLM Agent 面对长时程攻击的安全性
- **Paper**：[AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks](https://proceedings.mlr.press/v306/jiang26as.html)
- **Venue/status**：ICML 2026 · peer-reviewed
- **Code**：[GitHub](https://github.com/TanqiuJiang/AgentLAB)
- **Tags**：`long-horizon` · `benchmark` · `memory-poisoning` · `tool-chaining` · `objective-drift`
- **Why selected**：It targets the blind spot of single-turn tests by studying attacks that accumulate across turns, tool chains, and persistent state.
- **Three core contributions**：

  1. Defines five long-horizon attacks: intent hijacking, tool chaining, task injection, objective drifting, and memory poisoning.
  2. Covers 28 agent environments and 644 security cases.
  3. Shows that single-turn defenses do not reliably stop adaptive multi-turn attacks.

### Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents

- **Chinese title**：小心你的 Agent：LLM Agent 后门威胁研究
- **Paper**：[Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Abstract-Conference.html)
- **Venue/status**：NeurIPS 2024 · peer-reviewed
- **Code**：[GitHub](https://github.com/lancopku/agent-backdoor-attacks)
- **Tags**：`backdoor` · `planning` · `reasoning` · `observation` · `tool-use`
- **Why selected**：It shows that an agent backdoor can corrupt intermediate reasoning or tool choice even when the final answer looks correct.
- **Three core contributions**：

  1. Separates Query, Observation, and Thought backdoors.
  2. Extends backdoor outcomes to intermediate reasoning and tool behavior.
  3. Studies effectiveness, stealth, and defenses on ReAct agents.


## Multi-Agent Security
<a id="multi-agent-security"></a>

### Red-Teaming LLM Multi-Agent Systems via Communication Attacks

- **Chinese title**：通过通信攻击红队测试 LLM 多 Agent 系统
- **Paper**：[Red-Teaming LLM Multi-Agent Systems via Communication Attacks](https://aclanthology.org/2025.findings-acl.349/)
- **Venue/status**：Findings of ACL 2025 · peer-reviewed
- **Code**：No official public code found
- **Tags**：`multi-agent` · `communication` · `agent-in-the-middle` · `red-team`
- **Why selected**：AiTM compromises collaboration by modifying inter-agent messages without taking over an individual agent, making it central to communication integrity.
- **Three core contributions**：

  1. Introduces Agent-in-the-Middle communication attacks.
  2. Uses a reflective adversarial agent to craft context- and role-compatible messages.
  3. Evaluates system-wide effects across frameworks, topologies, and applications.

### Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems

- **Chinese title**：Prompt Infection：多 Agent 系统中的 LLM 到 LLM 提示注入
- **Paper**：[Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems](https://arxiv.org/abs/2410.07283)
- **Venue/status**：arXiv preprint · preprint
- **Code**：No official public code found
- **Tags**：`multi-agent` · `prompt-injection` · `self-replication` · `data-exfiltration`
- **Why selected**：It turns single-agent injection into a self-replicating chain across agents, showing that message passing is itself a trust boundary.
- **Three core contributions**：

  1. Introduces self-replicating LLM-to-LLM prompt infection.
  2. Demonstrates cross-agent data theft, scams, misinformation, and disruption.
  3. Proposes LLM Tagging and evaluates it with existing safeguards.


## Offensive Agent Capability
<a id="offensive-capability"></a>

### LLM Agents Can Autonomously Hack Websites

- **Chinese title**：LLM Agent 可以自主攻击网站
- **Paper**：[LLM Agents Can Autonomously Hack Websites](https://arxiv.org/abs/2402.06664)
- **Venue/status**：arXiv preprint · preprint
- **Code**：No official public code found
- **Tags**：`cybersecurity` · `autonomous-agent` · `web-security` · `offensive-capability`
- **Why selected**：It studies the opposite risk: agents as low-cost attackers. Its claims must be read alongside limits of the test sites, model versions, and tool permissions.
- **Three core contributions**：

  1. Builds an autonomous web-hacking agent with browser and code tools.
  2. Evaluates exploitation across common vulnerability classes on sandboxed sites.
  3. Compares how models, tools, and planning components affect success and cost.

## Maintenance and corrections

Issues and pull requests are welcome. New entries must include a verifiable paper page, accurate publication status, official code when available, a selection reason, and three core contributions. See [`CONTRIBUTING.md`](CONTRIBUTING.md).
