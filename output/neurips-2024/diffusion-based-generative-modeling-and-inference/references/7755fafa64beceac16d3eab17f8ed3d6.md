---
title: "LLM-AutoDA: Large Language Model-Driven Automatic Data Augmentation for Long-tailed Problems"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7755fafa64beceac16d3eab17f8ed3d6-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference']
tags: ['long-tailed-learning', 'data-augmentation', 'llm-driven', 'generative-models', 'class-imbalance']
venue: "NeurIPS 2024"
tldr: "LLM-AutoDA uses large language models to automatically generate targeted data augmentation strategies for long-tailed distribution problems in deep learning."
---

# LLM-AutoDA: Large Language Model-Driven Automatic Data Augmentation for Long-tailed Problems

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7755fafa64beceac16d3eab17f8ed3d6-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/7755fafa64beceac16d3eab17f8ed3d6-Abstract-Conference.html)

**TLDR**: LLM-AutoDA uses large language models to automatically generate targeted data augmentation strategies for long-tailed distribution problems in deep learning.

## Abstract

The long-tailed distribution is the underlying nature of real-world data, and it presents unprecedented challenges for training deep learning models. Existing long-tailed learning paradigms based on re-balancing or data augmentation have partially alleviated the long-tailed problem. However, they still have limitations, such as relying on manually designed augmentation strategies, having a limited search space, and using fixed augmentation strategies. To address these limitations, this paper proposes a novel LLM-based long-tailed data augmentation framework called LLM-AutoDA, which leverages large-scale pretrained models to automatically search for the optimal augmentation strategies suitable for long-tailed data distributions. In addition, it applies this strategy to the original imbalanced data to create an augmented dataset and fine-tune the underlying long-tailed learning model. The performance improvement on the validation set serves as a reward signal to update the generation model, enabling the generation of more effective augmentation strategies in the next iteration. We conducted extensive experiments on multiple mainstream long-tailed learning benchmarks. The results show that LLM-AutoDA outperforms state-of-the-art data augmentation methods and other re-balancing methods significantly.