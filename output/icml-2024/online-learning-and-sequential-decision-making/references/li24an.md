---
title: "Configurable Mirror Descent: Towards a Unification of Decision Making"
source: "https://proceedings.mlr.press/v235/li24an.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24an/li24an.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'online-learning-and-sequential-decision-making']
tags: ['mirror-descent', 'multi-agent', 'decision-making', 'unification', 'game-theory']
venue: "ICML 2024"
tldr: "Configurable Mirror Descent unifies single-agent, cooperative, competitive, and mixed multi-agent decision-making under a single framework."
---

# Configurable Mirror Descent: Towards a Unification of Decision Making

**Source**: [https://proceedings.mlr.press/v235/li24an.html](https://proceedings.mlr.press/v235/li24an.html)

**TLDR**: Configurable Mirror Descent unifies single-agent, cooperative, competitive, and mixed multi-agent decision-making under a single framework.

## Abstract

Decision-making problems, categorized as single-agent, e.g., Atari, cooperative multi-agent, e.g., Hanabi, competitive multi-agent, e.g., Hold’em poker, and mixed cooperative and competitive, e.g., football, are ubiquitous in the real world. Although various methods have been proposed to address the specific decision-making categories, these methods typically evolve independently and cannot generalize to other categories. Therefore, a fundamental question for decision-making is: Can we develop a single algorithm to tackle ALL categories of decision-making problems? There are several main challenges to address this question: i) different decision-making categories involve different numbers of agents and different relationships between agents, ii) different categories have different solution concepts and evaluation measures, and iii) there lacks a comprehensive benchmark covering all the categories. This work presents a preliminary attempt to address the question with three main contributions. i) We propose the generalized mirror descent (GMD), a generalization of MD variants, which considers multiple historical policies and works with a broader class of Bregman divergences. ii) We propose the configurable mirror descent (CMD) where a meta-controller is introduced to dynamically adjust the hyper-parameters in GMD conditional on the evaluation measures. iii) We construct the GameBench with 15 academic-friendly games across different decision-making categories. Extensive experiments demonstrate that CMD achieves empirically competitive or better outcomes compared to baselines while providing the capability of exploring diverse dimensions of decision making.