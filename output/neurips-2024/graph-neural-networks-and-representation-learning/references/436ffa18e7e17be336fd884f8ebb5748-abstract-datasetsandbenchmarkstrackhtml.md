---
title: "NoisyGL: A Comprehensive Benchmark for Graph Neural Networks under Label Noise"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/436ffa18e7e17be336fd884f8ebb5748-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['graph-neural-networks-and-representation-learning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['graph-neural-networks', 'label-noise', 'node-classification-benchmark']
venue: "NeurIPS 2024"
tldr: "Introduces NoisyGL, a comprehensive benchmark for evaluating GNNs under label noise in node classification tasks."
---

# NoisyGL: A Comprehensive Benchmark for Graph Neural Networks under Label Noise

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/436ffa18e7e17be336fd884f8ebb5748-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/436ffa18e7e17be336fd884f8ebb5748-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces NoisyGL, a comprehensive benchmark for evaluating GNNs under label noise in node classification tasks.

## Abstract

Graph Neural Networks (GNNs) exhibit strong potential in node classification task through a message-passing mechanism. However, their performance often hinges on high-quality node labels, which are challenging to obtain in real-world scenarios due to unreliable sources or adversarial attacks. Consequently, label noise is common in real-world graph data, negatively impacting GNNs by propagating incorrect information during training. To address this issue, the study of Graph Neural Networks under Label Noise (GLN) has recently gained traction. However, due to variations in dataset selection, data splitting, and preprocessing techniques, the community currently lacks a comprehensive benchmark, which impedes deeper understanding and further development of GLN. To fill this gap, we introduce NoisyGL in this paper, the first comprehensive benchmark for graph neural networks under label noise. NoisyGL enables fair comparisons and detailed analyses of GLN methods on noisy labeled graph data across various datasets, with unified experimental settings and interface. Our benchmark has uncovered several important insights that were missed in previous research, and we believe these findings will be highly beneficial for future studies. We hope our open-source benchmark library will foster further advancements in this field. The code of the benchmark can be found in https://github.com/eaglelab-zju/NoisyGL.