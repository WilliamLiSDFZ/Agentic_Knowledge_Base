---
title: "Proving membership in LLM pretraining data via data watermarks"
source: "https://aclanthology.org/2024.findings-acl.788/"
pdf_url: ""
categories: ['privacy-risks-in-language-model-embeddings', 'llm-security-robustness-and-detection']
tags: ['data-watermarks', 'membership-inference', 'pretraining-data', 'copyright', 'black-box-access']
venue: "ACL 2024"
tldr: "Proposes data watermarking to detect whether copyrighted documents were included in LLM pretraining data."
---

# Proving membership in LLM pretraining data via data watermarks

**Source**: [https://aclanthology.org/2024.findings-acl.788/](https://aclanthology.org/2024.findings-acl.788/)

**TLDR**: Proposes data watermarking to detect whether copyrighted documents were included in LLM pretraining data.

## Abstract

AbstractDetecting whether copyright holders’ works were used in LLM pretraining is poised to be an important problem. This work proposes using data watermarks to enable principled detection with only black-box model access, provided that the rightholder contributed multiple training documents and watermarked them before public release. By applying a randomly sampled data watermark, detection can be framed as hypothesis testing, which provides guarantees on the false detection rate. We study two watermarks: one that inserts random sequences, and another that randomly substitutes characters with Unicode lookalikes. We first show how three aspects of watermark design - watermark length, number of duplications, and interference - affect the power of the hypothesis test. Next, we study how a watermark’s detection strength changes under model and dataset scaling: while increasing the dataset size decreases the strength of the watermark, watermarks remain strong if the model size also increases. Finally, we view SHA hashes as natural watermarks and show that we can robustly detect hashes from BLOOM-176B’s training data, as long as they occurred at least 90 times. Together, our results point towards a promising future for data watermarks in real world use.