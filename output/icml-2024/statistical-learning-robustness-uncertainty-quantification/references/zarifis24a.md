---
title: "Robustly Learning Single-Index Models via Alignment Sharpness"
source: "https://proceedings.mlr.press/v235/zarifis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zarifis24a/zarifis24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'neural-network-learning-dynamics-theory']
tags: ['single-index-models', 'robust-learning', 'agnostic-learning']
venue: "ICML 2024"
tldr: "An efficient algorithm achieving constant-factor approximation for learning Single-Index Models under adversarial noise via alignment sharpness."
---

# Robustly Learning Single-Index Models via Alignment Sharpness

**Source**: [https://proceedings.mlr.press/v235/zarifis24a.html](https://proceedings.mlr.press/v235/zarifis24a.html)

**TLDR**: An efficient algorithm achieving constant-factor approximation for learning Single-Index Models under adversarial noise via alignment sharpness.

## Abstract

We study the problem of learning Single-Index Models under the $L_2^2$ loss in the agnostic model. We give an efficient learning algorithm, achieving a constant factor approximation to the optimal loss, that succeeds under a range of distributions (including log-concave distributions) and a broad class of monotone and Lipschitz link functions. This is the first efficient constant factor approximate agnostic learner, even for Gaussian data and for any nontrivial class of link functions. Prior work for the case of unknown link function either works in the realizable setting or does not attain constant factor approximation. The main technical ingredient enabling our algorithm and analysis is a novel notion of a local error bound in optimization that we term alignment sharpness and that may be of broader interest.