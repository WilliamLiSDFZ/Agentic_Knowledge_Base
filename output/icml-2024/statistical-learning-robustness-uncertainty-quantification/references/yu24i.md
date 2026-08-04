---
title: "Generalization Bound and New Algorithm for Clean-Label Backdoor Attack"
source: "https://proceedings.mlr.press/v235/yu24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24i/yu24i.pdf"
categories: ['adversarial-robustness-and-model-security', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['backdoor-attack', 'clean-label', 'generalization-bound']
venue: "ICML 2024"
tldr: "Theoretical generalization bounds for clean-label backdoor attacks and a new algorithm leveraging these bounds for improved attack design."
---

# Generalization Bound and New Algorithm for Clean-Label Backdoor Attack

**Source**: [https://proceedings.mlr.press/v235/yu24i.html](https://proceedings.mlr.press/v235/yu24i.html)

**TLDR**: Theoretical generalization bounds for clean-label backdoor attacks and a new algorithm leveraging these bounds for improved attack design.

## Abstract

The generalization bound is a crucial theoretical tool for assessing the generalizability of learning methods and there exist vast literatures on generalizability of normal learning, adversarial learning, and data poisoning. Unlike other data poison attacks, the backdoor attack has the special property that the poisoned triggers are contained in both the training set and the test set and the purpose of the attack is two-fold. To our knowledge, the generalization bound for the backdoor attack has not been established. In this paper, we fill this gap by deriving algorithm-independent generalization bounds in the clean-label backdoor attack scenario. Precisely, based on the goals of backdoor attack, we give upper bounds for the clean sample population errors and the poison population errors in terms of the empirical error on the poisoned training dataset. Furthermore, based on the theoretical result, a new clean-label backdoor attack is proposed that computes the poisoning trigger by combining adversarial noise and indiscriminate poison. We show its effectiveness in a variety of settings.