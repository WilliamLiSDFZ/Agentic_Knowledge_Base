---
title: "Beyond Sole Strength: Customized Ensembles for Generalized Vision-Language Models"
source: "https://proceedings.mlr.press/v235/lu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24a/lu24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['vision-language-models', 'CLIP', 'ensemble', 'generalization', 'domain-adaptation']
venue: "ICML 2024"
tldr: "Improves open-world generalization of vision-language models through customized ensemble strategies rather than single-model refinement."
---

# Beyond Sole Strength: Customized Ensembles for Generalized Vision-Language Models

**Source**: [https://proceedings.mlr.press/v235/lu24a.html](https://proceedings.mlr.press/v235/lu24a.html)

**TLDR**: Improves open-world generalization of vision-language models through customized ensemble strategies rather than single-model refinement.

## Abstract

Fine-tuning pre-trained vision-language models (VLMs), e.g., CLIP, for the open-world generalization has gained increasing popularity due to its practical value. However, performance advancements are limited when relying solely on intricate algorithmic designs for a single model, even one exhibiting strong performance, e.g., CLIP-ViT-B/16. This paper, for the first time, explores the collaborative potential of leveraging much weaker VLMs to enhance the generalization of a robust single model. The affirmative findings motivate us to address the generalization problem from a novel perspective, i.e., ensemble of pre-trained VLMs. We introduce three customized ensemble strategies, each tailored to one specific scenario. Firstly, we introduce the zero-shot ensemble, automatically adjusting the logits of different models based on their confidence when only pre-trained VLMs are available. Furthermore, for scenarios with extra few-shot samples, we propose the training-free and tuning ensemble, offering flexibility based on the availability of computing resources. The code is available at https://github.com/zhiheLu/Ensemble_VLM.git.