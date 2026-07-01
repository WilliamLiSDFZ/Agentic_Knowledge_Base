---
title: "CulturePark: Boosting Cross-cultural Understanding in Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/77f089cd16dbc36ddd1caeb18446fbdd-Abstract-Conference.html"
categories: ['llm-agent-communication-and-cooperation', 'llm-values-ethics-alignment-evaluation']
tags: ['cultural-bias', 'llm-agents', 'cross-cultural-data']
venue: "NeurIPS 2024"
tldr: "CulturePark uses LLM-based multi-agent communication to generate culturally diverse datasets that reduce cultural bias in large language models."
---

# CulturePark: Boosting Cross-cultural Understanding in Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/77f089cd16dbc36ddd1caeb18446fbdd-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/77f089cd16dbc36ddd1caeb18446fbdd-Abstract-Conference.html)

**TLDR**: CulturePark uses LLM-based multi-agent communication to generate culturally diverse datasets that reduce cultural bias in large language models.

## Abstract

Cultural bias is pervasive in many large language models (LLMs), largely due to the deficiency of data representative of different cultures.Typically, cultural datasets and benchmarks are constructed either by extracting subsets of existing datasets or by aggregating from platforms such as Wikipedia and social media.However, these approaches are highly dependent on real-world data and human annotations, making them costly and difficult to scale.Inspired by cognitive theories on social communication, this paper introduces CulturePark, an LLM-powered multi-agent communication framework for cultural data collection.CulturePark simulates cross-cultural human communication with LLM-based agents playing roles in different cultures.It generates high-quality cross-cultural dialogues encapsulating human beliefs, norms, and customs.Using CulturePark, we generated 41,000 cultural samples to fine-tune eight culture-specific LLMs.We evaluated these models across three downstream tasks: content moderation, cultural alignment, and cultural education.Results show that for content moderation, our GPT-3.5-based models either match or outperform GPT-4 on $41$ datasets. Regarding cultural alignment, our models surpass GPT-4 on Hofstede's VSM 13 framework.Furthermore, for cultural education of human participants, our models demonstrate superior outcomes in both learning efficacy and user experience compared to GPT-4. CulturePark proves an important step in addressing cultural bias and advancing the democratization of AI, highlighting the critical role of culturally inclusive data in model training. Code is released at https://github.com/Scarelette/CulturePark.