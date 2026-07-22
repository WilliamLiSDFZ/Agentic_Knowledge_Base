---
title: "CHARP: Conversation History AwaReness Probing for Knowledge-grounded Dialogue Systems"
source: "https://aclanthology.org/2024.findings-acl.90/"
pdf_url: ""
categories: ['coreference-resolution-and-dialogue-understanding', 'llm-hallucination-detection-and-mitigation']
tags: ['dialogue', 'knowledge-grounded', 'annotation-artifacts', 'faithfulness', 'conversation-history']
venue: "ACL 2024"
tldr: "Reveals annotation artifacts in FaithDial that cause models to ignore conversation history in knowledge-grounded dialogue."
---

# CHARP: Conversation History AwaReness Probing for Knowledge-grounded Dialogue Systems

**Source**: [https://aclanthology.org/2024.findings-acl.90/](https://aclanthology.org/2024.findings-acl.90/)

**TLDR**: Reveals annotation artifacts in FaithDial that cause models to ignore conversation history in knowledge-grounded dialogue.

## Abstract

AbstractIn this work, we dive deep into one of the popular knowledge-grounded dialogue benchmarks that focus on faithfulness, FaithDial. We show that a significant portion of the FaithDial data contains annotation artifacts, which may bias models towards completely ignoring the conversation history. We therefore introduce CHARP, a testbed, designed for evaluating supposedly non-hallucinatory models trained on the FaithDial dataset. Our extensive analysis reveals that models primarily exhibit poor performance on CHARP due to their inability to effectively attend to and reason over the conversation history. Furthermore, the evaluation methods of FaithDial fail to capture these shortcomings, neglecting the conversational history. Our findings indicate that there is substantial room for contribution in both dataset creation and hallucination evaluation for knowledge-grounded dialogue, and that CHARP can serve as a tool for monitoring the progress in this particular research area. Data, models, and source code will be publicly available upon acceptance.