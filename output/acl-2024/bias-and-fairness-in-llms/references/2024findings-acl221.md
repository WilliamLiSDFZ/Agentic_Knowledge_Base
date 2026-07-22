---
title: "Adversarial Preference Optimization: Enhancing Your Alignment via RM-LLM Game"
source: "https://aclanthology.org/2024.findings-acl.221/"
categories: ['llm-training-alignment-and-evaluation', 'bias-and-fairness-in-llms']
tags: ['preference-optimization', 'adversarial-training', 'reward-model']
venue: "ACL 2024"
tldr: "Proposes an adversarial game between a reward model and LLM to continuously generate hard preference data for improved alignment without manual annotation."
---

# Adversarial Preference Optimization: Enhancing Your Alignment via RM-LLM Game

**Source**: [https://aclanthology.org/2024.findings-acl.221/](https://aclanthology.org/2024.findings-acl.221/)

**TLDR**: Proposes an adversarial game between a reward model and LLM to continuously generate hard preference data for improved alignment without manual annotation.

## Abstract

AbstractHuman preference alignment is essential to improve the interaction quality of large language models (LLMs). Existing alignment methods depend on manually annotated preference data to guide the LLM optimization directions. However, continuously updating LLMs for alignment raises a distribution gap between model-generated samples and human-annotated responses, hindering training effectiveness. To mitigate this issue, previous methods require additional preference annotation on newly generated samples to adapt to the shifted distribution, which consumes a large amount of annotation resources. Targeting more efficient human preference optimization, we propose an Adversarial Preference Optimization (APO) framework, in which the LLM and the reward model update alternatively via a min-max game. Through adversarial training, the reward model can adapt to the shifted generation distribution of the LLM without any additional annotation. With comprehensive experiments, we find the proposed adversarial training framework further enhances existing alignment baselines in terms of LLM helpfulness and harmlessness. The code is at https://github.com/Linear95/APO.