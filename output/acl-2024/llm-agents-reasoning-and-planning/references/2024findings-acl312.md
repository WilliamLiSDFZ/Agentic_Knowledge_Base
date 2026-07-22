---
title: "Se2: Sequential Example Selection for In-Context Learning"
source: "https://aclanthology.org/2024.findings-acl.312/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['in-context-learning', 'example-selection', 'sequential']
venue: "ACL 2024"
tldr: "A sequential example selection method for ICL jointly considers selection and ordering to improve LLM performance."
---

# Se2: Sequential Example Selection for In-Context Learning

**Source**: [https://aclanthology.org/2024.findings-acl.312/](https://aclanthology.org/2024.findings-acl.312/)

**TLDR**: A sequential example selection method for ICL jointly considers selection and ordering to improve LLM performance.

## Abstract

AbstractThe remarkable capability of large language models(LLMs) for in-context learning(ICL) needs to be activated by demonstration examples. Prior work has extensively explored the selection of examples for ICL, predominantly following the “select then organize” paradigm, such approaches often neglect the internal relationships between examples and exist an inconsistency between the training and inference. In this paper, we formulate the problem as a Sequential Selection problem and introduce Se2, a sequential-aware method that leverages the LLM’s feedback on varying context, aiding in capturing inter-relationships and sequential information among examples, significantly enriching the contextuality and relevance of ICL prompts. Meanwhile, we utilize beam search to seek and construct example sequences, enhancing both quality and diversity. Extensive experiments across 23 NLP tasks from 8 distinct categories illustrate that Se2 markedly surpasses competitive baselines and achieves 42% relative improvement over random selection. Further in-depth analysis shows the effectiveness of proposed strategies, highlighting Se2‘s exceptional stability and adaptability across various scenarios. Code available at https://github.com/microsoft/LMOps.