---
title: "KOMBO: Korean Character Representations Based on the Combination Rules of Subcharacters"
source: "https://aclanthology.org/2024.findings-acl.302/"
pdf_url: ""
categories: ['nlp-for-asian-languages', 'language-model-representations-and-embedding-spaces']
tags: ['Korean', 'subcharacter', 'language-model']
venue: "ACL 2024"
tldr: "KOMBO introduces a Korean character representation framework based on Hangeul's subcharacter combination rules for pretrained models."
---

# KOMBO: Korean Character Representations Based on the Combination Rules of Subcharacters

**Source**: [https://aclanthology.org/2024.findings-acl.302/](https://aclanthology.org/2024.findings-acl.302/)

**TLDR**: KOMBO introduces a Korean character representation framework based on Hangeul's subcharacter combination rules for pretrained models.

## Abstract

AbstractThe Korean writing system, Hangeul, has a unique character representation rigidly following the invention principles recorded in Hunminjeongeum. However, existing pre-trained language models (PLMs) for Korean have overlooked these principles. In this paper, we introduce a novel framework for Korean PLMs called KOMBO, which firstly brings the invention principles of Hangeul to represent character. Our proposed method, KOMBO, exhibits notable experimental proficiency across diverse NLP tasks. In particular, our method outperforms the state-of-the-art Korean PLM by an average of 2.11% in five Korean natural language understanding tasks. Furthermore, extensive experiments demonstrate that our proposed method is suitable for comprehending the linguistic features of the Korean language. Consequently, we shed light on the superiority of using subcharacters over the typical subword-based approach for Korean PLMs. Our code is available at: https://github.com/SungHo3268/KOMBO.