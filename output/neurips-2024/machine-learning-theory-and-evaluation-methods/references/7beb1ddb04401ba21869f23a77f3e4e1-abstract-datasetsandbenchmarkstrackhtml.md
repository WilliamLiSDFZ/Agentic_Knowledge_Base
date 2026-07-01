---
title: "Navigating the Maze of Explainable AI: A Systematic Approach to Evaluating Methods and Metrics"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7beb1ddb04401ba21869f23a77f3e4e1-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['explainability', 'evaluation-metrics', 'systematic-review']
venue: "NeurIPS 2024"
tldr: "A systematic framework for evaluating the efficacy of explainable AI methods and their associated metrics across diverse design parameters."
---

# Navigating the Maze of Explainable AI: A Systematic Approach to Evaluating Methods and Metrics

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7beb1ddb04401ba21869f23a77f3e4e1-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/7beb1ddb04401ba21869f23a77f3e4e1-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A systematic framework for evaluating the efficacy of explainable AI methods and their associated metrics across diverse design parameters.

## Abstract

Explainable AI (XAI) is a rapidly growing domain with a myriad of proposed methods as well as metrics aiming to evaluate their efficacy. However, current studies are often of limited scope, examining only a handful of XAI methods and ignoring underlying design parameters for performance, such as the model architecture or the nature of input data.  Moreover, they often rely on one or a few metrics and neglect thorough validation, increasing the risk of selection bias and ignoring discrepancies among metrics. These shortcomings leave practitioners confused about which method to choose for their problem. In response, we introduce LATEC, a large-scale benchmark that critically evaluates 17 prominent XAI methods using 20 distinct metrics.  We systematically incorporate vital design parameters like varied architectures and diverse input modalities, resulting in 7,560 examined combinations.  Through LATEC, we showcase the high risk of conflicting metrics leading to unreliable rankings and consequently propose a more robust evaluation scheme. Further, we comprehensively evaluate various XAI methods to assist practitioners in selecting appropriate methods aligning with their needs. Curiously, the emerging top-performing method, Expected Gradients, is not examined in any relevant related study. LATEC reinforces its role in future XAI research by publicly releasing all 326k saliency maps and 378k metric scores as a (meta-)evaluation dataset. The benchmark is hosted at: https://github.com/IML-DKFZ/latec.