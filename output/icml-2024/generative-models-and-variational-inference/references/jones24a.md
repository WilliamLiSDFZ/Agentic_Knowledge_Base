---
title: "Learning to Infer Generative Template Programs for Visual Concepts"
source: "https://proceedings.mlr.press/v235/jones24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jones24a/jones24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'generative-models-and-variational-inference']
tags: ['neurosymbolic', 'program-synthesis', 'visual-concepts', 'few-shot-learning']
venue: "ICML 2024"
tldr: "A neurosymbolic system learns to infer template programs from domain-specific languages to represent flexible visual concepts from few examples."
---

# Learning to Infer Generative Template Programs for Visual Concepts

**Source**: [https://proceedings.mlr.press/v235/jones24a.html](https://proceedings.mlr.press/v235/jones24a.html)

**TLDR**: A neurosymbolic system learns to infer template programs from domain-specific languages to represent flexible visual concepts from few examples.

## Abstract

People grasp flexible visual concepts from a few examples. We explore a neurosymbolic system that learns how to infer programs that capture visual concepts in a domain-general fashion. We introduce Template Programs: programmatic expressions from a domain-specific language that specify structural and parametric patterns common to an input concept. Our framework supports multiple concept-related tasks, including few-shot generation and co-segmentation through parsing. We develop a learning paradigm that allows us to train networks that infer Template Programs directly from visual datasets that contain concept groupings. We run experiments across multiple visual domains: 2D layouts, Omniglot characters, and 3D shapes. We find that our method outperforms task-specific alternatives, and performs competitively against domain-specific approaches for the limited domains where they exist.