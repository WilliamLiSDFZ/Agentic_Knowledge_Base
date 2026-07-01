---
title: "FOOGD: Federated Collaboration for Both Out-of-distribution Generalization and Detection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/efd1e27afcb94addd03b9e14c8d9f78f-Abstract-Conference.html"
categories: ['privacy-preserving-federated-distributed-learning']
tags: ['federated-learning', 'out-of-distribution-detection', 'distribution-shift']
venue: "NeurIPS 2024"
tldr: "FOOGD is a federated learning framework that simultaneously addresses out-of-distribution generalization and detection by modeling score functions collaboratively across clients."
---

# FOOGD: Federated Collaboration for Both Out-of-distribution Generalization and Detection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/efd1e27afcb94addd03b9e14c8d9f78f-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/efd1e27afcb94addd03b9e14c8d9f78f-Abstract-Conference.html)

**TLDR**: FOOGD is a federated learning framework that simultaneously addresses out-of-distribution generalization and detection by modeling score functions collaboratively across clients.

## Abstract

Federated learning (FL) is a promising machine learning paradigm that collaborates with client models to capture global knowledge. However, deploying FL models in real-world scenarios remains unreliable due to the coexistence of in-distribution data and unexpected out-of-distribution (OOD) data, such as covariate-shift and semantic-shift data. Current FL researches typically address either covariate-shift data through OOD generalization or semantic-shift data via OOD detection, overlooking the simultaneous occurrence of various OOD shifts. In this work, we propose FOOGD, a method that estimates the probability density of each client and obtains reliable global distribution as guidance for the subsequent FL process. Firstly, SM3D in FOOGD estimates score model for arbitrary distributions without prior constraints, and detects semantic-shift data powerfully. Then SAG in FOOGD provides invariant yet diverse knowledge for both local covariate-shift generalization and client performance generalization. In empirical validations, FOOGD significantly enjoys three main advantages: (1) reliably estimating non-normalized decentralized distributions, (2) detecting semantic shift data via score values, and (3) generalizing to covariate-shift data by regularizing feature extractor. The project is open in https://github.com/XeniaLLL/FOOGD-main.git.