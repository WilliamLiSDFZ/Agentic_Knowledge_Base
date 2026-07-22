---
title: "PARADISE: Evaluating Implicit Planning Skills of Language Models with Procedural Warnings and Tips Dataset"
source: "https://aclanthology.org/2024.findings-acl.599/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'llm-assisted-structured-procedure-analysis']
tags: ['implicit-planning', 'procedural-knowledge', 'language-model-evaluation']
venue: "ACL 2024"
tldr: "PARADISE evaluates LLMs' implicit planning skills using a procedural warnings and tips dataset with linguistic complexity."
---

# PARADISE: Evaluating Implicit Planning Skills of Language Models with Procedural Warnings and Tips Dataset

**Source**: [https://aclanthology.org/2024.findings-acl.599/](https://aclanthology.org/2024.findings-acl.599/)

**TLDR**: PARADISE evaluates LLMs' implicit planning skills using a procedural warnings and tips dataset with linguistic complexity.

## Abstract

AbstractRecently, there has been growing interest within the community regarding whether large language models are capable of planning or executing plans. However, most prior studies use LLMs to generate high-level plans for simplified scenarios lacking linguistic complexity and domain diversity, limiting analysis of their planning abilities. These setups constrain evaluation methods (e.g., predefined action space), architectural choices (e.g., only generative models), and overlook the linguistic nuances essential for realistic analysis. To tackle this, we present PARADISE, an abductive reasoning task using Q&A format on practical procedural text sourced from wikiHow. It involves tip and warning inference tasks directly associated with goals, excluding intermediary steps, with the aim of testing the ability of the models to infer implicit knowledge of the plan solely from the given goal. Our experiments, utilizing fine-tuned language models and zero-shot prompting, reveal the effectiveness of task-specific small models over large language models in most scenarios. Despite advancements, all models fall short of human performance. Notably, our analysis uncovers intriguing insights, such as variations in model behavior with dropped keywords, struggles of BERT-family and GPT-4 with physical and abstract goals, and the proposed tasks offering valuable prior knowledge for other unseen procedural tasks. The PARADISE dataset and associated resources are publicly available for further research exploration with https://anonymous.4open.science/r/paradise-53BD/README.md.