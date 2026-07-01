---
title: "Swift Sampler: Efficient Learning of Sampler by 10 Parameters"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6c9dcffe0b9cc3b05d83bcdddb250690-Abstract-Conference.html"
categories: ['deep-learning-optimization-and-generalization-theory']
tags: ['data-sampling', 'meta-learning', 'training-efficiency']
venue: "NeurIPS 2024"
tldr: "Introduces a lightweight 10-parameter sampler that efficiently learns optimal data sampling probabilities to improve deep learning model convergence."
---

# Swift Sampler: Efficient Learning of Sampler by 10 Parameters

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6c9dcffe0b9cc3b05d83bcdddb250690-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/6c9dcffe0b9cc3b05d83bcdddb250690-Abstract-Conference.html)

**TLDR**: Introduces a lightweight 10-parameter sampler that efficiently learns optimal data sampling probabilities to improve deep learning model convergence.

## Abstract

Data selection is essential for training deep learning models. An effective data sampler assigns proper sampling probability for training data and helps the model converge to a good local minimum with high performance. Previous studies in data sampling are mainly based on heuristic rules or learning through a huge amount of time-consuming trials. In this paper, we propose an automatic swift sampler search algorithm, SS, to explore automatically learning effective samplers efficiently. In particular, SS utilizes a novel formulation to map a sampler to a low dimension of hyper-parameters and uses an approximated local minimum to quickly examine the quality of a sampler. Benefiting from its low computational expense, SS can be applied on large-scale data sets with high efficiency. Comprehensive experiments on various tasks demonstrate that SS powered sampling can achieve obvious improvements (e.g., 1.5% on ImageNet) and transfer among different neural networks. Project page: https://github.com/Alexander-Yao/Swift-Sampler.