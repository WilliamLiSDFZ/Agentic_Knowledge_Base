---
title: "A Theoretical Analysis of Backdoor Poisoning Attacks in Convolutional Neural Networks"
source: "https://proceedings.mlr.press/v235/li24at.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24at/li24at.pdf"
categories: ['adversarial-robustness-and-model-security', 'neural-network-learning-dynamics-theory']
tags: ['backdoor-attacks', 'poisoning', 'convolutional-neural-networks', 'theoretical-analysis', 'adversarial']
venue: "ICML 2024"
tldr: "A theoretical analysis characterizes backdoor poisoning attacks in CNNs, explaining how adversaries manipulate training to induce targeted misclassification."
---

# A Theoretical Analysis of Backdoor Poisoning Attacks in Convolutional Neural Networks

**Source**: [https://proceedings.mlr.press/v235/li24at.html](https://proceedings.mlr.press/v235/li24at.html)

**TLDR**: A theoretical analysis characterizes backdoor poisoning attacks in CNNs, explaining how adversaries manipulate training to induce targeted misclassification.

## Abstract

The rising threat of backdoor poisoning attacks (BPAs) on Deep Neural Networks (DNNs) has become a significant concern in recent years. In such attacks, the adversaries strategically target a specific class and generate a poisoned training set. The neural network (NN), well-trained on the poisoned training set, is able to predict any input with the trigger pattern as the targeted label, while maintaining accurate outputs for clean inputs. However, why the BPAs work remains less explored. To fill this gap, we employ a dirty-label attack and conduct a detailed analysis of BPAs in a two-layer convolutional neural network. We provide theoretical insights and results on the effectiveness of BPAs. Our experimental results on two real-world datasets validate our theoretical findings.