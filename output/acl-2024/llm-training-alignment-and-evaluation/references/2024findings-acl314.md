---
title: "StructEval: Deepen and Broaden Large Language Model Assessment via Structured Evaluation"
source: "https://aclanthology.org/2024.findings-acl.314/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'nlp-benchmark-design-and-interpretability']
tags: ['evaluation-framework', 'structured-assessment', 'benchmark-design']
venue: "ACL 2024"
tldr: "Introduces StructEval, a structured multi-item evaluation framework to more reliably assess LLM capabilities beyond memorization."
---

# StructEval: Deepen and Broaden Large Language Model Assessment via Structured Evaluation

**Source**: [https://aclanthology.org/2024.findings-acl.314/](https://aclanthology.org/2024.findings-acl.314/)

**TLDR**: Introduces StructEval, a structured multi-item evaluation framework to more reliably assess LLM capabilities beyond memorization.

## Abstract

AbstractEvaluation is the baton for the development of large language models. Current evaluations typically employ a single-item assessment paradigm for each atomic test objective, which struggle to discern whether a model genuinely possesses the required capabilities or merely memorizes/guesses the answers to specific questions. To this end, this paper proposes a novel evaluation framework referred to as StructEval. Starting from an atomic test objective, StructEval deepens and broadens the evaluation by conducting a structured assessment across multiple cognitive levels and critical concepts, and therefore offers a comprehensive, robust and consistent evaluations for large language models. Experiments on three widely-used benchmarks demonstrate that StructEval serves as a reliable tool for resisting the risk of data contamination, and reducing the interference of potential biases, thereby providing a more reliable and consistent conclusion regarding model capabilities. Our framework also sheds light on the design of future principled and trustworthy LLM evaluation protocols.