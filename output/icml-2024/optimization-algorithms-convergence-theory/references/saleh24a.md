---
title: "Learning from Integral Losses in Physics Informed Neural Networks"
source: "https://proceedings.mlr.press/v235/saleh24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/saleh24a/saleh24a.pdf"
categories: ['neural-operators-for-pde-solving', 'optimization-algorithms-convergence-theory']
tags: ['physics-informed-neural-networks', 'integro-differential-equations', 'integral-losses', 'PDE', 'training']
venue: "ICML 2024"
tldr: "A training approach for physics-informed neural networks under partial integro-differential equations is proposed using integral-form losses to avoid intractable residual evaluations."
---

# Learning from Integral Losses in Physics Informed Neural Networks

**Source**: [https://proceedings.mlr.press/v235/saleh24a.html](https://proceedings.mlr.press/v235/saleh24a.html)

**TLDR**: A training approach for physics-informed neural networks under partial integro-differential equations is proposed using integral-form losses to avoid intractable residual evaluations.

## Abstract

This work proposes a solution for the problem of training physics-informed networks under partial integro-differential equations. These equations require an infinite or a large number of neural evaluations to construct a single residual for training. As a result, accurate evaluation may be impractical, and we show that naive approximations at replacing these integrals with unbiased estimates lead to biased loss functions and solutions. To overcome this bias, we investigate three types of potential solutions: the deterministic sampling approaches, the double-sampling trick, and the delayed target method. We consider three classes of PDEs for benchmarking; one defining Poisson problems with singular charges and weak solutions of up to 10 dimensions, another involving weak solutions on electro-magnetic fields and a Maxwell equation, and a third one defining a Smoluchowski coagulation problem. Our numerical results confirm the existence of the aforementioned bias in practice and also show that our proposed delayed target approach can lead to accurate solutions with comparable quality to ones estimated with a large sample size integral. Our implementation is open-source and available at https://github.com/ehsansaleh/btspinn.