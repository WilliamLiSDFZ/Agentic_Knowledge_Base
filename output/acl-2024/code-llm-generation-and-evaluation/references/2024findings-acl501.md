---
title: "StudentEval: A Benchmark of Student-Written Prompts for Large Language Models of Code"
source: "https://aclanthology.org/2024.findings-acl.501/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation', 'llm-training-alignment-and-evaluation']
tags: ['code-llm', 'student-prompts', 'benchmark']
venue: "ACL 2024"
tldr: "Presents StudentEval, a benchmark of non-expert student-written prompts to evaluate code LLMs beyond expert-written test cases."
---

# StudentEval: A Benchmark of Student-Written Prompts for Large Language Models of Code

**Source**: [https://aclanthology.org/2024.findings-acl.501/](https://aclanthology.org/2024.findings-acl.501/)

**TLDR**: Presents StudentEval, a benchmark of non-expert student-written prompts to evaluate code LLMs beyond expert-written test cases.

## Abstract

AbstractCode LLMs have the potential to make it easier for non-experts to understand and write code. However, current CodeLLM benchmarks rely on a single expert-written prompt per problem, making it hard to generalize their success to non-expert users. In this paper, we present a new natural-language-to-code benchmark of prompts written by a key population of non-experts: beginning programmers. StudentEval contains 1,749 prompts written by 80 students who have only completed one introductory Python course. StudentEval contains numerous non-expert prompts describing the same problem, enabling exploration of key factors in prompt success. We use StudentEval to evaluate 12 Code LLMs and find that StudentEval is a better discriminator of model performance than existing benchmarks. Our analysis of student prompting strategies reveals that nondeterministic LLM sampling can mislead students about the quality of their descriptions, a finding with key implications for Code LLMs in education.