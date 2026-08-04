---
title: "Rich-Observation Reinforcement Learning with Continuous Latent Dynamics"
source: "https://proceedings.mlr.press/v235/song24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/song24i/song24i.pdf"
categories: ['online-learning-and-sequential-decision-making', 'neural-network-learning-dynamics-theory']
tags: ['rich-observation-RL', 'latent-dynamics', 'sample-efficiency', 'continuous-control']
venue: "ICML 2024"
tldr: "A theoretical framework for rich-observation RL with continuous latent dynamics is introduced to improve sample efficiency in high-dimensional perceptual settings."
---

# Rich-Observation Reinforcement Learning with Continuous Latent Dynamics

**Source**: [https://proceedings.mlr.press/v235/song24i.html](https://proceedings.mlr.press/v235/song24i.html)

**TLDR**: A theoretical framework for rich-observation RL with continuous latent dynamics is introduced to improve sample efficiency in high-dimensional perceptual settings.

## Abstract

Sample-efficiency and reliability remain major bottlenecks toward wide adoption of reinforcement learning algorithms in continuous settings with high-dimensional perceptual inputs. Toward addressing these challenges, we introduce a new theoretical framework, RichCLD (“Rich-Observation RL with Continuous Latent Dynamics”), in which the agent performs control based on high-dimensional observations, but the environment is governed by low-dimensional latent states and Lipschitz continuous dynamics. Our main contribution is a new algorithm for this setting that is provably statistically and computationally efficient. The core of our algorithm is a new representation learning objective; we show that prior representation learning schemes tailored to discrete dynamics do not naturally extend to the continuous setting. Our new objective is amenable to practical implementation, and empirically, we find that it compares favorably to prior schemes in a standard evaluation protocol. We further provide several insights into the statistical complexity of the RichCLD framework, in particular proving that certain notions of Lipschitzness that admit sample-efficient learning in the absence of rich observations are insufficient in the rich-observation setting.