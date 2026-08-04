---
title: "AttNS: Attention-Inspired Numerical Solving For Limited Data Scenarios"
source: "https://proceedings.mlr.press/v235/huang24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24m/huang24m.pdf"
categories: ['neural-operators-for-pde-solving', 'learning-with-imperfect-data-and-bias']
tags: ['numerical-solvers', 'attention-mechanism', 'differential-equations']
venue: "ICML 2024"
tldr: "Proposes AttNS, an attention-inspired numerical solver improving generalization of AI-hybrid solvers for differential equations under limited data."
---

# AttNS: Attention-Inspired Numerical Solving For Limited Data Scenarios

**Source**: [https://proceedings.mlr.press/v235/huang24m.html](https://proceedings.mlr.press/v235/huang24m.html)

**TLDR**: Proposes AttNS, an attention-inspired numerical solver improving generalization of AI-hybrid solvers for differential equations under limited data.

## Abstract

We propose the attention-inspired numerical solver (AttNS), a concise method that helps the generalization and robustness issues faced by the AI-Hybrid numerical solver in solving differential equations due to limited data. AttNS is inspired by the effectiveness of attention modules in Residual Neural Networks (ResNet) in enhancing model generalization and robustness for conventional deep learning tasks. Drawing from the dynamical system perspective of ResNet, We seamlessly incorporate attention mechanisms into the design of numerical methods tailored for the characteristics of solving differential equations. Our results on benchmarks, ranging from high-dimensional problems to chaotic systems, showcase AttNS consistently enhancing various numerical solvers without any intricate model crafting. Finally, we analyze AttNS experimentally and theoretically, demonstrating its ability to achieve strong generalization and robustness while ensuring the convergence of the solver. This includes requiring less data compared to other advanced methods to achieve comparable generalization errors and better prevention of numerical explosion issues when solving differential equations.