---
title: "EX-FEVER: A Dataset for Multi-hop Explainable Fact Verification"
source: "https://aclanthology.org/2024.findings-acl.556/"
categories: ['computational-misinformation-narrative-framing-detection', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['fact-verification', 'explainability', 'multi-hop', 'evidence-retrieval', 'dataset']
venue: "ACL 2024"
tldr: "Introduces EX-FEVER, a dataset for multi-hop explainable fact verification requiring both accuracy and explainability."
---

# EX-FEVER: A Dataset for Multi-hop Explainable Fact Verification

**Source**: [https://aclanthology.org/2024.findings-acl.556/](https://aclanthology.org/2024.findings-acl.556/)

**TLDR**: Introduces EX-FEVER, a dataset for multi-hop explainable fact verification requiring both accuracy and explainability.

## Abstract

AbstractFact verification aims to automatically probe the veracity of a claim based on several pieces of evidence. Existing works are always engaging in accuracy improvement, let alone explainability, a critical capability of fact verification systems.Constructing an explainable fact verification system in a complex multi-hop scenario is consistently impeded by the absence of a relevant, high-quality dataset. Previous datasets either suffer from excessive simplification or fail to incorporate essential considerations for explainability. To address this, we present EX-FEVER, a pioneering dataset for multi-hop explainable fact verification. With over 60,000 claims involving 2-hop and 3-hop reasoning, each is created by summarizing and modifying information from hyperlinked Wikipedia documents. Each instance is accompanied by a veracity label and an explanation that outlines the reasoning path supporting the veracity classification. Additionally, we demonstrate a novel baseline system on our EX-FEVER dataset, showcasing document retrieval, explanation generation, and claim verification, and validate the significance of our dataset. Furthermore, we highlight the potential of utilizing Large Language Models in the fact verification task. We hope our dataset could make a significant contribution by providing ample opportunities to explore the integration of natural language explanations in the domain of fact verification.