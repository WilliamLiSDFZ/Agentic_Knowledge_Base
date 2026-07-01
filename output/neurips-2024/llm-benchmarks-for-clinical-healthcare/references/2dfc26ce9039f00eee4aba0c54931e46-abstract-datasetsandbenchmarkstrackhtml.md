---
title: "UltraMedical: Building Specialized Generalists in Biomedicine"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2dfc26ce9039f00eee4aba0c54931e46-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-benchmarks-for-clinical-healthcare']
tags: ['biomedical-llm', 'specialized-generalist', 'fine-tuning']
venue: "NeurIPS 2024"
tldr: "UltraMedical builds specialized yet generalizable biomedical LLMs by curating high-quality domain data and training strategies targeting clinical and scientific tasks."
---

# UltraMedical: Building Specialized Generalists in Biomedicine

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2dfc26ce9039f00eee4aba0c54931e46-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/2dfc26ce9039f00eee4aba0c54931e46-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: UltraMedical builds specialized yet generalizable biomedical LLMs by curating high-quality domain data and training strategies targeting clinical and scientific tasks.

## Abstract

Large Language Models (LLMs) have demonstrated remarkable capabilities across various domains and are moving towards more specialized areas. Recent advanced proprietary models such as GPT-4 and Gemini have achieved significant advancements in biomedicine, which have also raised privacy and security challenges. The construction of specialized generalists hinges largely on high-quality datasets, enhanced by techniques like supervised fine-tuning and reinforcement learning from human or AI feedback, and direct preference optimization. However, these leading technologies (e.g., preference learning) are still significantly limited in the open source community due to the scarcity of specialized data. In this paper, we present the UltraMedical collections, which consist of high-quality manual and synthetic datasets in the biomedicine domain, featuring preference annotations across multiple advanced LLMs. By utilizing these datasets, we fine-tune a suite of specialized medical models based on Llama-3 series, demonstrating breathtaking capabilities across various medical benchmarks. Moreover, we develop powerful reward models skilled in biomedical and general reward benchmark, enhancing further online preference learning within the biomedical LLM community.