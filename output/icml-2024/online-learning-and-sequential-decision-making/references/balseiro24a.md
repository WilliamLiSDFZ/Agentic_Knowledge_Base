---
title: "A Field Guide for Pacing Budget and ROS Constraints"
source: "https://proceedings.mlr.press/v235/balseiro24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/balseiro24a/balseiro24a.pdf"
categories: ['online-learning-matching-market-algorithms', 'online-learning-and-sequential-decision-making']
tags: ['budget-pacing', 'autobidding', 'online-advertising']
venue: "ICML 2024"
tldr: "This paper analyzes pacing budget and return-on-spend constraints for autobidding strategies in internet advertising platforms."
---

# A Field Guide for Pacing Budget and ROS Constraints

**Source**: [https://proceedings.mlr.press/v235/balseiro24a.html](https://proceedings.mlr.press/v235/balseiro24a.html)

**TLDR**: This paper analyzes pacing budget and return-on-spend constraints for autobidding strategies in internet advertising platforms.

## Abstract

Budget pacing is a popular service that has been offered by major internet advertising platforms since their inception. In the past few years, autobidding products that provide real-time bidding as a service to advertisers have seen a prominent rise in adoption. A popular autobidding stategy is value maximization subject to return-on-spend (ROS) constraints. For historical or business reasons, the systems that govern these two services, namely budget pacing and ROS pacing, are not necessarily always a single unified and coordinated entity that optimizes a global objective subject to both constraints. The purpose of this work is to theoretically and empirically compare algorithms with different degrees of coordination between these two pacing systems. In particular, we compare (a) a fully-decoupled sequential algorithm; (b) a minimally-coupled min-pacing algorithm; (c) a fully-coupled dual-based algorithm. Our main contribution is to theoretically analyze the min-pacing algorithm and show that it attains similar guarantees to the fully-coupled canonical dual-based algorithm. On the other hand, we show that the sequential algorithm, even though appealing by virtue of being fully decoupled, could badly violate the constraints. We validate our theoretical findings empirically by showing that the min-pacing algorithm performs almost as well as the canonical dual-based algorithm on a semi-synthetic dataset that was generated from a large online advertising platform’s auction data.