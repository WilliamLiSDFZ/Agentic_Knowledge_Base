---
title: "Adversarially Robust Deep Multi-View Clustering: A Novel Attack and Defense Framework"
source: "https://proceedings.mlr.press/v235/huang24ai.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24ai/huang24ai.pdf"
categories: ['adversarial-robustness-and-model-security', 'clustering-methods-and-multi-view-learning']
tags: ['adversarial-attack', 'multi-view-clustering', 'defense', 'robustness', 'deep-clustering']
venue: "ICML 2024"
tldr: "Proposes a novel attack and defense framework addressing adversarial robustness in deep multi-view clustering methods."
---

# Adversarially Robust Deep Multi-View Clustering: A Novel Attack and Defense Framework

**Source**: [https://proceedings.mlr.press/v235/huang24ai.html](https://proceedings.mlr.press/v235/huang24ai.html)

**TLDR**: Proposes a novel attack and defense framework addressing adversarial robustness in deep multi-view clustering methods.

## Abstract

Deep Multi-view Clustering (DMVC) stands out as a widely adopted technique aiming at enhanced clustering performance by leveraging diverse data sources. However, the critical issue of vulnerability to adversarial attacks is unexplored due to the lack of well-defined attack objectives. To fill this crucial gap, this paper is the first work to investigate the possibility of adversarial attacks on DMVC models. Specifically, we introduce an adversarial attack with Generative Adversarial Networks (GANs) with the aim to maximally change the complementarity and consistency of multiple views, thus leading to wrong clustering. Building upon this adversarial context, in the realm of defense, we propose a novel Adversarially Robust Deep Multi-View Clustering by leveraging adversarial training. Based on the analysis from an information-theoretic perspective, we design an Attack Mitigator that provides a foundation to guarantee the adversarial robustness of our DMVC models. Experiments conducted on multi-view datasets confirmed that our attack framework effectively reduces the clustering performance of the target model. Furthermore, our proposed adversarially robust method is also demonstrated to be an effective defense against such attacks. This work is a pioneer in exploring adversarial threats and advancing both theoretical understanding and practical strategies for robust multi-view clustering. Code is available at https://github.com/libertyhhn/AR-DMVC.