---
title: "Absolute Policy Optimization: Enhancing Lower Probability Bound of Performance with High Confidence"
source: "https://proceedings.mlr.press/v235/zhao24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24i/zhao24i.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['reinforcement-learning', 'trust-region', 'policy-optimization']
venue: "ICML 2024"
tldr: "Proposes Absolute Policy Optimization to enhance lower probability bounds on policy performance with high confidence guarantees."
---

# Absolute Policy Optimization: Enhancing Lower Probability Bound of Performance with High Confidence

**Source**: [https://proceedings.mlr.press/v235/zhao24i.html](https://proceedings.mlr.press/v235/zhao24i.html)

**TLDR**: Proposes Absolute Policy Optimization to enhance lower probability bounds on policy performance with high confidence guarantees.

## Abstract

In recent years, trust region on-policy reinforcement learning has achieved impressive results in addressing complex control tasks and gaming scenarios. However, contemporary state-of-the-art algorithms within this category primarily emphasize improvement in expected performance, lacking the ability to control over the worst-case performance outcomes. To address this limitation, we introduce a novel objective function, optimizing which leads to guaranteed monotonic improvement in the lower probability bound of performance with high confidence. Building upon this groundbreaking theoretical advancement, we further introduce a practical solution called Absolute Policy Optimization (APO). Our experiments demonstrate the effectiveness of our approach across challenging continuous control benchmark tasks and extend its applicability to mastering Atari games. Our findings reveal that APO as well as its efficient variation Proximal Absolute Policy Optimization (PAPO) significantly outperforms state-of-the-art policy gradient algorithms, resulting in substantial improvements in worst-case performance, as well as expected performance.