---
title: "DiffFPR: Diffusion Prior for Oversampled Fourier Phase Retrieval"
source: "https://proceedings.mlr.press/v235/li24bj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bj/li24bj.pdf"
categories: ['sparse-phase-retrieval-with-priors', 'generative-models-and-variational-inference']
tags: ['phase-retrieval', 'diffusion-prior', 'Fourier-oversampling']
venue: "ICML 2024"
tldr: "Leverages diffusion model priors to address ambiguity in oversampled Fourier phase retrieval for multi-channel image recovery."
---

# DiffFPR: Diffusion Prior for Oversampled Fourier Phase Retrieval

**Source**: [https://proceedings.mlr.press/v235/li24bj.html](https://proceedings.mlr.press/v235/li24bj.html)

**TLDR**: Leverages diffusion model priors to address ambiguity in oversampled Fourier phase retrieval for multi-channel image recovery.

## Abstract

This paper tackled the challenging Fourier phase retrieval problem, the absolute uniqueness of which does not hold. The existence of equivalent solution (a.k.a. trivial solution ambiguity) hinders the successful recovery, especially for multi-channel color image. The traditional iterative engine, such as the Relaxed Averaged Alternating Reflections (RAAR), can be applied to reconstruct the image channel-wisely. However, due to the relative uniqueness of the solution, the restoration is not automatically aligned with the accurate orientation for each channel, resulting in a reconstructed image that deviates significantly from the true solution manifold. To address this issue, by penalizing the mismatch of the image channels, a diffusion model as the strong prior of the color image is integrated into the iterative engine. The combination of the traditional iterative engine and the diffusion model provides an effective solution to the oversampled Fourier phase retrieval. The formed algorithm, DiffFPR, is validated by experiments. The code is available at https://github.com/Chilie/DiffFPR.