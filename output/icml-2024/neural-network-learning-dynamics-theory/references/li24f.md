---
title: "Improving Neural Logic Machines via Failure Reflection"
source: "https://proceedings.mlr.press/v235/li24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24f/li24f.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'neural-network-learning-dynamics-theory']
tags: ['neural-logic-machines', 'neural-symbolic', 'failure-reflection', 'reasoning', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "Enhances neural logic machines by incorporating failure reflection mechanisms to improve reasoning generalization and decision-making performance."
---

# Improving Neural Logic Machines via Failure Reflection

**Source**: [https://proceedings.mlr.press/v235/li24f.html](https://proceedings.mlr.press/v235/li24f.html)

**TLDR**: Enhances neural logic machines by incorporating failure reflection mechanisms to improve reasoning generalization and decision-making performance.

## Abstract

Reasoning is a fundamental ability towards artificial general intelligence (AGI). Fueled by the success of deep learning, the neural logic machines models (NLMs) have introduced novel neural-symbolic structures and demonstrate great performance and generalization on reasoning and decision-making tasks. However, the original training approaches of the NLMs are still far from perfect, the models would repeat similar mistakes during the training process which leads to sub-optimal performance. To mitigate this issue, we present a novel framework named Failure Reflection Guided Regularizer (FRGR). FRGR first dynamically identifies and summarizes the root cause if the model repeats similar mistakes during training. Then it penalizes the model if it makes similar mistakes in future training iterations. In this way, the model is expected to avoid repeating errors of similar root causes and converge faster to a better-performed optimum. Experimental results on multiple relational reasoning and decision-making tasks demonstrate the effectiveness of FRGR in improving performance, generalization, training efficiency, and data efficiency.