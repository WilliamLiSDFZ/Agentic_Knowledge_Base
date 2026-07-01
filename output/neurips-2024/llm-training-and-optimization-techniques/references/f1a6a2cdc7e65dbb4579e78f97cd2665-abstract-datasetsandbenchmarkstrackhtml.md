---
title: "A Practitioner's Guide to Real-World Continual Multimodal Pretraining"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f1a6a2cdc7e65dbb4579e78f97cd2665-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'llm-training-and-optimization-techniques']
tags: ['continual-pretraining', 'multimodal-foundation-models', 'vision-language']
venue: "NeurIPS 2024"
tldr: "Provides a practitioner's guide for continual multimodal pretraining of vision-language models to keep them updated with evolving data streams."
---

# A Practitioner's Guide to Real-World Continual Multimodal Pretraining

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f1a6a2cdc7e65dbb4579e78f97cd2665-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f1a6a2cdc7e65dbb4579e78f97cd2665-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Provides a practitioner's guide for continual multimodal pretraining of vision-language models to keep them updated with evolving data streams.

## Abstract

Multimodal foundation models serve numerous applications at the intersection of vision and language. Still, despite being pretrained on extensive data, they become outdated over time.To keep models updated, research into continual pretraining mainly explores scenarios with either (1) infrequent, indiscriminate updates on large-scale new data, or (2) frequent, sample-level updates.However, practical model deployment often operates in the gap between these two limit cases, as real-world applications demand adaptation to specific subdomains, tasks or concepts --- spread over the entire, varying life cycle of a model. In this work, we complement current perspectives on continual pretraining through a research test bed and offer comprehensive guidance for effective continual model updates in such scenarios.We first introduce FoMo-in-Flux, a continual multimodal pretraining benchmark with realistic compute constraints and practical deployment requirements, constructed over 63 datasets with diverse visual and semantic coverage.Using FoMo-in-Flux, we explore the complex landscape of practical continual pretraining through multiple perspectives: (1) data mixtures and stream orderings that emulate real-world deployment settings, (2) methods ranging from simple fine-tuning and traditional continual learning strategies to parameter-efficient updates and model merging, (3) meta-learning-rate schedules and mechanistic design choices, and (4) model and compute scaling. Together, our insights provide a practitioner's guide to continual multimodal pretraining for real-world deployment. Benchmark and code is provided here: https://github.com/ExplainableML/fomoinflux.