---
title: "dopanim: A Dataset of Doppelganger Animals with Noisy Annotations from Multiple Humans"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5b44b99d012922011f0be1031a98c4f9-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['noisy-annotations', 'doppelganger-animals', 'multi-annotator']
venue: "NeurIPS 2024"
tldr: "Introduces dopanim, a dataset of visually similar animals with noisy multi-human annotations for benchmarking noise-robust learning methods."
---

# dopanim: A Dataset of Doppelganger Animals with Noisy Annotations from Multiple Humans

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5b44b99d012922011f0be1031a98c4f9-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/5b44b99d012922011f0be1031a98c4f9-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces dopanim, a dataset of visually similar animals with noisy multi-human annotations for benchmarking noise-robust learning methods.

## Abstract

Human annotators typically provide annotated data for training machine learning models, such as neural networks. Yet, human annotations are subject to noise, impairing generalization performances. Methodological research on approaches counteracting noisy annotations requires corresponding datasets for a meaningful empirical evaluation. Consequently, we introduce a novel benchmark dataset, dopanim, consisting of about 15,750 animal images of 15 classes with ground truth labels. For approximately 10,500 of these images, 20 humans provided over 52,000 annotations with an accuracy of circa 67%. Its key attributes include (1) the challenging task of classifying doppelganger animals, (2) human-estimated likelihoods as annotations, and (3) annotator metadata. We benchmark well-known multi-annotator learning approaches using seven variants of this dataset and outline further evaluation use cases such as learning beyond hard class labels and active learning. Our dataset and a comprehensive codebase are publicly available to emulate the data collection process and to reproduce all empirical results.