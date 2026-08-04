---
title: "Trustless Audits without Revealing Data or Models"
source: "https://proceedings.mlr.press/v235/waiwitlikhit24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/waiwitlikhit24a/waiwitlikhit24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'open-ai-governance-and-data-ethics']
tags: ['trustless-audits', 'privacy', 'model-transparency', 'cryptography', 'data-ownership']
venue: "ICML 2024"
tldr: "Proposes a cryptographic framework for trustless auditing of ML models and training data without revealing proprietary models or datasets."
---

# Trustless Audits without Revealing Data or Models

**Source**: [https://proceedings.mlr.press/v235/waiwitlikhit24a.html](https://proceedings.mlr.press/v235/waiwitlikhit24a.html)

**TLDR**: Proposes a cryptographic framework for trustless auditing of ML models and training data without revealing proprietary models or datasets.

## Abstract

There is an increasing conflict between business incentives to hide models and data as trade secrets, and the societal need for algorithmic transparency. For example, a rightsholder who currently wishes to know whether their copyrighted works have been used during training must convince the model provider to allow a third party to audit the model and data. Finding a mutually agreeable third party is difficult, and the associated costs often make this approach impractical. In this work, we show that it is possible to simultaneously allow model providers to keep their models and data secret while allowing other parties to trustlessly audit properties of the model and data. We do this by designing a protocol called ZkAudit in which model providers publish cryptographic commitments of datasets and model weights, alongside a zero-knowledge proof (ZKP) certifying that published commitments are derived from training the model. Model providers can then respond to audit requests by privately computing any function F of the dataset (or model) and releasing the output of F alongside another ZKP certifying the correct execution of F. To enable ZkAudit, we develop new methods of computing ZKPs for SGD on modern neural nets for recommender systems and image classification models capable of high accuracies on ImageNet. Empirically, we show it is possible to provide trustless audits of DNNs, including copyright, censorship, and counterfactual audits with little to no loss in accuracy.