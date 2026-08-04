---
title: "Coprocessor Actor Critic: A Model-Based Reinforcement Learning Approach For Adaptive Brain Stimulation"
source: "https://proceedings.mlr.press/v235/pan24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pan24g/pan24g.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['brain-stimulation', 'model-based-RL', 'neural-dynamics', "Parkinson's-disease"]
venue: "ICML 2024"
tldr: "Introduces Coprocessor Actor Critic, a model-based reinforcement learning approach for adaptive brain stimulation that learns personalized stimulation policies for neurological conditions."
---

# Coprocessor Actor Critic: A Model-Based Reinforcement Learning Approach For Adaptive Brain Stimulation

**Source**: [https://proceedings.mlr.press/v235/pan24g.html](https://proceedings.mlr.press/v235/pan24g.html)

**TLDR**: Introduces Coprocessor Actor Critic, a model-based reinforcement learning approach for adaptive brain stimulation that learns personalized stimulation policies for neurological conditions.

## Abstract

Adaptive brain stimulation can treat neurological conditions such as Parkinson’s disease and post-stroke motor deficits by influencing abnormal neural activity. Because of patient heterogeneity, each patient requires a unique stimulation policy to achieve optimal neural responses. Model-free reinforcement learning (MFRL) holds promise in learning effective policies for a variety of similar control tasks, but is limited in domains like brain stimulation by a need for numerous costly environment interactions. In this work we introduce Coprocessor Actor Critic, a novel, model-based reinforcement learning (MBRL) approach for learning neural coprocessor policies for brain stimulation. Our key insight is that coprocessor policy learning is a combination of learning how to act optimally in the world and learning how to induce optimal actions in the world through stimulation of an injured brain. We show that our approach overcomes the limitations of traditional MFRL methods in terms of sample efficiency and task success and outperforms baseline MBRL approaches in a neurologically realistic model of an injured brain.