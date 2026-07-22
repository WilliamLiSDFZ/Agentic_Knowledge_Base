---
title: "Reformulating Domain Adaptation of Large Language Models as Adapt-Retrieve-Revise: A Case Study on Chinese Legal Domain"
source: "https://aclanthology.org/2024.findings-acl.299/"
categories: ['legal-nlp-benchmarks-and-applications']
tags: ['domain-adaptation', 'retrieval-augmented-generation', 'Chinese-legal-NLP']
venue: "ACL 2024"
tldr: "Reformulates LLM domain adaptation as an adapt-retrieve-revise pipeline to reduce hallucination in Chinese legal tasks."
---

# Reformulating Domain Adaptation of Large Language Models as Adapt-Retrieve-Revise: A Case Study on Chinese Legal Domain

**Source**: [https://aclanthology.org/2024.findings-acl.299/](https://aclanthology.org/2024.findings-acl.299/)

**TLDR**: Reformulates LLM domain adaptation as an adapt-retrieve-revise pipeline to reduce hallucination in Chinese legal tasks.

## Abstract

AbstractWhile large language models (LLMs) like GPT-4 have recently demonstrated astonishing zero-shot capabilities in general domain tasks, they often generate content with hallucinations in specific domains such as Chinese law, hindering their application in these areas. This is typically due to the absence of training data that encompasses such a specific domain, preventing GPT-4 from acquiring in-domain knowledge. A pressing challenge is that it’s not plausible to continue training LLMs of the GPT-4’s scale on in-domain data.This paper introduces a simple yet effective domain adaptation framework for GPT-4 by reformulating generation as an adapt-retrieve-revise process. The initial step is to adapt an affordable 7B LLM to the Chinese legal domain by continuing learning in-domain data. When solving an in-domain task, we leverage the adapted LLM to generate a draft answer given a task query. Then, the draft answer will be used to retrieve supporting evidence candidates from an external in-domain knowledge base. Finally, the draft answer and retrieved evidence are concatenated into a whole prompt to let GPT-4 assess the evidence and revise the draft answer to generate the final answer. Our proposal combines the advantages of the efficiency of adapting a smaller 7B model with the evidence-assessing capability of GPT-4 and effectively prevents GPT-4 from generating hallucinatory content. In the zero-shot setting of four Chinese legal tasks, our method improves the average score by +33.6 points, compared to GPT-4 direct generation. When compared to two stronger retrieval-based baselines, our method outperforms them by +17.0 and +23.5.