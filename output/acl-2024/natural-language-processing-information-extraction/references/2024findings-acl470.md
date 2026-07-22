---
title: "The State of Relation Extraction Data Quality: Is Bigger Always Better?"
source: "https://aclanthology.org/2024.findings-acl.470/"
categories: ['natural-language-processing-information-extraction', 'nlp-research-culture-and-practices']
tags: ['relation-extraction', 'data-quality', 'evaluation-practices', 'benchmarks']
venue: "ACL 2024"
tldr: "Analyzes the state of data quality and evaluation practices in relation extraction research, questioning whether larger datasets always yield better models."
---

# The State of Relation Extraction Data Quality: Is Bigger Always Better?

**Source**: [https://aclanthology.org/2024.findings-acl.470/](https://aclanthology.org/2024.findings-acl.470/)

**TLDR**: Analyzes the state of data quality and evaluation practices in relation extraction research, questioning whether larger datasets always yield better models.

## Abstract

AbstractRelation extraction (RE) extracts structured tuples of relationships (e.g. friend, enemy) between entities (e.g. Sherlock Holmes, John Watson) from text, with exciting potential applications. Hundreds of RE papers have been published in recent years; do their evaluation practices inform these goals? We review recent surveys and a sample of recent RE methods papers, compiling 38 datasets currently being used. Unfortunately, many have frequent label errors, and ones with known problems continue to be used. Many datasets focus on producing labels for a large number of relation types, often through error-prone annotation methods (e.g. distant supervision or crowdsourcing), and many recent papers rely exclusively on such datasets. We draw attention to a promising alternative: datasets with a small number of relations, often in specific domains like chemistry, finance, or biomedicine, where it is possible to obtain high quality expert annotations; such data can more realistically evaluate RE performance. The research community should consider more often using such resources.