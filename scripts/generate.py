#!/usr/bin/env python3
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data" / "papers.json").read_text(encoding="utf-8"))

CATEGORIES = {
    "survey-taxonomy": ("Survey & Taxonomy", "综述与分类"),
    "benchmark-evaluation": ("Benchmarks & Evaluation", "综合基准与评测"),
    "prompt-injection": ("Prompt Injection", "提示注入"),
    "defense-architecture": ("Defense Architecture", "防御与安全架构"),
    "rag-memory-security": ("RAG & Memory Security", "RAG 与记忆安全"),
    "tool-action-security": ("Tool & Action Security", "工具调用与行动安全"),
    "planning-long-horizon": ("Planning & Long-Horizon Security", "规划、后门与长时程安全"),
    "multi-agent-security": ("Multi-Agent Security", "多 Agent 协作安全"),
    "offensive-capability": ("Offensive Agent Capability", "Agent 进攻能力"),
}

ORDER = list(CATEGORIES)


def badge(status: str, zh: bool) -> str:
    if status == "peer-reviewed":
        return "正式发表" if zh else "peer-reviewed"
    return "预印本" if zh else "preprint"


def card(p: dict, zh: bool) -> str:
    title = p["title_zh"] if zh else p["title"]
    why = p["why_zh"] if zh else p["why_en"]
    contributions = p["contributions_zh"] if zh else p["contributions_en"]
    code = f"[GitHub]({p['code_url']})" if p["code_url"] else ("未找到作者公开代码" if zh else "No official public code found")
    labels = " · ".join(f"`{x}`" for x in p["tags"])
    out = [
        f"### {title}",
        "",
        f"- **{'英文标题' if zh else 'Chinese title'}**：{p['title'] if zh else p['title_zh']}",
        f"- **{'论文' if zh else 'Paper'}**：[{p['title']}]({p['paper_url']})",
        f"- **{'会议/状态' if zh else 'Venue/status'}**：{p['venue']} · {badge(p['status'], zh)}",
        f"- **{'代码' if zh else 'Code'}**：{code}",
        f"- **{'标签' if zh else 'Tags'}**：{labels}",
        f"- **{'为什么入选' if zh else 'Why selected'}**：{why}",
        f"- **{'三点核心贡献' if zh else 'Three core contributions'}**：",
        "",
    ]
    out.extend(f"  {i}. {v}" for i, v in enumerate(contributions, 1))
    out.append("")
    return "\n".join(out)


