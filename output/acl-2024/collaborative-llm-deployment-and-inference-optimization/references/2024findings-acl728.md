---
title: "Bayesian Prompt Ensembles: Model Uncertainty Estimation for Black-Box Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.728/"
categories: ['collaborative-llm-deployment-and-inference-optimization']
tags: ['uncertainty-estimation', 'bayesian', 'prompt-ensembles', 'black-box-llm']
venue: "ACL 2024"
tldr: "Proposes Bayesian prompt ensembles to estimate model uncertainty for black-box LLMs without access to internal probabilities."
---

# Bayesian Prompt Ensembles: Model Uncertainty Estimation for Black-Box Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.728/](https://aclanthology.org/2024.findings-acl.728/)

**TLDR**: Proposes Bayesian prompt ensembles to estimate model uncertainty for black-box LLMs without access to internal probabilities.

## Abstract

AbstractAn important requirement for the reliable deployment of pre-trained large language models (LLMs) is the well-calibrated quantification of the uncertainty in their outputs. While the likelihood of predicting the next token is a practical surrogate of the data uncertainty learned during training, model uncertainty is challenging to estimate, i.e., due to lack of knowledge acquired during training. Prior efforts to quantify uncertainty of neural networks require specific architectures or (re-)training strategies, which are impractical to apply to LLMs with several billion parameters, or for black-box models where the architecture and parameters are not available. In this paper, we propose Bayesian Prompts Ensembles (BayesPE), a novel approach to effectively obtain well-calibrated uncertainty for the output of pre-trained LLMs. BayesPE computes output probabilities through a weighted ensemble of different, but semantically equivalent, task instruction prompts. The relative weights of the different prompts in the ensemble are estimated through approximate Bayesian variational inference over a small labeled validation set. We demonstrate that BayesPE approximates a Bayesian input layer for the LLM, providing a lower bound on the expected model error. In our extensive experiments, we show that BayesPE achieves significantly superior uncertainty calibration compared to several baselines over a range of natural language classification tasks, both in zero- and few-shot settings.