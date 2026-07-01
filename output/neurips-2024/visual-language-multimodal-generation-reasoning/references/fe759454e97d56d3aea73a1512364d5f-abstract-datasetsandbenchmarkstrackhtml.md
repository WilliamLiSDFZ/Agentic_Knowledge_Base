---
title: "WikiDO: A New Benchmark Evaluating Cross-Modal Retrieval for Vision-Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fe759454e97d56d3aea73a1512364d5f-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['cross-modal-retrieval', 'vision-language-benchmark', 'evaluation']
venue: "NeurIPS 2024"
tldr: "Introduces WikiDO, a new benchmark for evaluating cross-modal retrieval capabilities of vision-language models beyond near-saturated existing datasets."
---

# WikiDO: A New Benchmark Evaluating Cross-Modal Retrieval for Vision-Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fe759454e97d56d3aea73a1512364d5f-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/fe759454e97d56d3aea73a1512364d5f-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces WikiDO, a new benchmark for evaluating cross-modal retrieval capabilities of vision-language models beyond near-saturated existing datasets.

## Abstract

Cross-modal (image-to-text and text-to-image) retrieval is an established task used in evaluation benchmarks to test the performance of vision-language models (VLMs). Several state-of-the-art VLMs (e.g. CLIP, BLIP-2) have achieved near-perfect performance on widely-used image-text retrieval benchmarks such as MSCOCO-Test-5K and Flickr30K-Test-1K. As a measure of out-of-distribution (OOD) generalization, prior works rely on zero-shot performance evaluated on one dataset (Flickr) using a VLM finetuned on another one (MSCOCO). We argue that such comparisons are insufficient to assess the OOD generalization capability of models due to high visual and linguistic similarity between the evaluation and finetuning datasets. To address this gap, we introduce WikiDO (drawn from Wikipedia Diversity Observatory), a novel cross-modal retrieval benchmark to assess the OOD generalization capabilities of pretrained VLMs. This consists of newly scraped 380K image-text pairs from Wikipedia with domain labels, a carefully curated, human-verified a)in-distribution (ID) test set (3K) and b) OOD test set (3K). The image-text pairs are very diverse in topics and geographical locations. We evaluate different VLMs of varying capacity on the \wikido benchmark; BLIP-2 achieves zero-shot performance of $R@1\approx66\%$ on the OOD test set, compared to $\approx$ $81\%$ on COCO and $\approx95\%$ on Flickr. When fine-tuned on WikiDO, the $R@1$ improvement is at most $\approx5\%$ on OOD instances compared to $\approx12\%$ on ID instances. We probe the VLMs with varying finetuning objectives and datasets of varying sizes to identify what aids OOD generalization the most. Our results confirm that WikiDO offers a strong cross-modal benchmark for current VLMs in specifically evaluating for OOD generalization. Our benchmark is hosted as a competition at https://kaggle.com/competitions/wikido24 with public access to dataset and code.