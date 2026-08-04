---
title: "A Theory of Fault-Tolerant Learning"
source: "https://proceedings.mlr.press/v235/wu24z.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24z/wu24z.pdf"
categories: ['adversarial-robustness-and-model-security', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['fault-tolerant-learning', 'learning-theory', 'adversarial-faults', 'robustness', 'mission-critical']
venue: "ICML 2024"
tldr: "Introduces a theoretical framework grounded in learning theory for fault-tolerant machine learning in mission-critical applications with real-world faults."
---

# A Theory of Fault-Tolerant Learning

**Source**: [https://proceedings.mlr.press/v235/wu24z.html](https://proceedings.mlr.press/v235/wu24z.html)

**TLDR**: Introduces a theoretical framework grounded in learning theory for fault-tolerant machine learning in mission-critical applications with real-world faults.

## Abstract

Developing machine learning models that account for potential faults encountered in real-world environments presents a fundamental challenge for mission-critical applications. In this paper, we introduce a novel theoretical framework grounded in learning theory for dealing with faults. In particular, we propose a framework called fault-tolerant PAC learning, aimed at identifying the most fault-tolerant models from a given hypothesis class (such as neural networks). We show that if faults occur randomly, fault-tolerant learning is equivalent to regular PAC learning. However, for adversarial faults, we show that the sample complexity of fault-tolerant PAC learning can grow linearly w.r.t. the number of perturbing functions induced by the faults, even for a hypothesis class with VC-dimension 1. We then provide a matching upper bound by restricting the number of perturbing functions. Finally, we show that the linear dependency on the number of perturbing functions can be substantially improved for deletion faults in neural networks. Our work provides a powerful formal framework and avenues for a number of future investigations on the precise characterization of fault-tolerant learning.