---
title: "Answer is All You Need: Instruction-following Text Embedding via Answering the Question"
source: "https://aclanthology.org/2024.acl-long.27/"
categories: ['language-model-representations-and-embedding-spaces', 'natural-language-processing-information-extraction']
tags: ['text-embedding', 'instruction-following', 'question-answering', 'similarity', 'representation-learning']
venue: "ACL 2024"
tldr: "This work builds instruction-following text embedders that capture user-specified similarity criteria by framing embedding as answering questions about text characteristics."
---

# Answer is All You Need: Instruction-following Text Embedding via Answering the Question

**Source**: [https://aclanthology.org/2024.acl-long.27/](https://aclanthology.org/2024.acl-long.27/)

**TLDR**: This work builds instruction-following text embedders that capture user-specified similarity criteria by framing embedding as answering questions about text characteristics.

## Abstract

AbstractThis work aims to build a text embedder that can capture characteristics of texts specified by user instructions clarifying the similarity criterion. While previous methods improve general task awareness by injecting the instruction information into encoding, they fail to be sensitive to clearer criteria like “evaluate similarity based on emotion”. We instead propose a different viewpoint, which treats the instruction as a “question” about the input text and encodes the expected answers to obtain the representation accordingly. Intuitively, texts with the same (implicit) semantics would share similar answers following the instruction, thus leading to more similar representations. Specifically, we propose InBedder that instantiates this learning-to-answer idea by only fine-tuning language models via abstractive question answering tasks. Despite its simplicity, InBedder demonstrates significantly improved instruction-following capabilities according to our proposed instruction awareness tests and instruction robustness tests, when applied to language models with large language models (LLMs) (e.g., llama-2-7b) and smaller encoder-based LMs (e.g., roberta-large). Additionally, our qualitative analysis of clustering outcomes, achieved by applying diverse instructions to the same unlabeled corpus, demonstrates a high degree of interpretability in the clusters formed.