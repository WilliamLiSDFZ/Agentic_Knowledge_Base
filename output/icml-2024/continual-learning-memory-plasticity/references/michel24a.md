---
title: "Rethinking Momentum Knowledge Distillation in Online Continual Learning"
source: "https://proceedings.mlr.press/v235/michel24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/michel24a/michel24a.pdf"
categories: ['continual-learning-memory-plasticity', 'knowledge-distillation-methods-and-applications']
tags: ['online-continual-learning', 'knowledge-distillation', 'momentum']
venue: "ICML 2024"
tldr: "Rethinks momentum-based knowledge distillation strategies for online continual learning to better handle catastrophic forgetting under single-pass data constraints."
---

# Rethinking Momentum Knowledge Distillation in Online Continual Learning

**Source**: [https://proceedings.mlr.press/v235/michel24a.html](https://proceedings.mlr.press/v235/michel24a.html)

**TLDR**: Rethinks momentum-based knowledge distillation strategies for online continual learning to better handle catastrophic forgetting under single-pass data constraints.

## Abstract

Online Continual Learning (OCL) addresses the problem of training neural networks on a continuous data stream where multiple classification tasks emerge in sequence. In contrast to offline Continual Learning, data can be seen only once in OCL, which is a very severe constraint. In this context, replay-based strategies have achieved impressive results and most state-of-the-art approaches heavily depend on them. While Knowledge Distillation (KD) has been extensively used in offline Continual Learning, it remains under-exploited in OCL, despite its high potential. In this paper, we analyze the challenges in applying KD to OCL and give empirical justifications. We introduce a direct yet effective methodology for applying Momentum Knowledge Distillation (MKD) to many flagship OCL methods and demonstrate its capabilities to enhance existing approaches. In addition to improving existing state-of-the-art accuracy by more than $10%$ points on ImageNet100, we shed light on MKD internal mechanics and impacts during training in OCL. We argue that similar to replay, MKD should be considered a central component of OCL. The code is available at https://github.com/Nicolas1203/mkd_ocl.