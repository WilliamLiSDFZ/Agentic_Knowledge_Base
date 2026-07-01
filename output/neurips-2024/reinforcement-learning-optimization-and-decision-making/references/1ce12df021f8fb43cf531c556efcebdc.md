---
title: "Embedding-Aligned Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1ce12df021f8fb43cf531c556efcebdc-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'reinforcement-learning-optimization-and-decision-making']
tags: ['reinforcement-learning', 'embedding-alignment', 'language-model-training']
venue: "NeurIPS 2024"
tldr: "EAGLE trains LLMs via reinforcement learning to align generated text with objectives defined in a latent embedding space."
---

# Embedding-Aligned Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1ce12df021f8fb43cf531c556efcebdc-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/1ce12df021f8fb43cf531c556efcebdc-Abstract-Conference.html)

**TLDR**: EAGLE trains LLMs via reinforcement learning to align generated text with objectives defined in a latent embedding space.

## Abstract

We propose a novel approach for training large language models (LLMs) to adhere to objectives defined within a latent embedding space. Our method leverages reinforcement learning (RL), treating a pre-trained LLM as an environment. Our embedding-aligned guided language (EAGLE) agent is trained to iteratively steer the LLM's generation towards optimal regions of the latent embedding space, w.r.t. some predefined criterion. We demonstrate the effectiveness of the EAGLE agent using the MovieLens 25M and Amazon Review datasets to surface content gaps that satisfy latent user demand. We also demonstrate the benefit of using an optimal design of a state-dependent action set to improve EAGLE's efficiency. Our work paves the way for controlled and grounded text generation using LLMs, ensuring consistency with domain-specific knowledge and data representations.