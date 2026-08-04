---
title: "Class-Imbalanced Graph Learning without Class Rebalancing"
source: "https://proceedings.mlr.press/v235/liu24ay.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ay/liu24ay.pdf"
categories: ['graph-neural-networks-and-topology', 'learning-with-imperfect-data-and-bias']
tags: ['class-imbalance', 'graph-neural-networks', 'node-classification']
venue: "ICML 2024"
tldr: "A class-rebalancing-free approach to imbalanced node classification on graphs that addresses root causes of imbalance without reweighting or resampling."
---

# Class-Imbalanced Graph Learning without Class Rebalancing

**Source**: [https://proceedings.mlr.press/v235/liu24ay.html](https://proceedings.mlr.press/v235/liu24ay.html)

**TLDR**: A class-rebalancing-free approach to imbalanced node classification on graphs that addresses root causes of imbalance without reweighting or resampling.

## Abstract

Class imbalance is prevalent in real-world node classification tasks and poses great challenges for graph learning models. Most existing studies are rooted in a class-rebalancing (CR) perspective and address class imbalance with class-wise reweighting or resampling. In this work, we approach the root cause of class-imbalance bias from an topological paradigm. Specifically, we theoretically reveal two fundamental phenomena in the graph topology that greatly exacerbate the predictive bias stemming from class imbalance. On this basis, we devise a lightweight topological augmentation framework BAT to mitigate the class-imbalance bias without class rebalancing. Being orthogonal to CR, BAT can function as an efficient plug-and-play module that can be seamlessly combined with and significantly boost existing CR techniques. Systematic experiments on real-world imbalanced graph learning tasks show that BAT can deliver up to 46.27% performance gain and up to 72.74% bias reduction over existing techniques. Code, examples, and documentations are available at https://github.com/ZhiningLiu1998/BAT.