---
title: "FedBPT: Efficient Federated Black-box Prompt Tuning for Large Language Models"
source: "https://proceedings.mlr.press/v235/sun24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24j/sun24j.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'large-language-model-alignment-and-capabilities']
tags: ['federated-learning', 'black-box-prompt-tuning', 'LLM', 'privacy', 'NLP']
venue: "ICML 2024"
tldr: "FedBPT enables efficient federated black-box prompt tuning of large language models without exposing private client data or model internals."
---

# FedBPT: Efficient Federated Black-box Prompt Tuning for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/sun24j.html](https://proceedings.mlr.press/v235/sun24j.html)

**TLDR**: FedBPT enables efficient federated black-box prompt tuning of large language models without exposing private client data or model internals.

## Abstract

Pre-trained language models (PLM) have revolutionized the NLP landscape, achieving stellar performances across diverse tasks. These models, while benefiting from vast training data, often require fine-tuning on specific data to cater to distinct downstream tasks. However, this data adaptation process has inherent security and privacy concerns, primarily when leveraging user-generated, device-residing data. Federated learning (FL) provides a solution, allowing collaborative model fine-tuning without centralized data collection. However, applying FL to finetune PLMs is hampered by challenges, including restricted model parameter access due to the high encapsulation, high computational requirements, and communication overheads. This paper introduces Federated Black-box Prompt Tuning (FedBPT), a framework designed to address these challenges. FedBPT allows the clients to treat the model as a black-box inference API. By focusing on training optimal prompts and utilizing gradient-free optimization methods, FedBPT reduces the number of exchanged variables, boosts communication efficiency, and minimizes computational and storage costs. Experiments highlight the framework’s ability to drastically cut communication and memory costs while maintaining competitive performance. Ultimately, FedBPT presents a promising solution for efficient, privacy-preserving fine-tuning of PLM in the age of large language models.