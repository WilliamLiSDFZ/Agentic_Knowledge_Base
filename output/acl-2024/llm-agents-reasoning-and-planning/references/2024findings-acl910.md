---
title: "SAGA: A Participant-specific Examination of Story Alternatives and Goal Applicability for a Deeper Understanding of Complex Events"
source: "https://aclanthology.org/2024.findings-acl.910/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'causal-reasoning-and-explanation-in-nlp']
tags: ['complex-events', 'goal-reasoning', 'story-understanding']
venue: "ACL 2024"
tldr: "SAGA is a benchmark for participant-specific reasoning over goals and story alternatives in complex event understanding."
---

# SAGA: A Participant-specific Examination of Story Alternatives and Goal Applicability for a Deeper Understanding of Complex Events

**Source**: [https://aclanthology.org/2024.findings-acl.910/](https://aclanthology.org/2024.findings-acl.910/)

**TLDR**: SAGA is a benchmark for participant-specific reasoning over goals and story alternatives in complex event understanding.

## Abstract

AbstractInterpreting and assessing goal driven actions is vital to understanding and reasoning over complex events. It is important to be able to acquire the knowledge needed for this understanding, though doing so is challenging. We argue that such knowledge can be elicited through a participant achievement lens. We analyze a complex event in a narrative according to the intended achievements of the participants in that narrative, the likely future actions of the participants, and the likelihood of goal success. We collect 6.3K high quality goal and action annotations reflecting our proposed participant achievement lens, with an average weighted Fleiss-Kappa IAA of 80%. Our collection contains annotated alternate versions of each narrative. These alternate versions vary minimally from the “original” story, but can license drastically different inferences. Our findings suggest that while modern large language models can reflect some of the goal-based knowledge we study, they find it challenging to fully capture the design and intent behind concerted actions, even when the model pretraining included the data from which we extracted the goal knowledge. We show that smaller models fine-tuned on our dataset can achieve performance surpassing larger models.