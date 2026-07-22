---
title: "Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step"
source: "https://aclanthology.org/2024.findings-acl.49/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['code-debugging', 'llm-agents', 'runtime-execution-verification']
venue: "ACL 2024"
tldr: "Presents an LLM-based debugger that verifies runtime execution step-by-step to iteratively fix generated code like a human debugger."
---

# Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step

**Source**: [https://aclanthology.org/2024.findings-acl.49/](https://aclanthology.org/2024.findings-acl.49/)

**TLDR**: Presents an LLM-based debugger that verifies runtime execution step-by-step to iteratively fix generated code like a human debugger.

## Abstract

AbstractLarge language models (LLMs) are leading significant progress in code generation. Beyond one-pass code generation, recent works further integrate unit tests and program verifiers into LLMs to iteratively refine the generated programs. However, these works consider the generated programs as an indivisible entity, which falls short for LLMs in debugging the programs, especially when the programs contain complex logic flows and data operations. In contrast, when human developers debug programs, they typically set breakpoints and selectively examine runtime execution information. The execution flow and the intermediate variables play a crucial role in the debugging process, yet they are underutilized in the existing literature on code generation. In this study, we introduce Large Language Model Debugger (LDB), a novel debugging framework that enables LLMs to refine their generated programs with the runtime execution information. Specifically, LDB segments the programs into basic blocks and tracks the values of intermediate variables after each block throughout the runtime execution. This allows LLMs to concentrate on simpler code units within the overall execution flow, verify their correctness against the task description block by block, and efficiently pinpoint any potential errors. Experiments demonstrate that LDB consistently enhances the baseline performance by up to 9.8% across the HumanEval, MBPP, and TransCoder benchmarks, archiving new state-of-the-art performance in code debugging for various LLM selections.