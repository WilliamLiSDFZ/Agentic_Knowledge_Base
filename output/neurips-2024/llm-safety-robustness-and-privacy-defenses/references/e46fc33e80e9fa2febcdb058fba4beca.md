---
title: "HuRef: HUman-REadable Fingerprint for Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e46fc33e80e9fa2febcdb058fba4beca-Abstract-Conference.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'llm-training-and-optimization-techniques']
tags: ['LLM-fingerprinting', 'copyright-protection', 'model-identification']
venue: "NeurIPS 2024"
tldr: "HuRef introduces a human-readable fingerprint for identifying base LLMs despite parameter alterations, aiding copyright protection."
---

# HuRef: HUman-REadable Fingerprint for Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e46fc33e80e9fa2febcdb058fba4beca-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/e46fc33e80e9fa2febcdb058fba4beca-Abstract-Conference.html)

**TLDR**: HuRef introduces a human-readable fingerprint for identifying base LLMs despite parameter alterations, aiding copyright protection.

## Abstract

Protecting the copyright of large language models (LLMs) has become crucial due to their resource-intensive training and accompanying carefully designed licenses. However, identifying the original base model of an LLM is challenging due to potential parameter alterations. In thisstudy, we introduce HuRef, a human-readable fingerprint for LLMs that uniquely identifies the base model without interfering with training or exposing model parameters to the public.We first observe that the vector direction of LLM parameters remains stable after the model has converged during pretraining, with negligible perturbations through subsequent training steps, including continued pretraining, supervised fine-tuning, and RLHF, which makes it a sufficient conditionto identify the base model.The necessity is validated by continuing to train an LLM with an extra term to drive away the model parameters' direction and the model becomes damaged. However, this direction is vulnerable to simple attacks like dimension permutation or matrix rotation, which significantly change it without affecting performance. To address this, leveraging the Transformer structure, we systematically analyze potential attacks and define three invariant terms that identify an LLM's base model. Due to the potential risk of information leakage, we cannot publish invariant terms directly. Instead, we map them to a Gaussian vector using an encoder, then convert it into a natural image using StyleGAN2, and finally publish the image. In our black-box setting, all fingerprinting steps are internally conducted by the LLMs owners. To ensure the published fingerprints are honestly generated, we introduced Zero-Knowledge Proof (ZKP).Experimental results across various LLMs demonstrate the effectiveness of our method. The code is available at https://github.com/LUMIA-Group/HuRef.