---
title: "Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modulo Frameworks"
source: "https://proceedings.mlr.press/v235/kambhampati24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kambhampati24a/kambhampati24a.pdf"
categories: ['position-papers-on-ml-research-directions', 'large-language-model-alignment-and-capabilities']
tags: ['LLM', 'planning', 'reasoning', 'LLM-Modulo', 'position-paper']
venue: "ICML 2024"
tldr: "Argues LLMs cannot plan autonomously but can serve as knowledge sources within LLM-Modulo frameworks that incorporate external verifiers."
---

# Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modulo Frameworks

**Source**: [https://proceedings.mlr.press/v235/kambhampati24a.html](https://proceedings.mlr.press/v235/kambhampati24a.html)

**TLDR**: Argues LLMs cannot plan autonomously but can serve as knowledge sources within LLM-Modulo frameworks that incorporate external verifiers.

## Abstract

We argue that auto-regressive LLMs cannot, by themselves, do planning or self-verification (which is after all a form of reasoning), and shed some light on the reasons for misunderstandings in the literature. We will also argue that LLMs should be viewed as universal approximate knowledge sources that have much more meaningful roles to play in planning/reasoning tasks beyond simple front-end/back-end format translators. We present a vision of LLM-Modulo Frameworks that combine the strengths of LLMs with external model-based verifiers in a tighter bi-directional interaction regime. We will show how the models driving the external verifiers themselves can be acquired with the help of LLMs. We will also argue that rather than simply pipelining LLMs and symbolic components, this LLM-Modulo Framework provides a better neuro-symbolic approach that offers tighter integration between LLMs and symbolic components, and allows extending the scope of model-based planning/reasoning regimes towards more flexible knowledge, problem and preference specifications.