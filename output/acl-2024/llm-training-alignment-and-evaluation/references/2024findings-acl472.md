---
title: "LLMCrit: Teaching Large Language Models to Use Criteria"
source: "https://aclanthology.org/2024.findings-acl.472/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['criteria-following', 'feedback', 'LLM-evaluation', 'instruction']
venue: "ACL 2024"
tldr: "LLMCrit teaches large language models to use explicit criteria for providing structured feedback on task completion quality."
---

# LLMCrit: Teaching Large Language Models to Use Criteria

**Source**: [https://aclanthology.org/2024.findings-acl.472/](https://aclanthology.org/2024.findings-acl.472/)

**TLDR**: LLMCrit teaches large language models to use explicit criteria for providing structured feedback on task completion quality.

## Abstract

AbstractHumans follow criteria when they execute tasks, and these criteria are directly used to assess the quality of task completion. Therefore, having models learn to use criteria to provide feedback can help humans or models to perform tasks better. However, current research in this area tends to consider only a limited number of criteria, or only a limited number of quality assessment aspects. To fill this gap, we propose a general framework that enables large language models (LLMs) to use comprehensive criteria for a task in delivering natural language feedback on task execution. In particular, we present a model-in-the-loop framework that semi-automatically derives criteria from collected guidelines for different writing tasks and constructs in-context demonstrations for each criterion. We choose three tasks from real-world scenarios to operationalize this idea: paper introduction writing, Python code writing, and Reddit post writing, and evaluate our feedback generation framework using different LLMs. The results reveal the fine-grained effects of adding criteria and demonstrations and provide valuable guidance on how to teach LLMs to use criteria more effectively.