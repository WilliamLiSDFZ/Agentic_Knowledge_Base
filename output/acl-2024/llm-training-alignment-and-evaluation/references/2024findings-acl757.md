---
title: "Choose Your Transformer: Improved Transferability Estimation of Transformer Models on Classification Tasks"
source: "https://aclanthology.org/2024.findings-acl.757/"
categories: ['language-model-representations-and-embedding-spaces', 'llm-training-alignment-and-evaluation']
tags: ['transfer-learning', 'model-selection', 'transformers']
venue: "ACL 2024"
tldr: "An improved method for estimating which pre-trained transformer will perform best on a downstream classification task without exhaustive fine-tuning."
---

# Choose Your Transformer: Improved Transferability Estimation of Transformer Models on Classification Tasks

**Source**: [https://aclanthology.org/2024.findings-acl.757/](https://aclanthology.org/2024.findings-acl.757/)

**TLDR**: An improved method for estimating which pre-trained transformer will perform best on a downstream classification task without exhaustive fine-tuning.

## Abstract

AbstractThere currently exists a multitude of pre-trained transformer language models (LMs) that are readily available. From a practical perspective, this raises the question of which pre-trained LM will perform best if fine-tuned for a specific downstream NLP task. However, exhaustively fine-tuning all available LMs to determine the best-fitting model is computationally infeasible. To address this problem, we present an approach that inexpensively estimates a ranking of the expected performance of a given set of candidate LMs for a given task. Following a layer-wise representation analysis, we extend existing approaches such as H-score and LogME by aggregating representations across all layers of the transformer model. We present an extensive analysis of 20 transformer LMs, 6 downstream NLP tasks, and various estimators (linear probing, kNN, H-score, and LogME). Our evaluation finds that averaging the layer representations significantly improves the Pearson correlation coefficient between the true model ranks and the estimate, increasing from 0.58 to 0.86 for LogME and from 0.65 to 0.88 for H-score.