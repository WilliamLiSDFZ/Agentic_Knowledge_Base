---
title: "Through the Lens of Split Vote: Exploring Disagreement, Difficulty and Calibration in Legal Case Outcome Classification"
source: "https://aclanthology.org/2024.acl-long.13/"
pdf_url: ""
categories: ['legal-nlp-benchmarks-and-applications', 'llm-training-alignment-and-evaluation']
tags: ['legal-NLP', 'split-vote', 'disagreement', 'calibration', 'case-outcome-classification']
venue: "ACL 2024"
tldr: "Explores how split votes in legal decisions reflect difficulty and calibration challenges in legal case outcome classification."
---

# Through the Lens of Split Vote: Exploring Disagreement, Difficulty and Calibration in Legal Case Outcome Classification

**Source**: [https://aclanthology.org/2024.acl-long.13/](https://aclanthology.org/2024.acl-long.13/)

**TLDR**: Explores how split votes in legal decisions reflect difficulty and calibration challenges in legal case outcome classification.

## Abstract

AbstractIn legal decisions, split votes (SV) occur when judges cannot reach a unanimous decision, posing a difficulty for lawyers who must navigate diverse legal arguments and opinions. In high-stakes domains, %as human-AI interaction systems become increasingly important, understanding the alignment of perceived difficulty between humans and AI systems is crucial to build trust. However, existing NLP calibration methods focus on a classifier’s awareness of predictive performance, measured against the human majority class, overlooking inherent human label variation (HLV). This paper explores split votes as naturally observable human disagreement and value pluralism. We collect judges’ vote distributions from the European Court of Human Rights (ECHR), and present SV-ECHR, a case outcome classification (COC) dataset with SV information. We build a taxonomy of disagreement with SV-specific subcategories. We further assess the alignment of perceived difficulty between models and humans, as well as confidence- and human-calibration of COC models. We observe limited alignment with the judge vote distribution. To our knowledge, this is the first systematic exploration of calibration to human judgements in legal NLP. Our study underscores the necessity for further research on measuring and enhancing model calibration considering HLV in legal decision tasks.