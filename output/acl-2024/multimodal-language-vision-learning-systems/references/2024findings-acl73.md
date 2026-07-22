---
title: "GeoEval: Benchmark for Evaluating LLMs and Multi-Modal Models on Geometry Problem-Solving"
source: "https://aclanthology.org/2024.findings-acl.73/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'multimodal-language-vision-learning-systems']
tags: ['geometry-problem-solving', 'multimodal-benchmark', 'mathematical-reasoning']
venue: "ACL 2024"
tldr: "Presents GeoEval, a benchmark for assessing LLMs and multimodal models on geometry problems requiring joint textual and visual understanding."
---

# GeoEval: Benchmark for Evaluating LLMs and Multi-Modal Models on Geometry Problem-Solving

**Source**: [https://aclanthology.org/2024.findings-acl.73/](https://aclanthology.org/2024.findings-acl.73/)

**TLDR**: Presents GeoEval, a benchmark for assessing LLMs and multimodal models on geometry problems requiring joint textual and visual understanding.

## Abstract

AbstractRecent advancements in large language models (LLMs) and multi-modal models (MMs) have demonstrated their remarkable capabilities in problem-solving. Yet, their proficiency in tackling geometry math problems, which necessitates an integrated understanding of both textual and visual information, has not been thoroughly evaluated. To address this gap, we introduce the GeoEval benchmark, a comprehensive collection that includes a main subset of 2,000 problems, a 750 problems subset focusing on backward reasoning, an augmented sub- set of 2,000 problems, and a hard subset of 300 problems. This benchmark facilitates a deeper investigation into the performance of LLMs and MMs in solving geometry math problems. Our evaluation of ten LLMs and MMs across these varied subsets reveals that the WizardMath model excels, achieving a 55.67% accuracy rate on the main subset but only a 6.00% accuracy on the hard subset. This highlights the critical need for testing models against datasets on which they have not been pre-trained. Additionally, our findings indicate that GPT-series models perform more effectively on problems they have rephrased, suggesting a promising method for enhancing model capabilities.