---
title: "Provably Robust DPO: Aligning Language Models with Noisy Feedback"
source: "https://proceedings.mlr.press/v235/ray-chowdhury24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ray-chowdhury24a/ray-chowdhury24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'learning-with-imperfect-data-and-bias']
tags: ['DPO', 'preference-learning', 'noisy-feedback', 'robust-alignment', 'language-models']
venue: "ICML 2024"
tldr: "This paper develops a provably robust variant of Direct Preference Optimization that aligns language models under noisy human preference feedback."
---

# Provably Robust DPO: Aligning Language Models with Noisy Feedback

**Source**: [https://proceedings.mlr.press/v235/ray-chowdhury24a.html](https://proceedings.mlr.press/v235/ray-chowdhury24a.html)

**TLDR**: This paper develops a provably robust variant of Direct Preference Optimization that aligns language models under noisy human preference feedback.

## Abstract

Learning from preference-based feedback has recently gained traction as a promising approach to align language models with human interests. While these aligned generative models have demonstrated impressive capabilities across various tasks, their dependence on high-quality human preference data poses a bottleneck in practical applications. Specifically, noisy (incorrect and ambiguous) preference pairs in the dataset might restrict the language models from capturing human intent accurately. While practitioners have recently proposed heuristics to mitigate the effect of noisy preferences, a complete theoretical understanding of their workings remain elusive. In this work, we aim to bridge this gap by introducing a general framework for policy optimization in the presence of random preference flips. We focus on the direct preference optimization (DPO) algorithm in particular since it assumes that preferences adhere to the Bradley-Terry-Luce (BTL) model, raising concerns about the impact of noisy data on the learned policy. We design a novel loss function, which de-bias the effect of noise on average, making a policy trained by minimizing that loss robust to the noise. Under log-linear parameterization of the policy class and assuming good feature coverage of the SFT policy, we prove that the sub-optimality gap of the proposed robust DPO (rDPO) policy compared to the optimal policy is of the order $O(\frac{1}{1-2\epsilon}\sqrt{\frac{d}{n}})$, where $\epsilon < 1/2$ is flip rate of labels, $d$ is policy parameter dimension and $n$ is size of dataset. Our experiments on IMDb sentiment generation and Anthropic’s helpful-harmless dataset shows that rDPO is robust to noise in preference labels compared to vanilla DPO and other heuristics proposed by practitioners.