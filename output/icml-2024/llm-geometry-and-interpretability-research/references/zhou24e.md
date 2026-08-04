---
title: "On the Emergence of Cross-Task Linearity in Pretraining-Finetuning Paradigm"
source: "https://proceedings.mlr.press/v235/zhou24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24e/zhou24e.pdf"
categories: ['llm-geometry-and-interpretability-research', 'neural-network-learning-dynamics-theory']
tags: ['pretraining-finetuning', 'task-arithmetic', 'linear-mode-connectivity']
venue: "ICML 2024"
tldr: "Discovers a cross-task linearity phenomenon in fine-tuned models from shared pretrained checkpoints, explaining the effectiveness of task arithmetic for model merging."
---

# On the Emergence of Cross-Task Linearity in Pretraining-Finetuning Paradigm

**Source**: [https://proceedings.mlr.press/v235/zhou24e.html](https://proceedings.mlr.press/v235/zhou24e.html)

**TLDR**: Discovers a cross-task linearity phenomenon in fine-tuned models from shared pretrained checkpoints, explaining the effectiveness of task arithmetic for model merging.

## Abstract

The pretraining-finetuning paradigm has become the prevailing trend in modern deep learning. In this work, we discover an intriguing linear phenomenon in models that are initialized from a common pretrained checkpoint and finetuned on different tasks, termed as Cross-Task Linearity (CTL). Specifically, we show that if we linearly interpolate the weights of two finetuned models, the features in the weight-interpolated model are often approximately equal to the linear interpolation of features in two finetuned models at each layer. We provide comprehensive empirical evidence supporting that CTL consistently occurs for finetuned models that start from the same pretrained checkpoint. We conjecture that in the pretraining-finetuning paradigm, neural networks approximately function as linear maps, mapping from the parameter space to the feature space. Based on this viewpoint, our study unveils novel insights into explaining model merging/editing, particularly by translating operations from the parameter space to the feature space. Furthermore, we delve deeper into the root cause for the emergence of CTL, highlighting the role of pretraining.