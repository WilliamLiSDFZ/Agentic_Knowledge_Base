---
title: "AlignRE: An Encoding and Semantic Alignment Approach for Zero-Shot Relation Extraction"
source: "https://aclanthology.org/2024.findings-acl.174/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'language-model-representations-and-embedding-spaces']
tags: ['zero-shot', 'relation-extraction', 'semantic-alignment']
venue: "ACL 2024"
tldr: "AlignRE improves zero-shot relation extraction by aligning sentence and relation prototype embeddings through semantic encoding."
---

# AlignRE: An Encoding and Semantic Alignment Approach for Zero-Shot Relation Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.174/](https://aclanthology.org/2024.findings-acl.174/)

**TLDR**: AlignRE improves zero-shot relation extraction by aligning sentence and relation prototype embeddings through semantic encoding.

## Abstract

AbstractZero-shot Relation Extraction (ZSRE) aims to predict unseen relations between entity pairs from input sentences. Existing prototype-based ZSRE methods encode relation descriptions into prototype embeddings and predict by measuring the similarity between sentence embeddings and prototype embeddings. However, these methods often overlook abundant side information of relations and suffer from a significant encoding gap between prototypes and sentences, limiting performance. To this end, we propose a framework named AlignRE, based on two Alignment methods for ZSRE. Specifically, we present a novel perspective centered on encoding schema alignment to enhance prototype-based ZSRE methods. We utilize well-designed prompt-tuning to bridge the encoding gap. To improve prototype quality, we explore and leverage multiple side information and propose a prototype aggregation method based on semantic alignment to create comprehensive relation prototype representations. We conduct experiments on FewRel and Wiki-ZSL datasets and consistently outperform state-of-the-art methods. Moreover, our method exhibits substantially faster performance and reduces the need for extensive manual labor in prototype construction. Code is available at https://github.com/lizehan1999/AlignRE.