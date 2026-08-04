---
title: "BadPart: Unified Black-box Adversarial Patch Attacks against Pixel-wise Regression Tasks"
source: "https://proceedings.mlr.press/v235/cheng24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheng24e/cheng24e.pdf"
categories: ['adversarial-robustness-and-model-security', '3d-vision-and-scene-understanding']
tags: ['adversarial-patches', 'black-box-attacks', 'pixel-wise-regression']
venue: "ICML 2024"
tldr: "BadPart proposes a unified black-box adversarial patch attack framework targeting pixel-wise regression tasks such as depth and optical flow estimation."
---

# BadPart: Unified Black-box Adversarial Patch Attacks against Pixel-wise Regression Tasks

**Source**: [https://proceedings.mlr.press/v235/cheng24e.html](https://proceedings.mlr.press/v235/cheng24e.html)

**TLDR**: BadPart proposes a unified black-box adversarial patch attack framework targeting pixel-wise regression tasks such as depth and optical flow estimation.

## Abstract

Pixel-wise regression tasks (e.g., monocular depth estimation (MDE) and optical flow estimation (OFE)) have been widely involved in our daily life in applications like autonomous driving, augmented reality and video composition. Although certain applications are security-critical or bear societal significance, the adversarial robustness of such models are not sufficiently studied, especially in the black-box scenario. In this work, we introduce the first unified black-box adversarial patch attack framework against pixel-wise regression tasks, aiming to identify the vulnerabilities of these models under query-based black-box attacks. We propose a novel square-based adversarial patch optimization framework and employ probabilistic square sampling and score-based gradient estimation techniques to generate the patch effectively and efficiently, overcoming the scalability problem of previous black-box patch attacks. Our attack prototype, named BadPart, is evaluated on both MDE and OFE tasks, utilizing a total of 7 models. BadPart surpasses 3 baseline methods in terms of both attack performance and efficiency. We also apply BadPart on the Google online service for portrait depth estimation, causing 43.5% relative distance error with 50K queries. State-of-the-art (SOTA) countermeasures cannot defend our attack effectively.