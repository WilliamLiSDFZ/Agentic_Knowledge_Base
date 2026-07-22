---
title: "Integrating Physician Diagnostic Logic into Large Language Models: Preference Learning from Process Feedback"
source: "https://aclanthology.org/2024.findings-acl.144/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'llm-training-alignment-and-evaluation']
tags: ['medical-dialogue', 'preference-learning', 'process-feedback']
venue: "ACL 2024"
tldr: "Integrates physician diagnostic logic into LLMs via preference learning from process feedback to improve medical dialogue generation quality."
---

# Integrating Physician Diagnostic Logic into Large Language Models: Preference Learning from Process Feedback

**Source**: [https://aclanthology.org/2024.findings-acl.144/](https://aclanthology.org/2024.findings-acl.144/)

**TLDR**: Integrates physician diagnostic logic into LLMs via preference learning from process feedback to improve medical dialogue generation quality.

## Abstract

AbstractThe utilization of large language models for medical dialogue generation has attracted considerable attention due to its potential to enhance response richness and coherence. While previous studies have made strides in optimizing model performance, there is a pressing need to bolster the model’s capacity for diagnostic logic to ensure patient safety. In response to this need, we propose an approach termed preference learning from process feedback (PLPF), which involves integrating the doctor’s diagnostic logic into LLMs. PLPF encompasses three key components: rule modeling, preference data generation, and preference alignment. These components collectively serve to train the model to adhere to the diagnostic process. Our experimental results, utilizing Standardized Patient Testing, demonstrate that PLPF enhances the diagnostic accuracy of the baseline model in medical conversations by 17.6%, surpassing the performance of traditional approaches. Moreover, PLPF exhibits effectiveness in both multi-round and single-round dialogue tasks, thereby highlighting its potential in improving medical dialogue generation. Our dataset is available at https://github.com/Chengfeng-Dou/SpTesting.