---
title: "Pairwise Alignment Improves Graph Domain Adaptation"
source: "https://proceedings.mlr.press/v235/liu24ci.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ci/liu24ci.pdf"
categories: ['graph-neural-networks-and-topology', 'test-time-adaptation-methods-and-evaluation']
tags: ['graph-domain-adaptation', 'pairwise-alignment', 'graph-neural-networks', 'distribution-shift', 'label-inference']
venue: "ICML 2024"
tldr: "Pairwise alignment improves graph domain adaptation by aligning node representations across source and target graphs to handle distribution shifts in graph-based learning."
---

# Pairwise Alignment Improves Graph Domain Adaptation

**Source**: [https://proceedings.mlr.press/v235/liu24ci.html](https://proceedings.mlr.press/v235/liu24ci.html)

**TLDR**: Pairwise alignment improves graph domain adaptation by aligning node representations across source and target graphs to handle distribution shifts in graph-based learning.

## Abstract

Graph-based methods, pivotal for label inference over interconnected objects in many real-world applications, often encounter generalization challenges, if the graph used for model training differs significantly from the graph used for testing. This work delves into Graph Domain Adaptation (GDA) to address the unique complexities of distribution shifts over graph data, where interconnected data points experience shifts in features, labels, and in particular, connecting patterns. We propose a novel, theoretically principled method, Pairwise Alignment (Pair-Align) to counter graph structure shift by mitigating conditional structure shift (CSS) and label shift (LS). Pair-Align uses edge weights to recalibrate the influence among neighboring nodes to handle CSS and adjusts the classification loss with label weights to handle LS. Our method demonstrates superior performance in real-world applications, including node classification with region shift in social networks, and the pileup mitigation task in particle colliding experiments. For the first application, we also curate the largest dataset by far for GDA studies. Our method shows strong performance in synthetic and other existing benchmark datasets.