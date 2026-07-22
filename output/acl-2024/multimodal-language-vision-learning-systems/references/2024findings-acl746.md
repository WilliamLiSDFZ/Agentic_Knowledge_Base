---
title: "SciMMIR: Benchmarking Scientific Multi-modal Information Retrieval"
source: "https://aclanthology.org/2024.findings-acl.746/"
categories: ['multimodal-language-vision-learning-systems']
tags: ['scientific-retrieval', 'multimodal-benchmark', 'image-text-pairing']
venue: "ACL 2024"
tldr: "Introduces SciMMIR, a benchmark for evaluating multi-modal information retrieval in scientific document contexts."
---

# SciMMIR: Benchmarking Scientific Multi-modal Information Retrieval

**Source**: [https://aclanthology.org/2024.findings-acl.746/](https://aclanthology.org/2024.findings-acl.746/)

**TLDR**: Introduces SciMMIR, a benchmark for evaluating multi-modal information retrieval in scientific document contexts.

## Abstract

AbstractMulti-modal information retrieval (MMIR) is a rapidly evolving field where significant progress has been made through advanced representation learning and cross-modality alignment research, particularly in image-text pairing.However, current benchmarks for evaluating MMIR performance on image-text pairings overlook the scientific domain, which has a notable gap with the generic data since the caption of scientific charts and tables usually describes the analysis of experimental results or scientific principles in contrast to human activity or scenery depicted in generic images.To bridge this gap, we develop a scientific domain-specific MMIR benchmark (SciMMIR) by leveraging open-access research paper corpora to extract data relevant to the scientific domain. This benchmark comprises 530K meticulously curated image-text pairs, extracted from figures and tables with detailed captions from scientific documents.We further annotate the image-text pairs with a two-level subset-subcategory hierarchy to facilitate a more comprehensive evaluation of the baselines. We conduct zero-shot and fine-tuned evaluations on prominent multi-modal image-captioning and visual language models, such as CLIP, BLIP, and BLIP-2.Our findings offer critical insights for MMIR in the scientific domain, including the impact of pre-training and fine-tuning settings and the effects of different visual and textual encoders.