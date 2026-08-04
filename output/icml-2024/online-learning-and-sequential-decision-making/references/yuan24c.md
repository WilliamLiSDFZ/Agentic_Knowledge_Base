---
title: "SHINE: Shielding Backdoors in Deep Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/yuan24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yuan24c/yuan24c.pdf"
categories: ['adversarial-robustness-and-model-security', 'online-learning-and-sequential-decision-making']
tags: ['backdoor-defense', 'deep-reinforcement-learning', 'shielding']
venue: "ICML 2024"
tldr: "SHINE is a backdoor defense framework tailored for deep reinforcement learning that shields policies against trigger-based attacks."
---

# SHINE: Shielding Backdoors in Deep Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/yuan24c.html](https://proceedings.mlr.press/v235/yuan24c.html)

**TLDR**: SHINE is a backdoor defense framework tailored for deep reinforcement learning that shields policies against trigger-based attacks.

## Abstract

Recent studies have discovered that a deep reinforcement learning (DRL) policy is vulnerable to backdoor attacks. Existing defenses against backdoor attacks either do not consider RL’s unique mechanism or make unrealistic assumptions, resulting in limited defense efficacy, practicability, and generalizability. We propose SHINE, a backdoor shielding method specific for DRL. SHINE designs novel policy explanation techniques to identify the backdoor triggers and a policy retraining algorithm to eliminate the impact of the triggers on backdoored agents. We theoretically justify that SHINE guarantees to improve a backdoored agent’s performance in a poisoned environment while ensuring its performance difference in the clean environment before and after shielding is bounded. We further conduct extensive experiments that evaluate SHINE against three mainstream DRL backdoor attacks in various benchmark RL environments. Our results show that SHINE significantly outperforms existing defenses in mitigating these backdoor attacks.