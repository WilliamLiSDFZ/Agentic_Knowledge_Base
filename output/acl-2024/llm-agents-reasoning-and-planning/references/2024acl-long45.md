---
title: "Learn from Failure: Fine-tuning LLMs with Trial-and-Error Data for Intuitionistic Propositional Logic Proving"
source: "https://aclanthology.org/2024.acl-long.45/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'neural-language-models-formal-language-theory']
tags: ['theorem-proving', 'fine-tuning', 'trial-and-error-learning']
venue: "ACL 2024"
tldr: "Fine-tunes LLMs on trial-and-error proof data to improve automated theorem proving for intuitionistic propositional logic."
---

# Learn from Failure: Fine-tuning LLMs with Trial-and-Error Data for Intuitionistic Propositional Logic Proving

**Source**: [https://aclanthology.org/2024.acl-long.45/](https://aclanthology.org/2024.acl-long.45/)

**TLDR**: Fine-tunes LLMs on trial-and-error proof data to improve automated theorem proving for intuitionistic propositional logic.

## Abstract

AbstractRecent advances in Automated Theorem Proving have shown the effectiveness of leveraging a (large) language model that generates tactics (i.e. proof steps) to search through proof states. The current model, while trained solely on successful proof paths, faces a discrepancy at the inference stage, as it must sample and try various tactics at each proof state until finding success, unlike its training which does not incorporate learning from failed attempts. Intuitively, a tactic that leads to a failed search path would indicate that similar tactics should receive less attention during the following trials. In this paper, we demonstrate the benefit of training models that additionally learn from failed search paths. Facing the lack of such trial-and-error data in existing open-source theorem-proving datasets, we curate a dataset on intuitionistic propositional logic theorems and formalize it in Lean, such that we can reliably check the correctness of proofs. We compare our model trained on relatively short trial-and-error information (TrialMaster) with models trained only on the correct paths and discover that the former solves more unseen theorems with lower trial searches.