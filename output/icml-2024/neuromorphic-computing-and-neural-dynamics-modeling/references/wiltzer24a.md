---
title: "A Distributional Analogue to the Successor Representation"
source: "https://proceedings.mlr.press/v235/wiltzer24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wiltzer24a/wiltzer24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['distributional-reinforcement-learning', 'successor-representation', 'return-distribution', 'policy-evaluation']
venue: "ICML 2024"
tldr: "Introduces a distributional successor representation that cleanly separates transition structure from reward for distributional RL."
---

# A Distributional Analogue to the Successor Representation

**Source**: [https://proceedings.mlr.press/v235/wiltzer24a.html](https://proceedings.mlr.press/v235/wiltzer24a.html)

**TLDR**: Introduces a distributional successor representation that cleanly separates transition structure from reward for distributional RL.

## Abstract

This paper contributes a new approach for distributional reinforcement learning which elucidates a clean separation of transition structure and reward in the learning process. Analogous to how the successor representation (SR) describes the expected consequences of behaving according to a given policy, our distributional successor measure (SM) describes the distributional consequences of this behaviour. We formulate the distributional SM as a distribution over distributions and provide theory connecting it with distributional and model-based reinforcement learning. Moreover, we propose an algorithm that learns the distributional SM from data by minimizing a two-level maximum mean discrepancy. Key to our method are a number of algorithmic techniques that are independently valuable for learning generative models of state. As an illustration of the usefulness of the distributional SM, we show that it enables zero-shot risk-sensitive policy evaluation in a way that was not previously possible.