---
title: "Initializing Variable-sized Vision Transformers from Learngene with Learnable Transformation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4c5e2bcbf21bdf40d75fddad0bd43dc9-Abstract-Conference.html"
categories: ['self-distillation-knowledge-transfer-gains']
tags: ['learngene', 'vision-transformers', 'weight-initialization']
venue: "NeurIPS 2024"
tldr: "Introduces learnable transformations within the Learngene framework to initialize variable-sized Vision Transformers accommodating diverse resource constraints."
---

# Initializing Variable-sized Vision Transformers from Learngene with Learnable Transformation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4c5e2bcbf21bdf40d75fddad0bd43dc9-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/4c5e2bcbf21bdf40d75fddad0bd43dc9-Abstract-Conference.html)

**TLDR**: Introduces learnable transformations within the Learngene framework to initialize variable-sized Vision Transformers accommodating diverse resource constraints.

## Abstract

In practical scenarios, it is necessary to build variable-sized models to accommodate diverse resource constraints, where weight initialization serves as a crucial step preceding training. The recently introduced Learngene framework firstly learns one compact module, termed learngene, from a large well-trained model, and then transforms learngene to initialize variable-sized models. However, the existing Learngene methods provide limited guidance on transforming learngene, where transformation mechanisms are manually designed and generally lack a learnable component. Moreover, these methods only consider transforming learngene along depth dimension, thus constraining the flexibility of learngene. Motivated by these concerns, we propose a novel and effective Learngene approach termed LeTs (Learnable Transformation), where we transform the learngene module along both width and depth dimension with a set of learnable matrices for flexible variablesized model initialization. Specifically, we construct an auxiliary model comprising the compact learngene module and learnable transformation matrices, enabling both components to be trained. To meet the varying size requirements of target models, we select specific parameters from well-trained transformation matrices to adaptively transform the learngene, guided by strategies such as continuous selection and magnitude-wise selection. Extensive experiments on ImageNet-1K demonstrate that Des-Nets initialized via LeTs outperform those with 100-epoch from scratch training after only 1 epoch tuning. When transferring to downstream image classification tasks, LeTs achieves better results while outperforming from scratch training after about 10 epochs within a 300-epoch training schedule.