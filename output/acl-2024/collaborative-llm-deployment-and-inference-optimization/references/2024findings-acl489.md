---
title: "BASS: Batched Attention-optimized Speculative Sampling"
source: "https://aclanthology.org/2024.findings-acl.489/"
categories: ['collaborative-llm-deployment-and-inference-optimization', 'transformer-architecture-analysis-and-design']
tags: ['speculative-decoding', 'batched-inference', 'throughput-optimization']
venue: "ACL 2024"
tldr: "Proposes BASS, a batched attention-optimized speculative sampling method to improve LLM inference latency and throughput."
---

# BASS: Batched Attention-optimized Speculative Sampling

**Source**: [https://aclanthology.org/2024.findings-acl.489/](https://aclanthology.org/2024.findings-acl.489/)

**TLDR**: Proposes BASS, a batched attention-optimized speculative sampling method to improve LLM inference latency and throughput.

## Abstract

AbstractSpeculative decoding has emerged as a powerful method to improve latency and throughput in hosting large language models. However, most existing implementations focus on generating a single sequence. Real-world generative AI applications often require multiple responses and how to perform speculative decoding in a batched setting while preserving its latency benefits poses non-trivial challenges. This paper describes a system of batched speculative decoding that sets a new state of the art in multi-sequence generation latency and that demonstrates superior GPU utilization as well as quality of generations within a time budget. For example, for a 7.8B-size model on a single A100 GPU and with a batch size of 8, each sequence is generated at an average speed of 5.8ms per token, the overall throughput being 1.1K tokens per second. These results represent state-of-the-art latency and a 2.15× speed-up over optimized regular decoding. Within a time budget that regular decoding does not finish, our system is able to generate sequences with HumanEval Pass@First of 43% and Pass@All of 61%, far exceeding what’s feasible with single-sequence speculative decoding. Our peak GPU utilization during decoding reaches as high as 15.8%, more than 3× the highest of that of regular decoding and around 10× of single-sequence speculative decoding.