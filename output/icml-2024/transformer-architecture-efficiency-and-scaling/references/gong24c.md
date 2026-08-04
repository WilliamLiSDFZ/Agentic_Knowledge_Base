---
title: "AST-T5: Structure-Aware Pretraining for Code Generation and Understanding"
source: "https://proceedings.mlr.press/v235/gong24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gong24c/gong24c.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['code-generation', 'abstract-syntax-tree', 'pretraining']
venue: "ICML 2024"
tldr: "AST-T5 introduces a structure-aware pretraining paradigm leveraging abstract syntax trees to improve LLM performance on code generation and understanding tasks."
---

# AST-T5: Structure-Aware Pretraining for Code Generation and Understanding

**Source**: [https://proceedings.mlr.press/v235/gong24c.html](https://proceedings.mlr.press/v235/gong24c.html)

**TLDR**: AST-T5 introduces a structure-aware pretraining paradigm leveraging abstract syntax trees to improve LLM performance on code generation and understanding tasks.

## Abstract

Large language models (LLMs) have made significant advancements in code-related tasks, yet many LLMs treat code as simple sequences, neglecting its structured nature. We introduce AST-T5, a novel pretraining paradigm that leverages the Abstract Syntax Tree (AST) for enhanced code generation, transpilation, and understanding. Using dynamic programming, our AST-Aware Segmentation retains code structure, while our AST-Aware Span Corruption objective equips the model to reconstruct various code structures. Unlike other models, AST-T5 avoids complex program analyses or architectural changes, so it integrates seamlessly with any encoder-decoder Transformer. Evaluations show that AST-T5 consistently outperforms similar-sized LMs across various code-related tasks including HumanEval and MBPP. Structure-awareness makes AST-T5 particularly powerful in code-to-code tasks, surpassing CodeT5 by 2 points in exact match score for the Bugs2Fix task and by 3 points in exact match score for Java-C# Transpilation in CodeXGLUE. Our code and model are publicly available at https://github.com/gonglinyuan/ast_t5.