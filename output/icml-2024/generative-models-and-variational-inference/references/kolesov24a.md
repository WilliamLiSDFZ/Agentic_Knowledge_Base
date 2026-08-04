---
title: "Estimating Barycenters of Distributions with Neural Optimal Transport"
source: "https://proceedings.mlr.press/v235/kolesov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kolesov24a/kolesov24a.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['Wasserstein-barycenter', 'optimal-transport', 'neural-networks', 'distribution-averaging']
venue: "ICML 2024"
tldr: "A neural optimal transport approach to efficiently estimate Wasserstein barycenters of collections of probability distributions."
---

# Estimating Barycenters of Distributions with Neural Optimal Transport

**Source**: [https://proceedings.mlr.press/v235/kolesov24a.html](https://proceedings.mlr.press/v235/kolesov24a.html)

**TLDR**: A neural optimal transport approach to efficiently estimate Wasserstein barycenters of collections of probability distributions.

## Abstract

Given a collection of probability measures, a practitioner sometimes needs to find an "average" distribution which adequately aggregates reference distributions. A theoretically appealing notion of such an average is the Wasserstein barycenter, which is the primal focus of our work. By building upon the dual formulation of Optimal Transport (OT), we propose a new scalable approach for solving the Wasserstein barycenter problem. Our methodology is based on the recent Neural OT solver: it has bi-level adversarial learning objective and works for general cost functions. These are key advantages of our method since the typical adversarial algorithms leveraging barycenter tasks utilize tri-level optimization and focus mostly on quadratic cost. We also establish theoretical error bounds for our proposed approach and showcase its applicability and effectiveness in illustrative scenarios and image data setups. Our source code is available at https://github.com/justkolesov/NOTBarycenters.