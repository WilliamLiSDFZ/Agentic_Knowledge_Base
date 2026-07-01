---
title: "GV-Rep: A Large-Scale Dataset for Genetic Variant Representation Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f2b86cbc0b3e31dd001aeb516afbe1e2-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'machine-learning-theory-and-evaluation-methods']
tags: ['genetic-variants', 'representation-learning', 'genomics-dataset']
venue: "NeurIPS 2024"
tldr: "Introduces a large-scale dataset and benchmark for learning representations of genetic variants to support diagnosis and treatment of genetic diseases."
---

# GV-Rep: A Large-Scale Dataset for Genetic Variant Representation Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f2b86cbc0b3e31dd001aeb516afbe1e2-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f2b86cbc0b3e31dd001aeb516afbe1e2-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a large-scale dataset and benchmark for learning representations of genetic variants to support diagnosis and treatment of genetic diseases.

## Abstract

Genetic variants (GVs) are defined as differences in the DNA sequences among individuals and play a crucial role in diagnosing and treating genetic diseases. The rapid decrease in next generation sequencing cost, analogous to Moore’s Law, has led to an exponential increase in the availability of patient-level GV data. This growth poses a challenge for clinicians who must efficiently prioritize patient-specific GVs and integrate them with existing genomic databases to inform patient management. To addressing the interpretation of GVs, genomic foundation models (GFMs) have emerged. However, these models lack standardized performance assessments, leading to considerable variability in model evaluations. This poses the question: *How effectively do deep learning methods classify unknown GVs and align them with clinically-verified GVs?* We argue that representation learning, which transforms raw data into meaningful feature spaces, is an effective approach for addressing both indexing and classification challenges. We introduce a large-scale Genetic Variant dataset, named $\textsf{GV-Rep}$, featuring variable-length contexts and detailed annotations, designed for deep learning models to learn GV representations across various traits, diseases, tissue types, and experimental contexts. Our contributions are three-fold: (i) $\textbf{Construction}$ of a comprehensive dataset with 7 million records, each labeled with characteristics of the corresponding variants, alongside additional data from 17,548 gene knockout tests across 1,107 cell types, 1,808 variant combinations, and 156 unique clinically-verified GVs from real-world patients. (ii) $\textbf{Analysis}$ of the structure and properties of the dataset. (iii) $\textbf{Experimentation}$ of the dataset with pre-trained genomic foundation models (GFMs). The results highlight a significant disparity between the current capabilities of GFMs and the accurate representation of GVs. We hope this dataset will advance genomic deep learning to bridge this gap.