---
title: "A Provable Decision Rule for Out-of-Distribution Detection"
source: "https://proceedings.mlr.press/v235/ma24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24t/ma24t.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['out-of-distribution-detection', 'decision-rule', 'provable-guarantees']
venue: "ICML 2024"
tldr: "A provable decision rule for OOD detection that complements score functions with theoretical guarantees for reliable deployment."
---

# A Provable Decision Rule for Out-of-Distribution Detection

**Source**: [https://proceedings.mlr.press/v235/ma24t.html](https://proceedings.mlr.press/v235/ma24t.html)

**TLDR**: A provable decision rule for OOD detection that complements score functions with theoretical guarantees for reliable deployment.

## Abstract

Out-of-distribution (OOD) detection task plays the key role in reliable and safety-critical applications. Existing researches mainly devote to designing or training the powerful score function but overlook investigating the decision rule based on the proposed score function. Different from previous work, this paper aims to design a decision rule with rigorous theoretical guarantee and well empirical performance. Specifically, we provide a new insight for the OOD detection task from a hypothesis testing perspective and propose a novel generalized Benjamini Hochberg (g-BH) procedure with empirical p-values to solve the testing problem. Theoretically, the g-BH procedure controls false discovery rate (FDR) at pre-specified level. Furthermore, we derive an upper bound of the expectation of false positive rate (FPR) for the g-BH procedure based on the tailed generalized Gaussian distribution family, indicating that the FPR of g-BH procedure converges to zero in probability. Finally, the extensive experimental results verify the superiority of g-BH procedure over the traditional threshold-based decision rule on several OOD detection benchmarks.