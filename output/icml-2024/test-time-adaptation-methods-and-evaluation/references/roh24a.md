---
title: "LEVI: Generalizable Fine-tuning via Layer-wise Ensemble of Different Views"
source: "https://proceedings.mlr.press/v235/roh24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/roh24a/roh24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['fine-tuning', 'layer-wise-ensemble', 'distribution-shift', 'foundation-models', 'generalization']
venue: "ICML 2024"
tldr: "LEVI improves out-of-distribution generalization of fine-tuned models via a layer-wise ensemble of different views of pre-trained representations."
---

# LEVI: Generalizable Fine-tuning via Layer-wise Ensemble of Different Views

**Source**: [https://proceedings.mlr.press/v235/roh24a.html](https://proceedings.mlr.press/v235/roh24a.html)

**TLDR**: LEVI improves out-of-distribution generalization of fine-tuned models via a layer-wise ensemble of different views of pre-trained representations.

## Abstract

Fine-tuning is becoming widely used for leveraging the power of pre-trained foundation models in new downstream tasks. While there are many successes of fine-tuning on various tasks, recent studies have observed challenges in the generalization of fine-tuned models to unseen distributions (i.e., out-of-distribution; OOD). To improve OOD generalization, some previous studies identify the limitations of fine-tuning data and regulate fine-tuning to preserve the general representation learned from pre-training data. However, potential limitations in the pre-training data and models are often ignored. In this paper, we contend that overly relying on the pre-trained representation may hinder fine-tuning from learning essential representations for downstream tasks and thus hurt its OOD generalization. It can be especially catastrophic when new tasks are from different (sub)domains compared to pre-training data. To address the issues in both pre-training and fine-tuning data, we propose a novel generalizable fine-tuning method LEVI (Layer-wise Ensemble of different VIews), where the pre-trained model is adaptively ensembled layer-wise with a small task-specific model, while preserving its efficiencies. By combining two complementing models, LEVI effectively suppresses problematic features in both the fine-tuning data and pre-trained model and preserves useful features for new tasks. Broad experiments with large language and vision models show that LEVI greatly improves fine-tuning generalization via emphasizing different views from fine-tuning data and pre-trained features.