def render(zh: bool) -> str:
    counts = Counter(p["category"] for p in DATA)
    title = "AI Agent 安全论文精选" if zh else "AI Agent Security Papers"
    subtitle = (
        "30 篇经过逐条核验、值得精读的 LLM / RAG / Agent 安全论文。中文解释为主，保留英文题名、术语、会议与原始链接。"
        if zh else
        "30 verified, high-value papers on LLM, RAG, and agent security. This English index mirrors the Chinese reading guide."
    )
    lines = [
        f"# {title}", "", subtitle, "",
        "[English](README.md) · [中文](README_CN.md)", "",
        "> Last verified: 2026-09-30. Publication status is recorded separately from preprints. A missing code link means no official public implementation was found during verification.", "" if not zh else "> 最后核验：2026-09-30。正式发表与预印本严格分开；代码栏为空表示核验时未找到作者公开实现。", "",
        "## " + ("如何使用" if zh else "How to use this repository"), "",
    ]
    if zh:
        lines += [
            "- 想快速入门：先读综述，再读 AgentDojo、ASB、InjecAgent、ToolEmu。",
            "- 想做 RAG/记忆安全：从 PoisonedRAG、AgentPoison、MINJA 开始。",
            "- 想做系统防御：对照阅读 StruQ、SecAlign、CaMeL 和 *The Attacker Moves Second*。",
            "- 想做多 Agent：先读 Prompt Infection，再读 AiTM。",
            "- 机器可读数据在 [`data/papers.json`](data/papers.json)，正则规则在 [`taxonomy/regex_rules.json`](taxonomy/regex_rules.json)。",
        ]
    else:
        lines += [
            "- Start with the survey, then AgentDojo, ASB, InjecAgent, and ToolEmu.",
            "- For RAG/memory security, begin with PoisonedRAG, AgentPoison, and MINJA.",
            "- For defenses, compare StruQ, SecAlign, CaMeL, and *The Attacker Moves Second*.",
            "- For multi-agent security, read Prompt Infection before AiTM.",
            "- Machine-readable records live in [`data/papers.json`](data/papers.json); regex rules are in [`taxonomy/regex_rules.json`](taxonomy/regex_rules.json).",
        ]
    lines += ["", "## " + ("分类总览" if zh else "Taxonomy overview"), "", "| " + ("主分类 | 数量 | 主要问题" if zh else "Primary category | Count | Main question") + " |", "|---|---:|---|"]
    descriptions_zh = {
        "survey-taxonomy":"这个领域包含哪些资产、攻击面和防御？", "benchmark-evaluation":"怎样公平地量化 Agent 安全？", "prompt-injection":"不可信文本如何劫持目标？", "defense-architecture":"怎样从训练或系统结构上限制注入？", "rag-memory-security":"知识库和持久记忆如何被污染？", "tool-action-security":"工具调用怎样造成真实副作用？", "planning-long-horizon":"攻击如何进入规划并跨多轮累积？", "multi-agent-security":"恶意内容如何沿通信链传播？", "offensive-capability":"Agent 本身能否成为自动化攻击者？"
    }
    descriptions_en = {
        "survey-taxonomy":"What assets, attack surfaces, and defenses define the field?", "benchmark-evaluation":"How should agent security be measured fairly?", "prompt-injection":"How can untrusted text hijack an objective?", "defense-architecture":"How can training or system design constrain injection?", "rag-memory-security":"How are corpora and persistent memory poisoned?", "tool-action-security":"How do tool calls produce real side effects?", "planning-long-horizon":"How do attacks enter plans and accumulate over time?", "multi-agent-security":"How does malicious content cross communication boundaries?", "offensive-capability":"Can an agent itself become an automated attacker?"
    }
    for cat in ORDER:
        name = CATEGORIES[cat][1 if zh else 0]
        desc = (descriptions_zh if zh else descriptions_en)[cat]
        lines.append(f"| [{name}](#{cat}) | {counts[cat]} | {desc} |")
    lines += ["", "## " + ("分类原则" if zh else "Classification principles"), ""]
    if zh:
        lines += [
            "每篇论文只有一个**主分类**，防止重复计数；同时保留多个标签表达交叉属性。主分类由人工核验，正则只负责给新增条目提出候选分类，因为仅凭标题无法可靠区分“攻击论文”和“防御论文”。详细规则见 [`taxonomy/README.md`](taxonomy/README.md)。",
            "",
            "入选标准：问题重要；威胁模型或方法有代表性；有正式会议、公开代码、基准影响力或明确的新攻击面；结论能够从论文/项目页核验。没有把引用量当作唯一标准。",
        ]
    else:
        lines += [
            "Each paper has one **primary category** to prevent double counting, plus multiple cross-cutting tags. Primary categories are human-verified; regex rules only suggest categories for new entries because titles alone cannot reliably distinguish attacks from defenses. See [`taxonomy/README.md`](taxonomy/README.md).",
            "",
            "Selection favors important problems, representative threat models or methods, peer-reviewed venues, public artifacts, benchmark influence, or a clearly new attack surface. Citation count alone is not a selection rule.",
        ]
    grouped = defaultdict(list)
    for p in DATA:
        grouped[p["category"]].append(p)
    for cat in ORDER:
        lines += ["", f"## {CATEGORIES[cat][1 if zh else 0]}", f"<a id=\"{cat}\"></a>", ""]
        for p in sorted(grouped[cat], key=lambda x: (-x["year"], x["title"])):
            lines.append(card(p, zh))
    lines += ["## " + ("维护与纠错" if zh else "Maintenance and corrections"), ""]
    if zh:
        lines += ["欢迎提交 Issue 或 PR。新增论文必须给出可核验的论文页、准确出版状态、作者公开代码（如有）、入选理由和三点核心贡献。详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。", ""]
    else:
        lines += ["Issues and pull requests are welcome. New entries must include a verifiable paper page, accurate publication status, official code when available, a selection reason, and three core contributions. See [`CONTRIBUTING.md`](CONTRIBUTING.md).", ""]
    return "\n".join(lines)


def write_csv() -> None:
    fields = ["id", "title", "title_zh", "year", "venue", "status", "category", "tags", "paper_url", "code_url", "why_zh", "why_en"]
    with (ROOT / "data" / "papers.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for p in DATA:
            row = {k: p.get(k, "") for k in fields}
            row["tags"] = ";".join(p["tags"])
            writer.writerow(row)


if __name__ == "__main__":
    (ROOT / "README.md").write_text(render(False), encoding="utf-8")
    (ROOT / "README_CN.md").write_text(render(True), encoding="utf-8")
    write_csv()
    print(f"Generated bilingual READMEs and CSV for {len(DATA)} papers.")
