---
title: "Sketch-Guided Constrained Decoding for Boosting Blackbox Large Language Models without Logit Access"
source: "https://aclanthology.org/2024.acl-short.23/"
categories: ['llm-training-alignment-and-evaluation', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['constrained-decoding', 'black-box-LLMs', 'text-generation', 'sketch-guided', 'inference']
venue: "ACL 2024"
tldr: "Proposes a sketch-guided constrained decoding method to enforce output constraints on black-box LLMs without requiring access to token logits."
---

# Sketch-Guided Constrained Decoding for Boosting Blackbox Large Language Models without Logit Access

**Source**: [https://aclanthology.org/2024.acl-short.23/](https://aclanthology.org/2024.acl-short.23/)

**TLDR**: Proposes a sketch-guided constrained decoding method to enforce output constraints on black-box LLMs without requiring access to token logits.

## Abstract

AbstractConstrained decoding, a technique for enforcing constraints on language model outputs, offers a way to control text generation without retraining or architectural modifications. Its application is, however, typically restricted to models that give users access to next-token distributions (usually via softmax logits), which poses a limitation with blackbox large language models (LLMs). This paper introduces sketch-guided constrained decoding (SketchGCD), a novel approach to constrained decoding for blackbox LLMs, which operates without access to the logits of the blackbox LLM. SketchGCD utilizes a locally hosted auxiliary model to refine the output of an unconstrained blackbox LLM, effectively treating this initial output as a “sketch” for further elaboration. This approach is complementary to traditional logit-based techniques and enables the application of constrained decoding in settings where full model transparency is unavailable. We demonstrate the efficacy of SketchGCD through experiments in closed information extraction and constituency parsing, showing how it enhances the utility and flexibility of blackbox LLMs for complex NLP tasks.