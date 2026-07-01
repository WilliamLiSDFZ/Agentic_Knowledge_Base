---
title: "Semantic Density: Uncertainty Quantification for Large Language Models through Confidence Measurement in Semantic Space"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f26d4fbaf7dfa115f1d4b3f104e26bce-Abstract-Conference.html"
categories: ['machine-learning-theory-and-evaluation-methods', 'llm-training-and-optimization-techniques']
tags: ['uncertainty-quantification', 'hallucination', 'semantic-density']
venue: "NeurIPS 2024"
tldr: "Proposes semantic density, a confidence measure in semantic space to quantify uncertainty and detect hallucinations in large language model outputs."
---

# Semantic Density: Uncertainty Quantification for Large Language Models through Confidence Measurement in Semantic Space

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f26d4fbaf7dfa115f1d4b3f104e26bce-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/f26d4fbaf7dfa115f1d4b3f104e26bce-Abstract-Conference.html)

**TLDR**: Proposes semantic density, a confidence measure in semantic space to quantify uncertainty and detect hallucinations in large language model outputs.

## Abstract

With the widespread application of Large Language Models (LLMs) to various domains, concerns regarding the trustworthiness of LLMs in safety-critical scenarios have been raised, due to their unpredictable tendency to hallucinate and generate misinformation. Existing LLMs do not have an inherent functionality to provide the users with an uncertainty/confidence metric for each response it generates, making it difficult to evaluate trustworthiness. Although several studies aim to develop uncertainty quantification methods for LLMs, they have fundamental limitations, such as being restricted to classification tasks, requiring additional training and data, considering only lexical instead of semantic information, and being prompt-wise but not response-wise. A new framework is proposed in this paper to address these issues. Semantic density extracts uncertainty/confidence information for each response from a probability distribution perspective in semantic space. It has no restriction on task types and is "off-the-shelf" for new models and tasks. Experiments on seven state-of-the-art LLMs, including the latest Llama 3 and Mixtral-8x22B models, on four free-form question-answering benchmarks demonstrate the superior performance and robustness of semantic density compared to prior approaches.