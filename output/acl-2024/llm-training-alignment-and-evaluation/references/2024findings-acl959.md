---
title: "Selective Prompting Tuning for Personalized Conversations with LLMs"
source: "https://aclanthology.org/2024.findings-acl.959/"
categories: ['llm-training-alignment-and-evaluation', 'emotion-aware-dialogue-and-empathy-systems']
tags: ['personalized-dialogue', 'persona', 'prompt-tuning', 'conversational-ai', 'llm']
venue: "ACL 2024"
tldr: "Proposes selective prompt tuning to improve persona integration for personalized conversations with large language models."
---

# Selective Prompting Tuning for Personalized Conversations with LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.959/](https://aclanthology.org/2024.findings-acl.959/)

**TLDR**: Proposes selective prompt tuning to improve persona integration for personalized conversations with large language models.

## Abstract

AbstractIn conversational AI, personalizing dialogues with persona profiles and contextual understanding is essential. Despite large language models’ (LLMs) improved response coherence, effective persona integration remains a challenge. In this work, we first study two common approaches for personalizing LLMs: textual prompting and direct fine-tuning. We observed that textual prompting often struggles to yield responses that are similar to the ground truths in datasets, while direct fine-tuning tends to produce repetitive or overly generic replies. To alleviate those issues, we propose **S**elective **P**rompt **T**uning (SPT), which softly prompts LLMs for personalized conversations in a selective way. Concretely, SPT initializes a set of soft prompts and uses a trainable dense retriever to adaptively select suitable soft prompts for LLMs according to different input contexts, where the prompt retriever is dynamically updated through feedback from the LLMs. Additionally, we propose context-prompt contrastive learning and prompt fusion learning to encourage the SPT to enhance the diversity of personalized conversations. Experiments on the CONVAI2 dataset demonstrate that SPT significantly enhances response diversity by up to 90%, along with improvements in other critical performance indicators. Those results highlight the efficacy of SPT in fostering engaging and personalized dialogue generation. The SPT model code is [publicly available](https://github.com/hqsiswiliam/SPT) for further exploration.