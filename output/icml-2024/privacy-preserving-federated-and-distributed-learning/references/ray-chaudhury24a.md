---
title: "Fair Federated Learning via the Proportional Veto Core"
source: "https://proceedings.mlr.press/v235/ray-chaudhury24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ray-chaudhury24a/ray-chaudhury24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'privacy-preserving-federated-and-distributed-learning']
tags: ['federated-learning', 'fairness', 'proportional-veto-core', 'agent-utilities', 'coalition']
venue: "ICML 2024"
tldr: "This paper introduces the proportional veto core as a practical fairness notion for federated learning that provides utility-based guarantees without strong assumptions."
---

# Fair Federated Learning via the Proportional Veto Core

**Source**: [https://proceedings.mlr.press/v235/ray-chaudhury24a.html](https://proceedings.mlr.press/v235/ray-chaudhury24a.html)

**TLDR**: This paper introduces the proportional veto core as a practical fairness notion for federated learning that provides utility-based guarantees without strong assumptions.

## Abstract

Previous work on fairness in federated learning introduced the notion of core stability, which provides utility-based fairness guarantees to any subset of participating agents. However, these guarantees require strong assumptions on agent utilities that render them impractical. To address this shortcoming, we measure the quality of output models in terms of their ordinal rank instead of their cardinal utility, and use this insight to adapt the classical notion of proportional veto core (PVC) from social choice theory to the federated learning setting. We prove that models that are PVC-stable exist in very general learning paradigms, even allowing non-convex model sets, as well as non-convex and non-concave loss functions. We also design Rank-Core-Fed, a distributed federated learning algorithm, to train a PVC-stable model. Finally, we demonstrate that Rank-Core-Fed outperforms baselines in terms of fairness on different datasets.