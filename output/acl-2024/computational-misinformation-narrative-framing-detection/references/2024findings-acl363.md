---
title: "HQP: A Human-Annotated Dataset for Detecting Online Propaganda"
source: "https://aclanthology.org/2024.findings-acl.363/"
pdf_url: ""
categories: ['computational-misinformation-narrative-framing-detection']
tags: ['propaganda-detection', 'human-annotation', 'online-content']
venue: "ACL 2024"
tldr: "Introduces HQP, a human-annotated dataset for detecting online propaganda with higher-quality labels than prior work."
---

# HQP: A Human-Annotated Dataset for Detecting Online Propaganda

**Source**: [https://aclanthology.org/2024.findings-acl.363/](https://aclanthology.org/2024.findings-acl.363/)

**TLDR**: Introduces HQP, a human-annotated dataset for detecting online propaganda with higher-quality labels than prior work.

## Abstract

AbstractOnline propaganda poses a severe threat to the integrity of societies. However, existing datasets for detecting online propaganda have a key limitation: they were annotated using weak labels that can be noisy and even incorrect. To address this limitation, our work makes the following contributions: (1) We present HQP: a novel dataset (N=30000) for detecting online propaganda with high-quality labels. To the best of our knowledge, HQP is the first large-scale dataset for detecting online propaganda that was created through human annotation. (2) We show empirically that state-of-the-art language models fail in detecting online propaganda when trained with weak labels (AUC: 64.03). In contrast, state-of-the-art language models can accurately detect online propaganda when trained with our high-quality labels (AUC: 92.25), which is an improvement of 44%. (3) We show that prompt-based learning using a small sample of high-quality labels can still achieve a reasonable performance (AUC: 80.27) while significantly reducing the cost of labeling. (4) We extend HQP to HQP+ to test how well propaganda across different contexts can be detected. Crucially, our work highlights the importance of high-quality labels for sensitive NLP tasks such as propaganda detection.