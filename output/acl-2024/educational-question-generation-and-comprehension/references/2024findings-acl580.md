---
title: "Automated Focused Feedback Generation for Scientific Writing Assistance"
source: "https://aclanthology.org/2024.findings-acl.580/"
pdf_url: ""
categories: ['educational-question-generation-and-comprehension', 'llm-training-alignment-and-evaluation']
tags: ['scientific-writing', 'automated-feedback', 'peer-review']
venue: "ACL 2024"
tldr: "Introduces an automated system for generating focused, content-level feedback to assist novice researchers in improving scientific manuscripts."
---

# Automated Focused Feedback Generation for Scientific Writing Assistance

**Source**: [https://aclanthology.org/2024.findings-acl.580/](https://aclanthology.org/2024.findings-acl.580/)

**TLDR**: Introduces an automated system for generating focused, content-level feedback to assist novice researchers in improving scientific manuscripts.

## Abstract

AbstractScientific writing is a challenging task, particularly for novice researchers who often rely on feedback from experienced peers. Recent work has primarily focused on improving surface form and style rather than manuscript content. In this paper, we propose a novel task: automated focused feedback generation for scientific writing assistance. We present SWIF2T: a Scientific WrIting Focused Feedback Tool. It is designed to generate specific, actionable and coherent comments, which identify weaknesses in a scientific paper and/or propose revisions to it. Our approach consists of four components - planner, investigator, reviewer and controller - leveraging multiple Large Language Models (LLMs) to implement them. We compile a dataset of 300 peer reviews citing weaknesses in scientific papers and conduct human evaluation. The results demonstrate the superiority in specificity, reading comprehension, and overall helpfulness of SWIF2T’s feedback compared to other approaches. In our analysis, we also identified cases where automatically generated reviews were judged better than human ones, suggesting opportunities for integration of AI-generated feedback in scientific writing.