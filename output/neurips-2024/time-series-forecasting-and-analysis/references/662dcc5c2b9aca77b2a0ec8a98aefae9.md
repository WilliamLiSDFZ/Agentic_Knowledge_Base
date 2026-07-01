---
title: "Large Pre-trained time series models for cross-domain Time series analysis tasks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/662dcc5c2b9aca77b2a0ec8a98aefae9-Abstract-Conference.html"
categories: ['time-series-forecasting-and-analysis', 'llm-training-and-optimization-techniques']
tags: ['large-pretrained-models', 'time-series', 'cross-domain']
venue: "NeurIPS 2024"
tldr: "This paper proposes large pre-trained time series models that enable efficient cross-domain transfer for diverse time-series analysis tasks."
---

# Large Pre-trained time series models for cross-domain Time series analysis tasks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/662dcc5c2b9aca77b2a0ec8a98aefae9-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/662dcc5c2b9aca77b2a0ec8a98aefae9-Abstract-Conference.html)

**TLDR**: This paper proposes large pre-trained time series models that enable efficient cross-domain transfer for diverse time-series analysis tasks.

## Abstract

Large pre-trained models have been vital in recent advancements in domains like language and vision, making model training for individual downstream tasks more efficient and provide superior performance. However, tackling time-series analysis tasks usually involves designing and training a separate model from scratch leveraging training data and domain expertise specific to the task. We tackle a significant challenge for pre-training a foundational time-series model from multi-domain time-series datasets: extracting semantically useful tokenized inputs to the model across heterogeneous time-series from different domains. We propose Large Pre-trained Time-series Models (LPTM) that introduces a novel method of adaptive segmentation that automatically identifies optimal dataset-specific segmentation strategy during pre-training. This enables LPTM to perform similar to or better than domain-specific state-of-art model when fine-tuned to different downstream time-series analysis tasks and under zero-shot settings. LPTM achieves superior forecasting and time-series classification results taking up to 40% less data and 50% less training time compared to state-of-art baselines.