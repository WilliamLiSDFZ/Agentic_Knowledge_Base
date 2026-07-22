---
title: "TOREE: Evaluating Topic Relevance of Student Essays for Chinese Primary and Middle School Education"
source: "https://aclanthology.org/2024.findings-acl.342/"
categories: ['topic-modeling-and-essay-evaluation']
tags: ['essay-scoring', 'topic-relevance', 'chinese-education']
venue: "ACL 2024"
tldr: "Introduces TOREE, a benchmark for evaluating topic relevance of student essays in Chinese primary and middle school education."
---

# TOREE: Evaluating Topic Relevance of Student Essays for Chinese Primary and Middle School Education

**Source**: [https://aclanthology.org/2024.findings-acl.342/](https://aclanthology.org/2024.findings-acl.342/)

**TLDR**: Introduces TOREE, a benchmark for evaluating topic relevance of student essays in Chinese primary and middle school education.

## Abstract

AbstractTopic relevance of an essay demands that the composition adheres to a clear theme and aligns well with the essay prompt requirements, a critical aspect of essay quality evaluation. However, existing research of Automatic Essay Scoring (AES) for Chinese essays has overlooked topic relevance and lacks detailed feedback, while Automatic Essay Comment Generation (AECG) faces much complexity and difficulty. Additionally, current Large Language Models, including GPT-4, often make incorrect judgments and provide overly impractical feedback when evaluating topic relevance. This paper introduces TOREE (Topic Relevance Evaluation), a comprehensive dataset developed to assess topic relevance in Chinese primary and middle school students’ essays, which is beneficial for AES, AECG and other applications. Moreover, our proposed two-step method utilizes TOREE through a combination of Supervised Fine-tuning and Preference Learning. Experimental results demonstrate that TOREE is of high quality, and our method significantly enhances models’ performance on two designed tasks for topic relevance evaluation, improving both automatic and human evaluations across four diverse LLMs.