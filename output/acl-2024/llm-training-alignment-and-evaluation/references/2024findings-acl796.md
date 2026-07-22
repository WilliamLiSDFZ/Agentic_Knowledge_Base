---
title: "Reinforcement Tuning for Detecting Stances and Debunking Rumors Jointly with Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.796/"
pdf_url: ""
categories: ['computational-misinformation-narrative-framing-detection', 'llm-training-alignment-and-evaluation']
tags: ['stance-detection', 'rumor-verification', 'multi-task-learning']
venue: "ACL 2024"
tldr: "Combines reinforcement tuning with LLMs to jointly detect stances and debunk rumors, addressing training data scarcity at multiple levels."
---

# Reinforcement Tuning for Detecting Stances and Debunking Rumors Jointly with Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.796/](https://aclanthology.org/2024.findings-acl.796/)

**TLDR**: Combines reinforcement tuning with LLMs to jointly detect stances and debunk rumors, addressing training data scarcity at multiple levels.

## Abstract

AbstractLearning multi-task models for jointly detecting stance and verifying rumors poses challenges due to the need for training data of stance at post level and rumor veracity at claim level, which are difficult to obtain. To address this issue, we leverage large language models (LLMs) as the foundation annotators for the joint stance detection (SD) and rumor verification (RV) tasks, dubbed as JSDRV. We introduce a novel reinforcement tuning framework to enhance the joint predictive capabilities of LLM-based SD and RV components. Specifically, we devise a policy for selecting LLM-annotated data at the two levels, employing a hybrid reward mechanism to choose high-quality labels for effective LLM fine-tuning on both tasks. Results demonstrate that JSDRV improves the capabilities of LLMs in the joint tasks, not only outperforming state-of-the-art methods but also generalizing to non-LLMs accommodated as task models.