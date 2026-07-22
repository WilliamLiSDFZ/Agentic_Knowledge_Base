---
title: "Can Large Language Models Mine Interpretable Financial Factors More Effectively? A Neural-Symbolic Factor Mining Agent Model"
source: "https://aclanthology.org/2024.findings-acl.233/"
categories: ['financial-reasoning-llm-benchmarks-and-datasets', 'llm-agents-reasoning-and-planning']
tags: ['financial-factor-mining', 'neural-symbolic', 'stock-returns']
venue: "ACL 2024"
tldr: "A neural-symbolic agent using LLMs to mine interpretable financial factors for stock return prediction."
---

# Can Large Language Models Mine Interpretable Financial Factors More Effectively? A Neural-Symbolic Factor Mining Agent Model

**Source**: [https://aclanthology.org/2024.findings-acl.233/](https://aclanthology.org/2024.findings-acl.233/)

**TLDR**: A neural-symbolic agent using LLMs to mine interpretable financial factors for stock return prediction.

## Abstract

AbstractFinding interpretable factors for stock returns is the most vital issue in the empirical asset pricing domain. As data-driven methods, existing factor mining models can be categorized into symbol-based and neural-based models. Symbol-based models are interpretable but inefficient, while neural-based approaches are efficient but lack interpretability. Hence, mining interpretable factors effectively presents a significant challenge. Inspired by the success of Large Language Models (LLMs) in various tasks, we propose a FActor Mining Agent (FAMA) model that enables LLMs to integrate the strengths of both neural and symbolic models for factor mining. In this paper, FAMA consists of two main components: Cross-Sample Selection (CSS) and Chain-of-Experience (CoE). CSS addresses the homogeneity challenges in LLMs during factor mining by assimilating diverse factors as in-context samples, whereas CoE enables LLMs to leverage past successful mining experiences, expediting the mining of effective factors. Experimental evaluations on real-world stock market data demonstrate the effectiveness of our approach by surpassing the SOTA RankIC by 0.006 and RankICIR by 0.105 in predicting S&P 500 returns. Furthermore, the investment simulation shows that our model can achieve superior performance with an annualized return of 38.4% and a Sharpe ratio of 667.2%.