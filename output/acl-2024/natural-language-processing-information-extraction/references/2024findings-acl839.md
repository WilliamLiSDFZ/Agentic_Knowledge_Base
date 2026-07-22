---
title: "ReLiK: Retrieve and LinK, Fast and Accurate Entity Linking and Relation Extraction on an Academic Budget"
source: "https://aclanthology.org/2024.findings-acl.839/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['entity-linking', 'relation-extraction', 'retriever-reader']
venue: "ACL 2024"
tldr: "Proposes ReLiK, a fast and accurate retriever-reader architecture for entity linking and relation extraction on an academic budget."
---

# ReLiK: Retrieve and LinK, Fast and Accurate Entity Linking and Relation Extraction on an Academic Budget

**Source**: [https://aclanthology.org/2024.findings-acl.839/](https://aclanthology.org/2024.findings-acl.839/)

**TLDR**: Proposes ReLiK, a fast and accurate retriever-reader architecture for entity linking and relation extraction on an academic budget.

## Abstract

AbstractEntity Linking (EL) and Relation Extraction (RE) are fundamental tasks in Natural Language Processing, serving as critical components in a wide range of applications. In this paper, we propose ReLiK, a Retriever-Reader architecture for both EL and RE, where, given an input text, the Retriever module undertakes the identification of candidate entities or relations that could potentially appear within the text. Subsequently, the Reader module is tasked to discern the pertinent retrieved entities or relations and establish their alignment with the corresponding textual spans. Notably, we put forward an innovative input representation that incorporates the candidate entities or relations alongside the text, making it possible to link entities or extract relations in a single forward pass and to fully leverage pre-trained language models contextualization capabilities, in contrast with previous Retriever-Reader-based methods, which require a forward pass for each candidate. Our formulation of EL and RE achieves state-of-the-art performance in both in-domain and out-of-domain benchmarks while using academic budget training and with up to 40x inference speed compared to competitors. Finally, we show how our architecture can be used seamlessly for Information Extraction (cIE), i.e. EL + RE, and setting a new state of the art by employing a shared Reader that simultaneously extracts entities and relations.