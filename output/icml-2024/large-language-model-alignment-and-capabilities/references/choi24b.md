---
title: "Listwise Reward Estimation for Offline Preference-based Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/choi24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/choi24b/choi24b.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['preference-based-rl', 'reward-learning', 'offline-rl']
venue: "ICML 2024"
tldr: "Listwise reward estimation is proposed for offline preference-based RL to better capture relative feedback signals from human preferences."
---

# Listwise Reward Estimation for Offline Preference-based Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/choi24b.html](https://proceedings.mlr.press/v235/choi24b.html)

**TLDR**: Listwise reward estimation is proposed for offline preference-based RL to better capture relative feedback signals from human preferences.

## Abstract

In Reinforcement Learning (RL), designing precise reward functions remains to be a challenge, particularly when aligning with human intent. Preference-based RL (PbRL) was introduced to address this problem by learning reward models from human feedback. However, existing PbRL methods have limitations as they often overlook the second-order preference that indicates the relative strength of preference. In this paper, we propose Listwise Reward Estimation (LiRE), a novel approach for offline PbRL that leverages second-order preference information by constructing a Ranked List of Trajectories (RLT), which can be efficiently built by using the same ternary feedback type as traditional methods. To validate the effectiveness of LiRE, we propose a new offline PbRL dataset that objectively reflects the effect of the estimated rewards. Our extensive experiments on the dataset demonstrate the superiority of LiRE, i.e., outperforming state-of-the-art baselines even with modest feedback budgets and enjoying robustness with respect to the number of feedbacks and feedback noise. Our code is available at https://github.com/chwoong/LiRE