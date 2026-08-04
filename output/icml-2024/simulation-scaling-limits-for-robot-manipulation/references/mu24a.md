---
title: "RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis"
source: "https://proceedings.mlr.press/v235/mu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mu24a/mu24a.pdf"
categories: ['llm-driven-automated-system-optimization', 'simulation-scaling-limits-for-robot-manipulation']
tags: ['robotic-behavior-synthesis', 'multimodal-code-generation', 'embodied-AI', 'LLM']
venue: "ICML 2024"
tldr: "RoboCodeX is a multimodal code generation framework that translates multimodal inputs into precise robot control programs for physical behavior synthesis."
---

# RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis

**Source**: [https://proceedings.mlr.press/v235/mu24a.html](https://proceedings.mlr.press/v235/mu24a.html)

**TLDR**: RoboCodeX is a multimodal code generation framework that translates multimodal inputs into precise robot control programs for physical behavior synthesis.

## Abstract

Robotic behavior synthesis, the problem of understanding multimodal inputs and generating precise physical control for robots, is an important part of Embodied AI. Despite successes in applying multimodal large language models for high-level understanding, it remains challenging to translate these conceptual understandings into detailed robotic actions while achieving generalization across various scenarios. In this paper, we propose a tree-structured multimodal code generation framework for generalized robotic behavior synthesis, termed RoboCodeX. RoboCodeX decomposes high-level human instructions into multiple object-centric manipulation units consisting of physical preferences such as affordance and safety constraints, and applies code generation to introduce generalization ability across various robotics platforms. To further enhance the capability to map conceptual and perceptual understanding into control commands, a specialized multimodal reasoning dataset is collected for pre-training and an iterative self-updating methodology is introduced for supervised fine-tuning. Extensive experiments demonstrate that RoboCodeX achieves state-of-the-art performance in both simulators and real robots on four different kinds of manipulation tasks and one embodied navigation task.