---
title: "NanoBaseLib: A Multi-Task Benchmark Dataset for Nanopore Sequencing"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8bce223b376f52fb86a148097eebb10d-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'ai-benchmarking-and-evaluation-methodology']
tags: ['nanopore-sequencing', 'benchmark', 'multi-task']
venue: "NeurIPS 2024"
tldr: "Introduces a multi-task benchmark dataset for nanopore sequencing biological analysis tasks."
---

# NanoBaseLib: A Multi-Task Benchmark Dataset for Nanopore Sequencing

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8bce223b376f52fb86a148097eebb10d-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/8bce223b376f52fb86a148097eebb10d-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a multi-task benchmark dataset for nanopore sequencing biological analysis tasks.

## Abstract

Nanopore sequencing is the third-generation sequencing technology with capabilities of generating long-read sequences and directly measuring modifications on DNA/RNA molecules, which makes it ideal for biological applications such as human Telomere-to-Telomere (T2T) genome assembly, Ebola virus surveillance and COVID-19 mRNA vaccine development. However, accuracies of computational methods in various tasks of Nanopore sequencing data analysis are far from satisfactory. For instance, the base calling accuracy of Nanopore RNA sequencing is $\sim$90\%, while the aim is $\sim$99.9\%. This highlights an urgent need of contributions from the machine learning community. A bottleneck that prevents machine learning researchers from entering this field is the lack of a large integrated benchmark dataset. To this end, we present NanoBaseLib, a comprehensive multi-task benchmark dataset. It integrates 16 public datasets with over 30 million reads for four critical tasks in Nanopore data analysis. To facilitate method development, we have preprocessed all the raw data using a uniform workflow, stored all the intermediate results in uniform formats, analysed test datasets with various baseline methods for four benchmark tasks, and developed a software package to easily access these results. NanoBaseLib is available at https://nanobaselib.github.io.