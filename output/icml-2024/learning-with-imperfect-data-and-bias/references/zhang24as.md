---
title: "Amend to Alignment: Decoupled Prompt Tuning for Mitigating Spurious Correlation in Vision-Language Models"
source: "https://proceedings.mlr.press/v235/zhang24as.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24as/zhang24as.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'test-time-adaptation-methods-and-evaluation']
tags: ['prompt-tuning', 'spurious-correlations', 'vision-language-models']
venue: "ICML 2024"
tldr: "Decoupled prompt tuning for vision-language models that disentangles spurious from causal features to mitigate bias from training data."
---

# Amend to Alignment: Decoupled Prompt Tuning for Mitigating Spurious Correlation in Vision-Language Models

**Source**: [https://proceedings.mlr.press/v235/zhang24as.html](https://proceedings.mlr.press/v235/zhang24as.html)

**TLDR**: Decoupled prompt tuning for vision-language models that disentangles spurious from causal features to mitigate bias from training data.

## Abstract

Fine-tuning the learnable prompt for a pre-trained vision-language model (VLM), such as CLIP, has demonstrated exceptional efficiency in adapting to a broad range of downstream tasks. Existing prompt tuning methods for VLMs do not distinguish spurious features introduced by biased training data from invariant features, and employ a uniform alignment process when adapting to unseen target domains. This can impair the cross-modal feature alignment when the testing data significantly deviate from the distribution of the training data, resulting in a poor out-of-distribution (OOD) generalization performance. In this paper, we reveal that the prompt tuning failure in such OOD scenarios can be attribute to the undesired alignment between the textual and the spurious feature. As a solution, we propose CoOPood, a fine-grained prompt tuning method that can discern the causal features and deliberately align the text modality with the invariant feature. Specifically, we design two independent contrastive phases using two lightweight projection layers during the alignment, each with different objectives: 1) pulling the text embedding closer to invariant image embedding and 2) pushing text embedding away from spurious image embedding. We have illustrated that CoOPood can serve as a general framework for VLMs and can be seamlessly integrated with existing prompt tuning methods. Extensive experiments on various OOD datasets demonstrate the performance superiority over state-of-the-art methods.