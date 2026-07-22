---
title: "KEEP CHATTING! An Attractive Dataset for Continuous Conversation Agents"
source: "https://aclanthology.org/2024.findings-acl.972/"
categories: ['emotion-aware-dialogue-and-empathy-systems', 'social-ai-temporal-dynamics-evaluation']
tags: ['conversational-agents', 'engagement', 'dataset']
venue: "ACL 2024"
tldr: "Introduces a dataset and task focused on training conversational agents to sustain user engagement in long-term ongoing chat interactions."
---

# KEEP CHATTING! An Attractive Dataset for Continuous Conversation Agents

**Source**: [https://aclanthology.org/2024.findings-acl.972/](https://aclanthology.org/2024.findings-acl.972/)

**TLDR**: Introduces a dataset and task focused on training conversational agents to sustain user engagement in long-term ongoing chat interactions.

## Abstract

AbstractOngoing chatting is an important step for conversational agents to build long-term connections with people. However, people tend to quickly lose interest in chatting if the conversational agent’s words are not engaging enough. In this paper, we present a novel task of increasing users’ willingness to continue talking to the agent.We collect a dataset named ContinuousChat by: (i) collecting personas and revising them, and then expanding the personas to detailed-personas through experiences, daily life, future plans, or interesting stories; (ii) expanding detailed-personas into the dialogues, and inject emotions and feelings into them; (iii) rewriting the dialogues in specific styles through few-shot prompt, conditioning on handwritten style-specific examples.We benchmark LLMs on ContinuousChat Dataset using both fine-tuning and in-context learning settings. Experiments over publicly available models demonstrate that although there is substantial room for improvement in generating style-specific dialogues, our ContinuousChat dataset is valuable in guiding conversational agents to generate more attractive dialogues and increase users’ willingness to continue the conversations.