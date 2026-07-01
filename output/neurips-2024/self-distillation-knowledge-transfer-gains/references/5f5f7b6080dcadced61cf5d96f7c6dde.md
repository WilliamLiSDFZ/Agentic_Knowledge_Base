---
title: "Color-Oriented Redundancy Reduction in Dataset Distillation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5f5f7b6080dcadced61cf5d96f7c6dde-Abstract-Conference.html"
categories: ['self-distillation-knowledge-transfer-gains', 'deep-learning-optimization-and-generalization-theory']
tags: ['dataset-distillation', 'color-redundancy', 'training-efficiency']
venue: "NeurIPS 2024"
tldr: "Proposes color-oriented redundancy reduction in dataset distillation to improve condensed dataset quality and training efficiency."
---

# Color-Oriented Redundancy Reduction in Dataset Distillation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5f5f7b6080dcadced61cf5d96f7c6dde-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/5f5f7b6080dcadced61cf5d96f7c6dde-Abstract-Conference.html)

**TLDR**: Proposes color-oriented redundancy reduction in dataset distillation to improve condensed dataset quality and training efficiency.

## Abstract

Dataset Distillation (DD) is designed to generate condensed representations of extensive image datasets, enhancing training efficiency. Despite recent advances, there remains considerable potential for improvement, particularly in addressing the notable redundancy within the color space of distilled images. In this paper, we propose a two-fold optimization strategy to minimize color redundancy at the individual image and overall dataset levels, respectively. At the image level, we employ a palette network, a specialized neural network, to dynamically allocate colors from a reduced color space to each pixel. The palette network identifies essential areas in synthetic images for model training, and consequently assigns more unique colors to them. At the dataset level, we develop a color-guided initialization strategy to minimize redundancy among images. Representative images with the least replicated color patterns are selected based on the information gain. A comprehensive performance study involving various datasets and evaluation scenarios is conducted, demonstrating the superior performance of our proposed color-aware DD compared to existing DD methods.