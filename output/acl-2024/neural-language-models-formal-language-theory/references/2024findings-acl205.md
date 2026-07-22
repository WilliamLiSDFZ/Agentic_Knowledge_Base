---
title: "Compositional Generalization with Grounded Language Models"
source: "https://aclanthology.org/2024.findings-acl.205/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'neural-language-models-formal-language-theory']
tags: ['compositional-generalization', 'grounded-language-models', 'knowledge-graphs', 'semantic-parsing', 'evaluation']
venue: "ACL 2024"
tldr: "Extends compositional generalization evaluation to grounded language models that use external knowledge graphs for semantic parsing."
---

# Compositional Generalization with Grounded Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.205/](https://aclanthology.org/2024.findings-acl.205/)

**TLDR**: Extends compositional generalization evaluation to grounded language models that use external knowledge graphs for semantic parsing.

## Abstract

AbstractGrounded language models use external sources of information, such as knowledge graphs, to meet some of the general challenges associated with pre-training. By extending previous work on compositional generalization in semantic parsing, we allow for a controlled evaluation of the degree to which these models learn and generalize from patterns in knowledge graphs. We develop a procedure for generating natural language questions paired with knowledge graphs that targets different aspects of compositionality and further avoids grounding the language models in information already encoded implicitly in their weights. We evaluate existing methods for combining language models with knowledge graphs and find them to struggle with generalization to sequences of unseen lengths and to novel combinations of seen base components. While our experimental results provide some insight into the expressive power of these models, we hope our work and released datasets motivate future research on how to better combine language models with structured knowledge representations.