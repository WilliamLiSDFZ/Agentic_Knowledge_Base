---
title: "The Merit of River Network Topology for Neural Flood Forecasting"
source: "https://proceedings.mlr.press/v235/kirschstein24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kirschstein24a/kirschstein24a.pdf"
categories: ['graph-neural-networks-and-topology', 'time-series-modeling-and-forecasting-methods']
tags: ['flood-forecasting', 'river-network-topology', 'graph-neural-networks']
venue: "ICML 2024"
tldr: "Investigates how incorporating river network topology into graph neural networks improves neural flood forecasting accuracy."
---

# The Merit of River Network Topology for Neural Flood Forecasting

**Source**: [https://proceedings.mlr.press/v235/kirschstein24a.html](https://proceedings.mlr.press/v235/kirschstein24a.html)

**TLDR**: Investigates how incorporating river network topology into graph neural networks improves neural flood forecasting accuracy.

## Abstract

Climate change exacerbates riverine floods, which occur with higher frequency and intensity than ever. The much-needed forecasting systems typically rely on accurate river discharge predictions. To this end, the SOTA data-driven approaches treat forecasting at spatially distributed gauge stations as isolated problems, even within the same river network. However, incorporating the known topology of the river network into the prediction model has the potential to leverage the adjacency relationship between gauges. Thus, we model river discharge for a network of gauging stations with GNNs and compare the forecasting performance achieved by different adjacency definitions. Our results show that the model fails to benefit from the river network topology information, both on the entire network and small subgraphs. The learned edge weights correlate with neither of the static definitions and exhibit no regular pattern. Furthermore, the GNNs struggle to predict sudden, narrow discharge spikes. Our work hints at a more general underlying phenomenon of neural prediction not always benefitting from graphical structure and may inspire a systematic study of the conditions under which this happens.