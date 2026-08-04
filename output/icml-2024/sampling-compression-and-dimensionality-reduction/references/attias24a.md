---
title: "Information Complexity of Stochastic Convex Optimization: Applications to Generalization, Memorization, and Tracing"
source: "https://proceedings.mlr.press/v235/attias24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/attias24a/attias24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'privacy-preserving-federated-and-distributed-learning']
tags: ['memorization', 'stochastic-convex-optimization', 'information-complexity', 'generalization', 'tracing']
venue: "ICML 2024"
tldr: "Studies the interplay between memorization and learning in SCO through an information-complexity lens connecting generalization and tracing."
---

# Information Complexity of Stochastic Convex Optimization: Applications to Generalization, Memorization, and Tracing

**Source**: [https://proceedings.mlr.press/v235/attias24a.html](https://proceedings.mlr.press/v235/attias24a.html)

**TLDR**: Studies the interplay between memorization and learning in SCO through an information-complexity lens connecting generalization and tracing.

## Abstract

In this work, we investigate the interplay between memorization and learning in the context of stochastic convex optimization (SCO). We define memorization via the information a learning algorithm reveals about its training data points. We then quantify this information using the framework of conditional mutual information (CMI) proposed by Steinke and Zakynthinou (2020). Our main result is a precise characterization of the tradeoff between the accuracy of a learning algorithm and its CMI, answering an open question posed by Livni (2023). We show that, in the $L^2$ Lipschitz–bounded setting and under strong convexity, every learner with an excess error $\epsilon$ has CMI bounded below by $\Omega(1/\epsilon^2)$ and $\Omega(1/\epsilon)$, respectively. We further demonstrate the essential role of memorization in learning problems in SCO by designing an adversary capable of accurately identifying a significant fraction of the training samples in specific SCO problems. Finally, we enumerate several implications of our results, such as a limitation of generalization bounds based on CMI and the incompressibility of samples in SCO problems.