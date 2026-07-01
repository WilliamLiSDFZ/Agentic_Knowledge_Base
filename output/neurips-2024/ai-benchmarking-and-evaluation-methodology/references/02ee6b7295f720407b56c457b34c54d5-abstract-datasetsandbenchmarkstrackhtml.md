---
title: "SciInstruct: a Self-Reflective Instruction Annotated Dataset for Training Scientific Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/02ee6b7295f720407b56c457b34c54d5-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-training-and-optimization-techniques', 'ai-benchmarking-and-evaluation-methodology']
tags: ['scientific-llm', 'self-reflective-annotation', 'instruction-tuning']
venue: "NeurIPS 2024"
tldr: "A self-reflective instruction-annotated dataset for training LLMs to better handle scientific concepts, equations, and calculations."
---

# SciInstruct: a Self-Reflective Instruction Annotated Dataset for Training Scientific Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/02ee6b7295f720407b56c457b34c54d5-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/02ee6b7295f720407b56c457b34c54d5-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A self-reflective instruction-annotated dataset for training LLMs to better handle scientific concepts, equations, and calculations.

## Abstract

Large Language Models (LLMs) have shown promise in assisting scientific discovery. However, such applications are currently limited by LLMs' deficiencies in understanding intricate scientific concepts, deriving symbolic equations, and solving advanced numerical calculations. To bridge these gaps, we introduce SciInstruct, a suite of scientific instructions for training scientific language models capable of college-level scientific reasoning. Central to our approach is a novel self-reflective instruction annotation framework to address the data scarcity challenge in the science domain. This framework leverages existing LLMs to generate step-by-step reasoning for unlabelled scientific questions, followed by a process of self-reflective critic-and-revise. Applying this framework, we curated a diverse and high-quality dataset encompassing physics, chemistry, math, and formal proofs. We analyze the curated SciInstruct from multiple interesting perspectives (e.g., domain, scale, source, question type, answer length, etc.). To verify the effectiveness of SciInstruct, we fine-tuned different language models with SciInstruct, i.e., ChatGLM3 (6B and 32B), Llama3-8B-Instruct, and Mistral-7B: MetaMath, enhancing their scientific and mathematical reasoning capabilities, without sacrificing the language understanding capabilities of the base model. We release all codes and SciInstruct at https://github.com/THUDM/SciGLM.