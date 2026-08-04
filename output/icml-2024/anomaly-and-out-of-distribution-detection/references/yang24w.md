---
title: "Exploration and Anti-Exploration with Distributional Random Network Distillation"
source: "https://proceedings.mlr.press/v235/yang24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24w/yang24w.pdf"
categories: ['online-learning-and-sequential-decision-making', 'anomaly-and-out-of-distribution-detection']
tags: ['exploration', 'reinforcement-learning', 'random-network-distillation']
venue: "ICML 2024"
tldr: "A distributional extension of Random Network Distillation that improves exploration-exploitation balance in deep reinforcement learning."
---

# Exploration and Anti-Exploration with Distributional Random Network Distillation

**Source**: [https://proceedings.mlr.press/v235/yang24w.html](https://proceedings.mlr.press/v235/yang24w.html)

**TLDR**: A distributional extension of Random Network Distillation that improves exploration-exploitation balance in deep reinforcement learning.

## Abstract

Exploration remains a critical issue in deep reinforcement learning for an agent to attain high returns in unknown environments. Although the prevailing exploration Random Network Distillation (RND) algorithm has been demonstrated to be effective in numerous environments, it often needs more discriminative power in bonus allocation. This paper highlights the “bonus inconsistency” issue within RND, pinpointing its primary limitation. To address this issue, we introduce the Distributional RND (DRND), a derivative of the RND. DRND enhances the exploration process by distilling a distribution of random networks and implicitly incorporating pseudo counts to improve the precision of bonus allocation. This refinement encourages agents to engage in more extensive exploration. Our method effectively mitigates the inconsistency issue without introducing significant computational overhead. Both theoretical analysis and experimental results demonstrate the superiority of our approach over the original RND algorithm. Our method excels in challenging online exploration scenarios and effectively serves as an anti-exploration mechanism in D4RL offline tasks. Our code is publicly available at https://github.com/yk7333/DRND.