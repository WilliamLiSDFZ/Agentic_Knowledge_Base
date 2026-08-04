---
title: "Federated Continual Learning via Prompt-based Dual Knowledge Transfer"
source: "https://proceedings.mlr.press/v235/piao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/piao24a/piao24a.pdf"
categories: ['continual-learning-memory-plasticity', 'privacy-preserving-federated-and-distributed-learning']
tags: ['federated-learning', 'continual-learning', 'prompt-tuning']
venue: "ICML 2024"
tldr: "A prompt-based dual knowledge transfer framework for federated continual learning that promotes positive knowledge sharing across tasks and clients."
---

# Federated Continual Learning via Prompt-based Dual Knowledge Transfer

**Source**: [https://proceedings.mlr.press/v235/piao24a.html](https://proceedings.mlr.press/v235/piao24a.html)

**TLDR**: A prompt-based dual knowledge transfer framework for federated continual learning that promotes positive knowledge sharing across tasks and clients.

## Abstract

In Federated Continual Learning (FCL), the challenge lies in effectively facilitating knowledge transfer and enhancing the performance across various tasks on different clients. Current FCL methods predominantly focus on avoiding interference between tasks, thereby overlooking the potential for positive knowledge transfer across tasks learned by different clients at separate time intervals. To address this issue, we introduce a Prompt-based knowledge transfer FCL algorithm, called Powder, designed to effectively foster the transfer of knowledge encapsulated in prompts between various sequentially learned tasks and clients. Furthermore, we have devised a unique approach for prompt generation and aggregation, intending to alleviate privacy protection concerns and communication overhead, while still promoting knowledge transfer. Comprehensive experimental results demonstrate the superiority of our method in terms of reduction in communication costs, and enhancement of knowledge transfer. Code is available at https://github.com/piaohongming/Powder.