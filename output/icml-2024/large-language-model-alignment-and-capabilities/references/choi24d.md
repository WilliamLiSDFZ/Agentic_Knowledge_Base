---
title: "Embodied CoT Distillation From LLM To Off-the-shelf Agents"
source: "https://proceedings.mlr.press/v235/choi24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/choi24d/choi24d.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'large-language-model-alignment-and-capabilities']
tags: ['embodied-ai', 'chain-of-thought', 'knowledge-distillation']
venue: "ICML 2024"
tldr: "DeDer distills embodied chain-of-thought reasoning from large LLMs into efficient off-the-shelf agents for real-time decision making."
---

# Embodied CoT Distillation From LLM To Off-the-shelf Agents

**Source**: [https://proceedings.mlr.press/v235/choi24d.html](https://proceedings.mlr.press/v235/choi24d.html)

**TLDR**: DeDer distills embodied chain-of-thought reasoning from large LLMs into efficient off-the-shelf agents for real-time decision making.

## Abstract

We address the challenge of utilizing large language models (LLMs) for complex embodied tasks, in the environment where decision-making systems operate timely on capacity-limited, off-the-shelf devices. We present DeDer, a framework for decomposing and distilling the embodied reasoning capabilities from LLMs to efficient, small language model (sLM)-based policies. In DeDer, the decision-making process of LLM-based strategies is restructured into a hierarchy with a reasoning-policy and planning-policy. The reasoning-policy is distilled from the data that is generated through the embodied in-context learning and self-verification of an LLM, so it can produce effective rationales. The planning-policy, guided by the rationales, can render optimized plans efficiently. In turn, DeDer allows for adopting sLMs for both policies, deployed on off-the-shelf devices. Furthermore, to enhance the quality of intermediate rationales, specific to embodied tasks, we devise the embodied knowledge graph, and to generate multiple rationales timely through a single inference, we also use the contrastively prompted attention model. Our experiments with the ALFRED benchmark demonstrate that DeDer surpasses leading language planning and distillation approaches, indicating the applicability and efficiency of sLM-based embodied policies derived through DeDer.