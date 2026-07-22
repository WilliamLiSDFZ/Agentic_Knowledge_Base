---
title: "An Ensemble-of-Experts Framework for Rehearsal-free Continual Relation Extraction"
source: "https://aclanthology.org/2024.findings-acl.83/"
categories: ['continual-learning-for-nlp-tasks', 'natural-language-processing-information-extraction']
tags: ['continual-relation-extraction', 'rehearsal-free', 'ensemble-of-experts']
venue: "ACL 2024"
tldr: "Proposes a rehearsal-free ensemble-of-experts framework for continual relation extraction that avoids storing samples and associated privacy risks."
---

# An Ensemble-of-Experts Framework for Rehearsal-free Continual Relation Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.83/](https://aclanthology.org/2024.findings-acl.83/)

**TLDR**: Proposes a rehearsal-free ensemble-of-experts framework for continual relation extraction that avoids storing samples and associated privacy risks.

## Abstract

AbstractContinual relation extraction (CRE) aims to continuously learn relations in new tasks without forgetting old relations in previous tasks.Current CRE methods are all rehearsal-based which need to store samples and thus may encounter privacy and security issues.This paper targets rehearsal-free continual relation extraction for the first time and decomposes it into task identification and within-task prediction sub-problems. Existing rehearsal-free methods focus on training a model (expert) for within-task prediction yet neglect to enhance models’ capability of task identification.In this paper, we propose an Ensemble-of-Experts (EoE) framework for rehearsal-free continual relation extraction. Specifically, we first discriminatively train each expert by augmenting analogous relations across tasks to enhance the expert’s task identification ability. We then propose a cascade voting mechanism to form an ensemble of experts for effectively aggregating their abilities.Extensive experiments demonstrate that our method outperforms current rehearsal-free methods and is even better than rehearsal-based CRE methods.