---
title: "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews"
source: "https://proceedings.mlr.press/v235/liang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liang24b/liang24b.pdf"
categories: ['anomaly-and-out-of-distribution-detection']
tags: ['LLM-detection', 'peer-review', 'AI-generated-text']
venue: "ICML 2024"
tldr: "A maximum likelihood approach is presented to estimate the fraction of LLM-modified text at scale, applied to AI conference peer reviews."
---

# Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews

**Source**: [https://proceedings.mlr.press/v235/liang24b.html](https://proceedings.mlr.press/v235/liang24b.html)

**TLDR**: A maximum likelihood approach is presented to estimate the fraction of LLM-modified text at scale, applied to AI conference peer reviews.

## Abstract

We present an approach for estimating the fraction of text in a large corpus which is likely to be substantially modified or produced by a large language model (LLM). Our maximum likelihood model leverages expert-written and AI-generated reference texts to accurately and efficiently examine real-world LLM-use at the corpus level. We apply this approach to a case study of scientific peer review in AI conferences that took place after the release of ChatGPT: ICLR 2024, NeurIPS 2023, CoRL 2023 and EMNLP 2023. Our results suggest that between 6.5% and 16.9% of text submitted as peer reviews to these conferences could have been substantially modified by LLMs, i.e. beyond spell-checking or minor writing updates. The circumstances in which generated text occurs offer insight into user behavior: the estimated fraction of LLM-generated text is higher in reviews which report lower confidence, were submitted close to the deadline, and from reviewers who are less likely to respond to author rebuttals. We also observe corpus-level trends in generated text which may be too subtle to detect at the individual level, and discuss the implications of such trends on peer review. We call for future interdisciplinary work to examine how LLM use is changing our information and knowledge practices.