---
title: "Semi-Truths: A Large-Scale Dataset of AI-Augmented Images for Evaluating Robustness of AI-Generated Image detectors"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d5cdf7e56422f2a229c497dd89c3b995-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'generative-models-for-visual-style-and-appearance']
tags: ['AI-generated-image-detection', 'robustness', 'semi-synthetic-dataset']
venue: "NeurIPS 2024"
tldr: "A large-scale dataset of AI-augmented images to benchmark and evaluate the robustness of AI-generated image detectors against partial diffusion-based manipulations."
---

# Semi-Truths: A Large-Scale Dataset of AI-Augmented Images for Evaluating Robustness of AI-Generated Image detectors

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d5cdf7e56422f2a229c497dd89c3b995-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/d5cdf7e56422f2a229c497dd89c3b995-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A large-scale dataset of AI-augmented images to benchmark and evaluate the robustness of AI-generated image detectors against partial diffusion-based manipulations.

## Abstract

Text-to-image diffusion models have impactful applications in art, design, and entertainment, yet these technologies also pose significant risks by enabling the creation and dissemination of misinformation. Although recent advancements have produced AI-generated image detectors that claim robustness against various augmentations, their true effectiveness remains uncertain. Do these detectors reliably identify images with different levels of augmentation? Are they biased toward specific scenes or data distributions? To investigate, we introduce **Semi-Truths**, featuring $27,600$ real images, $223,400$ masks, and $1, 329, 155$ AI-augmented images that feature targeted and localized perturbations produced using diverse augmentation techniques, diffusion models, and data distributions. Each augmented image is accompanied by metadata for standardized and targeted evaluation of detector robustness. Our findings suggest that state-of-the-art detectors exhibit varying sensitivities to the types and degrees of perturbations, data distributions, and augmentation methods used, offering new insights into their performance and limitations. The code for the augmentation and evaluation pipeline is available at https://github.com/J-Kruk/SemiTruths.