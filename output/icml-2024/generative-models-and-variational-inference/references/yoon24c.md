---
title: "FRAG: Frequency Adapting Group for Diffusion Video Editing"
source: "https://proceedings.mlr.press/v235/yoon24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yoon24c/yoon24c.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['video-editing', 'diffusion-models', 'frequency-adaptation', 'consistency']
venue: "ICML 2024"
tldr: "A frequency adapting group mechanism is proposed for diffusion-based video editing to achieve smooth and consistent modifications."
---

# FRAG: Frequency Adapting Group for Diffusion Video Editing

**Source**: [https://proceedings.mlr.press/v235/yoon24c.html](https://proceedings.mlr.press/v235/yoon24c.html)

**TLDR**: A frequency adapting group mechanism is proposed for diffusion-based video editing to achieve smooth and consistent modifications.

## Abstract

In video editing, the hallmark of a quality edit lies in its consistent and unobtrusive adjustment. Modification, when integrated, must be smooth and subtle, preserving the natural flow and aligning seamlessly with the original vision. Therefore, our primary focus is on overcoming the current challenges in high quality edit to ensure that each edit enhances the final product without disrupting its intended essence. However, quality deterioration such as blurring and flickering is routinely observed in recent diffusion video editing systems. We confirm that this deterioration often stems from high-frequency leak: the diffusion model fails to accurately synthesize high-frequency components during denoising process. To this end, we devise Frequency Adapting Group (FRAG) which enhances the video quality in terms of consistency and fidelity by introducing a novel receptive field branch to preserve high-frequency components during the denoising process. FRAG is performed in a model-agnostic manner without additional training and validates the effectiveness on video editing benchmarks (i.e., TGVE, DAVIS).