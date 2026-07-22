---
title: "MoE-SLU: Towards ASR-Robust Spoken Language Understanding via Mixture-of-Experts"
source: "https://aclanthology.org/2024.findings-acl.882/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems', 'emotion-aware-dialogue-and-empathy-systems']
tags: ['spoken-language-understanding', 'asr-robustness', 'mixture-of-experts']
venue: "ACL 2024"
tldr: "Proposes MoE-SLU, a mixture-of-experts framework for ASR-robust spoken language understanding in task-oriented dialogue."
---

# MoE-SLU: Towards ASR-Robust Spoken Language Understanding via Mixture-of-Experts

**Source**: [https://aclanthology.org/2024.findings-acl.882/](https://aclanthology.org/2024.findings-acl.882/)

**TLDR**: Proposes MoE-SLU, a mixture-of-experts framework for ASR-robust spoken language understanding in task-oriented dialogue.

## Abstract

AbstractAs a crucial task in the task-oriented dialogue systems, spoken language understanding (SLU) has garnered increasing attention. However, errors from automatic speech recognition (ASR) often hinder the performance of understanding. To tackle this problem, we propose MoE-SLU, an ASR-Robust SLU framework based on the mixture-of-experts technique. Specifically, we first introduce three strategies to generate additional transcripts from clean transcripts. Then, we employ the mixture-of-experts technique to weigh the representations of the generated transcripts, ASR transcripts, and the corresponding clean manual transcripts. Additionally, we also regularize the weighted average of predictions and the predictions of ASR transcripts by minimizing the Jensen-Shannon Divergence (JSD) between these two output distributions. Experiment results on three benchmark SLU datasets demonstrate that our MoE-SLU achieves state-of-the-art performance. Further model analysis also verifies the superiority of our method.