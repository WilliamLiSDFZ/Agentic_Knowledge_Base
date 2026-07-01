---
title: "SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/200661bf8f4993b7828a45a2a90f2ecf-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['vision-language-models', 'semantic-sensitivity', 'lexical-variation', 'benchmark', 'compositionality']
venue: "NeurIPS 2024"
tldr: "SUGARCREPE++ is a benchmark revealing that vision-language and language models are sensitive to semantically equivalent but lexically different sentence variations."
---

# SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/200661bf8f4993b7828a45a2a90f2ecf-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/200661bf8f4993b7828a45a2a90f2ecf-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: SUGARCREPE++ is a benchmark revealing that vision-language and language models are sensitive to semantically equivalent but lexically different sentence variations.

## Abstract

Despite their remarkable successes, state-of-the-art large language models (LLMs), including vision-and-language models (VLMs) and unimodal language models (ULMs), fail to understand precise semantics. For example, semantically equivalent sentences expressed using different lexical compositions elicit diverging representations. The degree of this divergence and its impact on encoded semantics is not very well understood. In this paper, we introduce the SUGARCREPE++ dataset to analyze the sensitivity of VLMs and ULMs to lexical and semantic alterations. Each sample in SUGARCREPE++ dataset consists of an image and a corresponding triplet of captions: a pair of semantically equivalent but lexically different positive captions and one hard negative caption. This poses a 3-way semantic (in)equivalence problem to the language models. We comprehensively evaluate VLMs and ULMs that differ in architecture, pre-training objectives and datasets to benchmark the performance of SUGARCREPE++ dataset. Experimental results highlight the difficulties of VLMs in distinguishing between lexical and semantic variations, particularly to object attributes and spatial relations. Although VLMs with larger pre-training datasets, model sizes, and multiple pre-training objectives achieve better performance on SUGARCREPE++, there is a significant opportunity for improvement. We demonstrate that models excelling on compositionality datasets may not perform equally well on SUGARCREPE++. This indicates that compositionality alone might not be sufficient to fully understand semantic and lexical alterations. Given the importance of the property that the SUGARCREPE++ dataset targets, it serves as a new challenge to the vision-and-language community. Data and code is available at https://github.com/Sri-Harsha/scpp.