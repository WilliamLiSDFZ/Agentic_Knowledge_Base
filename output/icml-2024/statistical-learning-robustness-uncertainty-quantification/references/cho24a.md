---
title: "Peeking with PEAK: Sequential, Nonparametric Composite Hypothesis Tests for Means of Multiple Data Streams"
source: "https://proceedings.mlr.press/v235/cho24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cho24a/cho24a.pdf"
categories: ['sequential-change-detection-theory-and-algorithms', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['sequential-testing', 'nonparametric', 'composite-hypothesis']
venue: "ICML 2024"
tldr: "PEAK is a novel nonparametric sequential test for composite hypotheses across multiple data streams using a testing-by-betting framework."
---

# Peeking with PEAK: Sequential, Nonparametric Composite Hypothesis Tests for Means of Multiple Data Streams

**Source**: [https://proceedings.mlr.press/v235/cho24a.html](https://proceedings.mlr.press/v235/cho24a.html)

**TLDR**: PEAK is a novel nonparametric sequential test for composite hypotheses across multiple data streams using a testing-by-betting framework.

## Abstract

We propose a novel nonparametric sequential test for composite hypotheses for means of multiple data streams. Our proposed method, peeking with expectation-based averaged capital (PEAK), builds upon the testing-by-betting framework and provides a non-asymptotic $\alpha$-level test across any stopping time. Our contributions are two-fold: (1) we propose a novel betting scheme and provide theoretical guarantees on type-I error control, power, and asymptotic growth rate/$e$-power in the setting of a single data stream; (2) we introduce PEAK, a generalization of this betting scheme to multiple streams, that (i) avoids using wasteful union bounds via averaging, (ii) is a test of power one under mild regularity conditions on the sampling scheme of the streams, and (iii) reduces computational overhead when applying the testing-as-betting approaches for pure-exploration bandit problems. We illustrate the practical benefits of PEAK using both synthetic and real-world HeartSteps datasets. Our experiments show that PEAK provides up to an 85% reduction in the number of samples before stopping compared to existing stopping rules for pure-exploration bandit problems, and matches the performance of state-of-the-art sequential tests while improving upon computational complexity.