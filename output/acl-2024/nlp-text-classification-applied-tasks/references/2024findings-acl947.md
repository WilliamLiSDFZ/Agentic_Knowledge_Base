---
title: "ProgGen: Generating Named Entity Recognition Datasets Step-by-step with Self-Reflexive Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.947/"
categories: ['natural-language-processing-information-extraction', 'nlp-text-classification-applied-tasks']
tags: ['named-entity-recognition', 'data-generation', 'self-reflection']
venue: "ACL 2024"
tldr: "ProgGen uses self-reflexive LLMs to generate step-by-step NER datasets, improving structured extraction with minimal supervision."
---

# ProgGen: Generating Named Entity Recognition Datasets Step-by-step with Self-Reflexive Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.947/](https://aclanthology.org/2024.findings-acl.947/)

**TLDR**: ProgGen uses self-reflexive LLMs to generate step-by-step NER datasets, improving structured extraction with minimal supervision.

## Abstract

AbstractAlthough Large Language Models (LLMs) exhibit remarkable adaptability across domains, these models often fall short in structured knowledge extraction tasks such as named entity recognition (NER). This paper explores an innovative, cost-efficient strategy to harness LLMs with modest NER capabilities for producing superior NER datasets. Our approach diverges from the basic class-conditional prompts by instructing LLMs to self-reflect on the specific domain, thereby generating domain-relevant attributes (such as category and emotions for movie reviews), which are utilized for creating attribute-rich training data. Furthermore, we preemptively generate entity terms and then develop NER context data around these entities, effectively bypassing the LLMs’ challenges with complex structures. Our experiments across both general and niche domains reveal significant performance enhancements over conventional data generation methods while being more cost-effective than existing alternatives.