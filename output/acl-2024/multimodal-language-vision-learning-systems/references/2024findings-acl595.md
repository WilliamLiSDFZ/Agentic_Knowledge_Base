---
title: "Fair Federated Learning with Biased Vision-Language Models"
source: "https://aclanthology.org/2024.findings-acl.595/"
categories: ['multimodal-language-vision-learning-systems', 'bias-and-fairness-in-llms']
tags: ['federated-learning', 'CLIP', 'fairness', 'bias', 'data-heterogeneity']
venue: "ACL 2024"
tldr: "Investigates and addresses group unfairness introduced by CLIP in federated learning settings with heterogeneous client data."
---

# Fair Federated Learning with Biased Vision-Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.595/](https://aclanthology.org/2024.findings-acl.595/)

**TLDR**: Investigates and addresses group unfairness introduced by CLIP in federated learning settings with heterogeneous client data.

## Abstract

AbstractExisting literature that integrates CLIP into federated learning (FL) largely ignores the inherent group unfairness within CLIP and its ethical implications on FL applications. Furthermore, such CLIP bias may be amplified in FL, due to the unique issue of data heterogeneity across clients. However, in identity-sensitive FL applications, model fairness (i.e., group fairness) is imperative for model development. Therefore, this work explores a critical question ignored by the existing literature: how can we build a fair FL framework using biased pre-trained VLMs (e.g., CLIP)? To address this problem, we propose a fairness-aware adaptation framework tailored for VLM (e.g., CLIP) in the context of FL, named Fair Federated Deep Visiual Prompting or FF-DVP. As implied by its name, trains a fair FL model with fairness-aware deep visual prompting (DVP). Moreover, incorporates modality-fused classification heads to learn client-specific knowledge and fairness constraints. These modules explicitly addresses a unique bias in FL, namely the bias triggered by data heterogeneity. We show that can be readily extended to prevailing parameter-efficient fine-tuning methods (e.g., adapter or LoRA) for debiasing. To the best of our knowledge, is the first to leverage biased VLMs for building fair FL frameworks. Extensive results on human face attribute recognition (FAR) applications suggest that effectively improves model fairness and training convergence, outperforming state-of-the-art baselines.