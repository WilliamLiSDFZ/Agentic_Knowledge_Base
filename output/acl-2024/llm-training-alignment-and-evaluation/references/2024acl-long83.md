---
title: "WaterBench: Towards Holistic Evaluation of Watermarks for Large Language Models"
source: "https://aclanthology.org/2024.acl-long.83/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llm-security-robustness-and-detection']
tags: ['watermarking', 'llm-evaluation', 'text-generation']
venue: "ACL 2024"
tldr: "WaterBench provides a holistic benchmark for evaluating LLM watermarking algorithms across generation quality and detection robustness."
---

# WaterBench: Towards Holistic Evaluation of Watermarks for Large Language Models

**Source**: [https://aclanthology.org/2024.acl-long.83/](https://aclanthology.org/2024.acl-long.83/)

**TLDR**: WaterBench provides a holistic benchmark for evaluating LLM watermarking algorithms across generation quality and detection robustness.

## Abstract

AbstractTo mitigate the potential misuse of large language models (LLMs), recent research has developed watermarking algorithms, which restrict the generation process to leave an invisible trace for watermark detection. Due to the two-stage nature of the task, most studies evaluate the generation and detection separately, thereby presenting a challenge in unbiased, thorough, and applicable evaluations. In this paper, we introduce WaterBench, the first comprehensive benchmark for LLM watermarks, in which we design three crucial factors: (1) For benchmarking procedure, to ensure an apples-to-apples comparison, we first adjust each watermarking method’s hyper-parameter to reach the same watermarking strength, then jointly evaluate their generation and detection performance. (2) For task selection, we diversify the input and output length to form a five-category taxonomy, covering 9 tasks. (3) For evaluation metric, we adopt the GPT4-Judge for automatically evaluating the decline of instruction-following abilities after watermarking. We evaluate 4 open-source watermarks on 2 LLMs under 2 watermarking strengths and observe the common struggles for current methods on maintaining the generation quality. The code and data are available at https://github.com/THU-KEG/WaterBench.