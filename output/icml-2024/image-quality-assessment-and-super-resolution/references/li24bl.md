---
title: "Compress Clean Signal from Noisy Raw Image: A Self-Supervised Approach"
source: "https://proceedings.mlr.press/v235/li24bl.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bl/li24bl.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'image-quality-assessment-and-super-resolution']
tags: ['image-compression', 'raw-images', 'self-supervised-denoising']
venue: "ICML 2024"
tldr: "Presents a self-supervised approach to compress clean signals from noisy raw images by jointly handling noise and compression."
---

# Compress Clean Signal from Noisy Raw Image: A Self-Supervised Approach

**Source**: [https://proceedings.mlr.press/v235/li24bl.html](https://proceedings.mlr.press/v235/li24bl.html)

**TLDR**: Presents a self-supervised approach to compress clean signals from noisy raw images by jointly handling noise and compression.

## Abstract

Raw images offer unique advantages in many low-level visual tasks due to their unprocessed nature. However, this unprocessed state accentuates noise, making raw images challenging to compress effectively. Current compression methods often overlook the ubiquitous noise in raw space, leading to increased bitrates and reduced quality. In this paper, we propose a novel raw image compression scheme that selectively compresses the noise-free component of the input, while discarding its real noise using a self-supervised approach. By excluding noise from the bitstream, both the coding efficiency and reconstruction quality are significantly enhanced. We curate an full-day dataset of raw images with calibrated noise parameters and reference images to evaluate the performance of models under a wide range of input signal-noise ratios. Experimental results demonstrate that our method surpasses existing compression techniques, achieving a more advantageous rate-distortion balance with improvements ranging from +2 to +10dB and yielding a bit saving of 2 to 50 times. The code will be released upon paper acceptance.