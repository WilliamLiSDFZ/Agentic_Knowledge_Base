---
title: "CaLM: Contrasting Large and Small Language Models to Verify Grounded Generation"
source: "https://aclanthology.org/2024.findings-acl.759/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'llm-training-alignment-and-evaluation']
tags: ['grounded-generation', 'contrastive-verification', 'hallucination-mitigation']
venue: "ACL 2024"
tldr: "Introduces CaLM, a contrastive approach using large and small language models together to verify and improve grounded text generation."
---

# CaLM: Contrasting Large and Small Language Models to Verify Grounded Generation

**Source**: [https://aclanthology.org/2024.findings-acl.759/](https://aclanthology.org/2024.findings-acl.759/)

**TLDR**: Introduces CaLM, a contrastive approach using large and small language models together to verify and improve grounded text generation.

## Abstract

AbstractGrounded generation aims to equip language models (LMs) with the ability to produce more credible and accountable responses by accurately citing verifiable sources. However, existing methods, by either feeding LMs with raw or preprocessed materials, remain prone to errors. To address this, we introduce CaLM, a novel verification framework. CaLM leverages the insight that a robust grounded response should be consistent with information derived solely from its cited sources. Our framework empowers smaller LMs, which rely less on parametric memory and excel at processing relevant information given a query, to validate the output of larger LMs. Larger LM responses that closely align with the smaller LMs’ output, which relies exclusively on cited documents, are verified. Responses showing discrepancies are iteratively refined through a feedback loop. Experiments on three open-domain question-answering datasets demonstrate significant performance gains of 1.5% to 7% absolute average without any required model fine-tuning.