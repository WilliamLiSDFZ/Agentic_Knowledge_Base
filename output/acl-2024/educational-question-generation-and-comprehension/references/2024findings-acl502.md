---
title: "ProLex: A Benchmark for Language Proficiency-oriented Lexical Substitution"
source: "https://aclanthology.org/2024.findings-acl.502/"
categories: ['text-simplification-evaluation-and-methods', 'educational-question-generation-and-comprehension']
tags: ['lexical-substitution', 'language-proficiency', 'benchmark']
venue: "ACL 2024"
tldr: "ProLex is a benchmark for proficiency-oriented lexical substitution aimed at supporting language learners in improving vocabulary."
---

# ProLex: A Benchmark for Language Proficiency-oriented Lexical Substitution

**Source**: [https://aclanthology.org/2024.findings-acl.502/](https://aclanthology.org/2024.findings-acl.502/)

**TLDR**: ProLex is a benchmark for proficiency-oriented lexical substitution aimed at supporting language learners in improving vocabulary.

## Abstract

AbstractLexical Substitution discovers appropriate substitutes for a given target word in a context sentence. However, the task fails to consider substitutes that are of equal or higher proficiency than the target, an aspect that could be beneficial for language learners looking to improve their writing. To bridge this gap, we propose a new task — language proficiency-oriented lexical substitution. We also introduce ProLex, a novel benchmark designed to assess systems’ ability to generate not only appropriate substitutes but also substitutes that demonstrate better language proficiency. Besides the benchmark, we propose models that can automatically perform the new task. We show that our best model, a Llama2-13B model fine-tuned with task-specific synthetic data, outperforms ChatGPT by an average of 3.2% in F-score and achieves comparable results with GPT-4 on ProLex.