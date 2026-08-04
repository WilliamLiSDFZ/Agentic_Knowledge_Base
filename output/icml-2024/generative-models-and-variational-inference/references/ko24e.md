---
title: "Stochastic Conditional Diffusion Models for Robust Semantic Image Synthesis"
source: "https://proceedings.mlr.press/v235/ko24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ko24e/ko24e.pdf"
categories: ['generative-models-and-variational-inference', 'learning-with-imperfect-data-and-bias']
tags: ['diffusion-models', 'semantic-image-synthesis', 'robustness', 'noisy-labels', 'conditional-generation']
venue: "ICML 2024"
tldr: "A stochastic conditional diffusion model for robust semantic image synthesis that handles noisy user-provided semantic maps."
---

# Stochastic Conditional Diffusion Models for Robust Semantic Image Synthesis

**Source**: [https://proceedings.mlr.press/v235/ko24e.html](https://proceedings.mlr.press/v235/ko24e.html)

**TLDR**: A stochastic conditional diffusion model for robust semantic image synthesis that handles noisy user-provided semantic maps.

## Abstract

Semantic image synthesis (SIS) is a task to generate realistic images corresponding to semantic maps (labels). However, in real-world applications, SIS often encounters noisy user inputs. To address this, we propose Stochastic Conditional Diffusion Model (SCDM), which is a robust conditional diffusion model that features novel forward and generation processes tailored for SIS with noisy labels. It enhances robustness by stochastically perturbing the semantic label maps through Label Diffusion, which diffuses the labels with discrete diffusion. Through the diffusion of labels, the noisy and clean semantic maps become similar as the timestep increases, eventually becoming identical at $t=T$. This facilitates the generation of an image close to a clean image, enabling robust generation. Furthermore, we propose a class-wise noise schedule to differentially diffuse the labels depending on the class. We demonstrate that the proposed method generates high-quality samples through extensive experiments and analyses on benchmark datasets, including a novel experimental setup simulating human errors during real-world applications. Code is available at https://github.com/mlvlab/SCDM.