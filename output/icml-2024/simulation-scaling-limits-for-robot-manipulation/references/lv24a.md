---
title: "RoboMP$^2$: A Robotic Multimodal Perception-Planning Framework with Multimodal Large Language Models"
source: "https://proceedings.mlr.press/v235/lv24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lv24a/lv24a.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', 'large-language-model-alignment-and-capabilities']
tags: ['multimodal-LLM', 'robotics', 'perception-planning', 'embodied-agents']
venue: "ICML 2024"
tldr: "RoboMP² is a robotic multimodal perception-planning framework leveraging multimodal large language models for improved embodied agent performance."
---

# RoboMP$^2$: A Robotic Multimodal Perception-Planning Framework with Multimodal Large Language Models

**Source**: [https://proceedings.mlr.press/v235/lv24a.html](https://proceedings.mlr.press/v235/lv24a.html)

**TLDR**: RoboMP² is a robotic multimodal perception-planning framework leveraging multimodal large language models for improved embodied agent performance.

## Abstract

Multimodal Large Language Models (MLLMs) have shown impressive reasoning abilities and general intelligence in various domains. It inspires researchers to train end-to-end MLLMs or utilize large models to generate policies with human-selected prompts for embodied agents. However, these methods exhibit limited generalization capabilities on unseen tasks or scenarios, and overlook the multimodal environment information which is critical for robots to make decisions. In this paper, we introduce a novel Robotic Multimodal Perception-Planning (RoboMP$^2$) framework for robotic manipulation which consists of a Goal-Conditioned Multimodal Preceptor (GCMP) and a Retrieval-Augmented Multimodal Planner (RAMP). Specially, GCMP captures environment states by employing a tailored MLLMs for embodied agents with the abilities of semantic reasoning and localization. RAMP utilizes coarse-to-fine retrieval method to find the $k$ most-relevant policies as in-context demonstrations to enhance the planner. Extensive experiments demonstrate the superiority of RoboMP$^2$ on both VIMA benchmark and real-world tasks, with around 10% improvement over the baselines.