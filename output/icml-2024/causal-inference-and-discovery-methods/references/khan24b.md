---
title: "Off-policy Evaluation Beyond Overlap: Sharp Partial Identification Under Smoothness"
source: "https://proceedings.mlr.press/v235/khan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/khan24b/khan24b.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['off-policy-evaluation', 'partial-identification', 'smoothness-assumptions']
venue: "ICML 2024"
tldr: "Develops sharp partial identification bounds for off-policy evaluation beyond overlap assumptions using smoothness constraints."
---

# Off-policy Evaluation Beyond Overlap: Sharp Partial Identification Under Smoothness

**Source**: [https://proceedings.mlr.press/v235/khan24b.html](https://proceedings.mlr.press/v235/khan24b.html)

**TLDR**: Develops sharp partial identification bounds for off-policy evaluation beyond overlap assumptions using smoothness constraints.

## Abstract

Off-policy evaluation, and the complementary problem of policy learning, use historical data collected under a logging policy to estimate and/or optimize the value of a target policy. Methods for these tasks typically assume overlap between the target and logging policy, enabling solutions based on importance weighting and/or imputation. Absent such an overlap assumption, existing work either relies on a well-specified model or optimizes needlessly conservative bounds. In this work, we develop methods for no-overlap policy evaluation without a well-specified model, relying instead on non-parametric assumptions on the expected outcome, with a particular focus on Lipschitz smoothness. Under such assumptions we are able to provide sharp bounds on the off-policy value, along with optimal estimators of those bounds. For Lipschitz smoothness, we construct a pair of linear programs that upper and lower bound the contribution of the no-overlap region to the off-policy value. We show that these programs have a concise closed form solution, and that their solutions converge under the Lipschitz assumption to the sharp partial identification bounds at a minimax optimal rate, up to log factors. We demonstrate the effectiveness our methods on two semi-synthetic examples, and obtain informative and valid bounds that are tighter than those possible without smoothness assumptions.