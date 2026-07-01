---
title: "Rethinking the Evaluation of Out-of-Distribution Detection: A Sorites Paradox"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a37bcf136d2e51eac4f74b33ee21c277-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['out-of-distribution-detection', 'benchmark-evaluation', 'semantic-ambiguity']
venue: "NeurIPS 2024"
tldr: "This paper identifies a Sorites Paradox in OOD detection benchmarks caused by semantically marginal OOD samples and proposes improved evaluation methodology."
---

# Rethinking the Evaluation of Out-of-Distribution Detection: A Sorites Paradox

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a37bcf136d2e51eac4f74b33ee21c277-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a37bcf136d2e51eac4f74b33ee21c277-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: This paper identifies a Sorites Paradox in OOD detection benchmarks caused by semantically marginal OOD samples and proposes improved evaluation methodology.

## Abstract

Most existing out-of-distribution (OOD) detection benchmarks classify samples with novel labels as the OOD data. However, some marginal OOD samples actually have close semantic contents to the in-distribution (ID) sample, which makes determining the OOD sample a Sorites Paradox. In this paper, we construct a benchmark named Incremental Shift OOD (IS-OOD) to address the issue, in which we divide the test samples into subsets with different semantic and covariate shift degrees relative to the ID dataset. The data division is achieved through a shift measuring method based on our proposed Language Aligned Image feature Decomposition (LAID). Moreover, we construct a Synthetic Incremental Shift (Syn-IS) dataset that contains high-quality generated images with more diverse covariate contents to complement the IS-OOD benchmark. We evaluate current OOD detection methods on our benchmark and find several important insights: (1) The performance of most OOD detection methods significantly improves as the semantic shift increases; (2) Some methods like GradNorm may have different OOD detection mechanisms as they rely less on semantic shifts to make decisions; (3) Excessive covariate shifts in the image are also likely to be considered as OOD for some methods. Our code and data are released in https://github.com/qqwsad5/IS-OOD.