---
title: "The Butterfly Effect of Altering Prompts: How Small Changes and Jailbreaks Affect Large Language Model Performance"
source: "https://aclanthology.org/2024.findings-acl.275/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['prompt-sensitivity', 'jailbreak', 'llm-robustness', 'prompt-engineering', 'evaluation']
venue: "ACL 2024"
tldr: "Analyzes how small prompt variations and jailbreaks cause butterfly-effect performance changes in LLMs used for data labeling."
---

# The Butterfly Effect of Altering Prompts: How Small Changes and Jailbreaks Affect Large Language Model Performance

**Source**: [https://aclanthology.org/2024.findings-acl.275/](https://aclanthology.org/2024.findings-acl.275/)

**TLDR**: Analyzes how small prompt variations and jailbreaks cause butterfly-effect performance changes in LLMs used for data labeling.

## Abstract

AbstractLarge Language Models (LLMs) are regularly being used to label data across many domains and for myriad tasks. By simply asking the LLM for an answer, or “prompting,” practitioners are able to use LLMs to quickly get a response for an arbitrary task. This prompting is done through a series of decisions by the practitioner, from simple wording of the prompt, to requesting the output in a certain data format, to jailbreaking in the case of prompts that address more sensitive topics. In this work, we ask: do variations in the way a prompt is constructed change the ultimate decision of the LLM? We answer this using a series of prompt variations across a variety of text classification tasks. We find that even the smallest of perturbations, such as adding a space at the end of a prompt, can cause the LLM to change its answer. Further, we find that requesting responses in XML and commonly used jailbreaks can have cataclysmic effects on the data labeled by LLMs.