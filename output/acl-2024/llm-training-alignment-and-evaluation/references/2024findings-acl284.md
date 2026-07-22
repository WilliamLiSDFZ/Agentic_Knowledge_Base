---
title: "Instruction Tuning with Retrieval-based Examples Ranking for Aspect-based Sentiment Analysis"
source: "https://aclanthology.org/2024.findings-acl.284/"
categories: ['multilingual-text-classification-and-sentiment-analysis', 'llm-training-alignment-and-evaluation']
tags: ['aspect-based-sentiment-analysis', 'instruction-tuning', 'retrieval-augmented-examples']
venue: "ACL 2024"
tldr: "Proposes retrieval-based example ranking for instruction tuning to improve LLM performance on aspect-based sentiment analysis tasks."
---

# Instruction Tuning with Retrieval-based Examples Ranking for Aspect-based Sentiment Analysis

**Source**: [https://aclanthology.org/2024.findings-acl.284/](https://aclanthology.org/2024.findings-acl.284/)

**TLDR**: Proposes retrieval-based example ranking for instruction tuning to improve LLM performance on aspect-based sentiment analysis tasks.

## Abstract

AbstractAspect-based sentiment analysis (ABSA) identifies sentiment information related to specific aspects and provides deeper market insights to businesses and organizations. With the emergence of large language models (LMs), recent studies have proposed using fixed examples for instruction tuning to reformulate ABSA as a generation task. However, the performance is sensitive to the selection of in-context examples; several retrieval methods are based on surface similarity and are independent of the LM generative objective. This study proposes an instruction learning method with retrieval-based example ranking for ABSA tasks. For each target sample, an LM was applied as a scorer to estimate the likelihood of the output given the input and a candidate example as the prompt, and training examples were labeled as positive or negative by ranking the scores. An alternating training schema is proposed to train both the retriever and LM. Instructional prompts can be constructed using high-quality examples. The LM is used for both scoring and inference, improving the generation efficiency without incurring additional computational costs or training difficulties. Extensive experiments on three ABSA subtasks verified the effectiveness of the proposed method, demonstrating its superiority over various strong baseline models. Code and data are released at https://github.com/zgMin/IT-RER-ABSA.