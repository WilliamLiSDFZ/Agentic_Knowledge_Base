---
title: "Multi-Agent Reinforcement Learning Meets Leaf Sequencing in Radiotherapy"
source: "https://proceedings.mlr.press/v235/gao24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24g/gao24g.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'online-learning-and-sequential-decision-making']
tags: ['multi-agent-RL', 'radiotherapy', 'leaf-sequencing', 'treatment-planning']
venue: "ICML 2024"
tldr: "A multi-agent deep reinforcement learning model is proposed for leaf sequencing in radiotherapy planning, outperforming traditional optimization approaches."
---

# Multi-Agent Reinforcement Learning Meets Leaf Sequencing in Radiotherapy

**Source**: [https://proceedings.mlr.press/v235/gao24g.html](https://proceedings.mlr.press/v235/gao24g.html)

**TLDR**: A multi-agent deep reinforcement learning model is proposed for leaf sequencing in radiotherapy planning, outperforming traditional optimization approaches.

## Abstract

In contemporary radiotherapy planning (RTP), a key module leaf sequencing is predominantly addressed by optimization-based approaches. In this paper, we propose a novel deep reinforcement learning (DRL) model termed as Reinforced Leaf Sequencer (RLS) in a multi-agent framework for leaf sequencing. The RLS model offers improvements to time-consuming iterative optimization steps via large-scale training and can control movement patterns through the design of reward mechanisms. We have conducted experiments on four datasets with four metrics and compared our model with a leading optimization sequencer. Our findings reveal that the proposed RLS model can achieve reduced fluence reconstruction errors, and potential faster convergence when integrated in an optimization planner. Additionally, RLS has shown promising results in a full artificial intelligence RTP pipeline. We hope this pioneer multi-agent RL leaf sequencer can foster future research on machine learning for RTP.