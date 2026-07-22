---
title: "CorNav: Autonomous Agent with Self-Corrected Planning for Zero-Shot Vision-and-Language Navigation"
source: "https://aclanthology.org/2024.findings-acl.745/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'multimodal-language-vision-learning-systems']
tags: ['vision-language-navigation', 'autonomous-agent', 'self-correction']
venue: "ACL 2024"
tldr: "Introduces CorNav, a zero-shot vision-and-language navigation agent with self-corrected planning for complex real-world environments."
---

# CorNav: Autonomous Agent with Self-Corrected Planning for Zero-Shot Vision-and-Language Navigation

**Source**: [https://aclanthology.org/2024.findings-acl.745/](https://aclanthology.org/2024.findings-acl.745/)

**TLDR**: Introduces CorNav, a zero-shot vision-and-language navigation agent with self-corrected planning for complex real-world environments.

## Abstract

AbstractUnderstanding and following natural language instructions while navigating through complex, real-world environments poses a significant challenge for general-purpose robots. These environments often include obstacles and pedestrians, making it essential for autonomous agents to possess the capability of self-corrected planning to adjust their actions based on feedback from the surroundings. However, the majority of existing vision-and-language navigation (VLN) methods primarily operate in less realistic simulator settings and do not incorporate environmental feedback into their decision-making processes. To address this gap, we introduce a novel zero-shot framework called CorNav, utilizing a large language model for decision-making and comprising two key components: 1) incorporating environmental feedback for refining future plans and adjusting its actions, and 2) multiple domain experts for parsing instructions, scene understanding, and refining predicted actions. In addition to the framework, we develop a 3D simulator that renders realistic scenarios using Unreal Engine 5. To evaluate the effectiveness and generalization of navigation agents in a zero-shot multi-task setting, we create a benchmark called NavBench. Our empirical study involves deploying 7 baselines across four tasks, i.e., goal-conditioned navigation given a specific object category, goal-conditioned navigation given simple instructions, finding abstract objects based on high-level instructions, and step-by-step instruction following. Extensive experiments demonstrate that CorNav consistently outperforms all baselines by a significant margin across all tasks. On average, CorNav achieves a success rate of 28.1%, surpassing the best baseline’s performance of 20.5%.