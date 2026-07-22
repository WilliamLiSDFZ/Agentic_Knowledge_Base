---
title: "Scented-EAE: Stage-Customized Entity Type Embedding for Event Argument Extraction"
source: "https://aclanthology.org/2024.findings-acl.309/"
categories: ['natural-language-processing-information-extraction']
tags: ['event-argument-extraction', 'entity-type-embedding', 'NER']
venue: "ACL 2024"
tldr: "Introduces stage-customized entity type embeddings to improve event argument extraction by leveraging entity type information."
---

# Scented-EAE: Stage-Customized Entity Type Embedding for Event Argument Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.309/](https://aclanthology.org/2024.findings-acl.309/)

**TLDR**: Introduces stage-customized entity type embeddings to improve event argument extraction by leveraging entity type information.

## Abstract

AbstractExisting methods for incorporating entities into EAE rely on prompts or NER. They typically fail to explicitly explore the role of entity types, which results in shallow argument comprehension and often encounter three issues: (1) weak semantic associations due to missing role-entity correspondence cues; (2) compromised semantic integrity from abandoning context after recognizing entities regardless of their types; (3) one-sided semantic understanding relying solely on argument role semantics. To tackle these issues, we propose Scented-EAE, an EAE model with stage-customized entity type embedding to explicitly underscore and explore the role of entity types, thus intervening in argument selection. Specifically, at the input stage, we strengthen semantic associations by prompting role-entity correspondence after extending a non-autoregressive decoder as part of the encoder. At the intermediate stage, we preserve semantic integrity by optimizing our proposed BIO-aware NER and EAE via a novel IPE joint learning. At the output stage, we expand semantic understanding dimensions by determining arguments using span selectors from argument roles and entity types. Experiments show that our model achieves state-of-the-art performance on mainstream benchmarks. In addition, it also exhibits robustness in low-resource settings with the help of prompts and entity types.