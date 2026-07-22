---
title: "imapScore: Medical Fact Evaluation Made Easy"
source: "https://aclanthology.org/2024.findings-acl.610/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp']
tags: ['medical-nlp', 'fact-evaluation', 'nlg-evaluation']
venue: "ACL 2024"
tldr: "imapScore proposes an automatic medical fact evaluation metric for NLG systems that focuses on clinically critical correctness in medical QA."
---

# imapScore: Medical Fact Evaluation Made Easy

**Source**: [https://aclanthology.org/2024.findings-acl.610/](https://aclanthology.org/2024.findings-acl.610/)

**TLDR**: imapScore proposes an automatic medical fact evaluation metric for NLG systems that focuses on clinically critical correctness in medical QA.

## Abstract

AbstractAutomatic evaluation of natural language generation (NLG) tasks has gained extensive research interests, since it can rapidly assess the performance of large language models (LLMs). However, automatic NLG evaluation struggles with medical QA because it fails to focus on the crucial correctness of medical facts throughout the generated text. To address this, this paper introduces a new data structure, imap, designed to capture key information in questions and answers, enabling evaluators to focus on essential details. The imap comprises three components: Query, Constraint, and Inform, each of which is in the form of term-value pairs to represent medical facts in a structural manner. We then introduce imapScore, which compares the corresponding medical term-value pairs in the imap to score generated texts. We utilize GPT-4 to extract imap from questions, human-annotated answers, and generated responses. To mitigate the diversity in medical terminology for fair term-value pairs comparison, we use a medical knowledge graph to assist GPT-4 in determining matches. To compare imapScore with existing NLG metrics, we establish a new benchmark dataset. The experimental results show that imapScore consistently outperforms state-of-the-art metrics, demonstrating an average improvement of 79.8% in correlation with human scores. Furthermore, incorporating imap into n-gram, embedding, and LLM metrics boosts the base versions, increasing correlation with human scores by averages of 89.9%, 81.7%, and 32.6%, respectively.