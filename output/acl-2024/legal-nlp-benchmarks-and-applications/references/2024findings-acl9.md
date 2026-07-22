---
title: "Which Side Are You On? A Multi-task Dataset for End-to-End Argument Summarisation and Evaluation"
source: "https://aclanthology.org/2024.findings-acl.9/"
categories: ['causal-reasoning-and-explanation-in-nlp', 'legal-nlp-benchmarks-and-applications']
tags: ['argument-mining', 'summarization', 'debate', 'multi-task']
venue: "ACL 2024"
tldr: "Presents a multi-task dataset for end-to-end argument summarization and evaluation to support automated debate systems using large language models."
---

# Which Side Are You On? A Multi-task Dataset for End-to-End Argument Summarisation and Evaluation

**Source**: [https://aclanthology.org/2024.findings-acl.9/](https://aclanthology.org/2024.findings-acl.9/)

**TLDR**: Presents a multi-task dataset for end-to-end argument summarization and evaluation to support automated debate systems using large language models.

## Abstract

AbstractWith the recent advances of large language models (LLMs), it is no longer infeasible to build an automated debate system that helps people to synthesise persuasive arguments. Previous work attempted this task by integrating multiple components. In our work, we introduce an argument mining dataset that captures the end-to-end process of preparing an argumentative essay for a debate, which covers the tasks of claim and evidence identification (Task 1 ED), evidence convincingness ranking (Task 2 ECR), argumentative essay summarisation and human preference ranking (Task 3 ASR) and metric learning for automated evaluation of resulting essays, based on human feedback along argument quality dimensions (Task 4 SQE). Our dataset contains 14k examples of claims that are fully annotated with various properties supporting the aforementioned tasks. We evaluate multiple generative baselines for each of these tasks, including representative LLMs. We find, that while they show promising results on individual tasks in our benchmark, their end-to-end performance on all four tasks in succession deteriorates significantly, both in automated measures as well as in human-centred evaluation. This challenge presented by our proposed dataset motivates future research on end-to-end argument mining and summarisation. The repository of this project is available at https://github.com/HarrywillDr/ArgSum-Datatset.