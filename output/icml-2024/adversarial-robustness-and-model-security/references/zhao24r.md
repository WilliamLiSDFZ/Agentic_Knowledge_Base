---
title: "Defense against Backdoor Attack on Pre-trained Language Models via Head Pruning and Attention Normalization"
source: "https://proceedings.mlr.press/v235/zhao24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24r/zhao24r.pdf"
categories: ['adversarial-robustness-and-model-security']
tags: ['backdoor-attacks', 'pre-trained-language-models', 'head-pruning', 'attention-normalization']
venue: "ICML 2024"
tldr: "This paper proposes a defense mechanism against backdoor attacks on pre-trained language models using head pruning and attention normalization."
---

# Defense against Backdoor Attack on Pre-trained Language Models via Head Pruning and Attention Normalization

**Source**: [https://proceedings.mlr.press/v235/zhao24r.html](https://proceedings.mlr.press/v235/zhao24r.html)

**TLDR**: This paper proposes a defense mechanism against backdoor attacks on pre-trained language models using head pruning and attention normalization.

## Abstract

Pre-trained language models (PLMs) are commonly used for various downstream natural language processing tasks via fine-tuning. However, recent studies have demonstrated that PLMs are vulnerable to backdoor attacks, which can mislabel poisoned samples to target outputs even after a vanilla fine-tuning process. The key challenge for defending against the backdoored PLMs is that end users who adopt the PLMs for their downstream tasks usually do not have any knowledge about the attacking strategies, such as triggers. To tackle this challenge, in this work, we propose a backdoor mitigation approach, PURE, via head pruning and normalization of attention weights. The idea is to prune the attention heads that are potentially affected by poisoned texts with only clean texts on hand and then further normalize the weights of remaining attention heads to mitigate the backdoor impacts. We conduct experiments to defend against various backdoor attacks on the classification task. The experimental results show the effectiveness of PURE in lowering the attack success rate without sacrificing the performance on clean texts.