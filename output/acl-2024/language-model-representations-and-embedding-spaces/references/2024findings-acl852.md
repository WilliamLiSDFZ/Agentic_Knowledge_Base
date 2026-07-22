---
title: "Generalisation First, Memorisation Second? Memorisation Localisation for Natural Language Classification Tasks"
source: "https://aclanthology.org/2024.findings-acl.852/"
categories: ['label-noise-robust-annotation-learning', 'language-model-representations-and-embedding-spaces']
tags: ['memorization', 'localization', 'text-classification']
venue: "ACL 2024"
tldr: "Investigates how and where neural models memorize atypical training examples in natural language classification tasks."
---

# Generalisation First, Memorisation Second? Memorisation Localisation for Natural Language Classification Tasks

**Source**: [https://aclanthology.org/2024.findings-acl.852/](https://aclanthology.org/2024.findings-acl.852/)

**TLDR**: Investigates how and where neural models memorize atypical training examples in natural language classification tasks.

## Abstract

AbstractMemorisation is a natural part of learning from real-world data: neural models pick up on atypical input-output combinations and store those training examples in their parameter space. That this happens is well-known, but how and where are questions that remain largely unanswered. Given a multi-layered neural model, where does memorisation occur in the millions of parameters?Related work reports conflicting findings: a dominant hypothesis based on image classification is that lower layers learn generalisable features and that deeper layers specialise and memorise. Work from NLP suggests this does not apply to language models, but has been mainly focused on memorisation of facts.We expand the scope of the localisation question to 12 natural language classification tasks and apply 4 memorisation localisation techniques.Our results indicate that memorisation is a gradual process rather than a localised one, establish that memorisation is task-dependent, and give nuance to the generalisation first, memorisation second hypothesis.