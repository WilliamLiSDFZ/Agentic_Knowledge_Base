---
title: "CR-UTP: Certified Robustness against Universal Text Perturbations on Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.588/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['certified-robustness', 'universal-perturbations', 'LLM-security']
venue: "ACL 2024"
tldr: "CR-UTP provides certified robustness guarantees for LLMs against universal text perturbations such as word substitutions."
---

# CR-UTP: Certified Robustness against Universal Text Perturbations on Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.588/](https://aclanthology.org/2024.findings-acl.588/)

**TLDR**: CR-UTP provides certified robustness guarantees for LLMs against universal text perturbations such as word substitutions.

## Abstract

AbstractIt is imperative to ensure the stability of every prediction made by a language model; that is, a language’s prediction should remain consistent despite minor input variations, like word substitutions. In this paper, we investigate the problem of certifying a language model’s robustness against Universal Text Perturbations (UTPs), which have been widely used in universal adversarial attacks and backdoor attacks. Existing certified robustness based on random smoothing has shown considerable promise in certifying the input-specific text perturbations (ISTPs), operating under the assumption that any random alteration of a sample’s clean or adversarial words would negate the impact of sample-wise perturbations. However, with UTPs, masking only the adversarial words can eliminate the attack. A naive method is to simply increase the masking ratio and the likelihood of masking attack tokens, but it leads to a significant reduction in both certified accuracy and the certified radius due to input corruption by extensive masking. To solve this challenge, we introduce a novel approach, the superior prompt search method, designed to identify a superior prompt that maintains higher certified accuracy under extensive masking. Additionally, we theoretically motivate why ensembles are a particularly suitable choice as base prompts for random smoothing. The method is denoted by superior prompt ensembling technique. We also empirically confirm this technique, obtaining state-of-the-art results in multiple settings. These methodologies, for the first time, enable high certified accuracy against both UTPs and ISTPs. The source code of CR-UTP is available at https://github.com/UCF-ML-Research/CR-UTP.