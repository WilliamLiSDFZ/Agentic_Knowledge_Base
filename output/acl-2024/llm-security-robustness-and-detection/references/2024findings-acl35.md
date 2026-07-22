---
title: "DPDLLM: A Black-box Framework for Detecting Pre-training Data from Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.35/"
categories: ['llm-security-robustness-and-detection', 'privacy-risks-in-language-model-embeddings']
tags: ['membership-inference', 'pre-training-data', 'black-box', 'copyright', 'llm-detection']
venue: "ACL 2024"
tldr: "Proposes a black-box framework to detect whether specific text was used in LLM pre-training data to address copyright concerns."
---

# DPDLLM: A Black-box Framework for Detecting Pre-training Data from Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.35/](https://aclanthology.org/2024.findings-acl.35/)

**TLDR**: Proposes a black-box framework to detect whether specific text was used in LLM pre-training data to address copyright concerns.

## Abstract

AbstractThe success of large language models (LLM) benefits from large-scale model parameters and large amounts of pre-training data. However, the textual data for training LLM can not be confirmed to be legal because they are crawled from different web sites. For example, there are copyrighted articles, personal reviews and information in the pre-training data for LLM which are illegal. To address the above issue and develop legal LLM, we propose to detect the pre-training data from LLM in a pure black-box way because the existing LLM services only return the generated text. The previous most related works are the membership inference attack (MIA) on machine learning models to detect the training data from them. But the existing methods are based on analyzing the output probabilities of models which are unrealistic to LLM services. To tackle the problem, we firstly construct the benchmark datasets by collecting textual data from different domains as the seen and unseen pre-training data for LLMs. Then, we investigate a black-box framework named DPDLLM, with the only access to the generated texts from LLM for detecting textual data whether was used to train it. In the proposed framework, we exploit GPT-2 as the reference model to fit the textual data and feed the generated text from LLM into it to acquire sequence probabilities as the significant feature for detection. The experimental results on the benchmark datasets demonstrate that DPDLLM is effective on different popular LLMs and outperforms the existing methods.