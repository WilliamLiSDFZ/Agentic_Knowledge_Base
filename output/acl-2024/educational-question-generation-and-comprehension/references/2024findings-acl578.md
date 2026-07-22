---
title: "Book2Dial: Generating Teacher Student Interactions from Textbooks for Cost-Effective Development of Educational Chatbots"
source: "https://aclanthology.org/2024.findings-acl.578/"
pdf_url: ""
categories: ['educational-question-generation-and-comprehension', 'llm-training-alignment-and-evaluation']
tags: ['educational-chatbot', 'synthetic-data', 'dialogue-generation']
venue: "ACL 2024"
tldr: "Proposes Book2Dial, a framework for generating synthetic teacher-student dialogues from textbooks to train educational chatbots cost-effectively."
---

# Book2Dial: Generating Teacher Student Interactions from Textbooks for Cost-Effective Development of Educational Chatbots

**Source**: [https://aclanthology.org/2024.findings-acl.578/](https://aclanthology.org/2024.findings-acl.578/)

**TLDR**: Proposes Book2Dial, a framework for generating synthetic teacher-student dialogues from textbooks to train educational chatbots cost-effectively.

## Abstract

AbstractEducational chatbots are a promising tool for assisting student learning. However, the development of effective chatbots in education has been challenging, as high-quality data is seldom available in this domain. In this paper, we propose a framework for generating synthetic teacher-student interactions grounded in a set of textbooks. Our approaches capture a key aspect of learning interactions where curious students with partial knowledge interactively ask teachers questions about the material in the textbook. We highlight various quality criteria that such dialogues must fulfill and compare several approaches relying on either prompting or finetuning large language models according to these criteria. We use the synthetic dialogues to train educational chatbots and show the benefits of further fine-tuning in educational domains. However, careful human evaluation shows that our best data synthesis method still suffers from hallucinations and tends to reiterate information from previous conversations. Our findings offer insights for future efforts in synthesizing conversational data that strikes a balance between size and quality. We will open-source our data and code.