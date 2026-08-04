---
title: "Understanding Unimodal Bias in Multimodal Deep Linear Networks"
source: "https://proceedings.mlr.press/v235/zhang24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24aa/zhang24aa.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['multimodal-learning', 'unimodal-bias', 'linear-networks']
venue: "ICML 2024"
tldr: "Develops a theoretical framework explaining unimodal bias in multimodal deep linear networks and conditions under which it arises."
---

# Understanding Unimodal Bias in Multimodal Deep Linear Networks

**Source**: [https://proceedings.mlr.press/v235/zhang24aa.html](https://proceedings.mlr.press/v235/zhang24aa.html)

**TLDR**: Develops a theoretical framework explaining unimodal bias in multimodal deep linear networks and conditions under which it arises.

## Abstract

Using multiple input streams simultaneously to train multimodal neural networks is intuitively advantageous but practically challenging. A key challenge is unimodal bias, where a network overly relies on one modality and ignores others during joint training. We develop a theory of unimodal bias with multimodal deep linear networks to understand how architecture and data statistics influence this bias. This is the first work to calculate the duration of the unimodal phase in learning as a function of the depth at which modalities are fused within the network, dataset statistics, and initialization. We show that the deeper the layer at which fusion occurs, the longer the unimodal phase. A long unimodal phase can lead to a generalization deficit and permanent unimodal bias in the overparametrized regime. Our results, derived for multimodal linear networks, extend to nonlinear networks in certain settings. Taken together, this work illuminates pathologies of multimodal learning under joint training, showing that late and intermediate fusion architectures can give rise to long unimodal phases and permanent unimodal bias. Our code is available at: https://yedizhang.github.io/unimodal-bias.html.