---
title: "From Geometry to Causality- Ricci Curvature and the Reliability of Causal Inference on Networks"
source: "https://proceedings.mlr.press/v235/farzam24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/farzam24a/farzam24a.pdf"
categories: ['causal-inference-and-discovery-methods']
tags: ['causal-inference', 'network-interference', 'ricci-curvature']
venue: "ICML 2024"
tldr: "Demonstrates that Ricci curvature of networks can characterize interference structure and improve reliability of causal inference on graphs."
---

# From Geometry to Causality- Ricci Curvature and the Reliability of Causal Inference on Networks

**Source**: [https://proceedings.mlr.press/v235/farzam24a.html](https://proceedings.mlr.press/v235/farzam24a.html)

**TLDR**: Demonstrates that Ricci curvature of networks can characterize interference structure and improve reliability of causal inference on graphs.

## Abstract

Causal inference on networks faces challenges posed in part by violations of standard identification assumptions due to dependencies between treatment units. Although graph geometry fundamentally influences such dependencies, the potential of geometric tools for causal inference on networked treatment units is yet to be unlocked. Moreover, despite significant progress utilizing graph neural networks (GNNs) for causal inference on networks, methods for evaluating their achievable reliability without ground truth are lacking. In this work we establish for the first time a theoretical link between network geometry, the graph Ricci curvature in particular, and causal inference, formalizing the intrinsic challenges that negative curvature poses to estimating causal parameters. The Ricci curvature can then be used to assess the reliability of causal estimates in structured data, as we empirically demonstrate. Informed by this finding, we propose a method using the geometric Ricci flow to reduce causal effect estimation error in networked data, showcasing how this newfound connection between graph geometry and causal inference could improve GNN-based causal inference. Bridging graph geometry and causal inference, this paper opens the door to geometric techniques for improving causal estimation on networks.