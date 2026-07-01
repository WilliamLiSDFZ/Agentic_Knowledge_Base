---
title: "LT-Defense: Searching-free Backdoor Defense via Exploiting the Long-tailed Effect"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/064f6bcd7d3c72fb187bfca35ba2bfd4-Abstract-Conference.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'llm-training-and-optimization-techniques']
tags: ['backdoor-defense', 'long-tailed-effect', 'language-models']
venue: "NeurIPS 2024"
tldr: "LT-Defense exploits the long-tailed distribution effect to defend language models against backdoor attacks without costly trigger search."
---

# LT-Defense: Searching-free Backdoor Defense via Exploiting the Long-tailed Effect

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/064f6bcd7d3c72fb187bfca35ba2bfd4-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/064f6bcd7d3c72fb187bfca35ba2bfd4-Abstract-Conference.html)

**TLDR**: LT-Defense exploits the long-tailed distribution effect to defend language models against backdoor attacks without costly trigger search.

## Abstract

Language models have shown vulnerability against backdoor attacks, threatening the security of services based on them. To mitigate the threat, existing solutions attempted to search for backdoor triggers, which can be time-consuming when handling a large search space. Looking into the attack process, we observe that poisoned data will create a long-tailed effect in the victim model, causing the decision boundary to shift towards the attack targets. Inspired by this observation, we introduce LT-Defense, the first searching-free backdoor defense via exploiting the long-tailed effect. Specifically, LT-Defense employs a small set of clean examples and two metrics to distinguish backdoor-related features in the target model. Upon detecting a backdoor model, LT-Defense additionally provides test-time backdoor freezing and attack target prediction. Extensive experiments demonstrate the effectiveness of LT-Defense in both detection accuracy and efficiency, e.g., in task-agnostic scenarios, LT-Defense achieves 98% accuracy across 1440 models with less than 1% of the time cost of state-of-the-art solutions.