---
title: "LLM Factoscope: Uncovering LLMs’ Factual Discernment through Measuring Inner States"
source: "https://aclanthology.org/2024.findings-acl.608/"
categories: ['llm-hallucination-detection-and-mitigation', 'language-model-representations-and-embedding-spaces']
tags: ['hallucination', 'factual-discernment', 'inner-states', 'LLM', 'probability-analysis']
venue: "ACL 2024"
tldr: "Proposes LLM Factoscope, which uncovers LLMs' factual discernment by measuring internal state representations during generation."
---

# LLM Factoscope: Uncovering LLMs’ Factual Discernment through Measuring Inner States

**Source**: [https://aclanthology.org/2024.findings-acl.608/](https://aclanthology.org/2024.findings-acl.608/)

**TLDR**: Proposes LLM Factoscope, which uncovers LLMs' factual discernment by measuring internal state representations during generation.

## Abstract

AbstractLarge Language Models (LLMs) have revolutionized various domains with extensive knowledge and creative capabilities. However, a critical issue with LLMs is their tendency to produce outputs that diverge from factual reality. This phenomenon is particularly concerning in sensitive applications such as medical consultation and legal advice, where accuracy is paramount. Inspired by human lie detectors using physiological responses, we introduce the LLM Factoscope, a novel Siamese network-based model that leverages the inner states of LLMs for factual detection. Our investigation reveals distinguishable patterns in LLMs’ inner states when generating factual versus non-factual content. We demonstrate its effectiveness across various architectures, achieving over 96% accuracy on our custom-collected factual detection dataset. Our work opens a new avenue for utilizing LLMs’ inner states for factual detection and encourages further exploration into LLMs’ inner workings for enhanced reliability and transparency.