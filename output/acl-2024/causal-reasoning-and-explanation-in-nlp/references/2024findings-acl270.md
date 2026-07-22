---
title: "SyntaxShap: Syntax-aware Explainability Method for Text Generation"
source: "https://aclanthology.org/2024.findings-acl.270/"
pdf_url: ""
categories: ['causal-reasoning-and-explanation-in-nlp']
tags: ['explainability', 'syntax-aware', 'text-generation']
venue: "ACL 2024"
tldr: "Proposes SyntaxShap, a syntax-aware explainability method for sequence-to-sequence text generation models."
---

# SyntaxShap: Syntax-aware Explainability Method for Text Generation

**Source**: [https://aclanthology.org/2024.findings-acl.270/](https://aclanthology.org/2024.findings-acl.270/)

**TLDR**: Proposes SyntaxShap, a syntax-aware explainability method for sequence-to-sequence text generation models.

## Abstract

AbstractTo harness the power of large language models in safety-critical domains, we need to ensure the explainability of their predictions. However, despite the significant attention to model interpretability, there remains an unexplored domain in explaining sequence-to-sequence tasks using methods tailored for textual data. This paper introduces *SyntaxShap*, a local, model-agnostic explainability method for text generation that takes into consideration the syntax in the text data. The presented work extends Shapley values to account for parsing-based syntactic dependencies. Taking a game theoric approach, SyntaxShap only considers coalitions constraint by the dependency tree. We adopt a model-based evaluation to compare SyntaxShap and its weighted form to state-of-the-art explainability methods adapted to text generation tasks, using diverse metrics including faithfulness, coherency, and semantic alignment of the explanations to the model. We show that our syntax-aware method produces explanations that help build more faithful and coherent explanations for predictions by autoregressive models. Confronted with the misalignment of human and AI model reasoning, this paper also highlights the need for cautious evaluation strategies in explainable AI.