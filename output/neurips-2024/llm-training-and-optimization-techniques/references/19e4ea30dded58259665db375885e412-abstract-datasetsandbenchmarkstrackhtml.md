---
title: "DataComp-LM: In search of the next generation of training sets for language models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/19e4ea30dded58259665db375885e412-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-training-and-optimization-techniques', 'ai-benchmarking-and-evaluation-methodology']
tags: ['language-model-pretraining', 'dataset-curation', 'benchmark', 'common-crawl']
venue: "NeurIPS 2024"
tldr: "Introduces DataComp-LM, a testbed for controlled dataset experiments to identify next-generation training sets for language models."
---

# DataComp-LM: In search of the next generation of training sets for language models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/19e4ea30dded58259665db375885e412-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/19e4ea30dded58259665db375885e412-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces DataComp-LM, a testbed for controlled dataset experiments to identify next-generation training sets for language models.

## Abstract

We introduce DataComp for Language Models, a testbed for controlled dataset experiments with the goal of improving language models.As part of DCLM, we provide a standardized corpus of 240T tokens extracted from Common Crawl, effective pretraining recipes based on the OpenLM framework, and a broad suite of 53 downstream evaluations.Participants in the DCLM benchmark can experiment with data curation strategies such as deduplication, filtering, and data mixing atmodel scales ranging from 412M to 7B parameters.As a baseline for DCLM, we conduct extensive experiments and find that model-based filtering is key to assembling a high-quality training set.The resulting dataset, DCLM-Baseline, enables training a 7B parameter language model from scratch to 63% 5-shot accuracy on MMLU with 2T training tokens.Compared to MAP-Neo, the previous state-of-the-art in open-data language models, DCLM-Baseline represents a 6 percentage point improvement on MMLU while being trained with half the compute.Our results highlight the importance of dataset design for training language models and offer a starting point for further research on data curation. We release the \dclm benchmark, framework, models, and datasets at https://www.datacomp.ai/dclm/