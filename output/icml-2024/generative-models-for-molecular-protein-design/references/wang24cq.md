---
title: "Knowledge-aware Reinforced Language Models for Protein Directed Evolution"
source: "https://proceedings.mlr.press/v235/wang24cq.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cq/wang24cq.pdf"
categories: ['generative-models-for-molecular-protein-design']
tags: ['directed-evolution', 'protein-optimization', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "A knowledge-aware reinforced language model framework is proposed to incorporate domain knowledge into machine-learning-assisted protein directed evolution."
---

# Knowledge-aware Reinforced Language Models for Protein Directed Evolution

**Source**: [https://proceedings.mlr.press/v235/wang24cq.html](https://proceedings.mlr.press/v235/wang24cq.html)

**TLDR**: A knowledge-aware reinforced language model framework is proposed to incorporate domain knowledge into machine-learning-assisted protein directed evolution.

## Abstract

Directed evolution, a cornerstone of protein optimization, is to harness natural mutational processes to enhance protein functionality. Existing Machine Learning-assisted Directed Evolution (MLDE) methodologies typically rely on data-driven strategies and often overlook the profound domain knowledge in biochemical fields. In this paper, we introduce a novel Knowledge-aware Reinforced Language Model (KnowRLM) for MLDE. An Amino Acid Knowledge Graph (AAKG) is constructed to represent the intricate biochemical relationships among amino acids. We further propose a Protein Language Model (PLM)-based policy network that iteratively samples mutants through preferential random walks on the AAKG using a dynamic sliding window mechanism. The novel mutants are actively sampled to fine-tune a fitness predictor as the reward model, providing feedback to the knowledge-aware policy. Finally, we optimize the whole system in an active learning approach that mimics biological settings in practice.KnowRLM stands out for its ability to utilize contextual amino acid information from knowledge graphs, thus attaining advantages from both statistical patterns of protein sequences and biochemical properties of amino acids.Extensive experiments demonstrate the superior performance of KnowRLM in more efficiently identifying high-fitness mutants compared to existing methods.