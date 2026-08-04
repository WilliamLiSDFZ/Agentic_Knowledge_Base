---
title: "Position: TrustLLM: Trustworthiness in Large Language Models"
source: "https://proceedings.mlr.press/v235/huang24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24x/huang24x.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'ai-safety-governance-alignment-positions']
tags: ['trustworthiness', 'large-language-models', 'safety', 'benchmark', 'evaluation']
venue: "ICML 2024"
tldr: "Introduces TrustLLM, a comprehensive benchmark and study evaluating trustworthiness dimensions of large language models."
---

# Position: TrustLLM: Trustworthiness in Large Language Models

**Source**: [https://proceedings.mlr.press/v235/huang24x.html](https://proceedings.mlr.press/v235/huang24x.html)

**TLDR**: Introduces TrustLLM, a comprehensive benchmark and study evaluating trustworthiness dimensions of large language models.

## Abstract

Large language models (LLMs) have gained considerable attention for their excellent natural language processing capabilities. Nonetheless, these LLMs present many challenges, particularly in the realm of trustworthiness. This paper introduces TrustLLM, a comprehensive study of trustworthiness in LLMs, including principles for different dimensions of trustworthiness, established benchmark, evaluation, and analysis of trustworthiness for mainstream LLMs, and discussion of open challenges and future directions. Specifically, we first propose a set of principles for trustworthy LLMs that span eight different dimensions. Based on these principles, we further establish a benchmark across six dimensions including truthfulness, safety, fairness, robustness, privacy, and machine ethics. We then present a study evaluating 16 mainstream LLMs in TrustLLM, consisting of over 30 datasets. Our findings firstly show that in general trustworthiness and capability (i.e., functional effectiveness) are positively related. Secondly, our observations reveal that proprietary LLMs generally outperform most open-source counterparts in terms of trustworthiness, raising concerns about the potential risks of widely accessible open-source LLMs. However, a few open-source LLMs come very close to proprietary ones, suggesting that open-source models can achieve high levels of trustworthiness without additional mechanisms like moderator, offering valuable insights for developers in this field. Thirdly, it is important to note that some LLMs may be overly calibrated towards exhibiting trustworthiness, to the extent that they compromise their utility by mistakenly treating benign prompts as harmful and consequently not responding. Besides these observations, we’ve uncovered key insights into the multifaceted trustworthiness in LLMs. We emphasize the importance of ensuring transparency not only in the models themselves but also in the technologies that underpin trustworthiness. We advocate that the establishment of an AI alliance between industry, academia, the open-source community to foster collaboration is imperative to advance the trustworthiness of LLMs.