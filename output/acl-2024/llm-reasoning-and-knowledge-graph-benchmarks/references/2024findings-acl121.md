---
title: "The Knowledge Alignment Problem: Bridging Human and External Knowledge for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.121/"
categories: ['llm-hallucination-detection-and-mitigation', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['knowledge-alignment', 'hallucination', 'grounding']
venue: "ACL 2024"
tldr: "Identifies and addresses the knowledge alignment problem where LLMs ignore correct external groundings and hallucinate due to user-LLM knowledge gaps."
---

# The Knowledge Alignment Problem: Bridging Human and External Knowledge for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.121/](https://aclanthology.org/2024.findings-acl.121/)

**TLDR**: Identifies and addresses the knowledge alignment problem where LLMs ignore correct external groundings and hallucinate due to user-LLM knowledge gaps.

## Abstract

AbstractLarge language models often necessitate grounding on external knowledge to generate faithful and reliable answers. Yet even with the correct groundings in the reference, they can ignore them and rely on wrong groundings or their inherent biases to hallucinate when users, being largely unaware of the specifics of the stored information, pose questions that might not directly correlate with the retrieved groundings. In this work, we formulate this knowledge alignment problem and introduce MixAlign, a framework that interacts with both the human user and the knowledge base to obtain and integrate clarifications on how the user question relates to the stored information. MixAlign employs a language model to achieve automatic knowledge alignment and, if necessary, further enhances this alignment through human user clarifications. Experimental results highlight the crucial role of knowledge alignment in boosting model performance and mitigating hallucination, with improvements noted up to 22.2% and 27.1% respectively. We also demonstrate the effectiveness of MixAlign in improving knowledge alignment by producing high-quality, user-centered clarifications.