---
title: "IOI: Invisible One-Iteration Adversarial Attack on No-Reference Image- and Video-Quality Metrics"
source: "https://proceedings.mlr.press/v235/shumitskaya24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shumitskaya24a/shumitskaya24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'image-quality-assessment-and-super-resolution']
tags: ['adversarial-attack', 'no-reference-quality-metrics', 'video-quality']
venue: "ICML 2024"
tldr: "Proposes IOI, a fast one-iteration invisible adversarial attack on no-reference image and video quality metrics."
---

# IOI: Invisible One-Iteration Adversarial Attack on No-Reference Image- and Video-Quality Metrics

**Source**: [https://proceedings.mlr.press/v235/shumitskaya24a.html](https://proceedings.mlr.press/v235/shumitskaya24a.html)

**TLDR**: Proposes IOI, a fast one-iteration invisible adversarial attack on no-reference image and video quality metrics.

## Abstract

No-reference image- and video-quality metrics are widely used in video processing benchmarks. The robustness of learning-based metrics under video attacks has not been widely studied. In addition to having success, attacks on metrics that can be employed in video processing benchmarks must be fast and imperceptible. This paper introduces an Invisible One-Iteration (IOI) adversarial attack on no-reference image and video quality metrics. The proposed method uses two modules to ensure high visual quality and temporal stability of adversarial videos and runs for one iteration, which makes it fast. We compared our method alongside eight prior approaches using image and video datasets via objective and subjective tests. Our method exhibited superior visual quality across various attacked metric architectures while maintaining comparable attack success and speed. We made the code available on GitHub: https://github.com/katiashh/ioi-attack.