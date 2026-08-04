---
title: "Premier-TACO is a Few-Shot Policy Learner: Pretraining Multitask Representation via Temporal Action-Driven Contrastive Loss"
source: "https://proceedings.mlr.press/v235/zheng24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24g/zheng24g.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['few-shot-learning', 'multitask-pretraining', 'contrastive-learning', 'sequential-decision-making']
venue: "ICML 2024"
tldr: "Premier-TACO pretrains multitask temporal representations via contrastive loss to improve few-shot policy learning in sequential decision-making."
---

# Premier-TACO is a Few-Shot Policy Learner: Pretraining Multitask Representation via Temporal Action-Driven Contrastive Loss

**Source**: [https://proceedings.mlr.press/v235/zheng24g.html](https://proceedings.mlr.press/v235/zheng24g.html)

**TLDR**: Premier-TACO pretrains multitask temporal representations via contrastive loss to improve few-shot policy learning in sequential decision-making.

## Abstract

We present Premier-TACO, a multitask feature representation learning approach designed to improve few-shot policy learning efficiency in sequential decision-making tasks. Premier-TACO leverages a subset of multitask offline datasets for pretraining a general feature representation, which captures critical environmental dynamics and is fine-tuned using minimal expert demonstrations. It advances the temporal action contrastive learning (TACO) objective, known for state-of-the-art results in visual control tasks, by incorporating a novel negative example sampling strategy. This strategy is crucial in significantly boosting TACO’s computational efficiency, making large-scale multitask offline pretraining feasible. Our extensive empirical evaluation in a diverse set of continuous control benchmarks including Deepmind Control Suite, MetaWorld, and LIBERO demonstrate Premier-TACO’s effective- ness in pretraining visual representations, significantly enhancing few-shot imitation learning of novel tasks.