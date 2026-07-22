---
title: "Countering Reward Over-Optimization in LLM with Demonstration-Guided Reinforcement Learning"
source: "https://aclanthology.org/2024.findings-acl.740/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation']
tags: ['reinforcement-learning', 'reward-over-optimization', 'demonstration-guidance']
venue: "ACL 2024"
tldr: "Demonstration-guided reinforcement learning is proposed to counter reward over-optimization in LLM fine-tuning without heavy KL regularization."
---

# Countering Reward Over-Optimization in LLM with Demonstration-Guided Reinforcement Learning

**Source**: [https://aclanthology.org/2024.findings-acl.740/](https://aclanthology.org/2024.findings-acl.740/)

**TLDR**: Demonstration-guided reinforcement learning is proposed to counter reward over-optimization in LLM fine-tuning without heavy KL regularization.

## Abstract

AbstractWhile reinforcement learning (RL) has been proven essential for tuning large language models (LLMs), it can lead to reward over-optimization (ROO). Existing approaches address ROO by adding KL regularization, requiring computationally expensive hyperparameter tuning. Additionally, KL regularization focuses solely on regularizing the language policy, neglecting a potential source of regularization: the reward function itself. Inspired by demonstration-guided RL, we here introduce the Reward Calibration from Demonstration (RCfD), which leverages human demonstrations and a reward model to recalibrate the reward objective. Formally, given a prompt, the RCfD objective minimizes the distance between the demonstrations’ and LLM’s rewards rather than directly maximizing the reward function. This objective shift avoids incentivizing the LLM to exploit the reward model and promotes more natural and diverse language generation.We show the effectiveness of RCfD in three RL language tasks, where it achieves comparable performance to carefully tuned baselines while mitigating ROO.