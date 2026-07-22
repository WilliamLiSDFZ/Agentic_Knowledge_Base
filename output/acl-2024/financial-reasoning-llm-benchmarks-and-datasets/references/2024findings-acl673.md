---
title: "Evaluating Mathematical Reasoning of Large Language Models: A Focus on Error Identification and Correction"
source: "https://aclanthology.org/2024.findings-acl.673/"
categories: ['llm-training-alignment-and-evaluation', 'financial-reasoning-llm-benchmarks-and-datasets']
tags: ['mathematical-reasoning', 'error-identification', 'llm-evaluation']
venue: "ACL 2024"
tldr: "Evaluates LLMs on mathematical reasoning by focusing on their ability to identify and correct errors rather than just solve problems."
---

# Evaluating Mathematical Reasoning of Large Language Models: A Focus on Error Identification and Correction

**Source**: [https://aclanthology.org/2024.findings-acl.673/](https://aclanthology.org/2024.findings-acl.673/)

**TLDR**: Evaluates LLMs on mathematical reasoning by focusing on their ability to identify and correct errors rather than just solve problems.

## Abstract

AbstractThe rapid advancement of Large Language Models (LLMs) in the realm of mathematical reasoning necessitates comprehensive evaluations to gauge progress and inspire future directions. Existing assessments predominantly focus on problem-solving from the examinee perspective, overlooking a dual perspective of examiner regarding error identification and correction. From the examiner perspective, we define four evaluation tasks for error identification and correction along with a new dataset with annotated error types and steps. We also design diverse prompts to thoroughly evaluate eleven representative LLMs. Our principal findings indicate that GPT-4 outperforms all models, while open-source model LLaMA-2-7B demonstrates comparable abilities to closed-source models GPT-3.5 and Gemini Pro. Notably, calculation error proves the most challenging error type. Moreover, prompting LLMs with the error types can improve the average correction accuracy by 47.9%. These results reveal potential directions for developing the mathematical reasoning abilities of LLMs. Our code and dataset is available on https://github.com/LittleCirc1e/EIC.