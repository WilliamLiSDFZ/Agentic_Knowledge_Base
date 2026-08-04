---
title: "Towards Efficient Exact Optimization of Language Model Alignment"
source: "https://proceedings.mlr.press/v235/ji24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ji24c/ji24c.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'optimization-algorithms-convergence-theory']
tags: ['LLM-alignment', 'policy-optimization', 'KL-divergence', 'reward-maximization', 'exact-optimization']
venue: "ICML 2024"
tldr: "This paper derives an efficient exact optimization approach for language model alignment that maximizes expected human-preference rewards with minimal policy deviation."
---

# Towards Efficient Exact Optimization of Language Model Alignment

**Source**: [https://proceedings.mlr.press/v235/ji24c.html](https://proceedings.mlr.press/v235/ji24c.html)

**TLDR**: This paper derives an efficient exact optimization approach for language model alignment that maximizes expected human-preference rewards with minimal policy deviation.

## Abstract

The alignment of language models with human preferences is vital for their application in real-world tasks. The problem is formulated as optimizing the model’s policy to maximize the expected reward that reflects human preferences with minimal deviation from the initial policy. While considered as a straightforward solution, reinforcement learning (RL) suffers from high variance in policy updates, which impedes efficient policy improvement. Recently, direct preference optimization (DPO) was proposed to directly optimize the policy from preference data. However, we show that DPO derived based on the optimal solution of the problem leads to a compromised mean-seeking approximation of the optimal solution in practice. In this paper, we propose efficient exact optimization (EXO) of the alignment objective. EXO is guaranteed to optimize in the same direction as RL algorithms asymptotically for arbitrary policy parametrization. This leads to the same mode-seeking solution, while enables efficient optimization by circumventing the complexities of RL. We also compare our method to DPO with both theoretical and empirical analyses, and further demonstrate the advantages of our method over existing approaches on realistic human preference data. Code is available at https://github.com/haozheji/exact-optimization.