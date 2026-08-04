---
title: "RoboDreamer: Learning Compositional World Models for Robot Imagination"
source: "https://proceedings.mlr.press/v235/zhou24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24f/zhou24f.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', 'generative-models-and-variational-inference']
tags: ['world-models', 'compositional-generation', 'robot-planning']
venue: "ICML 2024"
tldr: "Presents RoboDreamer, a compositional world model leveraging text-to-video generation for robot imagination and decision-making with improved generalization."
---

# RoboDreamer: Learning Compositional World Models for Robot Imagination

**Source**: [https://proceedings.mlr.press/v235/zhou24f.html](https://proceedings.mlr.press/v235/zhou24f.html)

**TLDR**: Presents RoboDreamer, a compositional world model leveraging text-to-video generation for robot imagination and decision-making with improved generalization.

## Abstract

Text-to-video models have demonstrated substantial potential in robotic decision-making, enabling the imagination of realistic plans of future actions as well as accurate environment simulation. However, one major issue in such models is generalization – models are limited to synthesizing videos subject to language instructions similar to those seen at training time. This is heavily limiting in decision-making, where we seek a powerful world model to synthesize plans of unseen combinations of objects and actions in order to solve previously unseen tasks in new environments. To resolve this issue, we introduce RoboDreamer, an innovative approach for learning a compositional world model by factorizing the video generation. We leverage the natural compositionality of language to parse instructions into a set of lower-level primitives, which we condition a set of models on to generate videos. We illustrate how this factorization naturally enables compositional generalization, by allowing us to formulate a new natural language instruction as a combination of previously seen components. We further show how such a factorization enables us to add additional multimodal goals, allowing us to specify a video we wish to generate given both natural language instructions and a goal image. Our approach can successfully synthesize video plans on unseen goals in the RT-X, enables successful robot execution in simulation, and substantially outperforms monolithic baseline approaches to video generation.