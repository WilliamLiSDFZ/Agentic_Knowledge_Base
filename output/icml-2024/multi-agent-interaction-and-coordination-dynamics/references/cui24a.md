---
title: "Major-Minor Mean Field Multi-Agent Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/cui24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cui24a/cui24a.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['mean-field', 'multi-agent-reinforcement-learning', 'major-minor']
venue: "ICML 2024"
tldr: "Extends mean field multi-agent reinforcement learning to major-minor settings, enabling tractable solutions for heterogeneous agent interactions."
---

# Major-Minor Mean Field Multi-Agent Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/cui24a.html](https://proceedings.mlr.press/v235/cui24a.html)

**TLDR**: Extends mean field multi-agent reinforcement learning to major-minor settings, enabling tractable solutions for heterogeneous agent interactions.

## Abstract

Multi-agent reinforcement learning (MARL) remains difficult to scale to many agents. Recent MARL using Mean Field Control (MFC) provides a tractable and rigorous approach to otherwise difficult cooperative MARL. However, the strict MFC assumption of many independent, weakly-interacting agents is too inflexible in practice. We generalize MFC to instead simultaneously model many similar and few complex agents – as Major-Minor Mean Field Control (M3FC). Theoretically, we give approximation results for finite agent control, and verify the sufficiency of stationary policies for optimality together with a dynamic programming principle. Algorithmically, we propose Major-Minor Mean Field MARL (M3FMARL) for finite agent systems instead of the limiting system. The algorithm is shown to approximate the policy gradient of the underlying M3FC MDP. Finally, we demonstrate its capabilities experimentally in various scenarios. We observe a strong performance in comparison to state-of-the-art policy gradient MARL methods.