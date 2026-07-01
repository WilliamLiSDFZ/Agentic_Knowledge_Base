---
title: "IPM-LSTM: A Learning-Based Interior Point Method for Solving Nonlinear Programs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/de0da9c42ee713f2ceaeed7bc40c522d-Abstract-Conference.html"
categories: ['neural-combinatorial-optimization-and-learning']
tags: ['interior-point-method', 'nonlinear-programming', 'lstm-solver']
venue: "NeurIPS 2024"
tldr: "Proposes IPM-LSTM, a learning-based approach that accelerates interior point methods for solving constrained nonlinear programs using LSTMs."
---

# IPM-LSTM: A Learning-Based Interior Point Method for Solving Nonlinear Programs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/de0da9c42ee713f2ceaeed7bc40c522d-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/de0da9c42ee713f2ceaeed7bc40c522d-Abstract-Conference.html)

**TLDR**: Proposes IPM-LSTM, a learning-based approach that accelerates interior point methods for solving constrained nonlinear programs using LSTMs.

## Abstract

Solving constrained nonlinear programs (NLPs) is of great importance in various domains such as power systems, robotics, and wireless communication networks. One widely used approach for addressing NLPs is the interior point method (IPM). The most computationally expensive procedure in IPMs is to solve systems of linear equations via matrix factorization. Recently, machine learning techniques have been adopted to expedite classic optimization algorithms. In this work, we propose using Long Short-Term Memory (LSTM) neural networks to approximate the solution of linear systems and integrate this approximating step into an IPM. The resulting approximate NLP solution is then utilized to warm-start an interior point solver. Experiments on various types of NLPs, including Quadratic Programs and Quadratically Constrained Quadratic Programs, show that our approach can significantly accelerate NLP solving, reducing iterations by up to 60% and solution time by up to 70% compared to the default solver.