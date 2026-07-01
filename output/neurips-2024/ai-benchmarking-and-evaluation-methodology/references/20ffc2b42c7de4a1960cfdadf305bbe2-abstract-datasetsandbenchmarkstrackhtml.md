---
title: "DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/20ffc2b42c7de4a1960cfdadf305bbe2-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['multimodal-LLM', 'vision-experts', 'image-text-data', 'visual-perception']
venue: "NeurIPS 2024"
tldr: "Presents DenseFusion-1M, a dataset merging multiple vision expert models to provide comprehensive image-text annotations for training MLLMs."
---

# DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/20ffc2b42c7de4a1960cfdadf305bbe2-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/20ffc2b42c7de4a1960cfdadf305bbe2-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents DenseFusion-1M, a dataset merging multiple vision expert models to provide comprehensive image-text annotations for training MLLMs.

## Abstract

Existing Multimodal Large Language Models (MLLMs) increasingly emphasize complex understanding of various visual elements, including multiple objects, text information, spatial relations. Their development for comprehensive visual perception hinges on the availability of high-quality image-text datasets that offer diverse visual elements and throughout image descriptions. However, the scarcity of such hyper-detailed datasets currently hinders progress within the MLLM community. The bottleneck stems from the limited perceptual capabilities of current caption engines, which fall short in providing complete and accurate annotations. To facilitate the cutting-edge research of MLLMs on comprehensive vision perception, we thereby propose Perceptual Fusion, using a low-budget but highly effective caption engine for complete and accurate image descriptions.  Specifically, Perceptual Fusion integrates diverse perception experts as image priors to provide explicit information on visual elements and adopts an efficient MLLM as a centric pivot to mimic advanced MLLMs' perception abilities. We carefully select 1M highly representative images from uncurated LAION dataset and generate dense descriptions using our engine, dubbed DenseFusion-1M. Extensive experiments validate that our engine outperforms its counterparts, where the resulting dataset significantly improves the perception and cognition abilities of existing MLLMs across diverse vision-language benchmarks, especially with high-resolution images as inputs. The code and dataset are available at https://huggingface.co/datasets/BAAI/DenseFusion-1M.