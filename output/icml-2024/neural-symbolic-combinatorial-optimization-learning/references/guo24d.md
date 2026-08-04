---
title: "ACM-MILP: Adaptive Constraint Modification via Grouping and Selection for Hardness-Preserving MILP Instance Generation"
source: "https://proceedings.mlr.press/v235/guo24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guo24d/guo24d.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'optimization-algorithms-convergence-theory']
tags: ['MILP', 'instance-generation', 'constraint-modification', 'combinatorial-optimization', 'data-augmentation']
venue: "ICML 2024"
tldr: "An adaptive constraint modification method that generates hardness-preserving MILP instances via grouping and selection."
---

# ACM-MILP: Adaptive Constraint Modification via Grouping and Selection for Hardness-Preserving MILP Instance Generation

**Source**: [https://proceedings.mlr.press/v235/guo24d.html](https://proceedings.mlr.press/v235/guo24d.html)

**TLDR**: An adaptive constraint modification method that generates hardness-preserving MILP instances via grouping and selection.

## Abstract

Data plays a pivotal role in the development of both classic and learning-based methods for Mixed-Integer Linear Programming (MILP). However, the scarcity of data in real-world applications underscores the necessity for MILP instance generation methods. Currently, these methods primarily rely on iterating random single-constraint modifications, disregarding the underlying problem structure with constraint interrelations, thereby leading to compromised quality and solvability. In this paper, we propose ACM-MILP, a framework for MILP instance generation, to achieve adaptive constraint modification and constraint interrelation modeling. It employs an adaptive constraint selection mechanism based on probability estimation within the latent space to preserve instance characteristics. Meanwhile, it detects and groups strongly related constraints through community detection, enabling collective modifications that account for constraint dependencies. Experimental results show significant improvements in problem-solving hardness similarity under our framework. Additionally, in the downstream task, we showcase the efficacy of our generated instances for hyperparameter tuning. Source code is available: https://github.com/Thinklab-SJTU/ACM-MILP.