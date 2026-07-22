---
title: "Iterative Refinement of Project-Level Code Context for Precise Code Generation with Compiler Feedback"
source: "https://aclanthology.org/2024.findings-acl.138/"
categories: ['code-llm-generation-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['code-generation', 'compiler-feedback', 'project-context']
venue: "ACL 2024"
tldr: "Presents an iterative refinement approach that incorporates project-level code context and compiler feedback to improve LLM-based code generation accuracy."
---

# Iterative Refinement of Project-Level Code Context for Precise Code Generation with Compiler Feedback

**Source**: [https://aclanthology.org/2024.findings-acl.138/](https://aclanthology.org/2024.findings-acl.138/)

**TLDR**: Presents an iterative refinement approach that incorporates project-level code context and compiler feedback to improve LLM-based code generation accuracy.

## Abstract

AbstractLarge Language Models (LLMs) have shown remarkable progress in automated code generation. Yet, LLM-generated code may contain errors in API usage, class, data structure, or missing project-specific information. As much of this project-specific context cannot fit into the prompts of LLMs, we must find ways to allow the model to explore the project-level code context. We present CoCoGen, a new code generation approach that uses compiler feedback to improve the LLM-generated code. CoCoGen first leverages static analysis to identify mismatches between the generated code and the project’s context. It then iteratively aligns and fixes the identified errors using information extracted from the code repository. We integrate CoCoGen with two representative LLMs, i.e., GPT-3.5-Turbo and Code Llama (13B), and apply it to Python code generation. Experimental results show that CoCoGen significantly improves the vanilla LLMs by over 80% in generating code dependent on the project context and consistently outperforms the existing retrieval-based code generation baselines.