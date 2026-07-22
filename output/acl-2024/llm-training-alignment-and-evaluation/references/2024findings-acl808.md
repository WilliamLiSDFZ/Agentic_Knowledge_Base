---
title: "OOP: Object-Oriented Programming Evaluation Benchmark for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.808/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation', 'llm-training-alignment-and-evaluation']
tags: ['code-generation', 'object-oriented-programming', 'benchmark']
venue: "ACL 2024"
tldr: "OOP introduces a benchmark for evaluating LLMs on object-oriented programming tasks, addressing gaps in existing functional-programming-focused benchmarks."
---

# OOP: Object-Oriented Programming Evaluation Benchmark for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.808/](https://aclanthology.org/2024.findings-acl.808/)

**TLDR**: OOP introduces a benchmark for evaluating LLMs on object-oriented programming tasks, addressing gaps in existing functional-programming-focused benchmarks.

## Abstract

AbstractAdvancing automated programming necessitates robust and comprehensive code generation benchmarks, yet current evaluation frameworks largely neglect object-oriented programming (OOP) in favour of functional programming (FP), e.g., HumanEval and MBPP. To address this, our study introduces a pioneering OOP-focused benchmark, featuring 431 Python programs that encompass essential OOP concepts and features like classes and encapsulation methods. We propose a novel evaluation metric, pass@o, tailored for OOP, enhancing traditional pass@k metric. Our evaluation of 23 leading large language models (LLMs), including both general and code-specialized models, reveals three key insights: 1) pass@o offers a more relevant and comprehensive assessment for OOP code generation; 2) Despite excelling in FP, code-specialized LLMs like WizardCoder lag in OOP compared to models like ChatGPT; 3) The poor performance of all advanced LLMs on our OOP benchmark highlights a critical need for improvements in this field. Our benchmark and scripts will be publicly released at GitHub.