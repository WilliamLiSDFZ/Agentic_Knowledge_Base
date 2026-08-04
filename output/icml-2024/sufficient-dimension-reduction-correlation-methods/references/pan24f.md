---
title: "RMIB: Representation Matching Information Bottleneck for Matching Text Representations"
source: "https://proceedings.mlr.press/v235/pan24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pan24f/pan24f.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'sufficient-dimension-reduction-correlation-methods']
tags: ['text-matching', 'information-bottleneck', 'domain-adaptation', 'representation-learning']
venue: "ICML 2024"
tldr: "Proposes a Representation Matching Information Bottleneck framework to improve generalization in asymmetrical-domain text matching by aligning text representation distributions."
---

# RMIB: Representation Matching Information Bottleneck for Matching Text Representations

**Source**: [https://proceedings.mlr.press/v235/pan24f.html](https://proceedings.mlr.press/v235/pan24f.html)

**TLDR**: Proposes a Representation Matching Information Bottleneck framework to improve generalization in asymmetrical-domain text matching by aligning text representation distributions.

## Abstract

Recent studies have shown that the domain matching of text representations will help improve the generalization ability of asymmetrical domains text matching tasks. This requires that the distribution of text representations should be as similar as possible, similar to matching with heterogeneous data domains, in order to make the data after feature extraction indistinguishable. However, how to match the distribution of text representations remains an open question, and the role of text representations distribution match is still unclear. In this work, we explicitly narrow the distribution of text representations by matching them with the same prior distribution. We theoretically prove that narrowing the distribution of text representations in asymmetrical domains text matching is equivalent to optimizing the information bottleneck (IB). Since the interaction between text representations plays an important role in asymmetrical domains text matching, IB does not restrict the interaction between text representations. Therefore, we propose the adequacy of interaction and the incompleteness of a single text representation on the basis of IB and obtain the representation matching information bottleneck (RMIB). We theoretically prove that the constraints on text representations in RMIB is equivalent to maximizing the mutual information between text representations on the premise that the task information is given. On four text matching models and five text matching datasets, we verify that RMIB can improve the performance of asymmetrical domains text matching. Our experimental code is available at https://github.com/chenxingphh/rmib.