---
title: "DFA-RAG: Conversational Semantic Router for Large Language Model with Definite Finite Automaton"
source: "https://proceedings.mlr.press/v235/sun24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24e/sun24e.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['RAG', 'finite-automaton', 'LLM', 'conversational-agent', 'compliance']
venue: "ICML 2024"
tldr: "DFA-RAG integrates a definite finite automaton with retrieval-augmented LLMs to enforce regulated and compliant responses in conversational agents."
---

# DFA-RAG: Conversational Semantic Router for Large Language Model with Definite Finite Automaton

**Source**: [https://proceedings.mlr.press/v235/sun24e.html](https://proceedings.mlr.press/v235/sun24e.html)

**TLDR**: DFA-RAG integrates a definite finite automaton with retrieval-augmented LLMs to enforce regulated and compliant responses in conversational agents.

## Abstract

This paper introduces the retrieval-augmented large language model with Definite Finite Automaton (DFA-RAG), a novel framework designed to enhance the capabilities of conversational agents using large language models (LLMs). Traditional LLMs face challenges in generating regulated and compliant responses in special scenarios with predetermined response guidelines, like emotional support and customer service. Our framework addresses these challenges by embedding a Definite Finite Automaton (DFA), learned from training dialogues, within the LLM. This structured approach acts as a semantic router which enables the LLM to adhere to a deterministic response pathway. The routing is achieved by the retrieval-augmentation generation (RAG) strategy, which carefully selects dialogue examples aligned with the current conversational context. The advantages of DFA-RAG include an interpretable structure through human-readable DFA, context-aware retrieval for responses in conversations, and plug-and-play compatibility with existing LLMs. Extensive benchmarks validate DFA-RAG’s effectiveness, indicating its potential as a valuable contribution to the conversational agent.