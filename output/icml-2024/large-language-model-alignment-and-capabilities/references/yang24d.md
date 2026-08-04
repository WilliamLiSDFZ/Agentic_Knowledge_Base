---
title: "DoraemonGPT: Toward Understanding Dynamic Scenes with Large Language Models (Exemplified as A Video Agent)"
source: "https://proceedings.mlr.press/v235/yang24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24d/yang24d.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['video-understanding', 'LLM-agent', 'dynamic-scene-analysis']
venue: "ICML 2024"
tldr: "Presents DoraemonGPT, an LLM-driven video agent for understanding dynamic scenes through task-guided symbolic reasoning and tool use."
---

# DoraemonGPT: Toward Understanding Dynamic Scenes with Large Language Models (Exemplified as A Video Agent)

**Source**: [https://proceedings.mlr.press/v235/yang24d.html](https://proceedings.mlr.press/v235/yang24d.html)

**TLDR**: Presents DoraemonGPT, an LLM-driven video agent for understanding dynamic scenes through task-guided symbolic reasoning and tool use.

## Abstract

Recent LLM-driven visual agents mainly focus on solving image-based tasks, which limits their ability to understand dynamic scenes, making it far from real-life applications like guiding students in laboratory experiments and identifying their mistakes. Hence, this paper explores DoraemonGPT, a comprehensive and conceptually elegant system driven by LLMs to understand dynamic scenes. Considering the video modality better reflects the ever-changing nature of real-world scenarios, we exemplify DoraemonGPT as a video agent. Given a video with a question/task, DoraemonGPT begins by converting the input video into a symbolic memory that stores task-related attributes. This structured representation allows for spatial-temporal querying and reasoning by well-designed sub-task tools, resulting in concise intermediate results. Recognizing that LLMs have limited internal knowledge when it comes to specialized domains (e.g., analyzing the scientific principles underlying experiments), we incorporate plug-and-play tools to assess external knowledge and address tasks across different domains. Moreover, a novel LLM-driven planner based on Monte Carlo Tree Search is introduced to explore the large planning space for scheduling various tools. The planner iteratively finds feasible solutions by backpropagating the result’s reward, and multiple solutions can be summarized into an improved final answer. We extensively evaluate DoraemonGPT’s effectiveness on three benchmarks and several in-the-wild scenarios. Project page: https://z-x-yang.github.io/doraemon-gpt.