---
title: "FairProof : Confidential and Certifiable Fairness for Neural Networks"
source: "https://proceedings.mlr.press/v235/yadav24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yadav24a/yadav24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'privacy-preserving-federated-and-distributed-learning']
tags: ['algorithmic-fairness', 'zero-knowledge-proofs', 'confidential-ML']
venue: "ICML 2024"
tldr: "Proposes FairProof, a system using cryptographic proofs to certify fairness of confidential neural network models without revealing model weights."
---

# FairProof : Confidential and Certifiable Fairness for Neural Networks

**Source**: [https://proceedings.mlr.press/v235/yadav24a.html](https://proceedings.mlr.press/v235/yadav24a.html)

**TLDR**: Proposes FairProof, a system using cryptographic proofs to certify fairness of confidential neural network models without revealing model weights.

## Abstract

Machine learning models are increasingly used in societal applications, yet legal and privacy concerns demand that they very often be kept confidential. Consequently, there is a growing distrust about the fairness properties of these models in the minds of consumers, who are often at the receiving end of model predictions. To this end, we propose Fairproof – a system that uses Zero-Knowledge Proofs (a cryptographic primitive) to publicly verify the fairness of a model, while maintaining confidentiality. We also propose a fairness certification algorithm for fully-connected neural networks which is befitting to ZKPs and is used in this system. We implement Fairproof in Gnark and demonstrate empirically that our system is practically feasible. Code is available at https://github.com/infinite-pursuits/FairProof.