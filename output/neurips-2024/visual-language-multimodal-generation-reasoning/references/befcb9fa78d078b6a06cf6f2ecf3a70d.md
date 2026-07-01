---
title: "Ask, Attend, Attack: An Effective Decision-Based Black-Box Targeted Attack for Image-to-Text Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/befcb9fa78d078b6a06cf6f2ecf3a70d-Abstract-Conference.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'visual-language-multimodal-generation-reasoning']
tags: ['adversarial-attacks', 'image-to-text', 'black-box-attack']
venue: "NeurIPS 2024"
tldr: "This work proposes a decision-based black-box targeted attack on image-to-text models using query-efficient ask-attend-attack strategies requiring no model internals."
---

# Ask, Attend, Attack: An Effective Decision-Based Black-Box Targeted Attack for Image-to-Text Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/befcb9fa78d078b6a06cf6f2ecf3a70d-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/befcb9fa78d078b6a06cf6f2ecf3a70d-Abstract-Conference.html)

**TLDR**: This work proposes a decision-based black-box targeted attack on image-to-text models using query-efficient ask-attend-attack strategies requiring no model internals.

## Abstract

While image-to-text models have demonstrated significant advancements in various vision-language tasks, they remain susceptible to adversarial attacks. Existing white-box attacks on image-to-text models require access to the architecture, gradients, and parameters of the target model, resulting in low practicality. Although the recently proposed gray-box attacks have improved practicality, they suffer from semantic loss during the training process, which limits their targeted attack performance. To advance adversarial attacks of image-to-text models, this paper focuses on a challenging scenario: decision-based black-box targeted attacks where the attackers only have access to the final output text and aim to perform targeted attacks. Specifically, we formulate the decision-based black-box targeted attack as a large-scale optimization problem. To efficiently solve the optimization problem, a three-stage process \textit{Ask, Attend, Attack}, called \textit{AAA}, is proposed to coordinate with the solver. \textit{Ask} guides attackers to create target texts that satisfy the specific semantics. \textit{Attend} identifies the crucial regions of the image for attacking, thus reducing the search space for the subsequent \textit{Attack}. \textit{Attack} uses an evolutionary algorithm to attack the crucial regions, where the attacks are semantically related to the target texts of \textit{Ask}, thus achieving targeted attacks without semantic loss. Experimental results on transformer-based and CNN+RNN-based image-to-text models confirmed the effectiveness of our proposed \textit{AAA}.