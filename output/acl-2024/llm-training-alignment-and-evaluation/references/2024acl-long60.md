---
title: "RORA: Robust Free-Text Rationale Evaluation"
source: "https://aclanthology.org/2024.acl-long.60/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'causal-reasoning-and-explanation-in-nlp']
tags: ['rationale-evaluation', 'explainable-nlp', 'robustness']
venue: "ACL 2024"
tldr: "RORA proposes a robust evaluation framework for free-text rationales in explainable NLP that handles diverse reasoning paths without definitive ground truth."
---

# RORA: Robust Free-Text Rationale Evaluation

**Source**: [https://aclanthology.org/2024.acl-long.60/](https://aclanthology.org/2024.acl-long.60/)

**TLDR**: RORA proposes a robust evaluation framework for free-text rationales in explainable NLP that handles diverse reasoning paths without definitive ground truth.

## Abstract

AbstractFree-text rationales play a pivotal role in explainable NLP, bridging the knowledge and reasoning gaps behind a model’s decision-making. However, due to the diversity of potential reasoning paths and a corresponding lack of definitive ground truth, their evaluation remains a challenge. Existing metrics rely on the degree to which a rationale supports a target label, but we find these fall short in evaluating rationales that inadvertently leak the label. To address this problem, we propose RORA, a RObust free-text RAtionale evaluation against label leakage. RORA quantifies the new information supplied by a rationale to justify the label. This is achieved by assessing the conditional 𝒱-information (Hewitt et al., 2021) with a predictive family robust against leaky features that can be exploited by a small model. RORA consistently outperforms existing approaches in evaluating human-written, synthetic, or model-generated rationales, particularly demonstrating robustness against label leakage. We also show that RORA aligns well with human judgment, providing a more reliable and accurate measurement across diverse free-text rationales.