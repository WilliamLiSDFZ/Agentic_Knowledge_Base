---
title: "MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c4bec0d2fd217e6c2c3eafeced432582-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'self-distillation-knowledge-transfer-gains']
tags: ['data-selection', 'LLM-pretraining', 'data-influence', 'efficient-training', 'model-aware']
venue: "NeurIPS 2024"
tldr: "Presents MATES, a model-aware dynamic data selection method using influence models to improve language model pretraining efficiency."
---

# MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c4bec0d2fd217e6c2c3eafeced432582-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/c4bec0d2fd217e6c2c3eafeced432582-Abstract-Conference.html)

**TLDR**: Presents MATES, a model-aware dynamic data selection method using influence models to improve language model pretraining efficiency.

## Abstract

Pretraining data selection has the potential to improve language model pretraining efficiency by utilizing higher-quality data from massive web data corpora. Current data selection methods, which rely on either hand-crafted rules or larger reference models, are conducted statically and do not capture the evolving data preferences during pretraining. In this paper, we introduce model-aware data selection with data influence models (MATES), where a data influence model continuously adapts to the evolving data preferences of the pretraining model and then selects the data most effective for the current pretraining progress. Specifically, we collect oracle data influence by locally probing the pretraining model and fine-tune a small data influence model to approximate it accurately. The data influence model then predicts data influence over the whole pretraining corpus and selects the most influential data for the next pretraining stage. Experiments of pretraining 410M and 1B models on the C4 dataset demonstrate that MATES significantly outperforms random data selection on extensive downstream tasks. It doubles the gains achieved by the state-of-the-art data selection approach that leverages larger reference models and reduces the total FLOPs required to reach certain performances by half. Further analyses validate the effectiveness of the locally probed oracle data influence and the approximation with data influence models. Our code is open-sourced at https://github.com/cxcscmu/MATES.