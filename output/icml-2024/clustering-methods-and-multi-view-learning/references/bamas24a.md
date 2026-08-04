---
title: "Analyzing $D^α$ seeding for $k$-means"
source: "https://proceedings.mlr.press/v235/bamas24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bamas24a/bamas24a.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'optimization-algorithms-convergence-theory']
tags: ['k-means-plus-plus', 'seeding-analysis', 'clustering-approximation']
venue: "ICML 2024"
tldr: "A tighter analysis of the D-alpha seeding algorithm for k-means clustering approximation guarantees is provided."
---

# Analyzing $D^α$ seeding for $k$-means

**Source**: [https://proceedings.mlr.press/v235/bamas24a.html](https://proceedings.mlr.press/v235/bamas24a.html)

**TLDR**: A tighter analysis of the D-alpha seeding algorithm for k-means clustering approximation guarantees is provided.

## Abstract

One of the most popular clustering algorithms is the celebrated $D^\alpha$ seeding algorithm (also know as $k$-means++ when $\alpha=2$) by Arthur and Vassilvitskii (2007), who showed that it guarantees in expectation an $O(2^{2\alpha}\cdot \log k)$-approximate solution to the ($k$,$\alpha$)-clustering cost (where distances are raised to the power $\alpha$) for any $\alpha\ge 1$. More recently, Balcan, Dick, and White (2018) observed experimentally that using $D^\alpha$ seeding with $\alpha>2$ can lead to a better solution with respect to the standard $k$-means objective (i.e. the $(k,2)$-clustering cost). In this paper, we provide a rigorous understanding of this phenomenon. For any $\alpha>2$, we show that $D^\alpha$ seeding guarantees in expectation an approximation factor of  \begin{equation*} O_\alpha \left(\left(\frac{\sigma_{\textrm{max}}}{\sigma_{\textrm{min}}}\right)^{2-4/\alpha}\cdot (g_\alpha \cdot \min \lbrace\ell,\log k\rbrace)^{2/\alpha}\right) \end{equation*} with respect to the standard $k$-means cost of any underlying clustering; where $g_\alpha$ is a parameter capturing the concentration of the points in each cluster, $\sigma_{\textrm{max}}$ and $\sigma_{\textrm{min}}$ are the maximum and minimum standard deviation of the clusters around their center, and $\ell$ is the number of distinct mixing weights in the underlying clustering (after rounding them to the nearest power of $2$). For instance, if the underlying clustering is defined by a mixture of $k$ Gaussian distributions with equal cluster variance (up to a constant-factor), then our result implies that: (1) if there are a constant number of mixing weights, any constant $\alpha>2$ yields a constant-factor approximation; (2) if the mixing weights are arbitrary, any constant $\alpha>2$ yields an $O\left(\log^{2/\alpha}k\right)$-approximation, and $\alpha=\Theta(\log\log k)$ yields an $O(\log\log k)^3$-approximation. We complement these results by some lower bounds showing that the dependency on $g_\alpha$ and $\sigma_{\textrm{max}}/\sigma_{\textrm{min}}$ is tight. Finally, we provide an experimental validation of the effects of the aforementioned parameters when using $D^\alpha$ seeding.