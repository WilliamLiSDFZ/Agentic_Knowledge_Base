---
title: "Tuning-free Estimation and Inference of Cumulative Distribution Function under Local Differential Privacy"
source: "https://proceedings.mlr.press/v235/liu24z.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24z/liu24z.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['local-differential-privacy', 'CDF-estimation', 'survival-analysis']
venue: "ICML 2024"
tldr: "A tuning-free algorithm for CDF estimation under local differential privacy is developed via a novel connection to the current status survival problem."
---

# Tuning-free Estimation and Inference of Cumulative Distribution Function under Local Differential Privacy

**Source**: [https://proceedings.mlr.press/v235/liu24z.html](https://proceedings.mlr.press/v235/liu24z.html)

**TLDR**: A tuning-free algorithm for CDF estimation under local differential privacy is developed via a novel connection to the current status survival problem.

## Abstract

We introduce a novel algorithm for estimating Cumulative Distribution Function (CDF) values under Local Differential Privacy (LDP) by exploiting an unexpected connection between LDP and the current status problem, a classical survival data problem in statistics. This connection leads to the development of tools for constrained isotonic estimation based on binary queries. Through mathematical proofs and extensive numerical testing, we demonstrate that our method achieves uniform and $L_2$ error bounds when estimating the entire CDF curve. By employing increasingly dense grids, the error bound can be improved, exhibiting an asymptotic normal distribution of the proposed estimator. Theoretically, we show that the error bound smoothly changes as the number of grids increases relative to the sample size $n$. Computationally, we demonstrate that our constrained isotonic estimator can be efficiently computed deterministically, eliminating the need for hyperparameters or random optimization.