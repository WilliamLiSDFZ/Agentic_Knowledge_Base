---
title: "EasyEdit: An Easy-to-use Knowledge Editing Framework for Large Language Models"
source: "https://aclanthology.org/2024.acl-demos.9/"
categories: ['llm-training-alignment-and-evaluation', 'llm-hallucination-detection-and-mitigation']
tags: ['knowledge-editing', 'LLM-frameworks', 'knowledge-cutoff']
venue: "ACL 2024"
tldr: "Presents EasyEdit, a unified framework for easily applying and evaluating knowledge editing methods in large language models."
---

# EasyEdit: An Easy-to-use Knowledge Editing Framework for Large Language Models

**Source**: [https://aclanthology.org/2024.acl-demos.9/](https://aclanthology.org/2024.acl-demos.9/)

**TLDR**: Presents EasyEdit, a unified framework for easily applying and evaluating knowledge editing methods in large language models.

## Abstract

AbstractLarge Language Models (LLMs) usually suffer from knowledge cutoff or fallacy issues, which means they are unaware of unseen events or generate text with incorrect facts owing to outdated/noisy data. To this end, many knowledge editing approaches for LLMs have emerged – aiming to subtly inject/edit updated knowledge or adjust undesired behavior while minimizing the impact on unrelated inputs. Nevertheless, due to significant differences among various knowledge editing methods and the variations in task setups, there is no standard implementation framework available for the community, which hinders practitioners from applying knowledge editing to applications. To address these issues, we propose EasyEdit, an easy-to-use knowledge editing framework for LLMs. It supports various cutting-edge knowledge editing approaches and can be readily applied to many well-known LLMs such as T5, GPT-J, LlaMA, etc. Empirically, we report the knowledge editing results on LlaMA-2 with EasyEdit, demonstrating that knowledge editing surpasses traditional fine-tuning in terms of reliability and generalization. We have released the source code on GitHub, along with Google Colab tutorials and comprehensive documentation for beginners to get started. Besides, we present an online system for real-time knowledge editing, and a demo video.