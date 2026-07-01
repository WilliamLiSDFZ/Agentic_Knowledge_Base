---
title: "iVideoGPT: Interactive VideoGPTs are Scalable World Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7dbb5bfab324e3b86af9bd0df15498dd-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making']
tags: ['world-models', 'video-generation', 'interactive-agents']
venue: "NeurIPS 2024"
tldr: "Introduces iVideoGPT, a scalable interactive world model built on video generative transformers for model-based decision-making."
---

# iVideoGPT: Interactive VideoGPTs are Scalable World Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7dbb5bfab324e3b86af9bd0df15498dd-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/7dbb5bfab324e3b86af9bd0df15498dd-Abstract-Conference.html)

**TLDR**: Introduces iVideoGPT, a scalable interactive world model built on video generative transformers for model-based decision-making.

## Abstract

World models empower model-based agents to interactively explore, reason, and plan within imagined environments for real-world decision-making. However, the high demand for interactivity poses challenges in harnessing recent advancements in video generative models for developing world models at scale. This work introduces Interactive VideoGPT (iVideoGPT), a scalable autoregressive transformer framework that integrates multimodal signals—visual observations, actions, and rewards—into a sequence of tokens, facilitating an interactive experience of agents via next-token prediction. iVideoGPT features a novel compressive tokenization technique that efficiently discretizes high-dimensional visual observations. Leveraging its scalable architecture, we are able to pre-train iVideoGPT on millions of human and robotic manipulation trajectories, establishing a versatile foundation that is adaptable to serve as interactive world models for a wide range of downstream tasks. These include action-conditioned video prediction, visual planning, and model-based reinforcement learning, where iVideoGPT achieves competitive performance compared with state-of-the-art methods. Our work advances the development of interactive general world models, bridging the gap between generative video models and practical model-based reinforcement learning applications. Code and pre-trained models are available at https://thuml.github.io/iVideoGPT.