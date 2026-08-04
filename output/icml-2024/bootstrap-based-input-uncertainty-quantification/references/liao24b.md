---
title: "Bootstrapping Fisher Market Equilibrium and First-Price Pacing Equilibrium"
source: "https://proceedings.mlr.press/v235/liao24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liao24b/liao24b.pdf"
categories: ['bootstrap-based-input-uncertainty-quantification']
tags: ['Fisher-market', 'bootstrap', 'equilibrium']
venue: "ICML 2024"
tldr: "Bootstrap-based methods are proposed for statistical inference on Fisher market equilibrium and first-price pacing equilibrium."
---

# Bootstrapping Fisher Market Equilibrium and First-Price Pacing Equilibrium

**Source**: [https://proceedings.mlr.press/v235/liao24b.html](https://proceedings.mlr.press/v235/liao24b.html)

**TLDR**: Bootstrap-based methods are proposed for statistical inference on Fisher market equilibrium and first-price pacing equilibrium.

## Abstract

Linear Fisher market (LFM) is an equilibrium model for fair and efficient resource allocation, and first-price pacing equilibrium (FPPE) is a model for budget-management in first-price auctions. One thing they have in common is that both have a corresponding Eisenberg-Gale convex program characterization. In this paper, we introduce and devise several statistically valid bootstrap inference procedures for LFM and FPPE. The most challenging part is to bootstrap general FPPE, which reduces to bootstrapping constrained M-estimators, a largely unexplored problem. We are able to devise a bootstrap procedure for FPPE with structures by using the powerful tool of epi-convergence theory. Experiments with synthetic and semi-real data verify our theory.