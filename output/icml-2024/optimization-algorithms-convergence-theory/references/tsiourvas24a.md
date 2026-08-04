---
title: "Overcoming the Optimizer’s Curse: Obtaining Realistic Prescriptions from Neural Networks"
source: "https://proceedings.mlr.press/v235/tsiourvas24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tsiourvas24a/tsiourvas24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'optimization-algorithms-convergence-theory']
tags: ['ReLU-networks', 'data-driven-optimization', 'prescriptive-analytics']
venue: "ICML 2024"
tldr: "Proposes methods to obtain optimal and realistic prescriptions from ReLU networks used for data-driven decision-making."
---

# Overcoming the Optimizer’s Curse: Obtaining Realistic Prescriptions from Neural Networks

**Source**: [https://proceedings.mlr.press/v235/tsiourvas24a.html](https://proceedings.mlr.press/v235/tsiourvas24a.html)

**TLDR**: Proposes methods to obtain optimal and realistic prescriptions from ReLU networks used for data-driven decision-making.

## Abstract

We study the problem of obtaining optimal and realistic prescriptions when using ReLU networks for data-driven decision-making. In this setting, the network is used to predict a quantity of interest and then is optimized to retrieve the decisions that maximize the quantity (e.g. find the best prices that maximize revenue). However, optimizing over-parameterized models often produces unrealistic prescriptions, far from the data manifold. This phenomenon is known as the Optimizer’s Curse. To tackle this problem, we model the requirement for the resulting decisions to align with the data manifold as a tractable optimization constraint. This is achieved by reformulating the highly nonlinear Local Outlier Factor (LOF) metric as a single linear or quadratic constraint. To solve the problem efficiently for large networks, we propose an adaptive sampling algorithm that reduces the initial hard-to-solve optimization problem into a small number of significantly easier-to-solve problems by restricting the decision space to realistic polytopes, i.e. polytopes of the decision space that contain at least one realistic data point. Experiments on publicly available networks demonstrate the efficacy and scalability of our approach.