---
title: "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation"
source: "https://proceedings.mlr.press/v235/chen24av.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24av/chen24av.pdf"
categories: ['llm-geometry-and-interpretability-research', 'large-language-model-alignment-and-capabilities']
tags: ['hallucination', 'inner-representations', 'LLM', 'sharpness']
venue: "ICML 2024"
tldr: "Discovers that in-context sharpness of LLM inner representations signals hallucinations and proposes a mitigation strategy."
---

# In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation

**Source**: [https://proceedings.mlr.press/v235/chen24av.html](https://proceedings.mlr.press/v235/chen24av.html)

**TLDR**: Discovers that in-context sharpness of LLM inner representations signals hallucinations and proposes a mitigation strategy.

## Abstract

Large language models (LLMs) frequently hallucinate, e.g., making factual errors, yet our understanding of why they make these errors remains limited. In this study, we aim to understand the underlying mechanisms of LLM hallucinations from the perspective of inner representations. We discover a pattern associated with hallucinations: correct generations tend to have sharper context activations in the hidden states of the in-context tokens, compared to that of the incorrect generations. Leveraging this signal, we propose an entropy-based metric to quantify the sharpness among the in-context hidden states and incorporate it into the decoding process, i.e, use the entropy value to adjust the next token prediction distribution to improve the factuality and overall quality of the generated text. Experiments on knowledge-seeking datasets (Natural Questions, HotpotQA, TriviaQA) and hallucination benchmark (TruthfulQA) demonstrate our consistent effectiveness, e.g., up to 8.6 absolute points on TruthfulQA. We believe this study can improve our understanding of hallucinations and serve as a practical solution for hallucination mitigation.