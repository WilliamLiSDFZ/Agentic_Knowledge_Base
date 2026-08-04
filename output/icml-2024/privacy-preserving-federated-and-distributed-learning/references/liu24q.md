---
title: "Mitigating Privacy Risk in Membership Inference by Convex-Concave Loss"
source: "https://proceedings.mlr.press/v235/liu24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24q/liu24q.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['membership-inference', 'privacy', 'convex-concave-loss']
venue: "ICML 2024"
tldr: "A convex-concave loss formulation is proposed to mitigate membership inference attack risk without the instability of gradient ascent approaches."
---

# Mitigating Privacy Risk in Membership Inference by Convex-Concave Loss

**Source**: [https://proceedings.mlr.press/v235/liu24q.html](https://proceedings.mlr.press/v235/liu24q.html)

**TLDR**: A convex-concave loss formulation is proposed to mitigate membership inference attack risk without the instability of gradient ascent approaches.

## Abstract

Machine learning models are susceptible to membership inference attacks (MIAs), which aim to infer whether a sample is in the training set. Existing work utilizes gradient ascent to enlarge the loss variance of training data, alleviating the privacy risk. However, optimizing toward a reverse direction may cause the model parameters to oscillate near local minima, leading to instability and suboptimal performance. In this work, we propose a novel method – Convex Concave Loss (CCL), which enables a high variance of training loss distribution by gradient descent. Our method is motivated by the theoretical analysis that convex losses tend to decrease the loss variance during training. Thus, our key idea behind CCL is to reduce the convexity of loss functions with a concave term. Trained with CCL, neural networks produce losses with high variance for training data, reinforcing the defense against MIAs. Extensive experiments demonstrate the superiority of CCL, achieving a state-of-the-art balance in the privacy-utility trade-off.