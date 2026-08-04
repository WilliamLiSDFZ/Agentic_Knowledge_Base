---
title: "DIDI: Diffusion-Guided Diversity for Offline Behavioral Generation"
source: "https://proceedings.mlr.press/v235/liu24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24s/liu24s.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['diffusion-models', 'offline-RL', 'behavioral-diversity']
venue: "ICML 2024"
tldr: "DIDI uses diffusion probabilistic models as priors to generate diverse behaviors from unlabeled offline data."
---

# DIDI: Diffusion-Guided Diversity for Offline Behavioral Generation

**Source**: [https://proceedings.mlr.press/v235/liu24s.html](https://proceedings.mlr.press/v235/liu24s.html)

**TLDR**: DIDI uses diffusion probabilistic models as priors to generate diverse behaviors from unlabeled offline data.

## Abstract

In this paper, we propose a novel approach called DIffusion-guided DIversity (DIDI) for offline behavioral generation. The goal of DIDI is to learn a diverse set of skills from a mixture of label-free offline data. We achieve this by leveraging diffusion probabilistic models as priors to guide the learning process and regularize the policy. By optimizing a joint objective that incorporates diversity and diffusion-guided regularization, we encourage the emergence of diverse behaviors while maintaining the similarity to the offline data. Experimental results in four decision-making domains (Push, Kitchen, Humanoid, and D4RL tasks) show that DIDI is effective in discovering diverse and discriminative skills. We also introduce skill stitching and skill interpolation, which highlight the generalist nature of the learned skill space. Further, by incorporating an extrinsic reward function, DIDI enables reward-guided behavior generation, facilitating the learning of diverse and optimal behaviors from sub-optimal data.