---
title: "Improving Machine Translation with Large Language Models: A Preliminary Study with Cooperative Decoding"
source: "https://aclanthology.org/2024.findings-acl.786/"
pdf_url: ""
categories: ['collaborative-llm-deployment-and-inference-optimization', 'nlp-for-asian-languages']
tags: ['machine-translation', 'cooperative-decoding', 'LLM', 'encoder-decoder', 'translation-quality']
venue: "ACL 2024"
tldr: "Proposes cooperative decoding between LLMs and encoder-decoder translation models to improve machine translation quality."
---

# Improving Machine Translation with Large Language Models: A Preliminary Study with Cooperative Decoding

**Source**: [https://aclanthology.org/2024.findings-acl.786/](https://aclanthology.org/2024.findings-acl.786/)

**TLDR**: Proposes cooperative decoding between LLMs and encoder-decoder translation models to improve machine translation quality.

## Abstract

AbstractContemporary translation engines based on the encoder-decoder framework have made significant strides in development.However, the emergence of Large Language Models (LLMs) has disrupted their position by presenting the potential for achieving superior translation quality.To uncover the circumstances in which LLMs excel and explore how their strengths can be harnessed to enhance translation quality,we first conduct a comprehensive analysis to assess the strengths and limitations of various commercial NMT systems and MT-oriented LLMs. Our findings indicate that neither NMT nor MT-oriented LLMs alone can effectively address all the translation issues, but MT-oriented LLMs show promise as a complementary solution to NMT systems.Building upon these insights, we propose Cooperative Decoding (CoDec), which treats NMT systems as a pretranslation model and MT-oriented LLMs as a supplemental solution to handle complex scenarios beyond the capability of NMT alone.Experimental results on the WMT22 test sets and a newly collected test set WebCrawl demonstrate the effectiveness and efficiency of CoDec, highlighting its potential as a robust solution for combining NMT systems with MT-oriented LLMs in the field of machine translation.