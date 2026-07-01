---
title: "Large Language Models' Expert-level Global History Knowledge Benchmark (HiST-LLM)"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/38cc5cba8e513547b96bc326e25610dc-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-benchmarks-for-clinical-healthcare']
tags: ['llm-benchmark', 'history-knowledge', 'humanities']
venue: "NeurIPS 2024"
tldr: "Introduces HiST-LLM, a benchmark evaluating expert-level global history knowledge and comprehension in large language models."
---

# Large Language Models' Expert-level Global History Knowledge Benchmark (HiST-LLM)

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/38cc5cba8e513547b96bc326e25610dc-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/38cc5cba8e513547b96bc326e25610dc-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces HiST-LLM, a benchmark evaluating expert-level global history knowledge and comprehension in large language models.

## Abstract

Large Language Models (LLMs) have the potential to transform humanities and social science research, yet their history knowledge and comprehension at a graduate level remains untested. Benchmarking LLMs in history is particularly challenging, given that human knowledge of history is inherently unbalanced, with more information available on Western history and recent periods. We introduce the History Seshat Test for LLMs (HiST-LLM), based on a subset of the Seshat Global History Databank, which provides a structured representation of human historical knowledge, containing 36,000 data points across 600 historical societies and over 2,700 scholarly references. This dataset covers every major world region from the Neolithic period to the Industrial Revolution and includes information reviewed and assembled by history experts and graduate research assistants. Using this dataset, we benchmark a total of seven models from the Gemini, OpenAI, and Llama families. We find that, in a four-choice format, LLMs have a balanced accuracy ranging from 33.6% (Llama-3.1-8B) to 46% (GPT-4-Turbo), outperforming random guessing (25%) but falling short of expert comprehension. LLMs perform better on earlier historical periods. Regionally, performance is more even but still better for the Americas and lowest in Oceania and Sub-Saharan Africa for the more advanced models. Our benchmark shows that while LLMs possess some expert-level historical knowledge, there is considerable room for improvement.