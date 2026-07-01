---
title: "ComBack: A Versatile Dataset for Enhancing Compiler Backend Development Efficiency"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/cbc9ba6ccf2db854fc8de25a2741e021-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['compiler-backend', 'dataset', 'code-generation']
venue: "NeurIPS 2024"
tldr: "Presents ComBack, a dataset designed to improve efficiency in compiler backend development for diverse processors."
---

# ComBack: A Versatile Dataset for Enhancing Compiler Backend Development Efficiency

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/cbc9ba6ccf2db854fc8de25a2741e021-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/cbc9ba6ccf2db854fc8de25a2741e021-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents ComBack, a dataset designed to improve efficiency in compiler backend development for diverse processors.

## Abstract

Compiler backends are tasked with generating executable machine code for processors. With the proliferation of diverse processors, it is imperative for programmers to tailor specific compiler backends to accommodate each one. Meanwhile, compiler backend development is a laborious and time-consuming task, lacking effective automation methods. Although language models have demonstrated strong abilities in code related tasks, the lack of appropriate datasets for compiler backend development limits the application of language models in this field.In this paper, we introduce ComBack, the first public dataset designed for improving compiler backend development capabilities of language models. ComBack includes 178 backends for mainstream compilers and three tasks including statement-level completion, next-statement suggestion and code generation, representing common development scenarios. We conducted experiments by fine-tuning six pre-trained language models with ComBack, demonstrating its effectiveness in enhancing model accuracy across the three tasks. We further evaluated the top-performing model(CodeT5+) across the three tasks for new targets, comparing its accuracy with conventional methods (Fork-Flow), ChatGPT-3.5-Turbo, and Code-LLaMA-34B-Instruct. Remarkably, fine-tuned CodeT5+ with only 220M parameters on ComBack outperformed Fork-Flow methods significantly and surpassed ChatGPT and Code-LLaMA. This suggests potential efficiency improvements in compiler development. ComBack is avaliable at https://huggingface.co/datasets/docz1105/ComBack.