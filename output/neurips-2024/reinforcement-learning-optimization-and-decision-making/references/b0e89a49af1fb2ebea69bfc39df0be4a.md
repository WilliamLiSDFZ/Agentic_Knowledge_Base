---
title: "Diffusion-based Curriculum Reinforcement Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b0e89a49af1fb2ebea69bfc39df0be4a-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'diffusion-based-generative-modeling-and-inference']
tags: ['curriculum-reinforcement-learning', 'diffusion-models', 'task-generation', 'exploration']
venue: "NeurIPS 2024"
tldr: "Diffusion models are used to generate structured curricula of increasing complexity to guide reinforcement learning agents toward desired outcomes."
---

# Diffusion-based Curriculum Reinforcement Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b0e89a49af1fb2ebea69bfc39df0be4a-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/b0e89a49af1fb2ebea69bfc39df0be4a-Abstract-Conference.html)

**TLDR**: Diffusion models are used to generate structured curricula of increasing complexity to guide reinforcement learning agents toward desired outcomes.

## Abstract

Curriculum Reinforcement Learning (CRL) is an approach to facilitate the learning process of agents by structuring tasks in a sequence of increasing complexity. Despite its potential, many existing CRL methods struggle to efficiently guide agents toward desired outcomes, particularly in the absence of domain knowledge. This paper introduces DiCuRL (Diffusion Curriculum Reinforcement Learning), a novel method that leverages conditional diffusion models to generate curriculum goals. To estimate how close an agent is to achieving its goal, our method uniquely incorporates a $Q$-function and a trainable reward function based on Adversarial Intrinsic Motivation within the diffusion model. Furthermore, it promotes exploration through the inherent noising and denoising mechanism present in the diffusion models and is environment-agnostic. This combination allows for the generation of challenging yet achievable goals, enabling agents to learn effectively without relying on domain knowledge. We demonstrate the effectiveness of DiCuRL in three different maze environments and two robotic manipulation tasks simulated in MuJoCo, where it outperforms or matches nine state-of-the-art CRL algorithms from the literature.