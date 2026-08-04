---
title: "Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study"
source: "https://proceedings.mlr.press/v235/xu24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24h/xu24h.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['RLHF', 'DPO', 'PPO']
venue: "ICML 2024"
tldr: "A comprehensive empirical and theoretical study comparing DPO and PPO for LLM alignment finds conditions under which each method is superior."
---

# Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study

**Source**: [https://proceedings.mlr.press/v235/xu24h.html](https://proceedings.mlr.press/v235/xu24h.html)

**TLDR**: A comprehensive empirical and theoretical study comparing DPO and PPO for LLM alignment finds conditions under which each method is superior.

## Abstract

Reinforcement Learning from Human Feedback (RLHF) is currently the most widely used method to align large language models (LLMs) with human preferences. Existing RLHF methods can be roughly categorized as either reward-based or reward-free. Novel applications such as ChatGPT and Claude leverage reward-based methods that first learn a reward model and apply actor-critic algorithms, such as Proximal Policy Optimization (PPO). However, in academic benchmarks, state-of-the-art results are often achieved via reward-free methods, such as Direct Preference Optimization (DPO). Is DPO truly superior to PPO? Why does PPO perform poorly on these benchmarks? In this paper, we first conduct both theoretical and empirical studies on the algorithmic properties of DPO and show that DPO may have fundamental limitations. Moreover, we also comprehensively examine PPO and reveal the key factors for the best performances of PPO in fine-tuning LLMs. Finally, we benchmark DPO and PPO across a collection of RLHF testbeds, ranging from dialogue to code generation. Experiment results demonstrate that PPO is able to surpass other alignment methods in all cases and achieve state-of-the-art results in challenging code competitions.