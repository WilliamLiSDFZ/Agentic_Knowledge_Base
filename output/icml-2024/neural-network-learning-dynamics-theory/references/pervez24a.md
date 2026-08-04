---
title: "Mechanistic Neural Networks for Scientific Machine Learning"
source: "https://proceedings.mlr.press/v235/pervez24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pervez24a/pervez24a.pdf"
categories: ['neural-operators-for-pde-solving', 'neural-network-learning-dynamics-theory']
tags: ['mechanistic-neural-networks', 'scientific-ML', 'differential-equations', 'physics-informed', 'dynamics']
venue: "ICML 2024"
tldr: "Introduces Mechanistic Neural Networks that explicitly learn governing differential equations within standard architectures for scientific machine learning."
---

# Mechanistic Neural Networks for Scientific Machine Learning

**Source**: [https://proceedings.mlr.press/v235/pervez24a.html](https://proceedings.mlr.press/v235/pervez24a.html)

**TLDR**: Introduces Mechanistic Neural Networks that explicitly learn governing differential equations within standard architectures for scientific machine learning.

## Abstract

This paper presents Mechanistic Neural Networks, a neural network design for machine learning applications in the sciences. It incorporates a new Mechanistic Block in standard architectures to explicitly learn governing differential equations as representations, revealing the underlying dynamics of data and enhancing interpretability and efficiency in data modeling. Central to our approach is a novel Relaxed Linear Programming Solver (NeuRLP) inspired by a technique that reduces solving linear ODEs to solving linear programs. This integrates well with neural networks and surpasses the limitations of traditional ODE solvers enabling scalable GPU parallel processing. Overall, Mechanistic Neural Networks demonstrate their versatility for scientific machine learning applications, adeptly managing tasks from equation discovery to dynamic systems modeling. We prove their comprehensive capabilities in analyzing and interpreting complex scientific data across various applications, showing significant performance against specialized state-of-the-art methods. Source code is available at https://github.com/alpz/mech-nn.