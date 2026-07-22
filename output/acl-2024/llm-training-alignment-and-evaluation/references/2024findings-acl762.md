---
title: "OpenCodeInterpreter: Integrating Code Generation with Execution and Refinement"
source: "https://aclanthology.org/2024.findings-acl.762/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation', 'llm-training-alignment-and-evaluation']
tags: ['code-generation', 'execution-feedback', 'iterative-refinement', 'open-source-llm']
venue: "ACL 2024"
tldr: "OpenCodeInterpreter is an open-source family of models that integrates code generation with execution feedback and iterative refinement to match GPT-4 Code Interpreter capabilities."
---

# OpenCodeInterpreter: Integrating Code Generation with Execution and Refinement

**Source**: [https://aclanthology.org/2024.findings-acl.762/](https://aclanthology.org/2024.findings-acl.762/)

**TLDR**: OpenCodeInterpreter is an open-source family of models that integrates code generation with execution feedback and iterative refinement to match GPT-4 Code Interpreter capabilities.

## Abstract

AbstractThe introduction of large language models has significantly advanced code generation. However, open-source models often lack the execution capabilities and iterative refinement of advanced systems like the GPT-4 Code Interpreter. To address this, we introduce OpenCodeInterpreter, a family of open-source code systems designed for generating, executing, and iteratively refining code. Supported by Code Feedback, a dataset featuring 68K multi-turn interactions, OpenCodeInterpreter integrates execution and human feedback for dynamic code refinement. Our comprehensive evaluation of OpenCodeInterpreter across key benchmarks such as HumanEval, MBPP, and their enhanced versions from EvalPlus reveals its exceptional performance. Notably, OpenCodeInterpreter-33B achieves an accuracy of 83.2 (76.4) on the average (and plus versions) of HumanEval and MBPP, closely rivaling GPT-4’s 84.2 (76.2) and further elevates to 91.6 (84.6) with synthesized human feedback from GPT-4. OpenCodeInterpreterbrings the gap between open-source code generation models and proprietary systems like GPT-4 Code Interpreter.