---
title: "DetKDS: Knowledge Distillation Search for Object Detectors"
source: "https://proceedings.mlr.press/v235/li24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24c/li24c.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'transformer-architecture-efficiency-and-scaling']
tags: ['knowledge-distillation', 'object-detection', 'neural-architecture-search', 'distillation-policy', 'automated']
venue: "ICML 2024"
tldr: "Presents DetKDS, the first framework to automatically search for optimal knowledge distillation policies for object detection models."
---

# DetKDS: Knowledge Distillation Search for Object Detectors

**Source**: [https://proceedings.mlr.press/v235/li24c.html](https://proceedings.mlr.press/v235/li24c.html)

**TLDR**: Presents DetKDS, the first framework to automatically search for optimal knowledge distillation policies for object detection models.

## Abstract

In this paper, we present DetKDS, the first framework that searches for optimal detection distillation policies. Manual design of detection distillers becomes challenging and time-consuming due to significant disparities in distillation behaviors between detectors with different backbones, paradigms, and label assignments. To tackle these challenges, we leverage search algorithms to discover optimal distillers for homogeneous and heterogeneous student-teacher pairs. Firstly, our search space encompasses global features, foreground-background features, instance features, logits response, and localization response as inputs. Then, we construct omni-directional cascaded transformations and obtain the distiller by selecting the advanced distance function and common weight value options. Finally, we present a divide-and-conquer evolutionary algorithm to handle the explosion of the search space. In this strategy, we first evolve the best distiller formulations of individual knowledge inputs and then optimize the combined weights of these multiple distillation losses. DetKDS automates the distillation process without requiring expert design or additional tuning, effectively reducing the teacher-student gap in various scenarios. Based on the analysis of our search results, we provide valuable guidance that contributes to detection distillation designs. Comprehensive experiments on different detectors demonstrate that DetKDS outperforms state-of-the-art methods in detection and instance segmentation tasks. For instance, DetKDS achieves significant gains than baseline detectors: $+3.7$, $+4.1$, $+4.0$, $+3.7$, and $+3.5$ AP on RetinaNet, Faster-RCNN, FCOS, RepPoints, and GFL, respectively. Code at: https://github.com/lliai/DetKDS.