---
title: "Predicting the Unpredictable: Uncertainty-Aware Reasoning over Temporal Knowledge Graphs via Diffusion Process"
source: "https://aclanthology.org/2024.findings-acl.343/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'causal-reasoning-and-explanation-in-nlp']
tags: ['temporal-knowledge-graph', 'reasoning', 'diffusion-process', 'uncertainty', 'future-prediction']
venue: "ACL 2024"
tldr: "Models temporal knowledge graph reasoning as a diffusion process to capture uncertainty in predicting future incomplete facts."
---

# Predicting the Unpredictable: Uncertainty-Aware Reasoning over Temporal Knowledge Graphs via Diffusion Process

**Source**: [https://aclanthology.org/2024.findings-acl.343/](https://aclanthology.org/2024.findings-acl.343/)

**TLDR**: Models temporal knowledge graph reasoning as a diffusion process to capture uncertainty in predicting future incomplete facts.

## Abstract

AbstractTemporal Knowledge Graph (TKG) reasoning seeks to predict future incomplete facts leveraging historical data. While existing approaches have shown effectiveness in addressing the task through various perspectives, such as graph learning and logic rules, they are limited in capturing the indeterminacy in future events, particularly in the case of rare/unseen facts. To tackle the highlighted issues, we introduce a novel approach by conceptualizing TKG reasoning as a sequence denoising process for future facts, namely DiffuTKG. Concretely, we first encodes the historical events as the conditional sequence. Then we gradually introduce Gaussian noise to corrupt target facts during the forward process and then employ a transformer-based conditional denoiser to restore them in the reverse phase. Moreover, we introduce an uncertainty regularization loss to mitigate the risk of prediction biases by favoring frequent scenarios over rare/unseen facts. Empirical results on four real-world datasets show that DiffuTKG outperforms state-of-the-art methods across multiple evaluation metrics.