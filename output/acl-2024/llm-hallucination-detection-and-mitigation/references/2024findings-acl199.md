---
title: "Enhancing Semantic Consistency of Large Language Models through Model Editing: An Interpretability-Oriented Approach"
source: "https://aclanthology.org/2024.findings-acl.199/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'llm-training-alignment-and-evaluation']
tags: ['semantic-consistency', 'model-editing', 'LLM', 'interpretability', 'fine-tuning']
venue: "ACL 2024"
tldr: "This paper proposes an interpretability-oriented model editing approach to improve semantic consistency of LLMs when presented with semantically equivalent but differently expressed prompts."
---

# Enhancing Semantic Consistency of Large Language Models through Model Editing: An Interpretability-Oriented Approach

**Source**: [https://aclanthology.org/2024.findings-acl.199/](https://aclanthology.org/2024.findings-acl.199/)

**TLDR**: This paper proposes an interpretability-oriented model editing approach to improve semantic consistency of LLMs when presented with semantically equivalent but differently expressed prompts.

## Abstract

AbstractA Large Language Model (LLM) tends to generate inconsistent and sometimes contradictory outputs when presented with a prompt that has equivalent semantics but is expressed differently from the original prompt. To achieve semantic consistency of an LLM, one of the key approaches is to finetune the model with prompt-output pairs with semantically equivalent meanings. Despite its effectiveness, a data-driven finetuning method incurs substantial computation costs in data preparation and model optimization. In this regime, an LLM is treated as a “black box”, restricting our ability to gain deeper insights into its internal mechanism. In this paper, we are motivated to enhance the semantic consistency of LLMs through a more interpretable method (i.e., model editing) to this end. We first identify the model components (i.e., attention heads) that have a key impact on the semantic consistency of an LLM. We subsequently inject biases into the output of these model components along the semantic-consistency activation direction. It is noteworthy that these modifications are cost-effective, without reliance on mass manipulations of the original model parameters. Through comprehensive experiments on the constructed NLU and open-source NLG datasets, our method demonstrates significant improvements in the semantic consistency and task performance of LLMs. Additionally, our method exhibits promising generalization capabilities by performing well on tasks beyond the primary tasks.