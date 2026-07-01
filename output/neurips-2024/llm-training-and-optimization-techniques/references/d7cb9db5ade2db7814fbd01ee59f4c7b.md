---
title: "Multiple Physics Pretraining for Spatiotemporal Surrogate Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d7cb9db5ade2db7814fbd01ee59f4c7b-Abstract-Conference.html"
categories: ['physics-informed-neural-operators-and-simulations', 'llm-training-and-optimization-techniques']
tags: ['physics-pretraining', 'spatiotemporal-surrogate', 'transformer-autoregressive']
venue: "NeurIPS 2024"
tldr: "Multiple physics pretraining trains a single transformer backbone autoregressively across diverse physical systems for generalizable spatiotemporal surrogate modeling."
---

# Multiple Physics Pretraining for Spatiotemporal Surrogate Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d7cb9db5ade2db7814fbd01ee59f4c7b-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d7cb9db5ade2db7814fbd01ee59f4c7b-Abstract-Conference.html)

**TLDR**: Multiple physics pretraining trains a single transformer backbone autoregressively across diverse physical systems for generalizable spatiotemporal surrogate modeling.

## Abstract

We introduce multiple physics pretraining (MPP), an autoregressive task-agnostic pretraining approach for physical surrogate modeling of spatiotemporal systems with transformers. In MPP, rather than training one model on a specific physical system, we train a backbone model to predict the dynamics of multiple heterogeneous physical systems simultaneously in order to learn features that are broadly useful across systems and facilitate transfer. In order to learn effectively in this setting, we introduce a shared embedding and normalization strategy that projects the fields of multiple systems into a shared embedding space. We validate the efficacy of our approach on both pretraining and downstream tasks over a broad fluid mechanics-oriented benchmark. We show that a single MPP-pretrained transformer is able to match or outperform task-specific baselines on all pretraining sub-tasks without the need for finetuning. For downstream tasks, we demonstrate that finetuning MPP-trained models results in more accurate predictions across multiple time-steps on systems with previously unseen physical components or higher dimensional systems compared to training from scratch or finetuning pretrained video foundation models. We open-source our code and model weights trained at multiple scales for reproducibility.