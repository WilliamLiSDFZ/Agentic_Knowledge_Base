---
title: "Policy-conditioned Environment Models are More Generalizable"
source: "https://proceedings.mlr.press/v235/chen24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24g/chen24g.pdf"
categories: ['online-learning-and-sequential-decision-making', 'generative-models-and-variational-inference']
tags: ['model-based-RL', 'policy-conditioned-dynamics', 'offline-RL', 'generalization']
venue: "ICML 2024"
tldr: "Policy-conditioned environment models improve generalizability by conditioning dynamics predictions on the target policy being evaluated."
---

# Policy-conditioned Environment Models are More Generalizable

**Source**: [https://proceedings.mlr.press/v235/chen24g.html](https://proceedings.mlr.press/v235/chen24g.html)

**TLDR**: Policy-conditioned environment models improve generalizability by conditioning dynamics predictions on the target policy being evaluated.

## Abstract

In reinforcement learning, it is crucial to have an accurate environment dynamics model to evaluate different policies’ value in downstream tasks like offline policy optimization and policy evaluation. However, the learned model is known to be inaccurate in predictions when evaluating target policies different from data-collection policies. In this work, we found that utilizing policy representation for model learning, called policy-conditioned model (PCM) learning, is useful to mitigate the problem, especially when the offline dataset is collected from diversified behavior policies. The reason beyond that is in this case, PCM becomes a meta-dynamics model that is trained to be aware of and focus on the evaluation policies that on-the-fly adjust the model to be suitable to the evaluation policies’ state-action distribution, thus improving the prediction accuracy. Based on that intuition, we propose an easy-to-implement yet effective algorithm of PCM for accurate model learning. We also give a theoretical analysis and experimental evidence to demonstrate the feasibility of reducing value gaps by adapting the dynamics model under different policies. Experiment results show that PCM outperforms the existing SOTA off-policy evaluation methods in the DOPE benchmark by a large margin, and derives significantly better policies in offline policy selection and model predictive control compared with the standard model learning method.