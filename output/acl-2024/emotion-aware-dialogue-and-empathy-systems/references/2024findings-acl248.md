---
title: "POP-CEE: Position-oriented Prompt-tuning Model for Causal Emotion Entailment"
source: "https://aclanthology.org/2024.findings-acl.248/"
pdf_url: ""
categories: ['emotion-aware-dialogue-and-empathy-systems', 'causal-reasoning-and-explanation-in-nlp']
tags: ['causal-emotion-entailment', 'prompt-tuning', 'conversation', 'emotion-cause', 'position-aware']
venue: "ACL 2024"
tldr: "Introduces a position-oriented prompt-tuning model to identify causes of emotional utterances in conversations."
---

# POP-CEE: Position-oriented Prompt-tuning Model for Causal Emotion Entailment

**Source**: [https://aclanthology.org/2024.findings-acl.248/](https://aclanthology.org/2024.findings-acl.248/)

**TLDR**: Introduces a position-oriented prompt-tuning model to identify causes of emotional utterances in conversations.

## Abstract

AbstractThe objective of the Causal Emotion Entailment (CEE) task is to identify the causes of the target emotional utterances in a given conversation. Most existing studies have focused on a fine-tuning paradigm based on a pretrained model, e.g., the BERT model. However, there are gaps between the pretrained task and the CEE task. Although a pretrained model enhances contextual comprehension to some extent, it cannot acquire specific knowledge that is relevant to the CEE task. In addition, in a typical CEE task, there are peculiarities in the distribution of the positions with different emotion types of emotion utterances and cause utterances in conversations. Existing methods employ a fixed-size window to capture the relationship between neighboring conversations; however, these methods ignore the specific semantic associations between emotions and cause utterances. To address these issues, we propose the Position-oriented Prompt-tuning (POP-CEE) model to solve the CEE task in an end-to-end manner. Specifically, we can model the CEE task by designing prompts with multiple unified goals and by exploring the positional relationship between emotion and cause utterances using a position constraint module. Experimental results demonstrate that the proposed POP-CEE model achieves state-of-the-art performance on a benchmark dataset. Ourcode and data can be found at: https://github.com/Zh0uzh/POP-CEE.