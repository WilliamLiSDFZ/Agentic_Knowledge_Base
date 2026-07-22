---
title: "Do Pre-Trained Language Models Detect and Understand Semantic Underspecification? Ask the DUST!"
source: "https://aclanthology.org/2024.findings-acl.572/"
categories: ['language-model-human-cognitive-linguistic-alignment', 'language-model-representations-and-embedding-spaces']
tags: ['semantic-underspecification', 'language-understanding', 'probing']
venue: "ACL 2024"
tldr: "Proposes DUST, a benchmark to test whether pre-trained language models can detect and resolve semantically underspecified sentences."
---

# Do Pre-Trained Language Models Detect and Understand Semantic Underspecification? Ask the DUST!

**Source**: [https://aclanthology.org/2024.findings-acl.572/](https://aclanthology.org/2024.findings-acl.572/)

**TLDR**: Proposes DUST, a benchmark to test whether pre-trained language models can detect and resolve semantically underspecified sentences.

## Abstract

AbstractIn everyday language use, speakers frequently utter and interpret sentences that are semantically underspecified, namely, whose content is insufficient to fully convey their message or interpret them univocally. For example, to interpret the underspecified sentence “Don’t spend too much”, which leaves implicit what (not) to spend, additional linguistic context or outside knowledge is needed. In this work, we propose a novel Dataset of semantically Underspecified Sentences grouped by Type (DUST) and use it to study whether pre-trained language models (LMs) correctly identify and interpret underspecified sentences. We find that newer LMs are reasonably able to identify underspecified sentences when explicitly prompted. However, interpreting them correctly is much harder for any LMs. Our experiments show that when interpreting underspecified sentences, LMs exhibit little uncertainty, contrary to what theoretical accounts of underspecification would predict. Overall, our study reveals limitations in current models’ processing of sentence semantics and highlights the importance of using naturalistic data and communicative scenarios when evaluating LMs’ language capabilities.