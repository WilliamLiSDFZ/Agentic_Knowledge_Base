---
title: "LinguaLinked: Distributed Large Language Model Inference on Mobile Devices"
source: "https://aclanthology.org/2024.acl-demos.16/"
categories: ['collaborative-llm-deployment-and-inference-optimization']
tags: ['distributed-inference', 'mobile-devices', 'LLM-deployment', 'decentralized']
venue: "ACL 2024"
tldr: "LinguaLinked enables decentralized distributed LLM inference across mobile devices to overcome individual memory constraints."
---

# LinguaLinked: Distributed Large Language Model Inference on Mobile Devices

**Source**: [https://aclanthology.org/2024.acl-demos.16/](https://aclanthology.org/2024.acl-demos.16/)

**TLDR**: LinguaLinked enables decentralized distributed LLM inference across mobile devices to overcome individual memory constraints.

## Abstract

AbstractDeploying Large Language Models (LLMs) locally on mobile devices presents a significant challenge due to their extensive memory requirements. In this paper, we introduce LinguaLinked, a system for decentralized, distributed LLM inference on mobile devices. LinguaLinked enables collaborative execution of the inference task across multiple trusted devices and ensures data privacy by processing information locally. LinguaLinked uses three key strategies. First, an optimized model assignment technique segments LLMs and uses linear optimization to align segments with each device's capabilities. Second, an optimized data transmission mechanism ensures efficient and structured data flow between model segments while also maintaining the integrity of the original model structure. Finally, LinguaLinked incorporates a runtime load balancer that actively monitors and redistributes tasks among mobile devices to prevent bottlenecks, enhancing the system's overall efficiency and responsiveness. We demonstrate that LinguaLinked facilitates efficient LLM inference while maintaining consistent throughput and minimal latency through extensive testing across various mobile devices, from high-end to low-end Android devices.