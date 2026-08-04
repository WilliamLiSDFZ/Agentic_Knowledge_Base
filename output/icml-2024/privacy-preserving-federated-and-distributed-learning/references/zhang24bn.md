---
title: "GroupCover: A Secure, Efficient and Scalable Inference Framework for On-device Model Protection based on TEEs"
source: "https://proceedings.mlr.press/v235/zhang24bn.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bn/zhang24bn.pdf"
categories: ['adversarial-robustness-and-model-security', 'privacy-preserving-federated-and-distributed-learning']
tags: ['model-protection', 'trusted-execution-environment', 'DNN-IP-protection', 'on-device-inference', 'security']
venue: "ICML 2024"
tldr: "Presents GroupCover, a secure and scalable inference framework for on-device DNN model protection using Trusted Execution Environments."
---

# GroupCover: A Secure, Efficient and Scalable Inference Framework for On-device Model Protection based on TEEs

**Source**: [https://proceedings.mlr.press/v235/zhang24bn.html](https://proceedings.mlr.press/v235/zhang24bn.html)

**TLDR**: Presents GroupCover, a secure and scalable inference framework for on-device DNN model protection using Trusted Execution Environments.

## Abstract

Due to the high cost of training DNN models, how to protect the intellectual property of DNN models, especially when the models are deployed to users’ devices, is becoming an important topic. One practical solution is to use Trusted Execution Environments (TEEs) and researchers have proposed various model obfuscation solutions to make full use of the high-security guarantee of TEEs and the high performance of collocated GPUs. In this paper, we first identify a common vulnerability, namely the fragility of randomness, that is shared by existing TEE-based model obfuscation solutions. This vulnerability benefits model-stealing attacks and allows the adversary to recover about 97% of the secret model. To improve the security of TEE-shielded DNN models, we further propose a new model obfuscation approach GroupCover, which uses sufficient randomization and mutual covering obfuscation to protect model weights. Experimental results demonstrate that GroupCover can achieve a comparable security level as the upper-bound (black-box protection), which is remarkably over 3x compared with existing solutions. Besides, GroupCover introduces 19% overhead and negligible accuracy loss compared to model unprotected scheme.