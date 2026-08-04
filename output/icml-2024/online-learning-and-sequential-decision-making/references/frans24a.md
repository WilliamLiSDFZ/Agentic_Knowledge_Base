---
title: "Unsupervised Zero-Shot Reinforcement Learning via Functional Reward Encodings"
source: "https://proceedings.mlr.press/v235/frans24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/frans24a/frans24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'test-time-adaptation-methods-and-evaluation']
tags: ['zero-shot-RL', 'reward-encoding', 'offline-pretraining']
venue: "ICML 2024"
tldr: "Functional reward encodings enable zero-shot adaptation to new downstream RL tasks from unlabeled offline trajectories."
---

# Unsupervised Zero-Shot Reinforcement Learning via Functional Reward Encodings

**Source**: [https://proceedings.mlr.press/v235/frans24a.html](https://proceedings.mlr.press/v235/frans24a.html)

**TLDR**: Functional reward encodings enable zero-shot adaptation to new downstream RL tasks from unlabeled offline trajectories.

## Abstract

Can we pre-train a generalist agent from a large amount of unlabeled offline trajectories such that it can be immediately adapted to any new downstream tasks in a zero-shot manner? In this work, we present a functional reward encoding (FRE) as a general, scalable solution to this zero-shot RL problem. Our main idea is to learn functional representations of any arbitrary tasks by encoding their state-reward samples using a transformer-based variational auto-encoder. This functional encoding not only enables the pre-training of an agent from a wide diversity of general unsupervised reward functions, but also provides a way to solve any new downstream tasks in a zero-shot manner, given a small number of reward-annotated samples. We empirically show that FRE agents trained on diverse random unsupervised reward functions can generalize to solve novel tasks in a range of simulated robotic benchmarks, often outperforming previous zero-shot RL and offline RL methods.