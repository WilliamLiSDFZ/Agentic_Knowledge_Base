---
title: "RClicks: Realistic Click Simulation for Benchmarking Interactive Segmentation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e6b5bcc872666d37c469e5c5ba723669-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['interactive-segmentation', 'click-simulation', 'benchmarking', 'SAM']
venue: "NeurIPS 2024"
tldr: "Introduces RClicks, a realistic click simulation framework for more accurately benchmarking interactive segmentation methods including SAM."
---

# RClicks: Realistic Click Simulation for Benchmarking Interactive Segmentation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e6b5bcc872666d37c469e5c5ba723669-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e6b5bcc872666d37c469e5c5ba723669-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces RClicks, a realistic click simulation framework for more accurately benchmarking interactive segmentation methods including SAM.

## Abstract

The emergence of Segment Anything (SAM) sparked research interest in the field of interactive segmentation, especially in the context of image editing tasks and speeding up data annotation. Unlike common semantic segmentation, interactive segmentation methods allow users to directly influence their output through prompts (e.g. clicks). However, click patterns in real-world interactive segmentation scenarios remain largely unexplored. Most methods rely on the assumption that users would click in the center of the largest erroneous area. Nevertheless, recent studies show that this is not always the case. Thus, methods may have poor performance in real-world deployment despite high metrics in a baseline benchmark. To accurately simulate real-user clicks, we conducted a large crowdsourcing study of click patterns in an interactive segmentation scenario and collected 475K real-user clicks. Drawing on ideas from saliency tasks, we develop a clickability model that enables sampling clicks, which closely resemble actual user inputs. Using our model and dataset, we propose RClicks benchmark for a comprehensive comparison of existing interactive segmentation methods on realistic clicks. Specifically, we evaluate not only the average quality of methods, but also the robustness w.r.t. click patterns. According to our benchmark, in real-world usage interactive segmentation models may perform worse than it has been reported in the baseline benchmark, and most of the methods are not robust. We believe that RClicks is a significant step towards creating interactive segmentation methods that provide the best user experience in real-world cases.