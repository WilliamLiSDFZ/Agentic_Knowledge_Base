---
title: "Graph Out-of-Distribution Detection Goes Neighborhood Shaping"
source: "https://proceedings.mlr.press/v235/bao24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bao24c/bao24c.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'graph-neural-networks-and-topology']
tags: ['graph-OOD-detection', 'neighborhood-shaping', 'topology']
venue: "ICML 2024"
tldr: "TopoOOD is introduced as a principled graph out-of-distribution detection approach leveraging graph topology and neighborhood structure."
---

# Graph Out-of-Distribution Detection Goes Neighborhood Shaping

**Source**: [https://proceedings.mlr.press/v235/bao24c.html](https://proceedings.mlr.press/v235/bao24c.html)

**TLDR**: TopoOOD is introduced as a principled graph out-of-distribution detection approach leveraging graph topology and neighborhood structure.

## Abstract

Despite the rich line of research works on out-of-distribution (OOD) detection on images, the literature on OOD detection for interdependent data, e.g., graphs, is still relatively limited. To fill this gap, we introduce TopoOOD as a principled approach that accommodates graph topology and neighborhood context for detecting OOD node instances on graphs. Meanwhile, we enrich the experiment settings by splitting in-distribution (ID) and OOD data based on distinct topological distributions, which presents new benchmarks for a more comprehensive analysis of graph-based OOD detection. The latter is designed to thoroughly assess the performance of these discriminators under distribution shifts involving structural information, providing a rigorous evaluation of methods in the emerging area of OOD detection on graphs. Our experimental results show the competitiveness of the proposed model across multiple datasets, as evidenced by up to a 15% increase in the AUROC and a 50% decrease in the FPR compared to existing state-of-the-art methods.