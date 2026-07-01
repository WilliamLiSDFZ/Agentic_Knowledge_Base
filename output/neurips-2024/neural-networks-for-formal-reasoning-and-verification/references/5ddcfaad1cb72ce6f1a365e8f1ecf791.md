---
title: "DeiSAM: Segment Anything with Deictic Prompting"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5ddcfaad1cb72ce6f1a365e8f1ecf791-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning', 'neural-networks-for-formal-reasoning-and-verification']
tags: ['image-segmentation', 'deictic-prompting', 'neuro-symbolic', 'natural-language', 'zero-shot']
venue: "NeurIPS 2024"
tldr: "Combines deictic natural language descriptions with SAM using neuro-symbolic reasoning for grounded zero-shot image segmentation."
---

# DeiSAM: Segment Anything with Deictic Prompting

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5ddcfaad1cb72ce6f1a365e8f1ecf791-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/5ddcfaad1cb72ce6f1a365e8f1ecf791-Abstract-Conference.html)

**TLDR**: Combines deictic natural language descriptions with SAM using neuro-symbolic reasoning for grounded zero-shot image segmentation.

## Abstract

Large-scale, pre-trained neural networks have demonstrated strong capabilities in various tasks, including zero-shot image segmentation. To identify concrete objects in complex scenes, humans instinctively rely on deictic descriptions in natural language, i.e., referring to something depending on the context such as "The object that is on the desk and behind the cup.". However, deep learning approaches cannot reliably interpret such deictic representations due to their lack of reasoning capabilities in complex scenarios. To remedy this issue, we propose DeiSAM — a combination of large pre-trained neural networks with differentiable logic reasoners — for deictic promptable segmentation. Given a complex, textual segmentation description, DeiSAM leverages Large Language Models (LLMs) to generate first-order logic rules and performs differentiable forward reasoning on generated scene graphs. Subsequently, DeiSAM segments objects by matching them to the logically inferred image regions. As part of our evaluation, we propose the Deictic Visual Genome (DeiVG) dataset, containing paired visual input and complex, deictic textual prompts. Our empirical results demonstrate that DeiSAM is a substantial improvement over purely data-driven baselines for deictic promptable segmentation.