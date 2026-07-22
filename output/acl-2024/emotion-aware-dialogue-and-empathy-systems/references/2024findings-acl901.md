---
title: "NoteChat: A Dataset of Synthetic Patient-Physician Conversations Conditioned on Clinical Notes"
source: "https://aclanthology.org/2024.findings-acl.901/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'emotion-aware-dialogue-and-empathy-systems']
tags: ['patient-physician-dialogue', 'multi-agent-llm', 'clinical-notes']
venue: "ACL 2024"
tldr: "A cooperative multi-agent LLM framework generates synthetic patient-physician dialogues conditioned on clinical notes."
---

# NoteChat: A Dataset of Synthetic Patient-Physician Conversations Conditioned on Clinical Notes

**Source**: [https://aclanthology.org/2024.findings-acl.901/](https://aclanthology.org/2024.findings-acl.901/)

**TLDR**: A cooperative multi-agent LLM framework generates synthetic patient-physician dialogues conditioned on clinical notes.

## Abstract

AbstractWe introduce NoteChat, a novel cooperative multi-agent framework leveraging Large Language Models (LLMs) to generate patient-physician dialogues. NoteChat embodies the principle that an ensemble of role-specific LLMs, through structured role-play and strategic prompting, can perform their assigned roles more effectively. The synergy among these role-playing LLMs results in a cohesive and efficient dialogue generation. Evaluation on MTS-dialogue, a benchmark dataset for patient-physician dialogues-note pairs, shows that models trained with the augmented synthetic patient-physician dialogues by NoteChat outperforms other state-of-the-art models for generating clinical notes. Our comprehensive automatic and human evaluation demonstrates that NoteChat substantially surpasses state-of-the-art models like ChatGPT and GPT-4 up to 22.78% by domain experts in generating superior synthetic patient-physician dialogues based on clinical notes. NoteChat has the potential to engage patients directly and help clinical documentation, a leading cause of physician burnout.