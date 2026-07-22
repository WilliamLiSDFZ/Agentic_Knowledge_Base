---
title: "Pearl: A Review-driven Persona-Knowledge Grounded Conversational Recommendation Dataset"
source: "https://aclanthology.org/2024.findings-acl.65/"
categories: ['llm-based-ranking-and-recommendation']
tags: ['conversational-recommendation', 'persona', 'knowledge-grounded']
venue: "ACL 2024"
tldr: "Presents Pearl, a review-driven persona-knowledge grounded dataset for conversational recommender systems."
---

# Pearl: A Review-driven Persona-Knowledge Grounded Conversational Recommendation Dataset

**Source**: [https://aclanthology.org/2024.findings-acl.65/](https://aclanthology.org/2024.findings-acl.65/)

**TLDR**: Presents Pearl, a review-driven persona-knowledge grounded dataset for conversational recommender systems.

## Abstract

AbstractConversational recommender systems are an emerging area that has garnered increasing interest in the community, especially with the advancements in large language models (LLMs) that enable sophisticated handling of conversational input. Despite the progress, the field still has many aspects left to explore. The currently available public datasets for conversational recommendation lack specific user preferences and explanations for recommendations, hindering high-quality recommendations. To address such challenges, we present a novel conversational recommendation dataset named PEARL, synthesized with persona- and knowledge-augmented LLM simulators. We obtain detailed persona and knowledge from real-world reviews and construct a large-scale dataset with over 57k dialogues. Our experimental results demonstrate that PEARL contains more specific user preferences, show expertise in the target domain, and provides recommendations more relevant to the dialogue context than those in prior datasets. Furthermore, we demonstrate the utility of PEARL by showing that our downstream models outperform baselines in both human and automatic evaluations. We release our dataset and code.