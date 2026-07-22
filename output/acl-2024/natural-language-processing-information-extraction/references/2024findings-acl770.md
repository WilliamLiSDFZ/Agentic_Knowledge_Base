---
title: "KIWI: A Dataset of Knowledge-Intensive Writing Instructions for Answering Research Questions"
source: "https://aclanthology.org/2024.findings-acl.770/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'natural-language-processing-information-extraction']
tags: ['knowledge-intensive', 'writing-instructions', 'long-form-answers', 'research-questions', 'instruction-following']
venue: "ACL 2024"
tldr: "Introduces KIWI, a benchmark dataset for evaluating LLMs on knowledge-intensive long-form writing tasks answering research questions."
---

# KIWI: A Dataset of Knowledge-Intensive Writing Instructions for Answering Research Questions

**Source**: [https://aclanthology.org/2024.findings-acl.770/](https://aclanthology.org/2024.findings-acl.770/)

**TLDR**: Introduces KIWI, a benchmark dataset for evaluating LLMs on knowledge-intensive long-form writing tasks answering research questions.

## Abstract

AbstractLarge language models (LLMs) adapted to follow user instructions are now widely deployed as conversational agents. In this work, we examine one increasingly common instruction-following task: providing writing assistance to compose a long-form answer. To evaluate the capabilities of current LLMs on this task, we construct KIWI, a dataset of knowledge-intensive writing instructions in the scientific domain. Given a research question, an initial model-generated answer and a set of relevant papers, an expert annotator iteratively issues instructions for the model to revise and improve its answer. We collect 1,260 interaction turns from 234 interaction sessions with three state-of-the-art LLMs. Each turn includes a user instruction, a model response, and a human evaluation of the model response. Through a detailed analysis of the collected responses, we find that all models struggle to incorporate new information into an existing answer, and to perform precise and unambiguous edits. Further, we find that models struggle to judge whether their outputs successfully followed user instructions, with accuracy at least 10 points short of human agreement. Our findings indicate that KIWI will be a valuable resource to measure progress and improve LLMs’ instruction-following capabilities for knowledge intensive writing tasks.