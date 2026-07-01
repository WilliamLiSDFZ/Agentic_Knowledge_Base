---
title: "IMPACT: A Large-scale Integrated Multimodal Patent Analysis and Creation Dataset for Design Patents"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e3301977b92f28e32639ec99eb08f4a1-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['multimodal-dataset', 'design-patents', 'figure-captioning']
venue: "NeurIPS 2024"
tldr: "IMPACT is a large-scale multimodal patent dataset of 500K design patents with 3.61M figures and detailed captions to support patent analysis and creation tasks."
---

# IMPACT: A Large-scale Integrated Multimodal Patent Analysis and Creation Dataset for Design Patents

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e3301977b92f28e32639ec99eb08f4a1-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e3301977b92f28e32639ec99eb08f4a1-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: IMPACT is a large-scale multimodal patent dataset of 500K design patents with 3.61M figures and detailed captions to support patent analysis and creation tasks.

## Abstract

In this paper, we introduce IMPACT (Integrated Multimodal Patent Analysis and Creation Dataset for Design Patents), a large-scale multimodal patent dataset with detailed captions for design patent figures. Our dataset includes half a million design patents comprising 3.61 million figures along with captions from patents granted by the United States Patent and Trademark Office (USPTO) over a 16-year period from 2007 to 2022. We incorporate the metadata of each patent application with elaborate captions that are coherent with multiple viewpoints of designs.  Even though patents themselves contain a variety of design figures, titles, and descriptions of viewpoints, we find that they lack detailed descriptions that are necessary to perform multimodal tasks such as classification and retrieval. IMPACT closes this gap thereby providing researchers with necessary ingredients to instantiate a variety of multimodal tasks. Our dataset has a huge potential for novel design inspiration and can be used with advanced computer vision models in tandem. We perform preliminary evaluations on the dataset on the popular patent analysis tasks such as classification and retrieval. Our results indicate that integrating images with generated captions significantly improves the performance of different models on the corresponding tasks. Given that design patents offer various benefits for modeling novel tasks, we propose two standard computer vision tasks that have not been investigated in analyzing patents as future directions using IMPACT as a benchmark viz., 3D Image Construction and Visual Question Answering (VQA). To facilitate research in these directions, we make our IMPACT dataset and the code/models used in this work publicly available at https://github.com/AI4Patents/IMPACT.