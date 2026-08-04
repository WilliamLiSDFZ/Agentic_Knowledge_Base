---
title: "Distinguishing the Knowable from the Unknowable with Language Models"
source: "https://proceedings.mlr.press/v235/ahdritz24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ahdritz24a/ahdritz24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification']
tags: ['epistemic-uncertainty', 'aleatoric-uncertainty', 'language-models', 'uncertainty-quantification']
venue: "ICML 2024"
tldr: "Studies whether language models can distinguish epistemic from aleatoric uncertainty in free-form text generation."
---

# Distinguishing the Knowable from the Unknowable with Language Models

**Source**: [https://proceedings.mlr.press/v235/ahdritz24a.html](https://proceedings.mlr.press/v235/ahdritz24a.html)

**TLDR**: Studies whether language models can distinguish epistemic from aleatoric uncertainty in free-form text generation.

## Abstract

We study the feasibility of identifying epistemic uncertainty (reflecting a lack of knowledge), as opposed to aleatoric uncertainty (reflecting entropy in the underlying distribution), in the outputs of large language models (LLMs) over free-form text. In the absence of ground-truth probabilities, we explore a setting where, in order to (approximately) disentangle a given LLM’s uncertainty, a significantly larger model stands in as a proxy for the ground truth. We show that small linear probes trained on the embeddings of frozen, pretrained models accurately predict when larger models will be more confident at the token level and that probes trained on one text domain generalize to others. Going further, we propose a fully unsupervised method that achieves non-trivial accuracy on the same task. Taken together, we interpret these results as evidence that LLMs naturally contain internal representations of different types of uncertainty that could potentially be leveraged to devise more informative indicators of model confidence in diverse practical settings. Code can be found at: https://github.com/KempnerInstitute/llm_uncertainty