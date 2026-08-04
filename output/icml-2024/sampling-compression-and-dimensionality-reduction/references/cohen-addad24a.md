---
title: "Perturb-and-Project: Differentially Private Similarities and Marginals"
source: "https://proceedings.mlr.press/v235/cohen-addad24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cohen-addad24a/cohen-addad24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'sampling-compression-and-dimensionality-reduction']
tags: ['differential-privacy', 'perturbation', 'projection']
venue: "ICML 2024"
tldr: "Revisits the perturb-and-project framework for differential privacy to design efficient algorithms for releasing private similarities and marginals."
---

# Perturb-and-Project: Differentially Private Similarities and Marginals

**Source**: [https://proceedings.mlr.press/v235/cohen-addad24a.html](https://proceedings.mlr.press/v235/cohen-addad24a.html)

**TLDR**: Revisits the perturb-and-project framework for differential privacy to design efficient algorithms for releasing private similarities and marginals.

## Abstract

We revisit the objective perturbations framework for differential privacy where noise is added to the input $A\in \mathcal{S}$ and the result is then projected back to the space of admissible datasets $\mathcal{S}$. Through this framework, we first design novel efficient algorithms to privately release pair-wise cosine similarities. Second, we derive a novel algorithm to compute $k$-way marginal queries over $n$ features. Prior work could achieve comparable guarantees only for $k$ even. Furthermore, we extend our results to $t$-sparse datasets, where our efficient algorithms yields novel, stronger guarantees whenever $t\le n^{5/6}/\log n.$ Finally, we provide a theoretical perspective on why fast input perturbation algorithms works well in practice. The key technical ingredients behind our results are tight sum-of-squares certificates upper bounding the Gaussian complexity of sets of solutions.