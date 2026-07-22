---
title: "LocalRQA: From Generating Data to Locally Training, Testing, and Deploying Retrieval-Augmented QA Systems"
source: "https://aclanthology.org/2024.acl-demos.14/"
pdf_url: ""
categories: ['collaborative-llm-deployment-and-inference-optimization']
tags: ['retrieval-augmented-generation', 'question-answering', 'local-deployment']
venue: "ACL 2024"
tldr: "LocalRQA is a toolkit for building, training, testing, and locally deploying retrieval-augmented QA systems using custom data."
---

# LocalRQA: From Generating Data to Locally Training, Testing, and Deploying Retrieval-Augmented QA Systems

**Source**: [https://aclanthology.org/2024.acl-demos.14/](https://aclanthology.org/2024.acl-demos.14/)

**TLDR**: LocalRQA is a toolkit for building, training, testing, and locally deploying retrieval-augmented QA systems using custom data.

## Abstract

AbstractRetrieval-augmented question-answering systems combine retrieval techniques with large language models to provide answers that are more accurate and informative. Many existing toolkits allow users to quickly build such systems using off-the-shelf models, but they fall short in supporting researchers and developers to customize the *model training, testing, and deployment process*. We propose LocalRQA, an open-source toolkit that features a wide selection of model training algorithms, evaluation methods, and deployment tools curated from the latest research. As a showcase, we build QA systems using online documentation obtained from Databricks and Faire’s websites. We find 7B-models trained and deployed using LocalRQA reach a similar performance compared to using OpenAI’s text-ada-002 and GPT-4-turbo.