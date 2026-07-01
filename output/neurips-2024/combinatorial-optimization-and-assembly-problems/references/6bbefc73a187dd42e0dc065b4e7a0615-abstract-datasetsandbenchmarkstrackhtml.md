---
title: "Assemblage: Automatic Binary Dataset Construction for Machine Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6bbefc73a187dd42e0dc065b4e7a0615-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['combinatorial-optimization-and-assembly-problems', 'ai-benchmarking-and-evaluation-methodology']
tags: ['binary-analysis', 'dataset-construction', 'reverse-engineering']
venue: "NeurIPS 2024"
tldr: "Presents an automatic pipeline for constructing large-scale high-quality binary code datasets for machine learning-based binary analysis tasks."
---

# Assemblage: Automatic Binary Dataset Construction for Machine Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6bbefc73a187dd42e0dc065b4e7a0615-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/6bbefc73a187dd42e0dc065b4e7a0615-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents an automatic pipeline for constructing large-scale high-quality binary code datasets for machine learning-based binary analysis tasks.

## Abstract

Binary code is pervasive, and binary analysis is a key task in reverse engineering, malware classification, and vulnerability discovery. Unfortunately, while there exist large corpuses of malicious binaries, obtaining high-quality corpuses of benign binaries for modern systems has proven challenging (e.g., due to licensing issues). Consequently, machine learning based pipelines for binary analysis utilize either costly commercial corpuses (e.g., VirusTotal) or open-source binaries (e.g., coreutils) available in limited quantities. To address these issues, we present Assemblage: an extensible cloud-based distributed system that crawls, configures, and builds Windows PE binaries to obtain high-quality binary corpuses suitable for training state-of-the-art models in binary analysis. We have run Assemblage on AWS over the past year, producing 890k Windows PE and 428k Linux ELF binaries across 29 configurations. Assemblage is designed to be both reproducible and extensible, enabling users to publish "recipes" for their datasets, and facilitating the extraction of a wide array of features. We evaluated Assemblage by using its data to train modern learning-based pipelines for compiler provenance and binary function similarity. Our results illustrate the practical need for robust corpuses of high-quality Windows PE binaries in training modern learning-based binary analyses.