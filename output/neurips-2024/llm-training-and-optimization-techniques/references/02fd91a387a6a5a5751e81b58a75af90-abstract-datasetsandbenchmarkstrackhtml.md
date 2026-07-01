---
title: "HelpSteer 2: Open-source dataset for training top-performing reward models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/02fd91a387a6a5a5751e81b58a75af90-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-training-and-optimization-techniques', 'ai-benchmarking-and-evaluation-methodology']
tags: ['preference-dataset', 'reward-model', 'human-alignment']
venue: "NeurIPS 2024"
tldr: "An open-source high-quality preference dataset for training top-performing reward models to align LLMs with human preferences."
---

# HelpSteer 2: Open-source dataset for training top-performing reward models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/02fd91a387a6a5a5751e81b58a75af90-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/02fd91a387a6a5a5751e81b58a75af90-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: An open-source high-quality preference dataset for training top-performing reward models to align LLMs with human preferences.

## Abstract

High-quality preference datasets are essential for training reward models that can effectively guide large language models (LLMs) in generating high-quality responses aligned with human preferences.As LLMs become stronger and better aligned, permissively licensed preference datasets, such as Open Assistant, HH-RLHF, and HelpSteer need to be updated to remain effective for reward modeling.Methods that distil preference data from proprietary LLMs such as GPT-4 have restrictions on commercial usage imposed by model providers.To improve upon both generated responses and attribute labeling quality, we release HelpSteer2, a permissively licensed preference dataset (CC-BY-4.0).  Using a powerful Nemotron-4-340B base model trained on HelpSteer2, we are able to achieve the SOTA score (92.0%) on Reward-Bench's primary dataset, outperforming currently listed open and proprietary models, as of June 12th, 2024.Notably, HelpSteer2 consists of only ten thousand response pairs, an order of magnitude fewer than existing preference datasets (e.g., HH-RLHF), which makes it highly efficient for training reward models. Our extensive experiments demonstrate that reward models trained with HelpSteer2 are effective in aligning LLMs. Additionally, we propose SteerLM 2.0, a model alignment approach that can effectively make use of the rich multi-attribute score predicted by our reward models. HelpSteer2 is available at https://huggingface.co/datasets/nvidia/HelpSteer2 and code is available at https://github.com/NVIDIA/NeMo-Aligner