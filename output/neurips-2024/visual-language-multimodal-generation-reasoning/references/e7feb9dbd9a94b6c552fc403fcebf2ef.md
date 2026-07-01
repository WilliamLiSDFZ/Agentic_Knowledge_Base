---
title: "Stabilizing Zero-Shot Prediction: A Novel Antidote to Forgetting in Continual Vision-Language Tasks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e7feb9dbd9a94b6c552fc403fcebf2ef-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning']
tags: ['continual-learning', 'vision-language-models', 'catastrophic-forgetting']
venue: "NeurIPS 2024"
tldr: "A novel method stabilizing zero-shot prediction in continual vision-language learning to mitigate catastrophic forgetting."
---

# Stabilizing Zero-Shot Prediction: A Novel Antidote to Forgetting in Continual Vision-Language Tasks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e7feb9dbd9a94b6c552fc403fcebf2ef-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/e7feb9dbd9a94b6c552fc403fcebf2ef-Abstract-Conference.html)

**TLDR**: A novel method stabilizing zero-shot prediction in continual vision-language learning to mitigate catastrophic forgetting.

## Abstract

Continual learning (CL) empowers pre-trained vision-language (VL) models to efficiently adapt to a sequence of downstream tasks. However, these models often encounter challenges in retaining previously acquired skills due to parameter shifts and limited access to historical data. In response, recent efforts focus on devising specific frameworks and various replay strategies, striving for a typical learning-forgetting trade-off. Surprisingly, both our empirical research and theoretical analysis demonstrate that the stability of the model in consecutive zero-shot predictions serves as a reliable indicator of its anti-forgetting capabilities for previously learned tasks. Motivated by these insights, we develop a novel replay-free CL method named ZAF (Zero-shot Antidote to Forgetting), which preserves acquired knowledge through a zero-shot stability regularization applied to wild data in a plug-and-play manner. To enhance efficiency in adapting to new tasks and seamlessly access historical models, we introduce a parameter-efficient EMA-LoRA neural architecture based on the Exponential Moving Average (EMA). ZAF utilizes new data for low-rank adaptation (LoRA), complemented by a zero-shot antidote on wild data, effectively decoupling learning from forgetting. Our extensive experiments demonstrate ZAF's superior performance and robustness in pre-trained models across various continual VL concept learning tasks, achieving leads of up to 3.70\%, 4.82\%, and 4.38\%, along with at least a 10x acceleration in training speed on three benchmarks, respectively. Additionally, our zero-shot antidote significantly reduces forgetting in existing models by at least 6.37\%. Our code is available at https://github.com/Zi-Jian-Gao/Stabilizing-Zero-Shot-Prediction-ZAF.