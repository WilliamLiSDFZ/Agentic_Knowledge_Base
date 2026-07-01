---
title: "MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/586640cda3db2dc77349013dcefee456-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['multimodal-llms', 'trustworthiness', 'benchmark', 'safety', 'evaluation']
venue: "NeurIPS 2024"
tldr: "Introduces MultiTrust, a comprehensive benchmark for holistically evaluating the trustworthiness of multimodal large language models across diverse dimensions."
---

# MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/586640cda3db2dc77349013dcefee456-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/586640cda3db2dc77349013dcefee456-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces MultiTrust, a comprehensive benchmark for holistically evaluating the trustworthiness of multimodal large language models across diverse dimensions.

## Abstract

Despite the superior capabilities of Multimodal Large Language Models (MLLMs) across diverse tasks, they still face significant trustworthiness challenges. Yet, current literature on the assessment of trustworthy MLLMs remains limited, lacking a holistic evaluation to offer thorough insights into future improvements. In this work, we establish MultiTrust, the first comprehensive and unified benchmark on the trustworthiness of MLLMs across five primary aspects: truthfulness, safety, robustness, fairness, and privacy. Our benchmark employs a rigorous evaluation strategy that addresses both multimodal risks and cross-modal impacts, encompassing 32 diverse tasks with self-curated datasets. Extensive experiments with 21 modern MLLMs reveal some previously unexplored trustworthiness issues and risks, highlighting the complexities introduced by the multimodality and underscoring the necessity for advanced methodologies to enhance their reliability. For instance, typical proprietary models still struggle with the perception of visually confusing images and are vulnerable to multimodal jailbreaking and adversarial attacks; MLLMs are more inclined to disclose privacy in text and reveal ideological and cultural biases even when paired with irrelevant images in inference, indicating that the multimodality amplifies the internal risks from base LLMs. Additionally, we release a scalable toolbox for standardized trustworthiness research, aiming to facilitate future advancements in this important field. Code and resources are publicly available at: https://multi-trust.github.io/.