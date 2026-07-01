---
title: "NovoBench: Benchmarking Deep Learning-based \emph{De Novo} Sequencing Methods in Proteomics"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bd281779e603522d92aa4f59c36012e4-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-for-molecular-biology']
tags: ['proteomics', 'de-novo-sequencing', 'mass-spectrometry']
venue: "NeurIPS 2024"
tldr: "A comprehensive benchmark for evaluating deep learning methods for de novo peptide sequencing from tandem mass spectrometry data."
---

# NovoBench: Benchmarking Deep Learning-based \emph{De Novo} Sequencing Methods in Proteomics

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bd281779e603522d92aa4f59c36012e4-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/bd281779e603522d92aa4f59c36012e4-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A comprehensive benchmark for evaluating deep learning methods for de novo peptide sequencing from tandem mass spectrometry data.

## Abstract

Tandem mass spectrometry has played a pivotal role in advancing proteomics, enabling the analysis of protein composition in biological tissues. Many deep learning methods have been developed for \emph{de novo} peptide sequencing task, i.e., predicting the peptide sequence for the observed mass spectrum. However, two key challenges seriously hinder the further research of this important task. Firstly, since there is no consensus for the evaluation datasets, the empirical results in different research papers are often not comparable, leading to unfair comparison. Secondly, the current methods are usually limited to amino acid-level or peptide-level precision and recall metrics. In this work, we present the first unified benchmark NovoBench for \emph{de novo} peptide sequencing, which comprises diverse mass spectrum data, integrated models, and comprehensive evaluation metrics. Recent impressive methods, including DeepNovo, PointNovo, Casanovo, InstaNovo, AdaNovo and $\pi$-HelixNovo are integrated into our framework. In addition to amino acid-level and peptide-level precision and recall, we also evaluate the models' performance in terms of identifying post-tranlational modifications (PTMs), efficiency and robustness to peptide length, noise peaks and missing fragment ratio, which are important influencing factors while seldom be considered. Leveraging this benchmark, we conduct a large-scale study of current methods, report many insightful findings that open up new possibilities for future development. The benchmark is open-sourced to facilitate future research and application. The code is available at \url{https://github.com/Westlake-OmicsAI/NovoBench}.