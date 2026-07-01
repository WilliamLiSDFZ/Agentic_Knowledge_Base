---
title: "Benchmarking Out-of-Distribution Generalization Capabilities of DNN-based Encoding Models for the Ventral Visual Cortex."
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a27eda1ce7c14f4875f15cf3d1737cc5-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['neural-encoding-models', 'out-of-distribution-generalization', 'visual-cortex']
venue: "NeurIPS 2024"
tldr: "Introduces MacaqueITBench to benchmark OOD generalization of DNN encoding models predicting macaque inferior temporal cortex responses."
---

# Benchmarking Out-of-Distribution Generalization Capabilities of DNN-based Encoding Models for the Ventral Visual Cortex.

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a27eda1ce7c14f4875f15cf3d1737cc5-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a27eda1ce7c14f4875f15cf3d1737cc5-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces MacaqueITBench to benchmark OOD generalization of DNN encoding models predicting macaque inferior temporal cortex responses.

## Abstract

We characterized the generalization capabilities of deep neural network encoding models when predicting neuronal responses from the visual cortex to flashed images. We collected MacaqueITBench, a large-scale dataset of neuronal population responses from the macaque inferior temporal (IT) cortex to over $300,000$ images, comprising $8,233$ unique natural images presented to seven monkeys over $109$ sessions. Using MacaqueITBench, we investigated the impact of distribution shifts on models predicting neuronal activity by dividing the images into Out-Of-Distribution (OOD) train and test splits. The OOD splits included variations in image contrast, hue, intensity, temperature, and saturation. Compared to the performance on in-distribution test images---the conventional way in which these models have been evaluated---models performed worse at predicting neuronal responses to out-of-distribution images, retaining as little as $20\\%$ of the performance on in-distribution test images. Additionally, the relative ranking of different models in terms of their ability to predict neuronal responses changed drastically across OOD shifts. The generalization performance under OOD shifts can be well accounted by a simple image similarity metric---the cosine distance between image representations extracted from a pre-trained object recognition model is a strong predictor of neuronal predictivity under different distribution shifts. The dataset of images, neuronal firing rate recordings, and computational benchmarks are hosted publicly at: https://github.com/Spandan-Madan/benchmarking_ood_generalization_visual_cortex.