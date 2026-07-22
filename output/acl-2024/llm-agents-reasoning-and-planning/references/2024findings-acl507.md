---
title: "Bi-Chainer: Automated Large Language Models Reasoning with Bidirectional Chaining"
source: "https://aclanthology.org/2024.findings-acl.507/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'causal-reasoning-and-explanation-in-nlp']
tags: ['logical-reasoning', 'bidirectional-chaining', 'chain-of-thought']
venue: "ACL 2024"
tldr: "Bi-Chainer improves LLM reasoning on complex logical problems by combining forward and backward chaining in a bidirectional framework."
---

# Bi-Chainer: Automated Large Language Models Reasoning with Bidirectional Chaining

**Source**: [https://aclanthology.org/2024.findings-acl.507/](https://aclanthology.org/2024.findings-acl.507/)

**TLDR**: Bi-Chainer improves LLM reasoning on complex logical problems by combining forward and backward chaining in a bidirectional framework.

## Abstract

AbstractLarge Language Models (LLMs) have shown human-like reasoning abilities but still face challenges in solving complex logical problems. Existing unidirectional chaining methods, such as forward chaining and backward chaining, suffer from issues like low prediction accuracy and efficiency. To address these, we propose a bidirectional chaining method, Bi-Chainer, which dynamically switches to depth-first reasoning in the opposite reasoning direction when it encounters multiple branching options within the current direction. Thus, the intermediate reasoning results can be utilized as guidance to facilitate the reasoning process. We show that Bi-Chainer achieves sizable accuracy boots over unidirectional chaining frameworks on four challenging logical reasoning datasets. Moreover, Bi-Chainer enhances the accuracy of intermediate proof steps and reduces the average number of inference calls, resulting in more efficient and accurate reasoning.