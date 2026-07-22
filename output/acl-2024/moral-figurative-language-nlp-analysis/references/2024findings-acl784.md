---
title: "Figuratively Speaking: Authorship Attribution via Multi-Task Figurative Language Modeling"
source: "https://aclanthology.org/2024.findings-acl.784/"
categories: ['moral-figurative-language-nlp-analysis', 'natural-language-processing-information-extraction']
tags: ['authorship-attribution', 'figurative-language', 'multi-task-learning']
venue: "ACL 2024"
tldr: "Multi-task figurative language modeling leverages FL features as stylometric signals for authorship attribution."
---

# Figuratively Speaking: Authorship Attribution via Multi-Task Figurative Language Modeling

**Source**: [https://aclanthology.org/2024.findings-acl.784/](https://aclanthology.org/2024.findings-acl.784/)

**TLDR**: Multi-task figurative language modeling leverages FL features as stylometric signals for authorship attribution.

## Abstract

AbstractThe identification of Figurative Language (FL) features in text is crucial for various Natural Language Processing (NLP) tasks, where understanding of the author’s intended meaning and its nuances is key for successful communication. At the same time, the use of a specific blend of various FL forms most accurately reflects a writer’s style, rather than the use of any single construct, such as just metaphors or irony. Thus, we postulate that FL features could play an important role in Authorship Attribution (AA) tasks. We believe that our is the first computational study of AA based on FL use. Accordingly, we propose a Multi-task Figurative Language Model (MFLM) that learns to detect multiple FL features in text at once. We demonstrate, through detailed evaluation across multiple test sets, that the our model tends to perform equally or outperform specialized binary models in FL detection. Subsequently, we evaluate the predictive capability of joint FL features towards the AA task on three datasets, observing improved AA performance through the integration of MFLM embeddings.