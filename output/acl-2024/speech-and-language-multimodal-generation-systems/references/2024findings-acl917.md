---
title: "Textless Acoustic Model with Self-Supervised Distillation for Noise-Robust Expressive Speech-to-Speech Translation"
source: "https://aclanthology.org/2024.findings-acl.917/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems']
tags: ['speech-to-speech-translation', 'self-supervised-distillation', 'noise-robustness']
venue: "ACL 2024"
tldr: "A textless acoustic model with self-supervised distillation is proposed for noise-robust expressive speech-to-speech translation."
---

# Textless Acoustic Model with Self-Supervised Distillation for Noise-Robust Expressive Speech-to-Speech Translation

**Source**: [https://aclanthology.org/2024.findings-acl.917/](https://aclanthology.org/2024.findings-acl.917/)

**TLDR**: A textless acoustic model with self-supervised distillation is proposed for noise-robust expressive speech-to-speech translation.

## Abstract

AbstractIn this paper, we propose a textless acoustic model with a self-supervised distillation strategy for noise-robust expressive speech-to-speech translation (S2ST).Recently proposed expressive S2ST systems have achieved impressive expressivity preservation performances by cascading unit-to-speech (U2S) generator to the speech-to-unit translation model. However, these systems are vulnerable to the presence of noise in input speech, which is an assumption in real-world translation scenarios. To address this limitation, we propose a U2S generator that incorporates a distillation with no label (DINO) self-supervised training strategy into it’s pretraining process.Because the proposed method captures noise-agnostic expressivity representation, it can generate qualified speech even in noisy environment.Objective and subjective evaluation results verified that the proposed method significantly improved the performance of the expressive S2ST system in noisy environments while maintaining competitive performance in clean environments.