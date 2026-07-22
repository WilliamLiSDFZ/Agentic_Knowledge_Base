---
title: "MRL Parsing Without Tears: The Case of Hebrew"
source: "https://aclanthology.org/2024.findings-acl.269/"
categories: ['unsupervised-and-structured-syntactic-parsing-methods', 'nlp-for-asian-languages']
tags: ['morphologically-rich-languages', 'hebrew', 'syntactic-parsing']
venue: "ACL 2024"
tldr: "A new approach to syntactic parsing for morphologically rich languages achieves state-of-the-art results for Hebrew without complex pipeline dependencies."
---

# MRL Parsing Without Tears: The Case of Hebrew

**Source**: [https://aclanthology.org/2024.findings-acl.269/](https://aclanthology.org/2024.findings-acl.269/)

**TLDR**: A new approach to syntactic parsing for morphologically rich languages achieves state-of-the-art results for Hebrew without complex pipeline dependencies.

## Abstract

AbstractSyntactic parsing remains a critical tool for relation extraction and information extraction, especially in resource-scarce languages where LLMs are lacking. Yet in morphologically rich languages (MRLs), where parsers need to identify multiple lexical units in each token, existing systems suffer in latency and setup complexity. Some use a pipeline to peel away the layers: first segmentation, then morphology tagging, and then syntax parsing; however, errors in earlier layers are then propagated forward. Others use a joint architecture to evaluate all permutations at once; while this improves accuracy, it is notoriously slow. In contrast, and taking Hebrew as a test case, we present a new “flipped pipeline”: decisions are made directly on the whole-token units by expert classifiers, each one dedicated to one specific task. The classifier predictions are independent of one another, and only at the end do we synthesize their predictions. This blazingly fast approach requires only a single huggingface call, without the need for recourse to lexicons or linguistic resources. When trained on the same training set used in previous studies, our model achieves near-SOTA performance on a wide array of Hebrew NLP tasks. Furthermore, when trained on a newly enlarged training corpus, our model achieves a new SOTA for Hebrew POS tagging and dependency parsing. We release this new SOTA model to the community. Because our architecture does not rely on any language-specific resources, it can serve as a model to develop similar parsers for other MRLs.