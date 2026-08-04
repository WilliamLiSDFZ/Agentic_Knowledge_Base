---
title: "On Statistical Learning Theory for Distributional Inputs"
source: "https://proceedings.mlr.press/v235/fiedler24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fiedler24a/fiedler24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'sampling-compression-and-dimensionality-reduction']
tags: ['kernel-methods', 'distributional-inputs', 'statistical-learning-theory']
venue: "ICML 2024"
tldr: "Theoretical analysis of kernel-based statistical learning on distributional inputs, addressing generalization and sample complexity questions."
---

# On Statistical Learning Theory for Distributional Inputs

**Source**: [https://proceedings.mlr.press/v235/fiedler24a.html](https://proceedings.mlr.press/v235/fiedler24a.html)

**TLDR**: Theoretical analysis of kernel-based statistical learning on distributional inputs, addressing generalization and sample complexity questions.

## Abstract

Kernel-based statistical learning on distributional inputs appears in many relevant applications, from medical diagnostics to causal inference, and poses intriguing theoretical questions. While this learning scenario received considerable attention from the machine learning community recently, many gaps in the theory remain. In particular, most works consider only the distributional regression setting, and focus on the regularized least-squares algorithm for this problem. In this work, we start to fill these gaps. We prove two oracle inequalities for kernel machines in general distributional learning scenarios, as well as a generalization result based on algorithmic stability. Our main results are formulated in great generality, utilizing general Hilbertian embeddings, which makes them applicable to a wide array of approaches to distributional learning. Additionally, we specialize our results to the cases of kernel mean embeddings and of the recently introduced Hilbertian embeddings based on sliced Wasserstein distances, providing concrete instances of the general setup. Our results considerably enlarge the scope of theoretically grounded distributional learning, and provide many interesting avenues for future work.