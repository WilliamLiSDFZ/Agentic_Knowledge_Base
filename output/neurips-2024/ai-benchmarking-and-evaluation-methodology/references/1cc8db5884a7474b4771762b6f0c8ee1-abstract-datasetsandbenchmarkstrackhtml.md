---
title: "Stress-Testing Long-Context Language Models with Lifelong ICL and Task Haystack"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1cc8db5884a7474b4771762b6f0c8ee1-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-training-and-optimization-techniques']
tags: ['long-context-llm', 'in-context-learning', 'evaluation-suite']
venue: "NeurIPS 2024"
tldr: "Lifelong ICL and Task Haystack are introduced to stress-test and diagnose how long-context language models utilize context across sequential tasks."
---

# Stress-Testing Long-Context Language Models with Lifelong ICL and Task Haystack

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1cc8db5884a7474b4771762b6f0c8ee1-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1cc8db5884a7474b4771762b6f0c8ee1-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Lifelong ICL and Task Haystack are introduced to stress-test and diagnose how long-context language models utilize context across sequential tasks.

## Abstract

We introduce Lifelong ICL, a problem setting that challenges long-context language models (LMs) to learn a sequence of language tasks through in-context learning (ICL). We further introduce Task Haystack, an evaluation suite dedicated to assessing and diagnosing how long-context LMs utilizes contexts in Lifelong ICL. When given a task instruction and test inputs, long-context LMs are expectedto leverage the relevant demonstrations in the Lifelong ICL prompt, avoid distraction and interference from other tasks, and achieve test accuracies that are not significantly worse than those of the Single-task ICL baseline.Task Haystack draws inspiration from the widely-adopted “needle-in-a-haystack” (NIAH) evaluation, but presents distinct new challenges. It requires models (1) to utilize the contexts at a deeper level, rather than resorting to simple copying and pasting; (2) to navigate through long streams of evolving topics and tasks, proxying the complexities and dynamism of contexts in real-world scenarios. Additionally, Task Haystack inherits the controllability of NIAH, providing model developers with tools and visualizations to identify model vulnerabilities effectively.We benchmark 14 long-context LMs using Task Haystack, finding that frontier models like GPT-4o still struggle with the setting, failing on 15% of cases on average. Most open-weight models further lack behind by a large margin, with failure rates reaching up to 61%. In our controlled analysis, we identify factors such as distraction and recency bias as contributors to these failure cases. Further, performance declines when task instructions are paraphrased at test time or when ICL demonstrations are repeated excessively, raising concerns about the robustness, instruction understanding, and true context utilization of long-context LMs. We release our code and data to encourage future research that investigates and addresses these limitations.