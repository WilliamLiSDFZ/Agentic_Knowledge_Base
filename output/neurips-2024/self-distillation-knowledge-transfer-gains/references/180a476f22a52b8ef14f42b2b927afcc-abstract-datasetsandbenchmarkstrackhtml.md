---
title: "$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/180a476f22a52b8ef14f42b2b927afcc-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-training-and-optimization-techniques', 'self-distillation-knowledge-transfer-gains']
tags: ['llm-scaling', 'model-merging', 'model-zoo']
venue: "NeurIPS 2024"
tldr: "A benchmark and framework for democratizing LLM scaling by aggregating and merging models from a large model zoo."
---

# $\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/180a476f22a52b8ef14f42b2b927afcc-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/180a476f22a52b8ef14f42b2b927afcc-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark and framework for democratizing LLM scaling by aggregating and merging models from a large model zoo.

## Abstract

As Large Language Models (LLMs) excel across tasks and specialized domains, scaling LLMs based on existing models has gained significant attention, which is challenged by potential performance drop when combining disparate models. Various techniques have been proposed to aggregate pre-trained LLMs, including model merging, Mixture-of-Experts, and stacking. Despite their merits, a comprehensive comparison and synergistic application of them to a diverse model zoo is yet to be adequately addressed.In light of this research gap, this paper introduces $\texttt{Model-GLUE}$, a holistic LLM scaling guideline. First, our work starts with a benchmarking of existing LLM scaling techniques, especially selective merging, and variants of mixture. Utilizing the insights from the benchmark results, we formulate a strategy for the selection and aggregation of a heterogeneous model zoo characterizing different architectures and initialization.Our methodology involves clustering mergeable models, selecting a merging strategy, and integrating model clusters through model-level mixture. Finally, evidenced by our experiments on a diverse Llama-2-based model zoo, $\texttt{Model-GLUE}$ shows an average performance enhancement of 5.61\%, achieved without additional training.Codes are available at https://github.com/Model-GLUE/Model-GLUE.