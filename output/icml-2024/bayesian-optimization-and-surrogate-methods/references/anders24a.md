---
title: "Adaptive Observation Cost Control for Variational Quantum Eigensolvers"
source: "https://proceedings.mlr.press/v235/anders24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/anders24a/anders24a.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization', 'bayesian-optimization-and-surrogate-methods']
tags: ['variational-quantum-eigensolver', 'sequential-minimal-optimization', 'observation-cost', 'quantum-optimization']
venue: "ICML 2024"
tldr: "Introduces adaptive observation cost control for VQE to reduce noise-driven computational overhead in SMO iterations."
---

# Adaptive Observation Cost Control for Variational Quantum Eigensolvers

**Source**: [https://proceedings.mlr.press/v235/anders24a.html](https://proceedings.mlr.press/v235/anders24a.html)

**TLDR**: Introduces adaptive observation cost control for VQE to reduce noise-driven computational overhead in SMO iterations.

## Abstract

The objective to be minimized in the variational quantum eigensolver (VQE) has a restricted form, which allows a specialized sequential minimal optimization (SMO) that requires only a few observations in each iteration. However, the SMO iteration is still costly due to the observation noise—one observation at a point typically requires averaging over hundreds to thousands of repeated quantum measurement shots for achieving a reasonable noise level. In this paper, we propose an adaptive cost control method, named subspace in confident region (SubsCoRe), for SMO. SubsCoRe uses the Gaussian process (GP) surrogate, and requires it to have low uncertainty over the subspace being updated, so that optimization in each iteration is performed with guaranteed accuracy. Adaptive cost control is performed by setting the required accuracy according to the progress of the optimization, and identifying the minimum number of measurement shots, as well as their distribution, satisfying the SubsCoRe requirement.