---
title: "Understanding Server-Assisted Federated Learning in the Presence of Incomplete Client Participation"
source: "https://proceedings.mlr.press/v235/yang24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24r/yang24r.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'learning-with-imperfect-data-and-bias']
tags: ['federated-learning', 'incomplete-participation', 'server-assisted']
venue: "ICML 2024"
tldr: "An analysis of server-assisted federated learning under realistic incomplete client participation scenarios with system heterogeneity."
---

# Understanding Server-Assisted Federated Learning in the Presence of Incomplete Client Participation

**Source**: [https://proceedings.mlr.press/v235/yang24r.html](https://proceedings.mlr.press/v235/yang24r.html)

**TLDR**: An analysis of server-assisted federated learning under realistic incomplete client participation scenarios with system heterogeneity.

## Abstract

Existing works in federated learning (FL) often assume either full client or uniformly distributed client participation. However, in reality, some clients may never participate in FL training (aka incomplete client participation) due to various system heterogeneity factors. A popular solution is the server-assisted federated learning (SA-FL) framework, where the server uses an auxiliary dataset. Despite empirical evidence of SA-FL’s effectiveness in addressing incomplete client participation, theoretical understanding of SA-FL is lacking. Furthermore, the effects of incomplete client participation in conventional FL are poorly understood. This motivates us to rigorously investigate SA-FL. Toward this end, we first show that conventional FL is not PAC-learnable under incomplete client participation in the worst case. Then, we show that the PAC-learnability of FL with incomplete client participation can indeed be revived by SA-FL, which theoretically justifies the use of SA-FL for the first time. Lastly, to provide practical guidance for SA-FL training under incomplete client participation, we propose the SAFARI (server-assisted federated averaging) algorithm that enjoys the same linear convergence speedup guarantees as classic FL with ideal client participation assumptions, offering the first SA-FL algorithm with convergence guarantee. Extensive experiments on different datasets show SAFARI significantly improves the performance under incomplete client participation.