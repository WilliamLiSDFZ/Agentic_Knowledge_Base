---
title: "Monotonic Representation of Numeric Attributes in Language Models"
source: "https://aclanthology.org/2024.acl-short.18/"
pdf_url: ""
categories: ['language-model-representations-and-embedding-spaces', 'transformer-architecture-analysis-and-design']
tags: ['numeric-attributes', 'monotonic-representation', 'language-model-editing']
venue: "ACL 2024"
tldr: "Introduces a method to find and edit monotonic internal representations of numeric attributes in language models."
---

# Monotonic Representation of Numeric Attributes in Language Models

**Source**: [https://aclanthology.org/2024.acl-short.18/](https://aclanthology.org/2024.acl-short.18/)

**TLDR**: Introduces a method to find and edit monotonic internal representations of numeric attributes in language models.

## Abstract

AbstractLanguage models (LMs) can express factual knowledge involving numeric properties such as Karl Popper was born in 1902. However, how this information is encoded in the model’s internal representations is not understood well. Here, we introduce a method for finding and editing representations of numeric properties such as an entity’s birth year. We find directions that encode numeric properties monotonically, in an interpretable fashion. When editing representations along these directions, LM output changes accordingly. For example, by patching activations along a “birthyear” direction we can make the LM express an increasingly late birthyear. Property-encoding directions exist across several numeric properties in all models under consideration, suggesting the possibility that monotonic representation of numeric properties consistently emerges during LM pretraining.Code: https://github.com/bheinzerling/numeric-property-reprA long version of this short paper is available at: https://arxiv.org/abs/2403.10381