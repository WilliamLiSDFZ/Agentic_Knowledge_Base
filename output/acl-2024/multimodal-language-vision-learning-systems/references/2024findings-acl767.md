---
title: "Selective “Selective Prediction”: Reducing Unnecessary Abstention in Vision-Language Reasoning"
source: "https://aclanthology.org/2024.findings-acl.767/"
categories: ['multimodal-language-vision-learning-systems', 'llm-hallucination-detection-and-mitigation']
tags: ['selective-prediction', 'vision-language-models', 'abstention']
venue: "ACL 2024"
tldr: "Proposes a method to reduce unnecessary abstention in selective prediction for vision-language reasoning systems."
---

# Selective “Selective Prediction”: Reducing Unnecessary Abstention in Vision-Language Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.767/](https://aclanthology.org/2024.findings-acl.767/)

**TLDR**: Proposes a method to reduce unnecessary abstention in selective prediction for vision-language reasoning systems.

## Abstract

AbstractSelective prediction minimizes incorrect predictions from vision-language models (VLMs) by allowing them to abstain from answering when uncertain. However, when deploying a vision-language system with low tolerance for inaccurate predictions, selective prediction may be over-cautious and abstain too frequently, even on many correct predictions. We introduce ReCoVERR, an inference-time algorithm to reduce the over-abstention of a selective vision-language system without increasing the error rate of the system’s predictions. When the VLM makes a low-confidence prediction, instead of abstaining ReCoVERR tries to find relevant clues in the image that provide additional evidence for the prediction. ReCoVERR uses an LLM to pose related questions to the VLM, collects high-confidence evidences, and if enough evidence confirms the prediction the system makes a prediction instead of abstaining. ReCoVERR enables three VLMs (BLIP2, InstructBLIP and LLaVA-1.5) to answer up to 20% more questions on the VQAv2 and A-OKVQA tasks without decreasing system accuracy, thus improving overall system reliability. Our code is available at https://github.com/tejas1995/ReCoVERR.