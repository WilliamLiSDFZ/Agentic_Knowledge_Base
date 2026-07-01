---
title: "AsyncDiff: Parallelizing Diffusion Models by Asynchronous Denoising"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ad15848baa3932c0d2deabf0e11d1dcd-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference']
tags: ['diffusion-models', 'parallel-inference', 'asynchronous-denoising', 'latency-reduction', 'acceleration']
venue: "NeurIPS 2024"
tldr: "AsyncDiff parallelizes diffusion model inference via asynchronous denoising across devices to reduce cumulative generation latency."
---

# AsyncDiff: Parallelizing Diffusion Models by Asynchronous Denoising

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ad15848baa3932c0d2deabf0e11d1dcd-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ad15848baa3932c0d2deabf0e11d1dcd-Abstract-Conference.html)

**TLDR**: AsyncDiff parallelizes diffusion model inference via asynchronous denoising across devices to reduce cumulative generation latency.

## Abstract

Diffusion models have garnered significant interest from the community for their great generative ability across various applications. However, their typical multi-step sequential-denoising nature gives rise to high cumulative latency, thereby precluding the possibilities of parallel computation. To address this, we introduce AsyncDiff, a universal and plug-and-play acceleration scheme that enables model parallelism across multiple devices. Our approach divides the cumbersome noise prediction model into multiple components, assigning each to a different device. To break the dependency chain between these components, it transforms the conventional sequential denoising into an asynchronous process by exploiting the high similarity between hidden states in consecutive diffusion steps. Consequently, each component is facilitated to compute in parallel on separate devices. The proposed strategy significantly reduces inference latency while minimally impacting the generative quality. Specifically, for the Stable Diffusion v2.1, AsyncDiff achieves a 2.7x speedup with negligible degradation and a 4.0x speedup with only a slight reduction of 0.38 in CLIP Score, on four NVIDIA A5000 GPUs. Our experiments also demonstrate AsyncDiff can be readily applied to video diffusion models with encouraging performances.