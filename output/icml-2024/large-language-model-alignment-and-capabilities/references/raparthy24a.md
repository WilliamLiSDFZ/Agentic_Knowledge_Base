---
title: "Generalization to New Sequential Decision Making Tasks with In-Context Learning"
source: "https://proceedings.mlr.press/v235/raparthy24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/raparthy24a/raparthy24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['in-context-learning', 'sequential-decision-making', 'transformers', 'few-shot', 'autonomous-agents']
venue: "ICML 2024"
tldr: "Transformers are shown to generalize to new sequential decision-making tasks using in-context learning from a handful of demonstrations without weight updates."
---

# Generalization to New Sequential Decision Making Tasks with In-Context Learning

**Source**: [https://proceedings.mlr.press/v235/raparthy24a.html](https://proceedings.mlr.press/v235/raparthy24a.html)

**TLDR**: Transformers are shown to generalize to new sequential decision-making tasks using in-context learning from a handful of demonstrations without weight updates.

## Abstract

Training autonomous agents that can learn new tasks from only a handful of demonstrations is a long-standing problem in machine learning. Recently, transformers have been shown to learn new language or vision tasks without any weight updates from only a few examples, also referred to as in-context learning. However, the sequential decision making setting poses additional challenges having a lower tolerance for errors since the environment’s stochasticity or the agent’s actions can lead to unseen, and sometimes unrecoverable, states. In this paper, we use an illustrative example to show that naively applying transformers to sequential decision making problems does not enable in-context learning of new tasks. We then demonstrate how training on sequences of trajectories with certain distributional properties leads to in-context learning of new sequential decision making tasks. We investigate different design choices and find that larger model and dataset sizes, as well as more task diversity, environment stochasticity, and trajectory burstiness, all result in better in-context learning of new out-of-distribution tasks. By training on large diverse offline datasets, our model is able to learn new MiniHack and Procgen tasks without any weight updates from just a handful of demonstrations.