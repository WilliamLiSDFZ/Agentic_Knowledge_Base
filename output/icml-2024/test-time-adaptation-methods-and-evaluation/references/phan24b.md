---
title: "Controllable Prompt Tuning For Balancing Group Distributional Robustness"
source: "https://proceedings.mlr.press/v235/phan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/phan24b/phan24b.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'test-time-adaptation-methods-and-evaluation']
tags: ['prompt-tuning', 'group-robustness', 'distribution-shift']
venue: "ICML 2024"
tldr: "A controllable prompt tuning method that balances worst-group and average-group performance under distribution shifts."
---

# Controllable Prompt Tuning For Balancing Group Distributional Robustness

**Source**: [https://proceedings.mlr.press/v235/phan24b.html](https://proceedings.mlr.press/v235/phan24b.html)

**TLDR**: A controllable prompt tuning method that balances worst-group and average-group performance under distribution shifts.

## Abstract

Models trained on data composed of different groups or domains can suffer from severe performance degradation under distribution shifts. While recent methods have largely focused on optimizing the worst-group objective, this often comes at the expense of good performance on other groups. To address this problem, we introduce an optimization scheme to achieve good performance across groups and find a good solution for all without severely sacrificing performance on any of them. However, directly applying such optimization involves updating the parameters of the entire network, making it both computationally expensive and challenging. Thus, we introduce Controllable Prompt Tuning (CPT), which couples our approach with prompt-tuning techniques. On spurious correlation benchmarks, our procedures achieve state-of-the-art results across both transformer and non-transformer architectures, as well as unimodal and multimodal data, while requiring only $0.4%$ tunable parameters.