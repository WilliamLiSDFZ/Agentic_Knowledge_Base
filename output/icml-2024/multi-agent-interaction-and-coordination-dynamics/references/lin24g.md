---
title: "Learning to Model the World With Language"
source: "https://proceedings.mlr.press/v235/lin24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24g/lin24g.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['world-models', 'language-grounding', 'agent-learning']
venue: "ICML 2024"
tldr: "A framework enabling agents to leverage diverse language to build world models for improved interaction and decision-making."
---

# Learning to Model the World With Language

**Source**: [https://proceedings.mlr.press/v235/lin24g.html](https://proceedings.mlr.press/v235/lin24g.html)

**TLDR**: A framework enabling agents to leverage diverse language to build world models for improved interaction and decision-making.

## Abstract

To interact with humans and act in the world, agents need to understand the range of language that people use and relate it to the visual world. While current agents can learn to execute simple language instructions, we aim to build agents that leverage diverse language—language like "this button turns on the TV" or "I put the bowls away"—that conveys general knowledge, describes the state of the world, provides interactive feedback, and more. Our key idea is that agents should interpret such diverse language as a signal that helps them predict the future: what they will observe, how the world will behave, and which situations will be rewarded. This perspective unifies language understanding with future prediction as a powerful self-supervised learning objective. We instantiate this in Dynalang, an agent that learns a multimodal world model to predict future text and image representations, and learns to act from imagined model rollouts. While current methods that learn language-conditioned policies degrade in performance with more diverse types of language, we show that Dynalang learns to leverage environment descriptions, game rules, and instructions to excel on tasks ranging from game-playing to navigating photorealistic home scans. Finally, we show that our method enables additional capabilities due to learning a generative model: Dynalang can be pretrained on text-only data, enabling learning from offline datasets, and generate language grounded in an environment.