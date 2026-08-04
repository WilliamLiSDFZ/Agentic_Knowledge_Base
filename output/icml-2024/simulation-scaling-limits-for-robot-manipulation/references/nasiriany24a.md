---
title: "PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs"
source: "https://proceedings.mlr.press/v235/nasiriany24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nasiriany24a/nasiriany24a.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation']
tags: ['vision-language-models', 'visual-prompting', 'robotic-control']
venue: "ICML 2024"
tldr: "PIVOT elicits actionable robot control knowledge from VLMs through iterative visual prompting without requiring text-only outputs."
---

# PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs

**Source**: [https://proceedings.mlr.press/v235/nasiriany24a.html](https://proceedings.mlr.press/v235/nasiriany24a.html)

**TLDR**: PIVOT elicits actionable robot control knowledge from VLMs through iterative visual prompting without requiring text-only outputs.

## Abstract

Vision language models (VLMs) have shown impressive capabilities across a variety of tasks, from logical reasoning to visual understanding. This opens the door to richer interaction with the world, for example robotic control. However, VLMs produce only textual outputs, while robotic control and other spatial tasks require outputting continuous coordinates, actions, or trajectories. How can we enable VLMs to handle such settings without fine-tuning on task-specific data? In this paper, we propose a novel visual prompting approach for VLMs that we call Prompting with Iterative Visual Optimization (PIVOT), which casts tasks as iterative visual question answering. In each iteration, the image is annotated with a visual representation of proposals that the VLM can refer to (e.g., candidate robot actions, localizations, or trajectories). The VLM then selects the best ones for the task. These proposals are iteratively refined, allowing the VLM to eventually zero in on the best available answer. We investigate PIVOT on real-world robotic navigation, real-world manipulation from images, instruction following in simulation, and additional spatial inference tasks such as localization. We find, perhaps surprisingly, that our approach enables zero-shot control of robotic systems without any robot training data, navigation in a variety of environments, and other capabilities. Although current performance is far from perfect, our work highlights potentials and limitations of this new regime and shows a promising approach for Internet-Scale VLMs in robotic and spatial reasoning domains.