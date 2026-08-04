---
title: "Contextualized Policy Recovery: Modeling and Interpreting Medical Decisions with Adaptive Imitation Learning"
source: "https://proceedings.mlr.press/v235/deuschel24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/deuschel24a/deuschel24a.pdf"
categories: ['causal-ml-for-clinical-decision-making', 'ai-explainability-uncertainty-human-decision-making']
tags: ['imitation-learning', 'interpretable-policy', 'medical-decisions', 'adaptive-learning', 'clinical-AI']
venue: "ICML 2024"
tldr: "Introduces contextualized policy recovery to model and interpret medical decision-making with adaptive imitation learning that avoids accuracy-interpretability tradeoffs."
---

# Contextualized Policy Recovery: Modeling and Interpreting Medical Decisions with Adaptive Imitation Learning

**Source**: [https://proceedings.mlr.press/v235/deuschel24a.html](https://proceedings.mlr.press/v235/deuschel24a.html)

**TLDR**: Introduces contextualized policy recovery to model and interpret medical decision-making with adaptive imitation learning that avoids accuracy-interpretability tradeoffs.

## Abstract

Interpretable policy learning seeks to estimate intelligible decision policies from observed actions; however, existing models force a tradeoff between accuracy and interpretability, limiting data-driven interpretations of human decision-making processes. Fundamentally, existing approaches are burdened by this tradeoff because they represent the underlying decision process as a universal policy, when in fact human decisions are dynamic and can change drastically under different contexts. Thus, we develop Contextualized Policy Recovery (CPR), which re-frames the problem of modeling complex decision processes as a multi-task learning problem, where each context poses a unique task and complex decision policies can be constructed piece-wise from many simple context-specific policies. CPR models each context-specific policy as a linear map, and generates new policy models on-demand as contexts are updated with new observations. We provide two flavors of the CPR framework: one focusing on exact local interpretability, and one retaining full global interpretability. We assess CPR through studies on simulated and real data, achieving state-of-the-art performance on predicting antibiotic prescription in intensive care units ($+22$% AUROC vs. previous SOTA) and predicting MRI prescription for Alzheimer’s patients ($+7.7$% AUROC vs. previous SOTA). With this improvement, CPR closes the accuracy gap between interpretable and black-box methods, allowing high-resolution exploration and analysis of context-specific decision models.