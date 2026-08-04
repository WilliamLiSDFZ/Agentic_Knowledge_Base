---
title: "DynSyn: Dynamical Synergistic Representation for Efficient Learning and Control in Overactuated Embodied Systems"
source: "https://proceedings.mlr.press/v235/he24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24o/he24o.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['overactuated-systems', 'musculoskeletal-control', 'reinforcement-learning', 'synergy']
venue: "ICML 2024"
tldr: "Proposes a dynamical synergistic representation to enable efficient policy learning for overactuated embodied systems."
---

# DynSyn: Dynamical Synergistic Representation for Efficient Learning and Control in Overactuated Embodied Systems

**Source**: [https://proceedings.mlr.press/v235/he24o.html](https://proceedings.mlr.press/v235/he24o.html)

**TLDR**: Proposes a dynamical synergistic representation to enable efficient policy learning for overactuated embodied systems.

## Abstract

Learning an effective policy to control high-dimensional, overactuated systems is a significant challenge for deep reinforcement learning algorithms. Such control scenarios are often observed in the neural control of vertebrate musculoskeletal systems. The study of these control mechanisms will provide insights into the control of high-dimensional, overactuated systems. The coordination of actuators, known as muscle synergies in neuromechanics, is considered a presumptive mechanism that simplifies the generation of motor commands. The dynamical structure of a system is the basis of its function, allowing us to derive a synergistic representation of actuators. Motivated by this theory, we propose the Dynamical Synergistic Representation (DynSyn) algorithm. DynSyn aims to generate synergistic representations from dynamical structures and perform task-specific, state-dependent adaptation to the representations to improve motor control. We demonstrate DynSyn’s efficiency across various tasks involving different musculoskeletal models, achieving state-of-the-art sample efficiency and robustness compared to baseline algorithms. DynSyn generates interpretable synergistic representations that capture the essential features of dynamical structures and demonstrates generalizability across diverse motor tasks.