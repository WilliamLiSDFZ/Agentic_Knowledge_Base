---
title: "Conformal Validity Guarantees Exist for Any Data Distribution (and How to Find Them)"
source: "https://proceedings.mlr.press/v235/prinster24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/prinster24a/prinster24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['conformal-prediction', 'validity-guarantees', 'distribution-free']
venue: "ICML 2024"
tldr: "Shows that conformal validity guarantees exist for any data distribution and provides methods to find them."
---

# Conformal Validity Guarantees Exist for Any Data Distribution (and How to Find Them)

**Source**: [https://proceedings.mlr.press/v235/prinster24a.html](https://proceedings.mlr.press/v235/prinster24a.html)

**TLDR**: Shows that conformal validity guarantees exist for any data distribution and provides methods to find them.

## Abstract

As artificial intelligence (AI) / machine learning (ML) gain widespread adoption, practitioners are increasingly seeking means to quantify and control the risk these systems incur. This challenge is especially salient when such systems have autonomy to collect their own data, such as in black-box optimization and active learning, where their actions induce sequential feedback-loop shifts in the data distribution. Conformal prediction is a promising approach to uncertainty and risk quantification, but prior variants’ validity guarantees have assumed some form of “quasi-exchangeability” on the data distribution, thereby excluding many types of sequential shifts. In this paper we prove that conformal prediction can theoretically be extended to any joint data distribution, not just exchangeable or quasi-exchangeable ones. Although the most general case is exceedingly impractical to compute, for concrete practical applications we outline a procedure for deriving specific conformal algorithms for any data distribution, and we use this procedure to derive tractable algorithms for a series of AI/ML-agent-induced covariate shifts. We evaluate the proposed algorithms empirically on synthetic black-box optimization and active learning tasks.