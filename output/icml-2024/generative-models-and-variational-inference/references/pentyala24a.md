---
title: "CaPS: Collaborative and Private Synthetic Data Generation from Distributed Sources"
source: "https://proceedings.mlr.press/v235/pentyala24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pentyala24a/pentyala24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'generative-models-and-variational-inference']
tags: ['synthetic-data', 'privacy', 'federated', 'distributed-sources', 'differential-privacy']
venue: "ICML 2024"
tldr: "Proposes CaPS, a collaborative and privacy-preserving framework for synthetic data generation from distributed data sources."
---

# CaPS: Collaborative and Private Synthetic Data Generation from Distributed Sources

**Source**: [https://proceedings.mlr.press/v235/pentyala24a.html](https://proceedings.mlr.press/v235/pentyala24a.html)

**TLDR**: Proposes CaPS, a collaborative and privacy-preserving framework for synthetic data generation from distributed data sources.

## Abstract

Data is the lifeblood of the modern world, forming a fundamental part of AI, decision-making, and research advances. With increase in interest in data, governments have taken important steps towards a regulated data world, drastically impacting data sharing and data usability and resulting in massive amounts of data confined within the walls of organizations. While synthetic data generation (SDG) is an appealing solution to break down these walls and enable data sharing, the main drawback of existing solutions is the assumption of a trusted aggregator for generative model training. Given that many data holders may not want to, or be legally allowed to, entrust a central entity with their raw data, we propose a framework for collaborative and private generation of synthetic tabular data from distributed data holders. Our solution is general, applicable to any marginal-based SDG, and provides input privacy by replacing the trusted aggregator with secure multi-party computation (MPC) protocols and output privacy via differential privacy (DP). We demonstrate the applicability and scalability of our approach for the state-of-the-art select-measure-generate SDG algorithms MWEM+PGM and AIM.