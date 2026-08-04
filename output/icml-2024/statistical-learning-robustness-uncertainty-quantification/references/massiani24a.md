---
title: "On the Consistency of Kernel Methods with Dependent Observations"
source: "https://proceedings.mlr.press/v235/massiani24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/massiani24a/massiani24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification']
tags: ['kernel-methods', 'dependent-observations', 'consistency']
venue: "ICML 2024"
tldr: "Establishes consistency of kernel methods such as SVMs and Gaussian processes under dependent (non-i.i.d.) observations."
---

# On the Consistency of Kernel Methods with Dependent Observations

**Source**: [https://proceedings.mlr.press/v235/massiani24a.html](https://proceedings.mlr.press/v235/massiani24a.html)

**TLDR**: Establishes consistency of kernel methods such as SVMs and Gaussian processes under dependent (non-i.i.d.) observations.

## Abstract

The consistency of a learning method is usually established under the assumption that the observations are a realization of an independent and identically distributed (i.i.d.) or mixing process. Yet, kernel methods such as support vector machines (SVMs), Gaussian processes, or conditional kernel mean embeddings (CKMEs) all give excellent performance under sampling schemes that are obviously non-i.i.d., such as when data comes from a dynamical system. We propose the new notion of empirical weak convergence (EWC) as a general assumption explaining such phenomena for kernel methods. It assumes the existence of a random asymptotic data distribution and is a strict weakening of previous assumptions in the field. Our main results then establish consistency of SVMs, kernel mean embeddings, and general Hilbert-space valued empirical expectations with EWC data. Our analysis holds for both finite- and infinite-dimensional outputs, as we extend classical results of statistical learning to the latter case. In particular, it is also applicable to CKMEs. Overall, our results open new classes of processes to statistical learning and can serve as a foundation for a theory of learning beyond i.i.d. and mixing.