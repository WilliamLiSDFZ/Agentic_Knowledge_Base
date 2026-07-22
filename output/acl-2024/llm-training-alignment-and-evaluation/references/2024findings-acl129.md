---
title: "Plum: Prompt Learning using Metaheuristics"
source: "https://aclanthology.org/2024.findings-acl.129/"
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['prompt-optimization', 'metaheuristics', 'llm-prompting']
venue: "ACL 2024"
tldr: "Plum applies metaheuristic search algorithms to automate prompt learning and discovery for large language models."
---

# Plum: Prompt Learning using Metaheuristics

**Source**: [https://aclanthology.org/2024.findings-acl.129/](https://aclanthology.org/2024.findings-acl.129/)

**TLDR**: Plum applies metaheuristic search algorithms to automate prompt learning and discovery for large language models.

## Abstract

AbstractSince the emergence of large language models, prompt learning has become a popular method for optimizing and customizing these models. Special prompts, such as Chain-of-Thought, have even revealed previously unknown reasoning capabilities within these models. However, the progress of discovering effective prompts has been slow, driving a desire for general prompt optimization methods. Unfortunately, few existing prompt learning methods satisfy the criteria of being truly “general”, i.e., automatic, discrete, black-box, gradient-free, and interpretable all at once. In this paper, we introduce metaheuristics, a branch of discrete non-convex optimization methods with over 100 options, as a promising approach to prompt learning. Within our paradigm, we test six typical methods: hill climbing, simulated annealing, genetic algorithms with/without crossover, tabu search, and harmony search, demonstrating their effectiveness in white-box and black-box prompt learning. Furthermore, we show that these methods can be used to discover more human-understandable prompts that were previously unknown in both reasoning and image generation tasks, opening the door to a cornucopia of possibilities in prompt optimization.