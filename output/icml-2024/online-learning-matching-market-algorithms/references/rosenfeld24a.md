---
title: "One-Shot Strategic Classification Under Unknown Costs"
source: "https://proceedings.mlr.press/v235/rosenfeld24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/rosenfeld24a/rosenfeld24a.pdf"
categories: ['strategic-information-manipulation-and-classification', 'online-learning-matching-market-algorithms']
tags: ['strategic-classification', 'unknown-costs', 'one-shot', 'manipulation-robustness', 'decision-rules']
venue: "ICML 2024"
tldr: "This paper studies one-shot strategic classification where the learner must make a single deployment decision under unknown strategic manipulation costs."
---

# One-Shot Strategic Classification Under Unknown Costs

**Source**: [https://proceedings.mlr.press/v235/rosenfeld24a.html](https://proceedings.mlr.press/v235/rosenfeld24a.html)

**TLDR**: This paper studies one-shot strategic classification where the learner must make a single deployment decision under unknown strategic manipulation costs.

## Abstract

The goal of strategic classification is to learn decision rules which are robust to strategic input manipulation. Earlier works assume that these responses are known; while some recent works handle unknown responses, they exclusively study online settings with repeated model deployments. But there are many domains – particularly in public policy, a common motivating use case – where multiple deployments are infeasible, or where even one bad round is unacceptable. To address this gap, we initiate the formal study of one-shot strategic classification under unknown responses, which requires committing to a single classifier once. Focusing on uncertainty in the users’ cost function, we begin by proving that for a broad class of costs, even a small mis-estimation of the true cost can entail trivial accuracy in the worst case. In light of this, we frame the task as a minimax problem, aiming to minimize worst-case risk over an uncertainty set of costs. We design efficient algorithms for both the full-batch and stochastic settings, which we prove converge (offline) to the minimax solution at the rate of $\tilde{\mathcal{O}}(T^{-\frac{1}{2}})$. Our analysis reveals important structure stemming from strategic responses, particularly the value of dual norm regularization with respect to the cost function.