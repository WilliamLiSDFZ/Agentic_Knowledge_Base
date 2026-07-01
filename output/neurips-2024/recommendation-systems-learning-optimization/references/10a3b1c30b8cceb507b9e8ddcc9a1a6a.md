---
title: "How Does Message Passing Improve Collaborative Filtering?"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/10a3b1c30b8cceb507b9e8ddcc9a1a6a-Abstract-Conference.html"
categories: ['recommendation-systems-learning-optimization', 'graph-neural-networks-and-representation-learning']
tags: ['collaborative-filtering', 'message-passing', 'graph-neural-networks']
venue: "NeurIPS 2024"
tldr: "This paper theoretically analyzes how message passing improves collaborative filtering in recommender systems by extracting structural graph knowledge."
---

# How Does Message Passing Improve Collaborative Filtering?

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/10a3b1c30b8cceb507b9e8ddcc9a1a6a-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/10a3b1c30b8cceb507b9e8ddcc9a1a6a-Abstract-Conference.html)

**TLDR**: This paper theoretically analyzes how message passing improves collaborative filtering in recommender systems by extracting structural graph knowledge.

## Abstract

Collaborative filtering (CF) has exhibited prominent results for recommender systems and been broadly utilized for real-world applications.A branch of research enhances CF methods by message passing (MP) used in graph neural networks, due to its strong capabilities of extracting knowledge from graph-structured data, like user-item bipartite graphs that naturally exist in CF. They assume that MP helps CF methods in a manner akin to its benefits for graph-based learning tasks in general (e.g., node classification). However, even though MP empirically improves CF, whether or not this assumption is correct still needs verification. To address this gap, we formally investigate why MP helps CF from multiple perspectives and show that many assumptions made by previous works are not entirely accurate. With our curated ablation studies and theoretical analyses, we discover that (i) MP improves the CF performance primarily by additional representations passed from neighbors during the forward pass instead of additional gradient updates to neighbor representations during the model back-propagation and (ii) MP usually helps low-degree nodes more than high-degree nodes.}Utilizing these novel findings, we present Test-time Aggregation for Collaborative Filtering, namely TAG-CF, a test-time augmentation framework that only conducts MP once at inference time. The key novelty of TAG-CF is that it effectively utilizes graph knowledge while circumventing most of notorious computational overheads of MP. Besides, TAG-CF is extremely versatile can be used as a plug-and-play module to enhance representations trained by different CF supervision signals. Evaluated on six datasets (i.e., five academic benchmarks and one real-world industrial dataset), TAG-CF consistently improves the recommendation performance of CF methods without graph by up to 39.2% on cold users and 31.7% on all users, with little to no extra computational overheads. Furthermore, compared with trending graph-enhanced CF methods, TAG-CF delivers comparable or even better performance with less than 1% of their total training times. Our code is publicly available at https://github.com/snap-research/Test-time-Aggregation-for-CF.