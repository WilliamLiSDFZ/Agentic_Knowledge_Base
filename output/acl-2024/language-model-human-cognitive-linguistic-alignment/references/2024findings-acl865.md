---
title: "Modeling Overregularization in Children with Small Language Models"
source: "https://aclanthology.org/2024.findings-acl.865/"
categories: ['language-model-human-cognitive-linguistic-alignment', 'neural-language-models-formal-language-theory']
tags: ['language-acquisition', 'overregularization', 'small-language-models']
venue: "ACL 2024"
tldr: "Models children's morphological overregularization errors using small language models to study language acquisition processes."
---

# Modeling Overregularization in Children with Small Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.865/](https://aclanthology.org/2024.findings-acl.865/)

**TLDR**: Models children's morphological overregularization errors using small language models to study language acquisition processes.

## Abstract

AbstractThe imitation of the children’s language acquisition process has been explored to make language models (LMs) more efficient.In particular, errors caused by children’s regularization (so-called overregularization, e.g., using wroted for the past tense of write) have been widely studied to reveal the mechanisms of language acquisition. Existing research has analyzed regularization in language acquisition only by modeling word inflection directly, which is unnatural in light of human language acquisition. In this paper, we hypothesize that language models that imitate the errors children make during language acquisition have a learning process more similar to humans. To verify this hypothesis, we analyzed the learning curve and error preferences of verb inflections in small-scale LMs using acceptability judgments. We analyze the differences in results by model architecture, data, and tokenization. Our model shows child-like U-shaped learning curves clearly for certain verbs, but the preferences for types of overgeneralization did not fully match the observations in children.