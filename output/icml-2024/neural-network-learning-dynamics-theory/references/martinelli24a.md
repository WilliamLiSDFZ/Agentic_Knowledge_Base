---
title: "Expand-and-Cluster: Parameter Recovery of Neural Networks"
source: "https://proceedings.mlr.press/v235/martinelli24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/martinelli24a/martinelli24a.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['parameter-recovery', 'neural-network-identifiability', 'expand-and-cluster']
venue: "ICML 2024"
tldr: "An expand-and-cluster algorithm that provably recovers the weights of a neural network from its input-output mapping."
---

# Expand-and-Cluster: Parameter Recovery of Neural Networks

**Source**: [https://proceedings.mlr.press/v235/martinelli24a.html](https://proceedings.mlr.press/v235/martinelli24a.html)

**TLDR**: An expand-and-cluster algorithm that provably recovers the weights of a neural network from its input-output mapping.

## Abstract

Can we identify the weights of a neural network by probing its input-output mapping? At first glance, this problem seems to have many solutions because of permutation, overparameterisation and activation function symmetries. Yet, we show that the incoming weight vector of each neuron is identifiable up to sign or scaling, depending on the activation function. Our novel method ’Expand-and-Cluster’ can identify layer sizes and weights of a target network for all commonly used activation functions. Expand-and-Cluster consists of two phases: (i) to relax the non-convex optimisation problem, we train multiple overparameterised student networks to best imitate the target function; (ii) to reverse engineer the target network’s weights, we employ an ad-hoc clustering procedure that reveals the learnt weight vectors shared between students – these correspond to the target weight vectors. We demonstrate successful weights and size recovery of trained shallow and deep networks with less than 10% overhead in the layer size and describe an ’ease-of-identifiability’ axis by analysing 150 synthetic problems of variable difficulty.