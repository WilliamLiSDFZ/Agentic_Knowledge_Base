---
title: "Online Adaptation of Language Models with a Memory of Amortized Contexts"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/eaf956b52bae51fbf387b8be4cc3ce18-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'online-learning-augmented-algorithms-and-optimization']
tags: ['online-learning', 'language-model-adaptation', 'amortized-contexts']
venue: "NeurIPS 2024"
tldr: "Proposes an online adaptation method for LLMs using a memory of amortized contexts to keep models updated with new information efficiently."
---

# Online Adaptation of Language Models with a Memory of Amortized Contexts

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/eaf956b52bae51fbf387b8be4cc3ce18-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/eaf956b52bae51fbf387b8be4cc3ce18-Abstract-Conference.html)

**TLDR**: Proposes an online adaptation method for LLMs using a memory of amortized contexts to keep models updated with new information efficiently.

## Abstract

Due to the rapid generation and dissemination of information, large language models (LLMs) quickly run out of date despite enormous development costs. To address the crucial need to keep models updated, online learning has emerged as a critical tool when utilizing LLMs for real-world applications. However, given the ever-expanding corpus of unseen documents and the large parameter space of modern LLMs, efficient adaptation is essential. To address these challenges, we propose Memory of Amortized Contexts (MAC), an efficient and effective online adaptation framework for LLMs with strong knowledge retention. We propose a feature extraction and memory-augmentation approach to compress and extract information from new documents into compact modulations stored in a memory bank. When answering questions, our model attends to and extracts relevant knowledge from this memory bank. To learn informative modulations in an efficient manner, we utilize amortization-based meta-learning, which substitutes an otherwise required optimization process with a single forward pass of the encoder. Subsequently, we learn to choose from and aggregate selected documents into a single modulation by conditioning on the question, allowing us to adapt a frozen language model during test time without requiring further gradient updates. Our experiment demonstrates the superiority of MAC in multiple aspects, including online adaptation performance, time, and memory efficiency. In addition, we show how MAC can be combined with and improve the performance of popular alternatives such as retrieval augmented generations (RAGs). Code is available at: https://github.com/jihoontack/MAC.