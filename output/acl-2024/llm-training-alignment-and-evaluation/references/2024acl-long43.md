---
title: "ABEX: Data Augmentation for Low-Resource NLU via Expanding Abstract Descriptions"
source: "https://aclanthology.org/2024.acl-long.43/"
categories: ['nlp-text-classification-applied-tasks', 'llm-training-alignment-and-evaluation']
tags: ['data-augmentation', 'low-resource', 'NLU', 'abstract-expand', 'text-generation']
venue: "ACL 2024"
tldr: "ABEX is a generative data augmentation method for low-resource NLU that abstracts documents and expands them into diverse training examples."
---

# ABEX: Data Augmentation for Low-Resource NLU via Expanding Abstract Descriptions

**Source**: [https://aclanthology.org/2024.acl-long.43/](https://aclanthology.org/2024.acl-long.43/)

**TLDR**: ABEX is a generative data augmentation method for low-resource NLU that abstracts documents and expands them into diverse training examples.

## Abstract

AbstractWe present ABEX, a novel and effective generative data augmentation methodology for low-resource Natural Language Understanding (NLU) tasks. ABEX is based on ABstract-and-EXpand, a novel paradigm for generating diverse forms of an input document – we first convert a document into its concise, abstract description and then generate new documents based on expanding the resultant abstraction. To learn the task of expanding abstract descriptions, we first train BART on a large-scale synthetic dataset with abstract-document pairs. Next, to generate abstract descriptions for a document, we propose a simple, controllable, and training-free method based on editing AMR graphs. ABEX brings the best of both worlds: by expanding from abstract representations, it preserves the original semantic properties of the documents, like style and meaning, thereby maintaining alignment with the original label and data distribution. At the same time, the fundamental process of elaborating on abstract descriptions facilitates diverse generations. We demonstrate the effectiveness of ABEX on 4 NLU tasks spanning 12 datasets and 4 low-resource settings. ABEX outperforms all our baselines qualitatively with improvements of 0.04% - 38.8%. Qualitatively, ABEX outperforms all prior methods from literature in terms of context and length diversity.