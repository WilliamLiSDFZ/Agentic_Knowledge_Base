---
title: "Hidden Traveling Waves bind Working Memory Variables in Recurrent Neural Networks"
source: "https://proceedings.mlr.press/v235/karuvally24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/karuvally24a/karuvally24a.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'sequence-models-for-memory-and-state']
tags: ['traveling-waves', 'working-memory', 'recurrent-neural-networks']
venue: "ICML 2024"
tldr: "Proposes a theoretical model of neural working memory in RNNs based on traveling wave dynamics within a neural lattice."
---

# Hidden Traveling Waves bind Working Memory Variables in Recurrent Neural Networks

**Source**: [https://proceedings.mlr.press/v235/karuvally24a.html](https://proceedings.mlr.press/v235/karuvally24a.html)

**TLDR**: Proposes a theoretical model of neural working memory in RNNs based on traveling wave dynamics within a neural lattice.

## Abstract

Traveling waves are a fundamental phenomenon in the brain, playing a crucial role in short-term information storage. In this study, we leverage the concept of traveling wave dynamics within a neural lattice to formulate a theoretical model of neural working memory in Recurrent Neural Networks (RNNs), study its properties, and its real world implications in AI. The proposed model diverges from traditional approaches, which assume information storage in static, register-like locations updated by interference. Instead, the model stores data as waves that is updated by the wave’s boundary conditions. We rigorously examine the model’s capabilities in representing and learning state histories, which are vital for learning history-dependent dynamical systems. The findings reveal that the model reliably stores external information and enhances the learning process by addressing the diminishing gradient problem of RNNs. To understand the model’s real-world applicability, we explore two cases: linear boundary condition and non-linear, self-attention-driven boundary condition. The experiments reveal that the linear scenario is effectively learned by RNNs through backpropagation when modeling history-dependent dynamical systems. Conversely, the non-linear scenario parallels an attention-only transformer. Collectively, our findings suggest the broader relevance of traveling waves in AI and its potential in advancing neural network architectures.