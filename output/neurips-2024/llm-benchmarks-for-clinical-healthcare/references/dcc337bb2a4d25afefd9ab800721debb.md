---
title: "Targeted Sequential Indirect Experiment Design"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/dcc337bb2a4d25afefd9ab800721debb-Abstract-Conference.html"
categories: ['causal-discovery-and-inference-methods', 'llm-benchmarks-for-clinical-healthcare']
tags: ['experiment-design', 'causal-queries', 'indirect-interventions']
venue: "NeurIPS 2024"
tldr: "Proposes a targeted sequential indirect experiment design framework for answering causal scientific hypotheses under complex unknown mechanisms."
---

# Targeted Sequential Indirect Experiment Design

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/dcc337bb2a4d25afefd9ab800721debb-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/dcc337bb2a4d25afefd9ab800721debb-Abstract-Conference.html)

**TLDR**: Proposes a targeted sequential indirect experiment design framework for answering causal scientific hypotheses under complex unknown mechanisms.

## Abstract

Scientific hypotheses typically concern specific aspects of complex, imperfectly understood or entirely unknown mechanisms, such as the effect of gene expression levels on phenotypes or how microbial communities influence environmental health. Such queries are inherently causal (rather than purely associational), but in many settings, experiments can not be conducted directly on the target variables of interest, but are indirect. Therefore, they perturb the target variable, but do not remove potential confounding factors. If, additionally, the resulting experimental measurements are high-dimensional and the studied mechanisms nonlinear, the query of interest is generally not identified. We develop an adaptive strategy to design indirect experiments that optimally inform a targeted query about the ground truth mechanism in terms of sequentially narrowing the gap between an upper and lower bound on the query. While the general formulation consists of a bi-level optimization procedure, we derive an efficiently estimable analytical kernel-based estimator of the bounds for the causal effect, a query of key interest, and demonstrate the efficacy of our approach in confounded, multivariate, nonlinear synthetic settings.