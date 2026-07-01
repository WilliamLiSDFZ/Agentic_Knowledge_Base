---
title: "Hidden in Plain Sight: Evaluating Abstract Shape Recognition in Vision-Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a13ff984831deea39e6132bafdfdd6d5-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['shape-recognition', 'vision-language-models', 'abstract-shapes', 'evaluation']
venue: "NeurIPS 2024"
tldr: "Evaluates abstract shape recognition capabilities of large vision-language models, revealing limitations in shape perception."
---

# Hidden in Plain Sight: Evaluating Abstract Shape Recognition in Vision-Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a13ff984831deea39e6132bafdfdd6d5-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a13ff984831deea39e6132bafdfdd6d5-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Evaluates abstract shape recognition capabilities of large vision-language models, revealing limitations in shape perception.

## Abstract

Despite the importance of shape perception in human vision, early neural image classifiers relied less on shape information for object recognition than other (often spurious) features. While recent research suggests that current large Vision-Language Models (VLMs) exhibit more reliance on shape, we find them to still be seriously limited in this regard. To quantify such limitations, we introduce IllusionBench, a dataset that challenges current cutting-edge VLMs to decipher shape information when the shape is represented by an arrangement of visual elements in a scene. Our extensive evaluations reveal that, while these shapes are easily detectable by human annotators, current VLMs struggle to recognize them, indicating important avenues for future work in developing more robust visual perception systems. The full dataset and codebase are available at: https://arshiahemmat.github.io/illusionbench/