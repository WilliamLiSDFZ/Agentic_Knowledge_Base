---
title: "CogBench: a large language model walks into a psychology lab"
source: "https://proceedings.mlr.press/v235/coda-forno24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/coda-forno24a/coda-forno24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'ai-explainability-uncertainty-human-decision-making']
tags: ['llm-evaluation', 'cognitive-benchmarks', 'psychology']
venue: "ICML 2024"
tldr: "Introduces CogBench, a benchmark evaluating LLMs using behavioral metrics inspired by cognitive psychology rather than pure performance metrics."
---

# CogBench: a large language model walks into a psychology lab

**Source**: [https://proceedings.mlr.press/v235/coda-forno24a.html](https://proceedings.mlr.press/v235/coda-forno24a.html)

**TLDR**: Introduces CogBench, a benchmark evaluating LLMs using behavioral metrics inspired by cognitive psychology rather than pure performance metrics.

## Abstract

Large language models (LLMs) have significantly advanced the field of artificial intelligence. Yet, evaluating them comprehensively remains challenging. We argue that this is partly due to the predominant focus on performance metrics in most benchmarks. This paper introduces CogBench, a benchmark that includes ten behavioral metrics derived from seven cognitive psychology experiments. This novel approach offers a toolkit for phenotyping LLMs’ behavior. We apply CogBench to 40 LLMs, yielding a rich and diverse dataset. We analyze this data using statistical multilevel modeling techniques, accounting for the nested dependencies among fine-tuned versions of specific LLMs. Our study highlights the crucial role of model size and reinforcement learning from human feedback (RLHF) in improving performance and aligning with human behavior. Interestingly, we find that open-source models are less risk-prone than proprietary models and that fine-tuning on code does not necessarily enhance LLMs’ behavior. Finally, we explore the effects of prompt-engineering techniques. We discover that chain-of-thought prompting improves probabilistic reasoning, while take-a-step-back prompting fosters model-based behaviors.