---
title: "Evaluating Large Language Model Biases in Persona-Steered Generation"
source: "https://aclanthology.org/2024.findings-acl.586/"
pdf_url: ""
categories: ['bias-and-fairness-in-llms']
tags: ['persona-steered-generation', 'opinion-bias', 'multidimensional-demographics']
venue: "ACL 2024"
tldr: "Evaluates LLM biases when generating text for personas defined by multiple intersecting demographic attributes."
---

# Evaluating Large Language Model Biases in Persona-Steered Generation

**Source**: [https://aclanthology.org/2024.findings-acl.586/](https://aclanthology.org/2024.findings-acl.586/)

**TLDR**: Evaluates LLM biases when generating text for personas defined by multiple intersecting demographic attributes.

## Abstract

AbstractThe task of persona-steered text generation requires large language models (LLMs) to generate text that reflects the distribution of views that an individual fitting a persona could have. People have multifaceted personas, but prior work on bias in LLM-generated opinions has only explored multiple-choice settings or one-dimensional personas. We define an incongruous persona as a persona with multiple traits where one trait makes its other traits less likely in human survey data, e.g. political liberals who support increased military spending. We find that LLMs are 9.7% less steerable towards incongruous personas than congruous ones, sometimes generating the stereotypical stance associated with its demographic rather than the target stance. Models that we evaluate that are fine-tuned with Reinforcement Learning from Human Feedback (RLHF) are more steerable, especially towards stances associated with political liberals and women, but present significantly less diverse views of personas. We also find variance in LLM steerability that cannot be predicted from multiple-choice opinion evaluation. Our results show the importance of evaluating models in open-ended text generation, as it can surface new LLM opinion biases. Moreover, such a setup can shed light on our ability to steer models toward a richer and more diverse range of viewpoints.