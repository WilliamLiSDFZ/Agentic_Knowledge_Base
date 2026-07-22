---
title: "Modelling Variability in Human Annotator Simulation"
source: "https://aclanthology.org/2024.findings-acl.67/"
pdf_url: ""
categories: ['label-noise-robust-annotation-learning']
tags: ['annotator-simulation', 'variability', 'human-evaluation', 'annotation']
venue: "ACL 2024"
tldr: "Models variability in human annotator simulation to better capture diverse subjective interpretations in evaluation tasks."
---

# Modelling Variability in Human Annotator Simulation

**Source**: [https://aclanthology.org/2024.findings-acl.67/](https://aclanthology.org/2024.findings-acl.67/)

**TLDR**: Models variability in human annotator simulation to better capture diverse subjective interpretations in evaluation tasks.

## Abstract

AbstractHuman annotator simulation (HAS) serves as a cost-effective substitute for human evaluation tasks such as data annotation and system assessment. It is important to incorporate the variability present in human evaluation into HAS, since it helps capture diverse subjective interpretations and mitigate potential biases and over-representation. This work introduces a novel framework for modelling variability in HAS. Conditional softmax flow (S-CNF) is proposed to model the distribution of subjective human annotations, which leverages diverse human annotations via meta-learning. This enables efficient generation of annotations that exhibit human variability for unlabelled input. In addition, a wide range of evaluation metrics are adopted to assess the capability and efficiency of HAS systems in predicting the aggregated behaviours of human annotators, matching the distribution of human annotations, and simulating the inter-annotator disagreements. Results demonstrate that the proposed method achieves state-of-the-art performance on two real-world human evaluation tasks: emotion recognition and toxic speech detection.