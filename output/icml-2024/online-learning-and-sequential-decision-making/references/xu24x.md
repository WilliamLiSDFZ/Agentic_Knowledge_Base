---
title: "Pricing with Contextual Elasticity and Heteroscedastic Valuation"
source: "https://proceedings.mlr.press/v235/xu24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24x/xu24x.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['dynamic-pricing', 'contextual-bandits', 'price-elasticity']
venue: "ICML 2024"
tldr: "A novel contextual dynamic pricing model incorporating feature-based price elasticity and heteroscedastic valuations is proposed with online learning guarantees."
---

# Pricing with Contextual Elasticity and Heteroscedastic Valuation

**Source**: [https://proceedings.mlr.press/v235/xu24x.html](https://proceedings.mlr.press/v235/xu24x.html)

**TLDR**: A novel contextual dynamic pricing model incorporating feature-based price elasticity and heteroscedastic valuations is proposed with online learning guarantees.

## Abstract

We study an online contextual dynamic pricing problem, where customers decide whether to purchase a product based on its features and price. We introduce a novel approach to modeling a customer’s expected demand by incorporating feature-based price elasticity, which can be equivalently represented as a valuation with heteroscedastic noise. To solve the problem, we propose a computationally efficient algorithm called "Pricing with Perturbation (PwP)", which enjoys an $O(\sqrt{dT\log T})$ regret while allowing arbitrary adversarial input context sequences. We also prove a matching lower bound at $\Omega(\sqrt{dT})$ to show the optimality regarding $d$ and $T$ (up to $\log T$ factors). Our results shed light on the relationship between contextual elasticity and heteroscedastic valuation, providing insights for effective and practical pricing strategies.