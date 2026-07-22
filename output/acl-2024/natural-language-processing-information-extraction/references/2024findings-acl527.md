---
title: "Semantic Role Labeling from Chinese Speech via End-to-End Learning"
source: "https://aclanthology.org/2024.findings-acl.527/"
categories: ['speech-and-language-multimodal-generation-systems', 'natural-language-processing-information-extraction']
tags: ['semantic-role-labeling', 'speech', 'Chinese', 'end-to-end', 'multimodal']
venue: "ACL 2024"
tldr: "Proposes an end-to-end model for semantic role labeling directly from Chinese speech input without intermediate text transcription."
---

# Semantic Role Labeling from Chinese Speech via End-to-End Learning

**Source**: [https://aclanthology.org/2024.findings-acl.527/](https://aclanthology.org/2024.findings-acl.527/)

**TLDR**: Proposes an end-to-end model for semantic role labeling directly from Chinese speech input without intermediate text transcription.

## Abstract

AbstractSemantic Role Labeling (SRL), crucial for understanding semantic relationships in sentences, has traditionally focused on text-based input. However, the increasing use of voice assistants and the need for hands-free interaction have highlighted the importance of SRL from speech.SRL from speech can be accomplished via a two-step pipeline directly: transcribing speech to text via Automatic Speech Recognition (ASR) and then applying text-based SRL, which could lead to error propagation and loss of useful acoustic features.Addressing these challenges, we present the first end-to-end approach for SRL from speech, integrating ASR and SRL in a joint-learning framework, focusing on the Chinese language. By employing a Stright-Through Gumbel-Softmax module for connecting ASR and SRL models, it enables gradient back-propagation and joint optimization, enhancing robustness and effectiveness.Experiments on the Chinese Proposition Bank 1.0 (CPB1.0) and a newly annotated dataset AS-SRL based on AISHELL-1 demonstrate the superiority of the end-to-end model over traditional pipelines, with significantly improved performance.