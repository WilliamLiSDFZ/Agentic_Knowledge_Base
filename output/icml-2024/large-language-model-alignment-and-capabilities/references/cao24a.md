---
title: "Successor Features for Efficient Multi-Subject Controlled Text Generation"
source: "https://proceedings.mlr.press/v235/cao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cao24a/cao24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['controlled-text-generation', 'successor-features', 'multi-subject', 'decoding']
venue: "ICML 2024"
tldr: "Uses successor features to enable efficient multi-subject controlled text generation in large language models without retraining."
---

# Successor Features for Efficient Multi-Subject Controlled Text Generation

**Source**: [https://proceedings.mlr.press/v235/cao24a.html](https://proceedings.mlr.press/v235/cao24a.html)

**TLDR**: Uses successor features to enable efficient multi-subject controlled text generation in large language models without retraining.

## Abstract

While large language models (LLMs) have achieved impressive performance in generating fluent and realistic text, controlling the generated text so that it exhibits properties such as safety, factuality, and non-toxicity remains challenging. Existing decoding-based controllable text generation methods are static in terms of the dimension of control; if the target subject is changed, they require new training. Moreover, it can quickly become prohibitive to concurrently control multiple subjects. To address these challenges, we first show that existing methods can be framed as a reinforcement learning problem, where an action-value function estimates the likelihood of a desired attribute appearing in the generated text. Then, we introduce a novel approach named SF-Gen, which leverages the concept of successor features to decouple the dynamics of LLMs from task-specific rewards. By employing successor features, our method proves to be memory-efficient and computationally efficient for both training and decoding, especially when dealing with multiple target subjects. To the best of our knowledge, our research represents the first application of successor features in text generation. In addition to its computational efficiency, the resultant language produced by our method is comparable to the SOTA (and outperforms baselines) in both control measures as well as language quality, which we demonstrate through a series of experiments in various controllable text generation tasks.