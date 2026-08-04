---
title: "Genie: Generative Interactive Environments"
source: "https://proceedings.mlr.press/v235/bruce24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bruce24a/bruce24a.pdf"
categories: ['generative-models-and-variational-inference', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['generative-models', 'interactive-environments', 'unsupervised-learning', 'video-generation']
venue: "ICML 2024"
tldr: "Genie is the first unsupervised generative interactive environment trained from unlabelled internet videos, enabling action-controllable virtual world generation."
---

# Genie: Generative Interactive Environments

**Source**: [https://proceedings.mlr.press/v235/bruce24a.html](https://proceedings.mlr.press/v235/bruce24a.html)

**TLDR**: Genie is the first unsupervised generative interactive environment trained from unlabelled internet videos, enabling action-controllable virtual world generation.

## Abstract

We introduce Genie, the first generative interactive environment trained in an unsupervised manner from unlabelled Internet videos. The model can be prompted to generate an endless variety of action-controllable virtual worlds described through text, synthetic images, photographs, and even sketches. At 11B parameters, Genie can be considered a foundation world model. It is comprised of a spatiotemporal video tokenizer, an autoregressive dynamics model, and a simple and scalable latent action model. Genie enables users to act in the generated environments on a frame-by-frame basis despite training without any ground-truth action labels or other domain specific requirements typically found in the world model literature. Further the resulting learned latent action space facilitates training agents to imitate behaviors from unseen videos, opening the path for training generalist agents of the future.