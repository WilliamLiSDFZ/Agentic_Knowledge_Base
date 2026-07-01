---
title: "Noisy Ostracods: A Fine-Grained, Imbalanced Real-World Dataset for Benchmarking Robust Machine Learning and Label Correction Methods"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5ab97f475339d66f8bb0a94312f57e40-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['noisy-labels', 'imbalanced-dataset', 'benchmarking']
venue: "NeurIPS 2024"
tldr: "Introduces a real-world noisy ostracod dataset for benchmarking robust machine learning and label correction methods in fine-grained classification."
---

# Noisy Ostracods: A Fine-Grained, Imbalanced Real-World Dataset for Benchmarking Robust Machine Learning and Label Correction Methods

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5ab97f475339d66f8bb0a94312f57e40-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/5ab97f475339d66f8bb0a94312f57e40-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a real-world noisy ostracod dataset for benchmarking robust machine learning and label correction methods in fine-grained classification.

## Abstract

We present the Noisy Ostracods, a noisy dataset for genus and species classificationof crustacean ostracods with specialists’ annotations. Over the 71466 specimenscollected, 5.58% of them are estimated to be noisy (possibly problematic) at genuslevel. The dataset is created to addressing a real-world challenge: creating aclean fine-grained taxonomy dataset. The Noisy Ostracods dataset has diversenoises from multiple sources. Firstly, the noise is open-set, including new classesdiscovered during curation that were not part of the original annotation. Thedataset has pseudo-classes, where annotators misclassified samples that shouldbelong to an existing class into a new pseudo-class. The Noisy Ostracods datasetis highly imbalanced with a imbalance factor ρ = 22429. This presents a uniquechallenge for robust machine learning methods, as existing approaches have notbeen extensively evaluated on fine-grained classification tasks with such diversereal-world noise. Initial experiments using current robust learning techniqueshave not yielded significant performance improvements on the Noisy Ostracodsdataset compared to cross-entropy training on the raw, noisy data. On the otherhand, noise detection methods have underperformed in error hit rate comparedto naive cross-validation ensembling for identifying problematic labels. Thesefindings suggest that the fine-grained, imbalanced nature, and complex noisecharacteristics of the dataset present considerable challenges for existing noiserobustalgorithms. By openly releasing the Noisy Ostracods dataset, our goalis to encourage further research into the development of noise-resilient machinelearning methods capable of effectively handling diverse, real-world noise in finegrainedclassification tasks. The dataset, along with its evaluation protocols, can beaccessed at https://github.com/H-Jamieu/Noisy_ostracods.