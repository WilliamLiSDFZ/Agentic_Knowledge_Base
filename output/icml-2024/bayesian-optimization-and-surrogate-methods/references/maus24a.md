---
title: "Joint Composite Latent Space Bayesian Optimization"
source: "https://proceedings.mlr.press/v235/maus24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/maus24a/maus24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods']
tags: ['Bayesian-optimization', 'composite-functions', 'latent-space']
venue: "ICML 2024"
tldr: "A joint composite latent space Bayesian optimization method that leverages intermediate observations of composite-structured functions."
---

# Joint Composite Latent Space Bayesian Optimization

**Source**: [https://proceedings.mlr.press/v235/maus24a.html](https://proceedings.mlr.press/v235/maus24a.html)

**TLDR**: A joint composite latent space Bayesian optimization method that leverages intermediate observations of composite-structured functions.

## Abstract

Bayesian Optimization (BO) is a technique for sample-efficient black-box optimization that employs probabilistic models to identify promising input for evaluation. When dealing with composite-structured functions, such as $f=g \circ h$, evaluating a specific location $x$ yields observations of both the final outcome $f(x) = g(h(x))$ as well as the intermediate output(s) $h(x)$. Previous research has shown that integrating information from these intermediate outputs can enhance BO performance substantially. However, existing methods struggle if the outputs $h(x)$ are high-dimensional. Many relevant problems fall into this setting, including in the context of generative AI, molecular design, or robotics. To effectively tackle these challenges, we introduce Joint Composite Latent Space Bayesian Optimization (JoCo), a novel framework that jointly trains neural network encoders and probabilistic models to adaptively compress high-dimensional input and output spaces into manageable latent representations. This enables effective BO on these compressed representations, allowing JoCo to outperform other state-of-the-art methods in high-dimensional BO on a wide variety of simulated and real-world problems.