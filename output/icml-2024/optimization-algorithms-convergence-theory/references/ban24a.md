---
title: "Fair Resource Allocation in Multi-Task Learning"
source: "https://proceedings.mlr.press/v235/ban24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ban24a/ban24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['multi-task-learning', 'fair-optimization', 'gradient-conflicts']
venue: "ICML 2024"
tldr: "A fair resource allocation framework for multi-task learning is proposed to address conflicting gradients across tasks."
---

# Fair Resource Allocation in Multi-Task Learning

**Source**: [https://proceedings.mlr.press/v235/ban24a.html](https://proceedings.mlr.press/v235/ban24a.html)

**TLDR**: A fair resource allocation framework for multi-task learning is proposed to address conflicting gradients across tasks.

## Abstract

By jointly learning multiple tasks, multi-task learning (MTL) can leverage the shared knowledge across tasks, resulting in improved data efficiency and generalization performance. However, a major challenge in MTL lies in the presence of conflicting gradients, which can hinder the fair optimization of some tasks and subsequently impede MTL’s ability to achieve better overall performance. Inspired by fair resource allocation in communication networks, we formulate the optimization of MTL as a utility maximization problem, where the loss decreases across tasks are maximized under different fairness measurements. To address the problem, we propose FairGrad, a novel optimization objective. FairGrad not only enables flexible emphasis on certain tasks but also achieves a theoretical convergence guarantee. Extensive experiments demonstrate that our method can achieve state-of-the-art performance among gradient manipulation methods on a suite of multi-task benchmarks in supervised learning and reinforcement learning. Furthermore, we incorporate the idea of $\alpha$-fairness into the loss functions of various MTL methods. Extensive empirical studies demonstrate that their performance can be significantly enhanced. Code is available at https://github.com/OptMN-Lab/fairgrad.