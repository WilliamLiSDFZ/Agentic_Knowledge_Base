---
title: "AdsorbDiff: Adsorbate Placement via Conditional Denoising Diffusion"
source: "https://proceedings.mlr.press/v235/kolluru24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kolluru24a/kolluru24a.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['diffusion-models', 'adsorbate-placement', 'catalyst-discovery', 'conditional-denoising', 'materials-science']
venue: "ICML 2024"
tldr: "A conditional denoising diffusion model for determining optimal adsorbate configurations on catalyst slabs."
---

# AdsorbDiff: Adsorbate Placement via Conditional Denoising Diffusion

**Source**: [https://proceedings.mlr.press/v235/kolluru24a.html](https://proceedings.mlr.press/v235/kolluru24a.html)

**TLDR**: A conditional denoising diffusion model for determining optimal adsorbate configurations on catalyst slabs.

## Abstract

Determining the optimal configuration of adsorbates on a slab (adslab) is pivotal in the exploration of novel catalysts across diverse applications. Traditionally, the quest for the lowest energy adslab configuration involves placing the adsorbate onto the slab followed by an optimization process. Prior methodologies have relied on heuristics, problem-specific intuitions, or brute-force approaches to guide adsorbate placement. In this work, we propose a novel framework for adsorbate placement using denoising diffusion. The model is designed to predict the optimal adsorbate site and orientation corresponding to the lowest energy configuration. Further, we have an end-to-end evaluation framework where diffusion-predicted adslab configuration is optimized with a pretrained machine learning force field and finally evaluated with Density Functional Theory (DFT). Our findings demonstrate an acceleration of up to 5x or 3.5x improvement in accuracy compared to the previous best approach. Given the novelty of this framework and application, we provide insights into the impact of pretraining, model architectures, and conduct extensive experiments to underscore the significance of this approach.