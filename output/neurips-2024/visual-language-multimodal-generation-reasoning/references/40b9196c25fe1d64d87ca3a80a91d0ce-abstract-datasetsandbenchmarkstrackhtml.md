---
title: "MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/40b9196c25fe1d64d87ca3a80a91d0ce-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'llm-training-and-optimization-techniques']
tags: ['multimodal-dataset', 'interleaved-image-text', 'large-scale-pretraining']
venue: "NeurIPS 2024"
tldr: "MINT-1T is an open-source multimodal interleaved dataset of one trillion tokens, scaling existing resources by 10x for training large multimodal models."
---

# MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/40b9196c25fe1d64d87ca3a80a91d0ce-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/40b9196c25fe1d64d87ca3a80a91d0ce-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: MINT-1T is an open-source multimodal interleaved dataset of one trillion tokens, scaling existing resources by 10x for training large multimodal models.

## Abstract

Multimodal interleaved datasets featuring free-form interleaved sequences of images and text are crucial for training frontier large multimodal models (LMMs). Despite the rapid progression of open-source LMMs, there remains a pronounced scarcity of large-scale, open-source multimodal interleaved datasets.In response, we introduce MINT-1T, the most extensive and diverse open-source Multimodal INTerleaved dataset to date. MINT-1T comprises of one trillion text tokens and 3.4 billion images, a 10x scale-up from existing open-source datasets. Additionally, we include previously untapped sources such as PDFs and ArXiv papers. As scaling multimodal interleaved datasets requires substantial engineering effort, sharing the data curation process and releasing the dataset greatly benefits the community. Our experiments show that LMMs trained on MINT-1T rival the performance of models trained on the previous leading dataset, OBELICS. We release our data at https://github.com/mlfoundations/MINT-1T.