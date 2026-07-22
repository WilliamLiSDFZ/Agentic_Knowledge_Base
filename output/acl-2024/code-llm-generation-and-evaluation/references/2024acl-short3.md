---
title: "Revisiting Code Similarity Evaluation with Abstract Syntax Tree Edit Distance"
source: "https://aclanthology.org/2024.acl-short.3/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation', 'string-to-string-alignment-algorithms-library\n\nwait,-let-me-reconsider-for-conciseness-(3-7-words):\n\n`string-similarity-and-alignment-algorithms']
tags: ['code-similarity', 'abstract-syntax-tree', 'edit-distance', 'evaluation-metrics', 'programming-languages']
venue: "ACL 2024"
tldr: "Revisits code similarity evaluation by applying AST edit distance across diverse programming languages and comparing it to traditional sequence similarity metrics."
---

# Revisiting Code Similarity Evaluation with Abstract Syntax Tree Edit Distance

**Source**: [https://aclanthology.org/2024.acl-short.3/](https://aclanthology.org/2024.acl-short.3/)

**TLDR**: Revisits code similarity evaluation by applying AST edit distance across diverse programming languages and comparing it to traditional sequence similarity metrics.

## Abstract

AbstractThis paper revisits recent code similarity evaluation metrics, particularly focusing on the application of Abstract Syntax Tree (AST) editing distance in diverse programming languages. In particular, we explore the usefulness of these metrics and compare them to traditional sequence similarity metrics. Our experiments showcase the effectiveness of AST editing distance in capturing intricate code structures, revealing a high correlation with established metrics. Furthermore, we explore the strengths and weaknesses of AST editing distance and prompt-based GPT similarity scores in comparison to BLEU score, execution match, and Jaccard Similarity. We propose, optimize, and publish an adaptable metric that demonstrates effectiveness across all tested languages, representing an enhanced version of Tree Similarity of Edit Distance (TSED).