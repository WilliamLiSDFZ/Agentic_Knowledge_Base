---
title: "Beyond Regular Grids: Fourier-Based Neural Operators on Arbitrary Domains"
source: "https://proceedings.mlr.press/v235/lingsch24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lingsch24a/lingsch24a.pdf"
categories: ['neural-operators-for-pde-solving']
tags: ['neural-operators', 'fourier', 'arbitrary-domains']
venue: "ICML 2024"
tldr: "This paper extends Fourier-based neural operators beyond regular grids to handle PDEs on arbitrary domains efficiently."
---

# Beyond Regular Grids: Fourier-Based Neural Operators on Arbitrary Domains

**Source**: [https://proceedings.mlr.press/v235/lingsch24a.html](https://proceedings.mlr.press/v235/lingsch24a.html)

**TLDR**: This paper extends Fourier-based neural operators beyond regular grids to handle PDEs on arbitrary domains efficiently.

## Abstract

The computational efficiency of many neural operators, widely used for learning solutions of PDEs, relies on the fast Fourier transform (FFT) for performing spectral computations. As the FFT is limited to equispaced (rectangular) grids, this limits the efficiency of such neural operators when applied to problems where the input and output functions need to be processed on general non-equispaced point distributions. Leveraging the observation that a limited set of Fourier (Spectral) modes suffice to provide the required expressivity of a neural operator, we propose a simple method, based on the efficient direct evaluation of the underlying spectral transformation, to extend neural operators to arbitrary domains. An efficient implementation of such direct spectral evaluations is coupled with existing neural operator models to allow the processing of data on arbitrary non-equispaced distributions of points. With extensive empirical evaluation, we demonstrate that the proposed method allows us to extend neural operators to arbitrary point distributions with significant gains in training speed over baselines, while retaining or improving the accuracy of Fourier neural operators (FNOs) and related neural operators.