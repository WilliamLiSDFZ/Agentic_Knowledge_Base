---
title: "Persuading across Diverse Domains: a Dataset and Persuasion Large Language Model"
source: "https://aclanthology.org/2024.acl-long.92/"
pdf_url: ""
categories: ['emotion-aware-dialogue-and-empathy-systems', 'llm-training-alignment-and-evaluation']
tags: ['persuasion', 'dialogue', 'multi-domain', 'dataset', 'LLM']
venue: "ACL 2024"
tldr: "Introduces a multi-domain persuasive dialogue dataset and model to improve LLMs' persuasion capabilities across diverse domains."
---

# Persuading across Diverse Domains: a Dataset and Persuasion Large Language Model

**Source**: [https://aclanthology.org/2024.acl-long.92/](https://aclanthology.org/2024.acl-long.92/)

**TLDR**: Introduces a multi-domain persuasive dialogue dataset and model to improve LLMs' persuasion capabilities across diverse domains.

## Abstract

AbstractPersuasive dialogue requires multi-turn following and planning abilities to achieve the goal of persuading users, which is still challenging even for state-of-the-art large language models (LLMs). Previous works focus on retrieval-based models or generative models in a specific domain due to a lack of data across multiple domains. In this paper, we leverage GPT-4 to create the first multi-domain persuasive dialogue dataset DailyPersuasion. Then we propose a general method named PersuGPT to learn a persuasion model based on LLMs through intent-to-strategy reasoning, which summarizes the intent of user’s utterance and reasons next strategy to respond. Moreover, we design a simulation-based preference optimization, which utilizes a learned user model and our model to simulate next turns and estimate their rewards more accurately. Experimental results on two datasets indicate that our proposed method outperforms all baselines in terms of automatic evaluation metric Win-Rate and human evaluation. The code and data are available at https://persugpt.github.io.