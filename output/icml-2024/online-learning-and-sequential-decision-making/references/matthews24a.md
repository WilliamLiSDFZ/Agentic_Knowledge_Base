---
title: "Craftax: A Lightning-Fast Benchmark for Open-Ended Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/matthews24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/matthews24a/matthews24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['open-ended-learning', 'reinforcement-learning-benchmark', 'sample-efficiency']
venue: "ICML 2024"
tldr: "Craftax, a fast and challenging benchmark designed for open-ended reinforcement learning research."
---

# Craftax: A Lightning-Fast Benchmark for Open-Ended Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/matthews24a.html](https://proceedings.mlr.press/v235/matthews24a.html)

**TLDR**: Craftax, a fast and challenging benchmark designed for open-ended reinforcement learning research.

## Abstract

Benchmarks play a crucial role in the development and analysis of reinforcement learning (RL) algorithms. We identify that existing benchmarks used for research into open-ended learning fall into one of two categories. Either they are too slow for meaningful research to be performed without enormous computational resources, like Crafter, NetHack and Minecraft, or they are not complex enough to pose a significant challenge, like Minigrid and Procgen. To remedy this, we first present Craftax-Classic: a ground-up rewrite of Crafter in JAX that runs up to 250x faster than the Python-native original. A run of PPO using 1 billion environment interactions finishes in under an hour using only a single GPU and averages 90% of the optimal reward. To provide a more compelling challenge we present the main Craftax benchmark, a significant extension of the Crafter mechanics with elements inspired from NetHack. Solving Craftax requires deep exploration, long term planning and memory, as well as continual adaptation to novel situations as more of the world is discovered. We show that existing methods including global and episodic exploration, as well as unsupervised environment design fail to make material progress on the benchmark. We therefore believe that Craftax can for the first time allow researchers to experiment in a complex, open-ended environment with limited computational resources.