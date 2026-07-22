---
title: "OTTAWA: Optimal TransporT Adaptive Word Aligner for Hallucination and Omission Translation Errors Detection"
source: "https://aclanthology.org/2024.findings-acl.377/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'string-to-string-alignment-algorithms-library\n\nwait,-let-me-reconsider-for-conciseness-(3-7-words):\n\n`string-similarity-and-alignment-algorithms']
tags: ['hallucination-detection', 'machine-translation', 'optimal-transport']
venue: "ACL 2024"
tldr: "Proposes OTTAWA, an optimal transport-based word aligner for detecting hallucination and omission errors in machine translation."
---

# OTTAWA: Optimal TransporT Adaptive Word Aligner for Hallucination and Omission Translation Errors Detection

**Source**: [https://aclanthology.org/2024.findings-acl.377/](https://aclanthology.org/2024.findings-acl.377/)

**TLDR**: Proposes OTTAWA, an optimal transport-based word aligner for detecting hallucination and omission errors in machine translation.

## Abstract

AbstractRecently, there has been considerable attention on detecting hallucinations and omissions in Machine Translation (MT) systems. The two dominant approaches to tackle this task involve analyzing the MT system’s internal states or relying on the output of external tools, such as sentence similarity or MT quality estimators. In this work, we introduce OTTAWA, a novel Optimal Transport (OT)-based word aligner specifically designed to enhance the detection of hallucinations and omissions in MT systems. Our approach explicitly models the missing alignments by introducing a “null” vector, for which we propose a novel one-side constrained OT setting to allow an adaptive null alignment. Our approach yields competitive results compared to state-of-the-art methods across 18 language pairs on the HalOmi benchmark. In addition, it shows promising features, such as the ability to distinguish between both error types and perform word-level detection without accessing the MT system’s internal states.