---
title: "Neural Image Compression with Text-guided Encoding for both Pixel-level and Perceptual Fidelity"
source: "https://proceedings.mlr.press/v235/lee24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24n/lee24n.pdf"
categories: ['image-quality-assessment-and-super-resolution', 'generative-models-and-variational-inference']
tags: ['image-compression', 'text-guided', 'perceptual-fidelity', 'pixel-fidelity']
venue: "ICML 2024"
tldr: "Develops a text-guided image compression method that jointly maintains both pixel-level and perceptual fidelity."
---

# Neural Image Compression with Text-guided Encoding for both Pixel-level and Perceptual Fidelity

**Source**: [https://proceedings.mlr.press/v235/lee24n.html](https://proceedings.mlr.press/v235/lee24n.html)

**TLDR**: Develops a text-guided image compression method that jointly maintains both pixel-level and perceptual fidelity.

## Abstract

Recent advances in text-guided image compression have shown great potential to enhance the perceptual quality of reconstructed images. These methods, however, tend to have significantly degraded pixel-wise fidelity, limiting their practicality. To fill this gap, we develop a new text-guided image compression algorithm that achieves both high perceptual and pixel-wise fidelity. In particular, we propose a compression framework that leverages text information mainly by text-adaptive encoding and training with joint image-text loss. By doing so, we avoid decoding based on text-guided generative models—known for high generative diversity—and effectively utilize the semantic information of text at a global level. Experimental results on various datasets show that our method can achieve high pixel-level and perceptual quality, with either human- or machine-generated captions. In particular, our method outperforms all baselines in terms of LPIPS, with some room for even more improvements when we use more carefully generated captions.