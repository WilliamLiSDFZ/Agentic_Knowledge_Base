---
title: "Knowledge-Driven Cross-Document Relation Extraction"
source: "https://aclanthology.org/2024.findings-acl.227/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'document-understanding-and-information-extraction']
tags: ['relation-extraction', 'cross-document', 'knowledge-driven', 'NLP']
venue: "ACL 2024"
tldr: "This paper proposes a knowledge-driven approach for extracting relations across multiple documents, addressing challenges unique to the cross-document setting."
---

# Knowledge-Driven Cross-Document Relation Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.227/](https://aclanthology.org/2024.findings-acl.227/)

**TLDR**: This paper proposes a knowledge-driven approach for extracting relations across multiple documents, addressing challenges unique to the cross-document setting.

## Abstract

AbstractRelation extraction (RE) is a well-known NLP application often treated as a sentence or document-level task. However, a handful of recent efforts explore it across documents or in the cross-document setting (CrossDocRE). This is distinct from the single document case because different documents often focus on disparate themes, while text within a document tends to have a single goal.Current CrossDocRE efforts do not consider domain knowledge, which are often assumed to be known to the reader when documents are authored. Here, we propose a novel approach, KXDocRE, that embed domain knowledge of entities with input text for cross-document RE. Our proposed framework has three main benefits over baselines: 1) it incorporates domain knowledge of entities along with documents’ text; 2) it offers interpretability by producing explanatory text for predicted relations between entities 3) it improves performance over the prior methods. Code and models are available at https://github.com/kracr/cross-doc-relation-extraction.