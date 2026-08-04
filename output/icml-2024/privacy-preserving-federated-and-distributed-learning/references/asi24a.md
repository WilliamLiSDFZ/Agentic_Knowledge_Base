---
title: "Private Vector Mean Estimation in the Shuffle Model: Optimal Rates Require Many Messages"
source: "https://proceedings.mlr.press/v235/asi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/asi24a/asi24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'sampling-compression-and-dimensionality-reduction']
tags: ['differential-privacy', 'shuffle-model', 'vector-mean-estimation', 'multi-message-protocol', 'optimal-rates']
venue: "ICML 2024"
tldr: "Proves that optimal error in private vector mean estimation under the shuffle model requires many messages and provides a matching protocol."
---

# Private Vector Mean Estimation in the Shuffle Model: Optimal Rates Require Many Messages

**Source**: [https://proceedings.mlr.press/v235/asi24a.html](https://proceedings.mlr.press/v235/asi24a.html)

**TLDR**: Proves that optimal error in private vector mean estimation under the shuffle model requires many messages and provides a matching protocol.

## Abstract

We study the problem of private vector mean estimation in the shuffle model of privacy where $n$ users each have a unit vector $v^{(i)} \in \mathbb{R}^d$. We propose a new multi-message protocol that achieves the optimal error using $O(\min(n\varepsilon^2,d))$ messages per user. Moreover, we show that any (unbiased) protocol that achieves optimal error must require each user to send $\Omega(\min(n\varepsilon^2,d)/\log(n))$ messages, demonstrating the optimality of our message complexity up to logarithmic factors. Additionally, we study the single-message setting and design a protocol that achieves mean squared error $O(dn^{d/(d+2)}\varepsilon^{-4/(d+2)})$. Moreover, we show that any single-message protocol must incur mean squared error $\Omega(dn^{d/(d+2)})$, showing that our protocol is optimal in the standard setting where $\varepsilon = \Theta(1)$. Finally, we study robustness to malicious users and show that malicious users can incur large additive error with a single shuffler.