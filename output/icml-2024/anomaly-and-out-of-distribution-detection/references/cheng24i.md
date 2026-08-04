---
title: "Can AI Assistants Know What They Don’t Know?"
source: "https://proceedings.mlr.press/v235/cheng24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheng24i/cheng24i.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'anomaly-and-out-of-distribution-detection']
tags: ['LLM-uncertainty', 'knowledge-awareness', 'open-domain-QA']
venue: "ICML 2024"
tldr: "A framework is proposed to enable AI assistants powered by LLMs to recognize and communicate the limits of their knowledge."
---

# Can AI Assistants Know What They Don’t Know?

**Source**: [https://proceedings.mlr.press/v235/cheng24i.html](https://proceedings.mlr.press/v235/cheng24i.html)

**TLDR**: A framework is proposed to enable AI assistants powered by LLMs to recognize and communicate the limits of their knowledge.

## Abstract

AI assistants powered by Large Language Models (LLMs) have demonstrated impressive performance in various tasks. However, LLMs still make factual errors in knowledge-intensive tasks such as open-domain question answering. These untruthful responses from AI assistants can pose significant risks in practical applications. Therefore, in this paper, we ask the question Can AI assistants know what they don’t know and express this awareness through natural language? To investigate this, we construct a model-specific "I don’t know" (Idk) dataset. This dataset includes Supervised Fine-tuning data and preference data, categorizing questions based on whether the assistant knows or does not know the answers. Then, we align the assistant with its corresponding Idk dataset using different alignment methods, including Supervised Fine-tuning and preference optimization. Experimental results show that, after alignment with the Idk dataset, the assistant is more capable of declining to answer questions outside its knowledge scope. The assistant aligned with the Idk dataset shows significantly higher truthfulness than the original assistant.