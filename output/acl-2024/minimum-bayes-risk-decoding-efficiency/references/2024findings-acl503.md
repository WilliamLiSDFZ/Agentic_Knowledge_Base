---
title: "Generating Diverse and High-Quality Texts by Minimum Bayes Risk Decoding"
source: "https://aclanthology.org/2024.findings-acl.503/"
pdf_url: ""
categories: ['minimum-bayes-risk-decoding-efficiency', 'llm-training-alignment-and-evaluation']
tags: ['minimum-bayes-risk', 'diverse-generation', 'decoding']
venue: "ACL 2024"
tldr: "Proposes an MBR decoding approach that jointly optimizes for both quality and diversity in text generation outputs."
---

# Generating Diverse and High-Quality Texts by Minimum Bayes Risk Decoding

**Source**: [https://aclanthology.org/2024.findings-acl.503/](https://aclanthology.org/2024.findings-acl.503/)

**TLDR**: Proposes an MBR decoding approach that jointly optimizes for both quality and diversity in text generation outputs.

## Abstract

AbstractOne of the most important challenges in text generation systems is to produce outputs that are not only correct but also diverse.Recently, Minimum Bayes-Risk (MBR) decoding has gained prominence for generating sentences of the highest quality among the decoding algorithms. However, existing algorithms proposed to generate diverse outputs are predominantly based on beam search or random sampling, thus their output quality is capped by these underlying decoding algorithms. In this paper, we investigate an alternative approach – we develop diversity-promoting decoding algorithms by enforcing diversity objectives to MBR decoding.We propose two variants of MBR; (i) Diverse MBR (DMBR) that adds a diversity penalty to the decoding objective and (ii) k-medoids MBR (KMBR) that reformulates the decoding task as a clustering problem.We evaluate DMBR and KMBR on a variety of directed text generation tasks using encoder-decoder models and a language model with prompting. The experimental results show that the proposed method achieves a better trade-off than the diverse beam search and sampling algorithms overall.