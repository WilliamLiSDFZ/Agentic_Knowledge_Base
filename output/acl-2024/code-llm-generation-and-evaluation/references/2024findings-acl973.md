---
title: "RePair: Automated Program Repair with Process-based Feedback"
source: "https://aclanthology.org/2024.findings-acl.973/"
categories: ['code-llm-generation-and-evaluation']
tags: ['automated-program-repair', 'process-feedback', 'code-generation']
venue: "ACL 2024"
tldr: "RePair uses process-based feedback to guide automated program repair, improving robustness of LLM-based code fixing."
---

# RePair: Automated Program Repair with Process-based Feedback

**Source**: [https://aclanthology.org/2024.findings-acl.973/](https://aclanthology.org/2024.findings-acl.973/)

**TLDR**: RePair uses process-based feedback to guide automated program repair, improving robustness of LLM-based code fixing.

## Abstract

AbstractThe gap between the trepidation of program reliability and the expense of repairs underscore the indispensability for Automated Program Repair (APR). APR is instrumental in transforming vulnerable programs into more robust ones, bolstering program reliability while simultaneously diminishing the financial burden of manual repairs. Commercial-scale language models (LM) have taken APR to unprecedented levels. However, due to the limitations of model capabilities by parameters, a one-step substantial modification may not achieve the desired effect for models with parameters less than 100B. Moreover, humans interact with the LLM through explicit prompts, which hinders the LLM from receiving feedback from compiler and test cases to automatically optimize its repair policies. Explicit prompts from humans not only increase additional manpower costs, but also pose potential misunderstandings between human’s intent and LMs.Based on the above considerations, we are exploring how to ensure small-scale LM still outperform through process supervision and feedback. We start by constructing a dataset named CodeNet4Repair, replete with multiple repair records, which supervises the fine-tuning of a foundational mode. Building upon the encouraging outcomes of reinforcement learning, we develop a reward model that serves as a critic, providing feedback for the fine-tuned LM’s action, progressively optimizing its policy. During inference, we require the LM to generate solutions iteratively until the repair effect no longer improves or hits the maximum step limit. The experimental results show that this process-based feedback not only outperforms larger outcome-based generation methods, but also nearly matches the performance of closed-source commercial large-scale LMs.