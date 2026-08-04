---
title: "Learning Reward for Robot Skills Using Large Language Models via Self-Alignment"
source: "https://proceedings.mlr.press/v235/zeng24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zeng24d/zeng24d.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'simulation-scaling-limits-for-robot-manipulation']
tags: ['reward-learning', 'LLM', 'robot-skills']
venue: "ICML 2024"
tldr: "A self-alignment approach using LLMs to iteratively refine reward functions for learning diverse robot manipulation skills."
---

# Learning Reward for Robot Skills Using Large Language Models via Self-Alignment

**Source**: [https://proceedings.mlr.press/v235/zeng24d.html](https://proceedings.mlr.press/v235/zeng24d.html)

**TLDR**: A self-alignment approach using LLMs to iteratively refine reward functions for learning diverse robot manipulation skills.

## Abstract

Learning reward functions remains the bottleneck to equip a robot with a broad repertoire of skills. Large Language Models (LLM) contain valuable task-related knowledge that can potentially aid in the learning of reward functions. However, the proposed reward function can be imprecise, thus ineffective which requires to be further grounded with environment information. We proposed a method to learn rewards more efficiently in the absence of humans. Our approach consists of two components: We first use the LLM to propose features and parameterization of the reward, then update the parameters through an iterative self-alignment process. In particular, the process minimizes the ranking inconsistency between the LLM and the learnt reward functions based on the execution feedback. The method was validated on 9 tasks across 2 simulation environments. It demonstrates a consistent improvement in training efficacy and efficiency, meanwhile consuming significantly fewer GPT tokens compared to the alternative mutation-based method.