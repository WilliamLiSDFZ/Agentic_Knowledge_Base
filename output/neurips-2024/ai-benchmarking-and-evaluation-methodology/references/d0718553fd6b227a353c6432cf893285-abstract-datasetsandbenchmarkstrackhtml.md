---
title: "Image2Struct: Benchmarking Structure Extraction for Vision-Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d0718553fd6b227a353c6432cf893285-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['vision-language-models', 'structure-extraction', 'benchmark', 'image-to-structure', 'evaluation']
venue: "NeurIPS 2024"
tldr: "Image2Struct is an automatic benchmark evaluating vision-language models on extracting structured representations such as LaTeX and code from images."
---

# Image2Struct: Benchmarking Structure Extraction for Vision-Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d0718553fd6b227a353c6432cf893285-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/d0718553fd6b227a353c6432cf893285-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Image2Struct is an automatic benchmark evaluating vision-language models on extracting structured representations such as LaTeX and code from images.

## Abstract

We introduce Image2Struct, a benchmark to evaluate vision-language models (VLMs) on extracting structure from images.Our benchmark 1) captures real-world use cases, 2) is fully automatic and does not require human judgment, and 3) is based on a renewable stream of fresh data.In Image2Struct, VLMs are prompted to generate the underlying structure (e.g., LaTeX code or HTML) from an input image (e.g., webpage screenshot).The structure is then rendered to produce an output image (e.g., rendered webpage), which is compared against the input image to produce a similarity score.This round-trip evaluation allows us to quantitatively evaluate VLMs on tasks with multiple valid structures.We create a pipeline that downloads fresh data from active online communities upon execution and evaluates the VLMs without human intervention.We introduce three domains (Webpages, LaTeX, and Musical Scores) and use five image metrics (pixel similarity, cosine similarity between the Inception vectors, learned perceptual image patch similarity, structural similarity index measure, and earth mover similarity) that allow efficient and automatic comparison between pairs of images. We evaluate Image2Struct on 14 prominent VLMs and find that scores vary widely, indicating that Image2Struct can differentiate between the performances of different VLMs.Additionally, the best score varies considerably across domains (e.g., 0.402 on sheet music vs. 0.830 on LaTeX equations), indicating that Image2Struct contains tasks of varying difficulty.For transparency, we release the full results at  https://crfm.stanford.edu/helm/image2struct/v1.0.1/.