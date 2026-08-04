---
title: "Auctionformer: A Unified Deep Learning Algorithm for Solving Equilibrium Strategies in Auction Games"
source: "https://proceedings.mlr.press/v235/huang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24c/huang24c.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['auction-games', 'equilibrium-solving', 'deep-learning']
venue: "ICML 2024"
tldr: "Presents Auctionformer, a unified deep learning algorithm for computing equilibrium strategies across diverse auction mechanisms and asymmetric bidders."
---

# Auctionformer: A Unified Deep Learning Algorithm for Solving Equilibrium Strategies in Auction Games

**Source**: [https://proceedings.mlr.press/v235/huang24c.html](https://proceedings.mlr.press/v235/huang24c.html)

**TLDR**: Presents Auctionformer, a unified deep learning algorithm for computing equilibrium strategies across diverse auction mechanisms and asymmetric bidders.

## Abstract

Auction games have been widely used in plenty of trading environments such as online advertising and real estate. The complexity of real-world scenarios, characterized by diverse auction mechanisms and bidder asymmetries, poses significant challenges in efficiently solving for equilibria. Traditional learning approaches often face limitations due to their specificity to certain settings and high resource demands. Addressing this, we introduce Auctionformer, an efficient transformer-based method to solve equilibria of diverse auctions in a unified framework. Leveraging the flexible tokenization schemes, Auctionformer translates varying auction games into a standard token series, making use of renowned Transformer architectures. Moreover, we employ Nash error as the loss term, sidestepping the need for underlying equilibrium solutions and enabling efficient training and inference. Furthermore, a few-shot framework supports adaptability to new mechanisms, reinforced by a self-supervised fine-tuning approach. Extensive experimental results affirm the superior performance of Auctionformer over contemporary methods, heralding its potential for broad real-world applications.