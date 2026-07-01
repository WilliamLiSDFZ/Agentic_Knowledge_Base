---
title: "PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bd92debabb5e6eb881ef81d88e0f22ae-Abstract-Conference.html"
categories: ['physics-informed-neural-operators-and-simulations', 'graph-neural-networks-and-representation-learning']
tags: ['fluid-dynamics', 'out-of-distribution', 'graph-ODE']
venue: "NeurIPS 2024"
tldr: "Proposes PURE, combining prompt evolution with graph ODEs to handle distribution shifts in out-of-distribution fluid dynamics modeling."
---

# PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bd92debabb5e6eb881ef81d88e0f22ae-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/bd92debabb5e6eb881ef81d88e0f22ae-Abstract-Conference.html)

**TLDR**: Proposes PURE, combining prompt evolution with graph ODEs to handle distribution shifts in out-of-distribution fluid dynamics modeling.

## Abstract

This work studies the problem of out-of-distribution fluid dynamics modeling. Previous works usually design effective neural operators to learn from mesh-based data structures. However, in real-world applications, they would suffer from distribution shifts from the variance of system parameters and temporal evolution of the dynamical system. In this paper, we propose a novel approach named \underline{P}rompt Evol\underline{u}tion with G\underline{r}aph OD\underline{E} (\method{}) for out-of-distribution fluid dynamics modeling. The core of our \method{} is to learn time-evolving prompts using a graph ODE to adapt spatio-temporal forecasting models to different scenarios. In particular, our \method{} first learns from historical observations and system parameters in the frequency domain to explore multi-view context information, which could effectively initialize prompt embeddings. More importantly, we incorporate the interpolation of observation sequences into a graph ODE, which can capture the temporal evolution of prompt embeddings for model adaptation. These time-evolving prompt embeddings are then incorporated into basic forecasting models to overcome temporal distribution shifts. We also minimize the mutual information between prompt embeddings and observation embeddings to enhance the robustness of our model to different distributions. Extensive experiments on various benchmark datasets validate the superiority of the proposed \method{} in comparison to various baselines.