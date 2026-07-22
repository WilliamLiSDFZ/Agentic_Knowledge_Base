---
title: "Automatic and Human-AI Interactive Text Generation (with a focus on Text Simplification and Revision)"
source: "https://aclanthology.org/2024.acl-tutorials.2/"
categories: ['text-simplification-evaluation-and-methods', 'llm-training-alignment-and-evaluation']
tags: ['text-simplification', 'text-revision', 'human-ai-interaction', 'nlg', 'tutorial']
venue: "ACL 2024"
tldr: "Surveys automatic and human-AI collaborative approaches to text-to-text generation with focus on simplification and revision."
---

# Automatic and Human-AI Interactive Text Generation (with a focus on Text Simplification and Revision)

**Source**: [https://aclanthology.org/2024.acl-tutorials.2/](https://aclanthology.org/2024.acl-tutorials.2/)

**TLDR**: Surveys automatic and human-AI collaborative approaches to text-to-text generation with focus on simplification and revision.

## Abstract

AbstractIn this tutorial, we focus on text-to-text generation, a class of natural language generation (NLG) tasks, that takes a piece of text as input and then generates a revision that is improved according to some specific criteria (e.g., readability or linguistic styles), while largely retaining the original meaning and the length of the text. This includes many useful applications, such as text simplification, paraphrase generation, style transfer, etc. In contrast to text summarization and open-ended text completion (e.g., story), the text-to-text generation tasks we discuss in this tutorial are more constrained in terms of semantic consistency and targeted language styles. This level of control makes these tasks ideal testbeds for studying the ability of models to generate text that is both semantically adequate and stylistically appropriate. Moreover, these tasks are interesting from a technical standpoint, as they require complex combinations of lexical and syntactical transformations, stylistic control, and adherence to factual knowledge, – all at once. With a special focus on text simplification and revision, this tutorial aims to provide an overview of the state-of-the-art natural language generation research from four major aspects – Data, Models, Human-AI Collaboration, and Evaluation – and to discuss and showcase a few significant and recent advances: (1) the use of non-retrogressive approaches; (2) the shift from fine-tuning to prompting with large language models; (3) the development of new learnable metric and fine-grained human evaluation framework; (4) a growing body of studies and datasets on non-English languages; (5) the rise of HCI+NLP+Accessibility interdisciplinary research to create real-world writing assistant systems.