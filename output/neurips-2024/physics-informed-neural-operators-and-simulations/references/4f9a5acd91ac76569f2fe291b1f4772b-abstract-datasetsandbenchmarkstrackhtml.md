---
title: "The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4f9a5acd91ac76569f2fe291b1f4772b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['physics-informed-neural-operators-and-simulations', 'ai-benchmarking-and-evaluation-methodology']
tags: ['physics-simulations', 'surrogate-models', 'benchmark-dataset', 'neural-operators', 'diverse-physics']
venue: "NeurIPS 2024"
tldr: "Introduces The Well, a large-scale benchmark dataset of diverse physics simulations designed to evaluate machine learning surrogate models."
---

# The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4f9a5acd91ac76569f2fe291b1f4772b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/4f9a5acd91ac76569f2fe291b1f4772b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces The Well, a large-scale benchmark dataset of diverse physics simulations designed to evaluate machine learning surrogate models.

## Abstract

Machine learning based surrogate models offer researchers powerful tools for accelerating simulation-based workflows. However, as standard datasets in this space often cover small classes of physical behavior, it can be difficult to evaluate the efficacy of new approaches. To address this gap, we introduce the Well: a large-scale collection of datasets containing numerical simulations of a wide variety of spatiotemporal physical systems. The Well draws from domain experts and numerical software developers to provide 15TB of data across 16 datasets covering diverse domains such as biological systems, fluid dynamics, acoustic scattering, as well as magneto-hydrodynamic simulations of extra-galactic fluids or supernova explosions. These datasets can be used individually or as part of a broader benchmark suite. To facilitate usage of the Well, we provide a unified PyTorch interface for training and evaluating models. We demonstrate the function of this library by introducing example baselines that highlight the new challenges posed by the complex dynamics of the Well. The code and data is available at https://github.com/PolymathicAI/the_well.