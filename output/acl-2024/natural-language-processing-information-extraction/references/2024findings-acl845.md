---
title: "Dual-Stage Multi-Task Syntax-Oriented Pre-Training for Syntactically Controlled Paraphrase Generation"
source: "https://aclanthology.org/2024.findings-acl.845/"
categories: ['unsupervised-and-structured-syntactic-parsing-methods', 'natural-language-processing-information-extraction']
tags: ['paraphrase-generation', 'syntax-controlled', 'pre-training', 'multi-task', 'syntactic-structure']
venue: "ACL 2024"
tldr: "A dual-stage multi-task syntax-oriented pre-training approach is proposed to improve syntactically controlled paraphrase generation."
---

# Dual-Stage Multi-Task Syntax-Oriented Pre-Training for Syntactically Controlled Paraphrase Generation

**Source**: [https://aclanthology.org/2024.findings-acl.845/](https://aclanthology.org/2024.findings-acl.845/)

**TLDR**: A dual-stage multi-task syntax-oriented pre-training approach is proposed to improve syntactically controlled paraphrase generation.

## Abstract

AbstractSyntactically Controlled Paraphrase Generation (SCPG), which aims at generating sentences having syntactic structures resembling given exemplars, is attracting more research efforts in recent years. We took an empirical survey on previous SCPG datasets and methods and found three tacitly approved while seldom mentioned intrinsic shortcomings/trade-offs in terms of data obtaining, task formulation, and pre-training strategies. As a mitigation to these shortcomings, we proposed a novel Dual-Stage Multi-Task (DSMT) pre-training scheme, involving a series of structure-oriented and syntax-oriented tasks, which, in our opinion, gives sequential text models the ability of com-prehending intrinsically non-sequential structures like Linearized Constituency Trees (LCTs), understanding the underlying syntactics, and even generating them by parsing sentences. We performed further pre-training of the popular T5 model on these novel tasks and fine-tuned the trained model on every possible variant of SCPG task in literature, finding that our models significantly outperformed (up to 10+ BLEU-4) previous state-of-the-art methods. Finally, we carried out ablation studies which demonstrated the effectiveness of our DSMT methods and emphasized on the SCPG performance gains compared to vanilla T5 models, especially on hard samples or under few-shot settings.