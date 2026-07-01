---
title: "FinBen: A Holistic Financial Benchmark for Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/adb1d9fa8be4576d28703b396b82ba1b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-benchmarks-for-clinical-healthcare']
tags: ['financial-benchmark', 'llm-evaluation', 'nlp']
venue: "NeurIPS 2024"
tldr: "Introduces FinBen, the first comprehensive open-source benchmark for evaluating LLMs across diverse financial tasks."
---

# FinBen: A Holistic Financial Benchmark for Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/adb1d9fa8be4576d28703b396b82ba1b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/adb1d9fa8be4576d28703b396b82ba1b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces FinBen, the first comprehensive open-source benchmark for evaluating LLMs across diverse financial tasks.

## Abstract

LLMs have transformed NLP and shown promise in various fields, yet their potential in finance is underexplored due to a lack of comprehensive benchmarks, the rapid development of LLMs, and the complexity of financial tasks. In this paper, we introduce FinBen, the first extensive open-source evaluation benchmark, including 42 datasets spanning 24 financial tasks, covering eight critical aspects: information extraction (IE), textual analysis, question answering (QA), text generation, risk management, forecasting, decision-making, and bilingual (English and Spanish). FinBen offers several key innovations: a broader range of tasks and datasets, the first evaluation of stock trading, novel agent and Retrieval-Augmented Generation (RAG) evaluation, and two novel datasets for regulations and stock trading. Our evaluation of 21 representative LLMs, including GPT-4, ChatGPT, and the latest Gemini, reveals several key findings: While LLMs excel in IE and textual analysis, they struggle with advanced reasoning and complex tasks like text generation and forecasting. GPT-4 excels in IE and stock trading, while Gemini is better at text generation and forecasting. Instruction-tuned LLMs improve textual analysis but offer limited benefits for complex tasks such as QA. FinBen has been used to host the first financial LLMs shared task at the FinNLP-AgentScen workshop during IJCAI-2024, attracting 12 teams. Their novel solutions outperformed GPT-4, showcasing FinBen's potential to drive innovations in financial LLMs. All datasets and code are publicly available for the research community, with results shared and updated regularly on the Open Financial LLM Leaderboard.