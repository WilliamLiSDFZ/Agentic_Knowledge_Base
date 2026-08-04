---
title: "Evaluation of Test-Time Adaptation Under Computational Time Constraints"
source: "https://proceedings.mlr.press/v235/alfarra24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/alfarra24a/alfarra24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['test-time-adaptation', 'evaluation-protocol', 'distribution-shift']
venue: "ICML 2024"
tldr: "This paper proposes a new online evaluation protocol for test-time adaptation that penalizes slower methods by reducing their available adaptation samples."
---

# Evaluation of Test-Time Adaptation Under Computational Time Constraints

**Source**: [https://proceedings.mlr.press/v235/alfarra24a.html](https://proceedings.mlr.press/v235/alfarra24a.html)

**TLDR**: This paper proposes a new online evaluation protocol for test-time adaptation that penalizes slower methods by reducing their available adaptation samples.

## Abstract

This paper proposes a novel online evaluation protocol for Test Time Adaptation (TTA) methods, which penalizes slower methods by providing them with fewer samples for adaptation. TTA methods leverage unlabeled data at test time to adapt to distribution shifts. Though many effective methods have been proposed, their impressive performance usually comes at the cost of significantly increased computation budgets. Current evaluation protocols overlook the effect of this extra computation cost, affecting their real-world applicability. To address this issue, we propose a more realistic evaluation protocol for TTA methods, where data is received in an online fashion from a constant-speed data stream, thereby accounting for the method’s adaptation speed. We apply our proposed protocol to benchmark several TTA methods on multiple datasets and scenarios. Extensive experiments shows that, when accounting for inference speed, simple and fast approaches can outperform more sophisticated but slower methods. For example, SHOT from 2020, outperforms the state-of-the-art method SAR from 2023 under our online setting. Our results reveal the importance of developing practical TTA methods that are both accurate and efficient.