---
title: "Distributionally Robust Reinforcement Learning with Interactive Data Collection: Fundamental Hardness and Near-Optimal Algorithms"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/170dc3e41f2d03e327e04dbab0fccbfb-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making']
tags: ['distributionally-robust-RL', 'sim-to-real', 'robust-MDP']
venue: "NeurIPS 2024"
tldr: "This paper establishes fundamental hardness results and near-optimal algorithms for distributionally robust RL with interactive data collection to address sim-to-real gaps."
---

# Distributionally Robust Reinforcement Learning with Interactive Data Collection: Fundamental Hardness and Near-Optimal Algorithms

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/170dc3e41f2d03e327e04dbab0fccbfb-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/170dc3e41f2d03e327e04dbab0fccbfb-Abstract-Conference.html)

**TLDR**: This paper establishes fundamental hardness results and near-optimal algorithms for distributionally robust RL with interactive data collection to address sim-to-real gaps.

## Abstract

The sim-to-real gap, which represents the disparity between training and testing environments, poses a significant challenge in reinforcement learning (RL). A promising approach to addressing this challenge is distributionally robust RL, often framed as a robust Markov decision process (RMDP). In this framework, the objective is to find a robust policy that achieves good performance under the worst-case scenario among all environments within a pre-specified uncertainty set centered around the training environment. Unlike previous work, which relies on a generative model or a pre-collected offline dataset enjoying good coverage of the deployment environment, we tackle robust RL via interactive data collection, where the learner interacts with the training environment only and refines the policy through trial and error. In this robust RL paradigm, two main challenges emerge: managing distributional robustness while striking a balance between exploration and exploitation during data collection. Initially, we establish that sample-efficient learning without additional assumptions is unattainable owing to the curse of support shift; i.e., the potential disjointedness of the distributional supports between the training and testing environments. To circumvent such a hardness result, we introduce the vanishing minimal value assumption to RMDPs with a total-variation (TV) distance robust set, postulating that the minimal value of the optimal robust value function is zero. We prove that such an assumption effectively eliminates the support shift issue for RMDPs with a TV distance robust set, and present an algorithm with a provable sample complexity guarantee. Our work makes the initial step to uncovering the inherent difficulty of robust RL via interactive data collection and sufficient conditions for designing a sample-efficient algorithm accompanied by sharp sample complexity analysis.