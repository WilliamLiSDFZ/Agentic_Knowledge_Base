---
title: "Feedback Efficient Online Fine-Tuning of Diffusion Models"
source: "https://proceedings.mlr.press/v235/uehara24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/uehara24a/uehara24a.pdf"
categories: ['generative-models-and-variational-inference', 'data-selection-and-active-learning-methods']
tags: ['diffusion-models', 'fine-tuning', 'reward-feedback']
venue: "ICML 2024"
tldr: "Proposes a feedback-efficient online fine-tuning method for diffusion models to optimize task-specific properties."
---

# Feedback Efficient Online Fine-Tuning of Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/uehara24a.html](https://proceedings.mlr.press/v235/uehara24a.html)

**TLDR**: Proposes a feedback-efficient online fine-tuning method for diffusion models to optimize task-specific properties.

## Abstract

Diffusion models excel at modeling complex data distributions, including those of images, proteins, and small molecules. However, in many cases, our goal is to model parts of the distribution that maximize certain properties: for example, we may want to generate images with high aesthetic quality, or molecules with high bioactivity. It is natural to frame this as a reinforcement learning (RL) problem, in which the objective is to finetune a diffusion model to maximize a reward function that corresponds to some property. Even with access to online queries of the ground-truth reward function, efficiently discovering high-reward samples can be challenging: they might have a low probability in the initial distribution, and there might be many infeasible samples that do not even have a well-defined reward (e.g., unnatural images or physically impossible molecules). In this work, we propose a novel reinforcement learning procedure that efficiently explores on the manifold of feasible samples. We present a theoretical analysis providing a regret guarantee, as well as empirical validation across three domains: images, biological sequences, and molecules.