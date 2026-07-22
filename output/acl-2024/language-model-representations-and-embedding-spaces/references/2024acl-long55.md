---
title: "AbsInstruct: Eliciting Abstraction Ability from LLMs through Explanation Tuning with Plausibility Estimation"
source: "https://aclanthology.org/2024.acl-long.55/"
categories: ['concept-embedding-taxonomy-hierarchy-representation', 'language-model-representations-and-embedding-spaces']
tags: ['abstraction', 'instruction-tuning', 'plausibility-estimation']
venue: "ACL 2024"
tldr: "AbsInstruct is a framework that improves LLMs' abstraction ability through explanation tuning with plausibility estimation to elicit hierarchical concept generalization."
---

# AbsInstruct: Eliciting Abstraction Ability from LLMs through Explanation Tuning with Plausibility Estimation

**Source**: [https://aclanthology.org/2024.acl-long.55/](https://aclanthology.org/2024.acl-long.55/)

**TLDR**: AbsInstruct is a framework that improves LLMs' abstraction ability through explanation tuning with plausibility estimation to elicit hierarchical concept generalization.

## Abstract

AbstractAbstraction ability is crucial in human intelligence, which can also benefit various tasks in NLP study. Existing work shows that LLMs are deficient in abstract ability, and how to improve it remains unexplored. In this work, we design the framework AbsInstruct to enhance LLMs’ abstraction ability through instruction tuning. The framework builds instructions with in-depth explanations to assist LLMs in capturing the underlying rationale of abstraction. Meanwhile, we introduce a plausibility estimator to select instructions that are more consistent with the abstraction knowledge of LLMs to be aligned. Then, our framework combines abstraction instructions with general-purpose ones to build a hybrid dataset. Extensive experiments and analyses demonstrate that our framework can considerably enhance LLMs’ abstraction ability with strong generalization performance while maintaining their general instruction-following abilities.