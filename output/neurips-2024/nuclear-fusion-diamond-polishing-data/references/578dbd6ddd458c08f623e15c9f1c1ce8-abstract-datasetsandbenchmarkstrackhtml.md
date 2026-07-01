---
title: "Nuclear Fusion Diamond Polishing Dataset"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/578dbd6ddd458c08f623e15c9f1c1ce8-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['nuclear-fusion-diamond-polishing-data']
tags: ['nuclear-fusion', 'diamond-polishing', 'inertial-confinement', 'surface-quality', 'dataset']
venue: "NeurIPS 2024"
tldr: "Introduces a dataset for monitoring and analyzing the polishing process of high-density carbon shells used as targets in inertial confinement fusion."
---

# Nuclear Fusion Diamond Polishing Dataset

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/578dbd6ddd458c08f623e15c9f1c1ce8-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/578dbd6ddd458c08f623e15c9f1c1ce8-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a dataset for monitoring and analyzing the polishing process of high-density carbon shells used as targets in inertial confinement fusion.

## Abstract

In the Inertial Confinement Fusion (ICF) process, roughly a 2mm spherical shell made of high-density carbon is used as a target for laser beams, which compress and heat it to energy levels needed for high fusion yield in nuclear fusion. These shells are polished meticulously to meet the standards for a fusion shot. However, the polishing of these shells involves multiple stages, with each stage taking several hours. To make sure that the polishing process is advancing in the right direction, we are able to measure the shell surface roughness. This measurement, however, is very labor-intensive, time-consuming, and requires a human operator. To help improve the polishing process we have released the first dataset to the public that consists of raw vibration signals with the corresponding polishing surface roughness changes. We show that this dataset can be used with a variety of neural network based methods for prediction of the change of polishing surface roughness, hence eliminating the need for the time-consuming manual process. This is the first dataset of its kind to be released in public and its use will allow the operator to make any necessary changes to the ICF polishing process for optimal results. This dataset contains the raw vibration data of multiple polishing runs with their extracted statistical features and the corresponding surface roughness values. Additionally, to generalize the prediction models to different polishing conditions, we also apply domain adaptation techniques to improve prediction accuracy for conditions unseen by the trained model. The dataset is available in \url{https://junzeliu.github.io/Diamond-Polishing-Dataset/}.