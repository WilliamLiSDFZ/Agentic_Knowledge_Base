---
title: "HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ba92705991cfbbcedc26e27e833ebbae-Abstract-Conference.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'ai-benchmarking-and-evaluation-methodology']
tags: ['hallucination-detection', 'LLM', 'unlabeled-data', 'semi-supervised', 'trustworthiness']
venue: "NeurIPS 2024"
tldr: "Proposes HaloScope, a method that harnesses unlabeled LLM-generated text to train hallucination detectors without extensive labeled data."
---

# HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ba92705991cfbbcedc26e27e833ebbae-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ba92705991cfbbcedc26e27e833ebbae-Abstract-Conference.html)

**TLDR**: Proposes HaloScope, a method that harnesses unlabeled LLM-generated text to train hallucination detectors without extensive labeled data.

## Abstract

The surge in applications of large language models (LLMs) has prompted concerns about the generation of misleading or fabricated information, known as hallucinations. Therefore, detecting hallucinations has become critical to maintaining trust in LLM-generated content. A primary challenge in learning a truthfulness classifier is the lack of a large amount of labeled truthful and hallucinated data. To address the challenge, we introduce HaloScope, a novel learning framework that leverages the unlabeled LLM generations in the wild for hallucination detection. Such unlabeled data arises freely upon deploying LLMs in the open world, and consists of both truthful and hallucinated information. To harness the unlabeled data, we present an automated scoring function for distinguishing between truthful and untruthful generations within unlabeled mixture data, thereby enabling the training of a binary classifier on top. Importantly, our framework does not require extra data collection and human annotations, offering strong flexibility and practicality for real-world applications. Extensive experiments show that HaloScope can achieve superior hallucination detection performance, outperforming the competitive rivals by a significant margin.