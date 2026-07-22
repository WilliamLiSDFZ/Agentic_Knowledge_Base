---
title: "UOR: Universal Backdoor Attacks on Pre-trained Language Models"
source: "https://aclanthology.org/2024.findings-acl.468/"
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['backdoor-attacks', 'pre-trained-models', 'universal-trigger']
venue: "ACL 2024"
tldr: "Introduces UOR, a universal backdoor attack framework on pre-trained language models that transfers across downstream tasks."
---

# UOR: Universal Backdoor Attacks on Pre-trained Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.468/](https://aclanthology.org/2024.findings-acl.468/)

**TLDR**: Introduces UOR, a universal backdoor attack framework on pre-trained language models that transfers across downstream tasks.

## Abstract

AbstractTask-agnostic and transferable backdoors implanted in pre-trained language models (PLMs) pose a severe security threat as they can be inherited to any downstream task. However, existing methods rely on manual selection of triggers and backdoor representations, hindering their effectiveness and universality across different PLMs or usage paradigms. In this paper, we propose a new backdoor attack method called UOR, which overcomes these limitations by turning manual selection into automatic optimization. Specifically, we design poisoned supervised contrastive learning, which can automatically learn more uniform and universal backdoor representations. This allows for more even coverage of the output space, thus hitting more labels in downstream tasks after fine-tuning. Furthermore, we utilize gradient search to select appropriate trigger words that can be adapted to different PLMs and vocabularies. Experiments show that UOR achieves better attack performance on various text classification tasks compared to manual methods. Moreover, we test on PLMs with different architectures, usage paradigms, and more challenging tasks, achieving higher scores for universality.