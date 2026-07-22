---
title: "Aligning Large Multimodal Models with Factually Augmented RLHF"
source: "https://aclanthology.org/2024.findings-acl.775/"
categories: ['multimodal-language-vision-learning-systems', 'llm-training-alignment-and-evaluation']
tags: ['multimodal-alignment', 'hallucination-mitigation', 'factually-augmented-rlhf']
venue: "ACL 2024"
tldr: "Addresses hallucination in large multimodal models by augmenting RLHF with factual information across modalities."
---

# Aligning Large Multimodal Models with Factually Augmented RLHF

**Source**: [https://aclanthology.org/2024.findings-acl.775/](https://aclanthology.org/2024.findings-acl.775/)

**TLDR**: Addresses hallucination in large multimodal models by augmenting RLHF with factual information across modalities.

## Abstract

AbstractLarge Multimodal Models (LMM) are built across modalities and the misalignment between two modalities can result in “hallucination”, generating textual outputs that are not grounded by the multimodal information in context. To address the multimodal misalignment issue, we adapt the Reinforcement Learning from Human Feedback (RLHF) from the text domain to the vision-language alignment, where human annotators are asked to compare two responses and pinpoint the more hallucinated one, and the vision-language model is trained to maximize the simulated human rewards. We propose a new alignment algorithm called Factually Augmented RLHF that augments the reward model with additional factual information such as image captions and ground-truth multi-choice options, which alleviates the reward hacking phenomenon in RLHF and further improves the performance. We also enhance the GPT-4-generated training data (for vision instruction tuning) with previously available human-written image-text pairs to improve the general capabilities of our model. To evaluate the proposed approach in real-world scenarios, we develop a new evaluation benchmark MMHAL-BENCH with a special focus on penalizing hallucinations. As the first LMM trained with RLHF, our approach achieves remarkable improvement on the LLaVA-Bench dataset with the 96% performance level of the text-only GPT-4 (while previous best methods can only achieve the 87% level), and an improvement of 60% on MMHAL-BENCH over other baselines.