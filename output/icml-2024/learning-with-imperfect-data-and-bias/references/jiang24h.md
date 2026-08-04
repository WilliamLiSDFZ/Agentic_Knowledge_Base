---
title: "Tabular Insights, Visual Impacts: Transferring Expertise from Tables to Images"
source: "https://proceedings.mlr.press/v235/jiang24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiang24h/jiang24h.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'learning-with-imperfect-data-and-bias']
tags: ['knowledge-transfer', 'cross-modal', 'tabular-to-image', 'modality-gap']
venue: "ICML 2024"
tldr: "A method is proposed to transfer knowledge from tabular expert data to enhance image-based predictions at inference time when tabular data is unavailable."
---

# Tabular Insights, Visual Impacts: Transferring Expertise from Tables to Images

**Source**: [https://proceedings.mlr.press/v235/jiang24h.html](https://proceedings.mlr.press/v235/jiang24h.html)

**TLDR**: A method is proposed to transfer knowledge from tabular expert data to enhance image-based predictions at inference time when tabular data is unavailable.

## Abstract

Transferring knowledge across diverse data modalities is receiving increasing attention in machine learning. This paper tackles the task of leveraging expert-derived, yet expensive, tabular data to enhance image-based predictions when tabular data is unavailable during inference. The primary challenges stem from the inherent complexity of accurately mapping diverse tabular data to visual contexts, coupled with the necessity to devise distinct strategies for numerical and categorical tabular attributes. We propose CHannel tAbulaR alignment with optiMal tranSport (Charms), which establishes an alignment between image channels and tabular attributes, enabling selective knowledge transfer that is pertinent to visual features. Specifically, Charms measures similarity distributions across modalities to effectively differentiate and transfer relevant tabular features, with a focus on morphological characteristics, enhancing the capabilities of visual classifiers. By maximizing the mutual information between image channels and tabular features, knowledge from both numerical and categorical tabular attributes are extracted. Experimental results demonstrate that Charms not only enhances the performance of image classifiers but also improves their interpretability by effectively utilizing tabular knowledge.