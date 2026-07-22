---
title: "A Unified Temporal Knowledge Graph Reasoning Model Towards Interpolation and Extrapolation"
source: "https://aclanthology.org/2024.acl-long.8/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['temporal-knowledge-graph', 'interpolation', 'extrapolation', 'reasoning']
venue: "ACL 2024"
tldr: "A unified model for temporal knowledge graph reasoning that handles both interpolation and extrapolation settings."
---

# A Unified Temporal Knowledge Graph Reasoning Model Towards Interpolation and Extrapolation

**Source**: [https://aclanthology.org/2024.acl-long.8/](https://aclanthology.org/2024.acl-long.8/)

**TLDR**: A unified model for temporal knowledge graph reasoning that handles both interpolation and extrapolation settings.

## Abstract

AbstractTemporal knowledge graph (TKG) reasoning has two settings: interpolation reasoning and extrapolation reasoning. Both of them draw plenty of research interest and have great significance. Methods of the former de-emphasize the temporal correlations among facts sequences, while methods of the latter require strict chronological order of knowledge and ignore inferring clues provided by missing facts of the past. These limit the practicability of TKG applications as almost all of the existing TKG reasoning methods are designed specifically to address either one setting. To this end, this paper proposes an original Temporal PAth-based Reasoning (TPAR) model for both the interpolation and extrapolation reasoning settings. TPAR performs a neural-driven symbolic reasoning fashion that is robust to ambiguous and noisy temporal data, and with fine interpretability as well. Comprehensive experiments show that TPAR outperforms SOTA methods on the link prediction task for both the interpolation and the extrapolation settings. A novel pipeline experimental setting is designed to evaluate the performances of SOTA combinations and the proposed TPAR towards interpolation and extrapolation reasoning. And more diverse experiments are conducted to show the robustness and interpretability of TPAR.