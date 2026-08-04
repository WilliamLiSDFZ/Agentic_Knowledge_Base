---
title: "DNA-SE: Towards Deep Neural-Nets Assisted Semiparametric Estimation"
source: "https://proceedings.mlr.press/v235/liu24bk.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bk/liu24bk.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['semiparametric-estimation', 'deep-neural-networks', 'causal-inference', 'missing-data', 'transfer-learning']
venue: "ICML 2024"
tldr: "A framework leveraging deep neural networks to assist semiparametric estimation, addressing numerical challenges in solving efficient influence function equations."
---

# DNA-SE: Towards Deep Neural-Nets Assisted Semiparametric Estimation

**Source**: [https://proceedings.mlr.press/v235/liu24bk.html](https://proceedings.mlr.press/v235/liu24bk.html)

**TLDR**: A framework leveraging deep neural networks to assist semiparametric estimation, addressing numerical challenges in solving efficient influence function equations.

## Abstract

Semiparametric statistics play a pivotal role in a wide range of domains, including but not limited to missing data, causal inference, and transfer learning, to name a few. In many settings, semiparametric theory leads to (nearly) statistically optimal procedures that yet involve numerically solving Fredholm integral equations of the second kind. Traditional numerical methods, such as polynomial or spline approximations, are difficult to scale to multi-dimensional problems. Alternatively, statisticians may choose to approximate the original integral equations by ones with closed-form solutions, resulting in computationally more efficient, but statistically suboptimal or even incorrect procedures. To bridge this gap, we propose a novel framework by formulating the semiparametric estimation problem as a bi-level optimization problem; and then we propose a scalable algorithm called Deep Neural-Nets Assisted Semiparametric Estimation ($\mathsf{DNA\mbox{-}SE}$) by leveraging the universal approximation property of Deep Neural-Nets (DNN) to streamline semiparametric procedures. Through extensive numerical experiments and a real data analysis, we demonstrate the numerical and statistical advantages of $\mathsf{DNA\mbox{-}SE}$ over traditional methods. To the best of our knowledge, we are the first to bring DNN into semiparametric statistics as a numerical solver of integral equations in our proposed general framework.