---
title: "From Representational Harms to Quality-of-Service Harms: A Case Study on Llama 2 Safety Safeguards"
source: "https://aclanthology.org/2024.findings-acl.927/"
pdf_url: ""
categories: ['bias-and-fairness-in-llms', 'llm-training-alignment-and-evaluation']
tags: ['safety', 'bias', 'quality-of-service-harms']
venue: "ACL 2024"
tldr: "This paper examines how Llama 2's safety safeguards shift harms from representational to quality-of-service harms, disproportionately affecting marginalized populations."
---

# From Representational Harms to Quality-of-Service Harms: A Case Study on Llama 2 Safety Safeguards

**Source**: [https://aclanthology.org/2024.findings-acl.927/](https://aclanthology.org/2024.findings-acl.927/)

**TLDR**: This paper examines how Llama 2's safety safeguards shift harms from representational to quality-of-service harms, disproportionately affecting marginalized populations.

## Abstract

AbstractRecent progress in large language models (LLMs) has led to their widespread adoption in various domains. However, these advancements have also introduced additional safety risks and raised concerns regarding their detrimental impact on already marginalized populations.Despite growing mitigation efforts to develop safety safeguards, such as supervised safety-oriented fine-tuning and leveraging safe reinforcement learning from human feedback, multiple concerns regarding the safety and ingrained biases in these models remain. Furthermore, previous work has demonstrated that models optimized for safety often display exaggerated safety behaviors, such as a tendency to refrain from responding to certain requests as a precautionary measure. As such, a clear trade-off between the helpfulness and safety of these models has been documented in the literature. In this paper, we further investigate the effectiveness of safety measures by evaluating models on already mitigated biases. Using the case of Llama 2 as an example, we illustrate how LLMs’ safety responses can still encode harmful assumptions. To do so, we create a set of non-toxic prompts, which we then use to evaluate Llama models. Through our new taxonomy of LLMs responses to users, we observe that the safety/helpfulness trade-offs are more pronounced for certain demographic groups which can lead to different kinds of harms such as quality-of-service harms for marginalized populations.