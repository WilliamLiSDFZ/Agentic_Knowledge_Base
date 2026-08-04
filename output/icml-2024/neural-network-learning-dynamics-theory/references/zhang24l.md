---
title: "Towards Certified Unlearning for Deep Neural Networks"
source: "https://proceedings.mlr.press/v235/zhang24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24l/zhang24l.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'neural-network-learning-dynamics-theory']
tags: ['machine-unlearning', 'certified-unlearning', 'deep-neural-networks']
venue: "ICML 2024"
tldr: "A framework extending certified unlearning guarantees from convex models to non-convex deep neural networks."
---

# Towards Certified Unlearning for Deep Neural Networks

**Source**: [https://proceedings.mlr.press/v235/zhang24l.html](https://proceedings.mlr.press/v235/zhang24l.html)

**TLDR**: A framework extending certified unlearning guarantees from convex models to non-convex deep neural networks.

## Abstract

In the field of machine unlearning, certified unlearning has been extensively studied in convex machine learning models due to its high efficiency and strong theoretical guarantees. However, its application to deep neural networks (DNNs), known for their highly nonconvex nature, still poses challenges. To bridge the gap between certified unlearning and DNNs, we propose several simple techniques to extend certified unlearning methods to nonconvex objectives. To reduce the time complexity, we develop an efficient computation method by inverse Hessian approximation without compromising certification guarantees. In addition, we extend our discussion of certification to nonconvergence training and sequential unlearning, considering that real-world users can send unlearning requests at different time points. Extensive experiments on three real-world datasets demonstrate the efficacy of our method and the advantages of certified unlearning in DNNs.