---
title: "A Two-Agent Game for Zero-shot Relation Triplet Extraction"
source: "https://aclanthology.org/2024.findings-acl.446/"
categories: ['natural-language-processing-information-extraction', 'code-llm-generation-and-evaluation']
tags: ['zero-shot', 'relation-extraction', 'two-agent-game']
venue: "ACL 2024"
tldr: "A two-agent game framework enables zero-shot relation triplet extraction by having agents collaboratively identify entity relationships."
---

# A Two-Agent Game for Zero-shot Relation Triplet Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.446/](https://aclanthology.org/2024.findings-acl.446/)

**TLDR**: A two-agent game framework enables zero-shot relation triplet extraction by having agents collaboratively identify entity relationships.

## Abstract

AbstractRelation triplet extraction is a fundamental task in natural language processing that aims to identify semantic relationships between entities in text. It is particularly challenging in the zero-shot setting, i.e., zero-shot relation triplet extraction (ZeroRTE), where the relation sets between training and test are disjoint. Existing methods deal with this task by integrating relations into prompts, which may lack sufficient understanding of the unseen relations. To address these limitations, this paper presents a novel Two-Agent Game (TAG) approach to deliberate and debate the semantics of unseen relations. TAG consists of two agents, a generator and an extractor. They iteratively interact in three key steps: attempting, criticizing, and rectifying. This enables the agents to fully debate and understand the unseen relations. Experimental results demonstrate consistent improvement over ALBERT-Large, BART, andGPT3.5, without incurring additional inference costs in all cases. Remarkably, our method outperforms strong baselines by a significant margin, achieving an impressive 6%-16% increase in F1 scores, particularly when dealingwith FewRel with five unseen relations.