---
title: "FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0235cbb8cd6425d0b55daefce388fc0b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['privacy-preserving-federated-distributed-learning', 'llm-benchmarks-for-clinical-healthcare']
tags: ['federated-learning', 'medical-foundation-models', 'knowledge-injection']
venue: "NeurIPS 2024"
tldr: "FedMEKI benchmarks privacy-preserving integration of medical knowledge into foundation models using cross-silo federated learning."
---

# FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0235cbb8cd6425d0b55daefce388fc0b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/0235cbb8cd6425d0b55daefce388fc0b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: FedMEKI benchmarks privacy-preserving integration of medical knowledge into foundation models using cross-silo federated learning.

## Abstract

This study introduces the Federated Medical Knowledge Injection (FedMEKI) platform, a new benchmark designed to address the unique challenges of integrating medical knowledge into foundation models under privacy constraints. By leveraging a cross-silo federated learning approach, FedMEKI circumvents the issues associated with centralized data collection, which is often prohibited under health regulations like the Health Insurance Portability and Accountability Act (HIPAA) in the USA. The platform is meticulously designed to handle multi-site, multi-modal, and multi-task medical data, which includes 7 medical modalities, including images, signals, texts, laboratory test results, vital signs, input variables, and output variables. The curated dataset to validate FedMEKI covers 8 medical tasks, including 6 classification tasks (lung opacity detection, COVID-19 detection, electrocardiogram (ECG) abnormal detection, mortality prediction, sepsis protection, and enlarged cardiomediastinum detection) and 2 generation tasks (medical visual question answering (MedVQA) and ECG noise clarification). This comprehensive dataset is partitioned across several clients to facilitate the decentralized training process under 16 benchmark approaches. FedMEKI not only preserves data privacy but also enhances the capability of medical foundation models by allowing them to learn from a broader spectrum of medical knowledge without direct data exposure, thereby setting a new benchmark in the application of foundation models within the healthcare sector.