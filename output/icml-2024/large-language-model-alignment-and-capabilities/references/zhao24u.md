---
title: "LangCell: Language-Cell Pre-training for Cell Identity Understanding"
source: "https://proceedings.mlr.press/v235/zhao24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24u/zhao24u.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['cell-identity', 'pre-training', 'language-model', 'single-cell-transcriptomics']
venue: "ICML 2024"
tldr: "LangCell is a language-cell pre-training framework that integrates natural language and transcriptomic data for comprehensive cell identity understanding."
---

# LangCell: Language-Cell Pre-training for Cell Identity Understanding

**Source**: [https://proceedings.mlr.press/v235/zhao24u.html](https://proceedings.mlr.press/v235/zhao24u.html)

**TLDR**: LangCell is a language-cell pre-training framework that integrates natural language and transcriptomic data for comprehensive cell identity understanding.

## Abstract

Cell identity encompasses various semantic aspects of a cell, including cell type, pathway information, disease information, and more, which are essential for biologists to gain insights into its biological characteristics. Understanding cell identity from the transcriptomic data, such as annotating cell types, has become an important task in bioinformatics. As these semantic aspects are determined by human experts, it is impossible for AI models to effectively carry out cell identity understanding tasks without the supervision signals provided by single-cell and label pairs. The single-cell pre-trained language models (PLMs) currently used for this task are trained only on a single modality, transcriptomics data, lack an understanding of cell identity knowledge. As a result, they have to be fine-tuned for downstream tasks and struggle when lacking labeled data with the desired semantic labels. To address this issue, we propose an innovative solution by constructing a unified representation of single-cell data and natural language during the pre-training phase, allowing the model to directly incorporate insights related to cell identity. More specifically, we introduce LangCell, the first Language-Cell pre-training framework. LangCell utilizes texts enriched with cell identity information to gain a profound comprehension of cross-modal knowledge. Results from experiments conducted on different benchmarks show that LangCell is the only single-cell PLM that can work effectively in zero-shot cell identity understanding scenarios, and also significantly outperforms existing models in few-shot and fine-tuning cell identity understanding scenarios.