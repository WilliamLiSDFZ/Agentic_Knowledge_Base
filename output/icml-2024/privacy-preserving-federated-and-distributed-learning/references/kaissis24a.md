---
title: "Beyond the Calibration Point: Mechanism Comparison in Differential Privacy"
source: "https://proceedings.mlr.press/v235/kaissis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kaissis24a/kaissis24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['differential-privacy', 'privacy-mechanisms', 'comparison', 'calibration']
venue: "ICML 2024"
tldr: "Argues that comparing DP mechanisms at a single (ε,δ) pair is insufficient and proposes richer mechanism comparison frameworks."
---

# Beyond the Calibration Point: Mechanism Comparison in Differential Privacy

**Source**: [https://proceedings.mlr.press/v235/kaissis24a.html](https://proceedings.mlr.press/v235/kaissis24a.html)

**TLDR**: Argues that comparing DP mechanisms at a single (ε,δ) pair is insufficient and proposes richer mechanism comparison frameworks.

## Abstract

In differentially private (DP) machine learning, the privacy guarantees of DP mechanisms are often reported and compared on the basis of a single $(\varepsilon, \delta)$-pair. This practice overlooks that DP guarantees can vary substantially even between mechanisms sharing a given $(\varepsilon, \delta)$, and potentially introduces privacy vulnerabilities which can remain undetected. This motivates the need for robust, rigorous methods for comparing DP guarantees in such cases. Here, we introduce the $\Delta$-divergence between mechanisms which quantifies the worst-case excess privacy vulnerability of choosing one mechanism over another in terms of $(\varepsilon, \delta)$, $f$-DP and in terms of a newly presented Bayesian interpretation. Moreover, as a generalisation of the Blackwell theorem, it is endowed with strong decision-theoretic foundations. Through application examples, we show that our techniques can facilitate informed decision-making and reveal gaps in the current understanding of privacy risks, as current practices in DP-SGD often result in choosing mechanisms with high excess privacy vulnerabilities.