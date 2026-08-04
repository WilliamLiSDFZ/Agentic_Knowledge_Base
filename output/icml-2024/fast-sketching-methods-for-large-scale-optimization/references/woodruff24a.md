---
title: "Coresets for Multiple $\ell_p$ Regression"
source: "https://proceedings.mlr.press/v235/woodruff24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/woodruff24a/woodruff24a.pdf"
categories: ['fast-sketching-methods-for-large-scale-optimization', 'sampling-compression-and-dimensionality-reduction']
tags: ['coresets', 'lp-regression', 'sketching', 'dimensionality-reduction']
venue: "ICML 2024"
tldr: "Constructs nearly optimal coresets for multiple-response ℓp linear regression, generalizing prior single-response coreset constructions."
---

# Coresets for Multiple $\ell_p$ Regression

**Source**: [https://proceedings.mlr.press/v235/woodruff24a.html](https://proceedings.mlr.press/v235/woodruff24a.html)

**TLDR**: Constructs nearly optimal coresets for multiple-response ℓp linear regression, generalizing prior single-response coreset constructions.

## Abstract

A coreset of a dataset with $n$ examples and $d$ features is a weighted subset of examples that is sufficient for solving downstream data analytic tasks. Nearly optimal constructions of coresets for least squares and $\ell_p$ linear regression with a single response are known in prior work. However, for multiple $\ell_p$ regression where there can be $m$ responses, there are no known constructions with size sublinear in $m$. In this work, we construct coresets of size $\tilde O(\varepsilon^{-2}d)$ for $p<2$ and $\tilde O(\varepsilon^{-p}d^{p/2})$ for $p>2$ independently of $m$ (i.e., dimension-free) that approximate the multiple $\ell_p$ regression objective at every point in the domain up to $(1\pm\varepsilon)$ relative error. If we only need to preserve the minimizer subject to a subspace constraint, we improve these bounds by an $\varepsilon$ factor for all $p>1$. All of our bounds are nearly tight. We give two application of our results. First, we settle the number of uniform samples needed to approximate $\ell_p$ Euclidean power means up to a $(1+\varepsilon)$ factor, showing that $\tilde\Theta(\varepsilon^{-2})$ samples for $p = 1$, $\tilde\Theta(\varepsilon^{-1})$ samples for $1 < p < 2$, and $\tilde\Theta(\varepsilon^{1-p})$ samples for $p>2$ is tight, answering a question of Cohen-Addad, Saulpic, and Schwiegelshohn. Second, we show that for $1
Cite this Paper



    BibTeX
  


@InProceedings{pmlr-v235-woodruff24a,
  title = 	 {Coresets for Multiple $\ell_p$ Regression},
  author =       {Woodruff, David and Yasuda, Taisuke},
  booktitle = 	 {Proceedings of the 41st International Conference on Machine Learning},
  pages = 	 {53202--53233},
  year = 	 {2024},
  editor = 	 {Salakhutdinov, Ruslan and Kolter, Zico and Heller, Katherine and Weller, Adrian and Oliver, Nuria and Scarlett, Jonathan and Berkenkamp, Felix},
  volume = 	 {235},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {21--27 Jul},
  publisher =    {PMLR},
  pdf = 	 {https://raw.githubusercontent.com/mlresearch/v235/main/assets/woodruff24a/woodruff24a.pdf},
  url = 	 {https://proceedings.mlr.press/v235/woodruff24a.html},
  abstract = 	 {A coreset of a dataset with $n$ examples and $d$ features is a weighted subset of examples that is sufficient for solving downstream data analytic tasks. Nearly optimal constructions of coresets for least squares and $\ell_p$ linear regression with a single response are known in prior work. However, for multiple $\ell_p$ regression where there can be $m$ responses, there are no known constructions with size sublinear in $m$. In this work, we construct coresets of size $\tilde O(\varepsilon^{-2}d)$ for $p<2$ and $\tilde O(\varepsilon^{-p}d^{p/2})$ for $p>2$ independently of $m$ (i.e., dimension-free) that approximate the multiple $\ell_p$ regression objective at every point in the domain up to $(1\pm\varepsilon)$ relative error. If we only need to preserve the minimizer subject to a subspace constraint, we improve these bounds by an $\varepsilon$ factor for all $p>1$. All of our bounds are nearly tight. We give two application of our results. First, we settle the number of uniform samples needed to approximate $\ell_p$ Euclidean power means up to a $(1+\varepsilon)$ factor, showing that $\tilde\Theta(\varepsilon^{-2})$ samples for $p = 1$, $\tilde\Theta(\varepsilon^{-1})$ samples for $1 < p < 2$, and $\tilde\Theta(\varepsilon^{1-p})$ samples for $p>2$ is tight, answering a question of Cohen-Addad, Saulpic, and Schwiegelshohn. Second, we show that for $1

Copy to Clipboard
Download




    Endnote
  


%0 Conference Paper
%T Coresets for Multiple $\ell_p$ Regression
%A David Woodruff
%A Taisuke Yasuda
%B Proceedings of the 41st International Conference on Machine Learning
%C Proceedings of Machine Learning Research
%D 2024
%E Ruslan Salakhutdinov
%E Zico Kolter
%E Katherine Heller
%E Adrian Weller
%E Nuria Oliver
%E Jonathan Scarlett
%E Felix Berkenkamp	
%F pmlr-v235-woodruff24a
%I PMLR
%P 53202--53233
%U https://proceedings.mlr.press/v235/woodruff24a.html
%V 235
%X A coreset of a dataset with $n$ examples and $d$ features is a weighted subset of examples that is sufficient for solving downstream data analytic tasks. Nearly optimal constructions of coresets for least squares and $\ell_p$ linear regression with a single response are known in prior work. However, for multiple $\ell_p$ regression where there can be $m$ responses, there are no known constructions with size sublinear in $m$. In this work, we construct coresets of size $\tilde O(\varepsilon^{-2}d)$ for $p<2$ and $\tilde O(\varepsilon^{-p}d^{p/2})$ for $p>2$ independently of $m$ (i.e., dimension-free) that approximate the multiple $\ell_p$ regression objective at every point in the domain up to $(1\pm\varepsilon)$ relative error. If we only need to preserve the minimizer subject to a subspace constraint, we improve these bounds by an $\varepsilon$ factor for all $p>1$. All of our bounds are nearly tight. We give two application of our results. First, we settle the number of uniform samples needed to approximate $\ell_p$ Euclidean power means up to a $(1+\varepsilon)$ factor, showing that $\tilde\Theta(\varepsilon^{-2})$ samples for $p = 1$, $\tilde\Theta(\varepsilon^{-1})$ samples for $1 < p < 2$, and $\tilde\Theta(\varepsilon^{1-p})$ samples for $p>2$ is tight, answering a question of Cohen-Addad, Saulpic, and Schwiegelshohn. Second, we show that for $1

Copy to Clipboard
Download




    APA
  


Woodruff, D. & Yasuda, T.. (2024). Coresets for Multiple $\ell_p$ Regression. Proceedings of the 41st International Conference on Machine Learning, in Proceedings of Machine Learning Research 235:53202-53233 Available from https://proceedings.mlr.press/v235/woodruff24a.html.



Copy to Clipboard
Download



Related Material


Download PDF
OpenReview