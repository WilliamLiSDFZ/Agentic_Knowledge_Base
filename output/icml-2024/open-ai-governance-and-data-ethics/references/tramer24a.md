---
title: "Position: Considerations for Differentially Private Learning with Large-Scale Public Pretraining"
source: "https://proceedings.mlr.press/v235/tramer24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tramer24a/tramer24a.pdf"
categories: ['position-papers-on-ml-research-directions', 'open-ai-governance-and-data-ethics']
tags: ['differential-privacy', 'transfer-learning', 'public-pretraining']
venue: "ICML 2024"
tldr: "A position paper critically examining the use of large web-scraped public datasets for differentially private machine learning via transfer learning."
---

# Position: Considerations for Differentially Private Learning with Large-Scale Public Pretraining

**Source**: [https://proceedings.mlr.press/v235/tramer24a.html](https://proceedings.mlr.press/v235/tramer24a.html)

**TLDR**: A position paper critically examining the use of large web-scraped public datasets for differentially private machine learning via transfer learning.

## Abstract

The performance of differentially private machine learning can be boosted significantly by leveraging the transfer learning capabilities of non-private models pretrained on large public datasets. We critically review this approach. We primarily question whether the use of large Web-scraped datasets should be viewed as differential-privacy-preserving. We further scrutinize whether existing machine learning benchmarks are appropriate for measuring the ability of pretrained models to generalize to sensitive domains. Finally, we observe that reliance on large pretrained models may lose other forms of privacy, requiring data to be outsourced to a more compute-powerful third party.