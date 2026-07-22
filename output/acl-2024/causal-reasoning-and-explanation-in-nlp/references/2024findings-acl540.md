---
title: "FRVA: Fact-Retrieval and Verification Augmented Entailment Tree Generation for Explainable Question Answering"
source: "https://aclanthology.org/2024.findings-acl.540/"
categories: ['causal-reasoning-and-explanation-in-nlp', 'educational-question-generation-and-comprehension']
tags: ['entailment-tree', 'explainable-qa', 'fact-retrieval', 'verification', 'structured-reasoning']
venue: "ACL 2024"
tldr: "FRVA augments entailment tree generation with fact retrieval and verification to build more accurate and explainable QA systems."
---

# FRVA: Fact-Retrieval and Verification Augmented Entailment Tree Generation for Explainable Question Answering

**Source**: [https://aclanthology.org/2024.findings-acl.540/](https://aclanthology.org/2024.findings-acl.540/)

**TLDR**: FRVA augments entailment tree generation with fact retrieval and verification to build more accurate and explainable QA systems.

## Abstract

AbstractStructured entailment tree can exhibit the reasoning chains from knowledge facts to predicted answers, which is important for constructing an explainable question answering system. Existing works mainly include directly generating the entire tree and stepwise generating the proof steps. The stepwise methods can exploit combinatoriality and generalize to longer steps, but they have large fact search spaces and error accumulation problems resulting in the generation of invalid steps. In this paper, inspired by the Dual Process Theory in cognitive science, we propose FRVA, a Fact-Retrieval and Verification Augmented bidirectional entailment tree generation method that contains two systems. Specifically, System 1 makes intuitive judgments through the fact retrieval module and filters irrelevant facts to reduce the search space. System 2 designs a deductive-abductive bidirectional reasoning module, and we construct cross-verification and multi-view contrastive learning to make the generated proof steps closer to the target hypothesis. We enhance the reliability of the stepwise proofs to mitigate error propagation. Experiment results on EntailmentBank show that FRVA outperforms previous models and achieves state-of-the-art performance in fact selection and structural correctness.