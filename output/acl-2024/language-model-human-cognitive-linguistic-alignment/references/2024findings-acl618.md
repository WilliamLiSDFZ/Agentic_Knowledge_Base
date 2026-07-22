---
title: "Are Machines Better at Complex Reasoning? Unveiling Human-Machine Inference Gaps in Entailment Verification"
source: "https://aclanthology.org/2024.findings-acl.618/"
pdf_url: ""
categories: ['language-model-human-cognitive-linguistic-alignment', 'nlp-benchmark-design-and-interpretability']
tags: ['entailment-verification', 'complex-reasoning', 'human-machine-comparison']
venue: "ACL 2024"
tldr: "Humans and machines show distinct inference gaps in entailment verification of complex multi-sentence premises."
---

# Are Machines Better at Complex Reasoning? Unveiling Human-Machine Inference Gaps in Entailment Verification

**Source**: [https://aclanthology.org/2024.findings-acl.618/](https://aclanthology.org/2024.findings-acl.618/)

**TLDR**: Humans and machines show distinct inference gaps in entailment verification of complex multi-sentence premises.

## Abstract

AbstractMaking inferences in text comprehension to understand the meaning is essential in language processing. This work studies the entailment verification (EV) problem of complex, multi-sentence premises requiring a system to make multiple inferences implicitly. Modern applications of EV in detecting inconsistent model-generated rationales require complex multi-hop reasoning. However, current textual inference datasets mostly contain short-sentence premises that partially focus on this. To address this, we compile an EV benchmark that includes datasets from three NLP domains (NLI, contextual QA, and rationales) containing multi-sentence premises. On benchmarking humans and LLMs, we find that LLMs are better than humans in multi-hop reasoning across extended contexts, while humans perform better in simple deductive reasoning tasks. We also finetune a Flan-T5 model for EV using two training objectives to obtain a strong open-source model that outperforms GPT-3.5 and rivals GPT-4. Finally, we use our finetuned model to filter out inconsistent model-generated rationales in self-consistency decoding, resulting in a 6% accuracy improvement on average across three MCQ datasets.