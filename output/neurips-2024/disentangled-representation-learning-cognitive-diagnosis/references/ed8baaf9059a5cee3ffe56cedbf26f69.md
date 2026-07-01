---
title: "Inference of Neural Dynamics Using Switching Recurrent Neural Networks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ed8baaf9059a5cee3ffe56cedbf26f69-Abstract-Conference.html"
categories: ['recurrent-and-spiking-neural-network-dynamics', 'disentangled-representation-learning-cognitive-diagnosis']
tags: ['neural-dynamics', 'switching-rnn', 'latent-variable-models']
venue: "NeurIPS 2024"
tldr: "Infers switching neural population dynamics using recurrent neural networks to capture distinct dynamical regimes in neural data."
---

# Inference of Neural Dynamics Using Switching Recurrent Neural Networks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ed8baaf9059a5cee3ffe56cedbf26f69-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ed8baaf9059a5cee3ffe56cedbf26f69-Abstract-Conference.html)

**TLDR**: Infers switching neural population dynamics using recurrent neural networks to capture distinct dynamical regimes in neural data.

## Abstract

Neural population activity often exhibits distinct dynamical features across time, which may correspond to distinct internal processes or behavior. Linear methods and variations thereof, such as Hidden Markov Model (HMM) and Switching Linear Dynamical System (SLDS), are often employed to identify discrete states with evolving neural dynamics. However, these techniques may not be able to capture the underlying nonlinear dynamics associated with neural propagation. Recurrent Neural Networks (RNNs) are commonly used to model neural dynamics thanks to their nonlinear characteristics. In our work, we develop Switching Recurrent Neural Networks (SRNN), RNNs with weights that switch across time, to reconstruct switching dynamics of neural time-series data. We apply these models to simulated data as well as cortical neural activity across mice and monkeys, which allows us to automatically detect discrete states that lead to the identification of varying neural dynamics. In a monkey reaching dataset with electrophysiology recordings, a mouse self-initiated lever pull dataset with widefield calcium recordings, and a mouse self-initiated decision making dataset with widefield calcium recording, SRNNs are able to automatically identify discrete states with distinct nonlinear neural dynamics. The inferred switches are aligned with the behavior, and the reconstructions show that the recovered neural dynamics are distinct across different stages of the behavior. We show that the neural dynamics have behaviorally-relevant switches across time and we are able to use SRNNs to successfully capture these switches and the corresponding dynamical features.