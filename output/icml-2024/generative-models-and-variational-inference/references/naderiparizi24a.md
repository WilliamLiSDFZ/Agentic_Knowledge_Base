---
title: "Don’t be so Negative! Score-based Generative Modeling with Oracle-assisted Guidance"
source: "https://proceedings.mlr.press/v235/naderiparizi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/naderiparizi24a/naderiparizi24a.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['score-based-diffusion', 'constrained-generation', 'oracle-guidance']
venue: "ICML 2024"
tldr: "Oracle-assisted guidance is introduced to steer score-based diffusion models toward constrained domains while maintaining generative quality."
---

# Don’t be so Negative! Score-based Generative Modeling with Oracle-assisted Guidance

**Source**: [https://proceedings.mlr.press/v235/naderiparizi24a.html](https://proceedings.mlr.press/v235/naderiparizi24a.html)

**TLDR**: Oracle-assisted guidance is introduced to steer score-based diffusion models toward constrained domains while maintaining generative quality.

## Abstract

Score-based diffusion models are a powerful class of generative models, widely utilized across diverse domains. Despite significant advancements in large-scale tasks such as text-to-image generation, their application to constrained domains has received considerably less attention. This work addresses model learning in a setting where, in addition to the training dataset, there further exists side-information in the form of an oracle that can label samples as being outside the support of the true data generating distribution. Specifically we develop a new denoising diffusion probabilistic modeling methodology, Gen-neG, that leverages this additional side-information. Gen-neG builds on classifier guidance in diffusion models to guide the generation process towards the positive support region indicated by the oracle. We empirically establish the utility of Gen-neG in applications including collision avoidance in self-driving simulators and safety-guarded human motion generation.