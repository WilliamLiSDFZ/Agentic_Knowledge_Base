---
title: "Rethinking Adversarial Robustness in the Context of the Right to be Forgotten"
source: "https://proceedings.mlr.press/v235/zhao24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24k/zhao24k.pdf"
categories: ['adversarial-robustness-and-model-security', 'privacy-preserving-federated-and-distributed-learning']
tags: ['machine-unlearning', 'adversarial-robustness', 'right-to-be-forgotten']
venue: "ICML 2024"
tldr: "Rethinks machine unlearning methods by examining the interplay between adversarial robustness and the right to be forgotten."
---

# Rethinking Adversarial Robustness in the Context of the Right to be Forgotten

**Source**: [https://proceedings.mlr.press/v235/zhao24k.html](https://proceedings.mlr.press/v235/zhao24k.html)

**TLDR**: Rethinks machine unlearning methods by examining the interplay between adversarial robustness and the right to be forgotten.

## Abstract

The past few years have seen an intense research interest in the practical needs of the "right to be forgotten", which has motivated researchers to develop machine unlearning methods to unlearn a fraction of training data and its lineage. While existing machine unlearning methods prioritize the protection of individuals’ private data, they overlook investigating the unlearned models’ susceptibility to adversarial attacks and security breaches. In this work, we uncover a novel security vulnerability of machine unlearning based on the insight that adversarial vulnerabilities can be bolstered, especially for adversarially robust models. To exploit this observed vulnerability, we propose a novel attack called Adversarial Unlearning Attack (AdvUA), which aims to generate a small fraction of malicious unlearning requests during the unlearning process. AdvUA causes a significant reduction of adversarial robustness in the unlearned model compared to the original model, providing an entirely new capability for adversaries that is infeasible in conventional machine learning pipelines. Notably, we also show that AdvUA can effectively enhance model stealing attacks by extracting additional decision boundary information, further emphasizing the breadth and significance of our research. We also conduct both theoretical analysis and computational complexity of AdvUA. Extensive numerical studies are performed to demonstrate the effectiveness and efficiency of the proposed attack.