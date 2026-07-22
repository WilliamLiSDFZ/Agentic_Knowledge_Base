---
title: "On Efficiently Representing Regular Languages as RNNs"
source: "https://aclanthology.org/2024.findings-acl.244/"
categories: ['neural-language-models-formal-language-theory']
tags: ['rnn', 'regular-languages', 'formal-language-theory']
venue: "ACL 2024"
tldr: "This work analyzes the efficiency of RNNs in representing regular languages and connects this to their empirical success as language models."
---

# On Efficiently Representing Regular Languages as RNNs

**Source**: [https://aclanthology.org/2024.findings-acl.244/](https://aclanthology.org/2024.findings-acl.244/)

**TLDR**: This work analyzes the efficiency of RNNs in representing regular languages and connects this to their empirical success as language models.

## Abstract

AbstractRecent work by Hewitt et al. (2020) provides an interpretation of the empirical success of recurrent neural networks (RNNs) as language models (LMs). It shows that RNNs can efficiently represent bounded hierarchical structures that are prevalent in human language.This suggests that RNNs’ success might be linked to their ability to model hierarchy. However, a closer inspection of hewitt-etal-2020-rnns construction shows that it is not inherently limited to hierarchical structures. This poses a natural question: What other classes of LMs RNNs can efficiently represent? To this end, we generalize Hewitt et al.’s (2020) construction and show that RNNs can efficiently represent a larger class of LMs than previously claimed—specifically, those that can be represented by a pushdown automaton with a bounded stack and a specific stack update function. Altogether, the efficiency of representing this diverse class of LMs with RNN LMs suggests novel interpretations of their inductive bias.