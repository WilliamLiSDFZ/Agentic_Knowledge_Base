---
title: "Vocal Call Locator Benchmark (VCL) for localizing rodent vocalizations from multi-channel audio"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c00d37d6b04d73b870b963a4d70051c1-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['audio-visual-speech-processing-and-benchmarks', 'wearable-biosignal-gesture-activity-benchmarks']
tags: ['rodent-vocalization', 'multi-channel-audio', 'sound-localization']
venue: "NeurIPS 2024"
tldr: "The Vocal Call Locator benchmark provides a dataset and evaluation framework for localizing rodent vocalizations from multi-channel audio recordings."
---

# Vocal Call Locator Benchmark (VCL) for localizing rodent vocalizations from multi-channel audio

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c00d37d6b04d73b870b963a4d70051c1-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c00d37d6b04d73b870b963a4d70051c1-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: The Vocal Call Locator benchmark provides a dataset and evaluation framework for localizing rodent vocalizations from multi-channel audio recordings.

## Abstract

Understanding the behavioral and neural dynamics of social interactions is a goalof contemporary neuroscience. Many machine learning methods have emergedin recent years to make sense of complex video and neurophysiological data thatresult from these experiments. Less focus has been placed on understanding howanimals process acoustic information, including social vocalizations. A criticalstep to bridge this gap is determining the senders and receivers of acoustic infor-mation in social interactions. While sound source localization (SSL) is a classicproblem in signal processing, existing approaches are limited in their ability tolocalize animal-generated sounds in standard laboratory environments. Advancesin deep learning methods for SSL are likely to help address these limitations,however there are currently no publicly available models, datasets, or benchmarksto systematically evaluate SSL algorithms in the domain of bioacoustics. Here,we present the VCL Benchmark: the first large-scale dataset for benchmarkingSSL algorithms in rodents. We acquired synchronized video and multi-channelaudio recordings of 767,295 sounds with annotated ground truth sources across 9conditions. The dataset provides benchmarks which evaluate SSL performance onreal data, simulated acoustic data, and a mixture of real and simulated data. Weintend for this benchmark to facilitate knowledge transfer between the neuroscienceand acoustic machine learning communities, which have had limited overlap.