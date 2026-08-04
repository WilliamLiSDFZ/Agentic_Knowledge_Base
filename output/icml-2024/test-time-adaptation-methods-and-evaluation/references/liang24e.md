---
title: "Realistic Unsupervised CLIP Fine-tuning with Universal Entropy Optimization"
source: "https://proceedings.mlr.press/v235/liang24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liang24e/liang24e.pdf"
categories: ['test-time-adaptation-methods-and-evaluation']
tags: ['CLIP', 'unsupervised-fine-tuning', 'entropy-optimization']
venue: "ICML 2024"
tldr: "Universal entropy optimization enables realistic unsupervised fine-tuning of CLIP without relying on class-name prior knowledge."
---

# Realistic Unsupervised CLIP Fine-tuning with Universal Entropy Optimization

**Source**: [https://proceedings.mlr.press/v235/liang24e.html](https://proceedings.mlr.press/v235/liang24e.html)

**TLDR**: Universal entropy optimization enables realistic unsupervised fine-tuning of CLIP without relying on class-name prior knowledge.

## Abstract

The emergence of vision-language models, such as CLIP, has spurred a significant research effort towards their application for downstream supervised learning tasks. Although some previous studies have explored the unsupervised fine-tuning of CLIP, they often rely on prior knowledge in the form of class names associated with ground truth labels. This paper explores a realistic unsupervised fine-tuning scenario, considering the presence of out-of-distribution samples from unknown classes within the unlabeled data. In particular, we focus on simultaneously enhancing out-of-distribution detection and the recognition of instances associated with known classes. To tackle this problem, we present a simple, efficient, and effective approach called Universal Entropy Optimization (UEO). UEO leverages sample-level confidence to approximately minimize the conditional entropy of confident instances and maximize the marginal entropy of less confident instances. Apart from optimizing the textual prompt, UEO incorporates optimization of channel-wise affine transformations within the visual branch of CLIP. Extensive experiments across 15 domains and 4 different types of prior knowledge validate the effectiveness of UEO compared to baseline methods. The code is at https://github.com/tim-learn/UEO.