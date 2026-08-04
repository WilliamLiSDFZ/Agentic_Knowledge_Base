---
title: "AD3: Implicit Action is the Key for World Models to Distinguish the Diverse Visual Distractors"
source: "https://proceedings.mlr.press/v235/wang24bq.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bq/wang24bq.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'generative-models-and-variational-inference']
tags: ['world-models', 'visual-distractors', 'model-based-rl', 'action-representation']
venue: "ICML 2024"
tldr: "Proposes AD3, a world model that uses implicit action representations to distinguish homogeneous visual distractors in visual control tasks."
---

# AD3: Implicit Action is the Key for World Models to Distinguish the Diverse Visual Distractors

**Source**: [https://proceedings.mlr.press/v235/wang24bq.html](https://proceedings.mlr.press/v235/wang24bq.html)

**TLDR**: Proposes AD3, a world model that uses implicit action representations to distinguish homogeneous visual distractors in visual control tasks.

## Abstract

Model-based methods have significantly contributed to distinguishing task-irrelevant distractors for visual control. However, prior research has primarily focused on heterogeneous distractors like noisy background videos, leaving homogeneous distractors that closely resemble controllable agents largely unexplored, which poses significant challenges to existing methods. To tackle this problem, we propose Implicit Action Generator (IAG) to learn the implicit actions of visual distractors, and present a new algorithm named implicit Action-informed Diverse visual Distractors Distinguisher (AD3), that leverages the action inferred by IAG to train separated world models. Implicit actions effectively capture the behavior of background distractors, aiding in distinguishing the task-irrelevant components, and the agent can optimize the policy within the task-relevant state space. Our method achieves superior performance on various visual control tasks featuring both heterogeneous and homogeneous distractors. The indispensable role of implicit actions learned by IAG is also empirically validated.