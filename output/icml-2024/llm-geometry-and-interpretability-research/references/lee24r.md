---
title: "Why Do Animals Need Shaping? A Theory of Task Composition and Curriculum Learning"
source: "https://proceedings.mlr.press/v235/lee24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24r/lee24r.pdf"
categories: ['llm-geometry-and-interpretability-research', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['curriculum-learning', 'task-composition', 'shaping', 'neuroscience', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "Develops a theory of curriculum learning explaining why shaping procedures accelerate animal and machine learning on complex tasks."
---

# Why Do Animals Need Shaping? A Theory of Task Composition and Curriculum Learning

**Source**: [https://proceedings.mlr.press/v235/lee24r.html](https://proceedings.mlr.press/v235/lee24r.html)

**TLDR**: Develops a theory of curriculum learning explaining why shaping procedures accelerate animal and machine learning on complex tasks.

## Abstract

Diverse studies in systems neuroscience begin with extended periods of curriculum training known as ‘shaping’ procedures. These involve progressively studying component parts of more complex tasks, and can make the difference between learning a task quickly, slowly or not at all. Despite the importance of shaping to the acquisition of complex tasks, there is as yet no theory that can help guide the design of shaping procedures, or more fundamentally, provide insight into its key role in learning. Modern deep reinforcement learning systems might implicitly learn compositional primitives within their multilayer policy networks. Inspired by these models, we propose and analyse a model of deep policy gradient learning of simple compositional reinforcement learning tasks. Using the tools of statistical physics, we solve for exact learning dynamics and characterise different learning strategies including primitives pre-training, in which task primitives are studied individually before learning compositional tasks. We find a complex interplay between task complexity and the efficacy of shaping strategies. Overall, our theory provides an analytical understanding of the benefits of shaping in a class of compositional tasks and a quantitative account of how training protocols can disclose useful task primitives, ultimately yielding faster and more robust learning.