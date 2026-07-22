---
title: "LLMs cannot find reasoning errors, but can correct them given the error location"
source: "https://aclanthology.org/2024.findings-acl.826/"
categories: ['llm-hallucination-detection-and-mitigation']
tags: ['self-correction', 'reasoning-errors', 'llm-evaluation']
venue: "ACL 2024"
tldr: "Shows LLMs cannot reliably detect reasoning errors independently but can correct them when the error location is provided."
---

# LLMs cannot find reasoning errors, but can correct them given the error location

**Source**: [https://aclanthology.org/2024.findings-acl.826/](https://aclanthology.org/2024.findings-acl.826/)

**TLDR**: Shows LLMs cannot reliably detect reasoning errors independently but can correct them when the error location is provided.

## Abstract

AbstractWhile self-correction has shown promise in improving LLM outputs in terms of style and quality (e.g. Chen et al., 2023b; Madaan et al.,2023), recent attempts to self-correct logical or reasoning errors often cause correct answers to become incorrect, resulting in worse performances overall (Huang et al., 2023). In this paper, we show that poor self-correction performance stems from LLMs’ inability tofind logical mistakes, rather than their ability to correct a known mistake. Firstly, we benchmark several state-of-the-art LLMs ontheir mistake-finding ability and demonstrate that they generally struggle with the task, even in highly objective, unambiguous cases. Secondly, we test the correction abilities of LLMs – separately from mistake finding – using a backtracking setup that feeds ground truth mistake location information to the model. We show that this boosts downstream task performance across our 5 reasoning tasks, indicating that LLMs’ correction abilities are robust. Finally, we show that it is possible to obtain mistake location information without ground truth labels or in-domain training data. We train a small classifier with out-of-domain data, which exhibits stronger mistake-finding performance than prompting a large model. We release our dataset of LLM-generated logical mistakes, BIG-Bench Mistake, to enable further research into locating LLM reasoning mistakes.