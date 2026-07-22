---
title: "Analyze, Generate and Refine: Query Expansion with LLMs for Zero-Shot Open-Domain QA"
source: "https://aclanthology.org/2024.findings-acl.708/"
categories: ['natural-language-processing-information-extraction', 'llm-agents-reasoning-and-planning']
tags: ['query-expansion', 'open-domain-qa', 'zero-shot-retrieval']
venue: "ACL 2024"
tldr: "Uses LLMs to analyze, generate, and refine query expansions for zero-shot open-domain question answering without supervised training."
---

# Analyze, Generate and Refine: Query Expansion with LLMs for Zero-Shot Open-Domain QA

**Source**: [https://aclanthology.org/2024.findings-acl.708/](https://aclanthology.org/2024.findings-acl.708/)

**TLDR**: Uses LLMs to analyze, generate, and refine query expansions for zero-shot open-domain question answering without supervised training.

## Abstract

AbstractQuery expansion (QE) is a critical component in the open-domain question answering (OpenQA) pipeline, enhancing the retrieval performance by broadening the scope of queries with additional relevant texts. However, existing methods like GAR and EAR rely heavily on supervised training and often struggle to maintain effectiveness across domains and datasets. Meanwhile, although large language models (LLMs) have demonstrated QE capability for information retrieval (IR) tasks, their application in OpenQA is hindered by the inadequate analysis of query’s informational needs and the lack of quality control for generated QEs, failing to meet the unique requirements of OpenQA. To bridge this gap, we propose a novel LLM-based QE approach named AGR for the OpenQA task, leveraging a three-step prompting strategy. AGR begins with an analysis of the query, followed by the generation of answer-oriented expansions, and culminates with a refinement process for better query formulation. Extensive experiments on four OpenQA datasets reveal that AGR not only rivals in-domain supervised methods in retrieval accuracy, but also outperforms state-of-the-art baselines in out-domain zero-shot scenarios. Moreover, it exhibits enhanced performance in end-to-end QA evaluations, underscoring the superiority of AGR for OpenQA.