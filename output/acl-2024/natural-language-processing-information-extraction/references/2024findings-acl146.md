---
title: "Episodic Memory Retrieval from LLMs: A Neuromorphic Mechanism to Generate Commonsense Counterfactuals for Relation Extraction"
source: "https://aclanthology.org/2024.findings-acl.146/"
categories: ['natural-language-processing-information-extraction']
tags: ['relation-extraction', 'counterfactual-generation', 'episodic-memory']
venue: "ACL 2024"
tldr: "Proposes a neuromorphic episodic memory mechanism to generate commonsense counterfactuals improving LLM-based relation extraction."
---

# Episodic Memory Retrieval from LLMs: A Neuromorphic Mechanism to Generate Commonsense Counterfactuals for Relation Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.146/](https://aclanthology.org/2024.findings-acl.146/)

**TLDR**: Proposes a neuromorphic episodic memory mechanism to generate commonsense counterfactuals improving LLM-based relation extraction.

## Abstract

AbstractLarge language models (LLMs) have achieved satisfactory performance in counterfactual generation. However, confined by the stochastic generation process of LLMs, there often are misalignments between LLMs and humans which hinder LLMs from handling complex tasks like relation extraction. As a result, LLMs may generate commonsense-violated counterfactuals like ‘eggs were produced by a box’. To bridge this gap, we propose to mimick the episodic memory retrieval, the working mechanism of human hippocampus, to align LLMs’ generation process with that of humans. In this way, LLMs can derive experience from their extensive memory, which keeps in line with the way humans gain commonsense. We then implement two central functions in the hippocampus, i.e., pattern separation and pattern completion, to retrieve the episodic memory from LLMs and generate commonsense counterfactuals for relation extraction. Experimental results demonstrate the improvements of our framework over existing methods in terms of the quality of counterfactuals.