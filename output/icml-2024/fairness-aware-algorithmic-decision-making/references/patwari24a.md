---
title: "PerceptAnon: Exploring the Human Perception of Image Anonymization Beyond Pseudonymization for GDPR"
source: "https://proceedings.mlr.press/v235/patwari24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/patwari24a/patwari24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'open-ai-governance-and-data-ethics']
tags: ['image-anonymization', 'GDPR', 'human-perception', 'privacy']
venue: "ICML 2024"
tldr: "Investigates human perception of image anonymization beyond face pseudonymization to better align anonymization techniques with GDPR requirements."
---

# PerceptAnon: Exploring the Human Perception of Image Anonymization Beyond Pseudonymization for GDPR

**Source**: [https://proceedings.mlr.press/v235/patwari24a.html](https://proceedings.mlr.press/v235/patwari24a.html)

**TLDR**: Investigates human perception of image anonymization beyond face pseudonymization to better align anonymization techniques with GDPR requirements.

## Abstract

Current image anonymization techniques, largely focus on localized pseudonymization, typically modify identifiable features like faces or full bodies and evaluate anonymity through metrics such as detection and re-identification rates. However, this approach often overlooks information present in the entire image post-anonymization that can compromise privacy, such as specific locations, objects/items, or unique attributes. Acknowledging the pivotal role of human judgment in anonymity, our study conducts a thorough analysis of perceptual anonymization, exploring its spectral nature and its critical implications for image privacy assessment, particularly in light of regulations such as the General Data Protection Regulation (GDPR). To facilitate this, we curated a dataset specifically tailored for assessing anonymized images. We introduce a learning-based metric, PerceptAnon, which is tuned to align with the human Perception of Anonymity. PerceptAnon evaluates both original-anonymized image pairs and solely anonymized images. Trained using human annotations, our metric encompasses both anonymized subjects and their contextual backgrounds, thus providing a comprehensive evaluation of privacy vulnerabilities. We envision this work as a milestone for understanding and assessing image anonymization, and establishing a foundation for future research. The codes and dataset are available in https://github.com/SonyResearch/gdpr_perceptanon.