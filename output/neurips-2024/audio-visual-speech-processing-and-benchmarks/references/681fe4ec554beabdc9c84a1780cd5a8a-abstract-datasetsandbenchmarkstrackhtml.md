---
title: "SD-Eval: A  Benchmark Dataset for Spoken Dialogue Understanding Beyond Words"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/681fe4ec554beabdc9c84a1780cd5a8a-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['audio-visual-speech-processing-and-benchmarks', 'ai-benchmarking-and-evaluation-methodology']
tags: ['spoken-dialogue', 'benchmark', 'paralinguistic', 'speech-understanding', 'chat-llm']
venue: "NeurIPS 2024"
tldr: "SD-Eval is a benchmark dataset for evaluating spoken dialogue understanding beyond textual content, covering paralinguistic and environmental speech information."
---

# SD-Eval: A  Benchmark Dataset for Spoken Dialogue Understanding Beyond Words

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/681fe4ec554beabdc9c84a1780cd5a8a-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/681fe4ec554beabdc9c84a1780cd5a8a-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: SD-Eval is a benchmark dataset for evaluating spoken dialogue understanding beyond textual content, covering paralinguistic and environmental speech information.

## Abstract

Speech encompasses a wealth of information, including but not limited to content, paralinguistic, and environmental information.This comprehensive nature of speech significantly impacts communication and is crucial for human-computer interaction.Chat-Oriented Large Language Models (LLMs), known for their general-purpose assistance capabilities, have evolved to handle multi-modal inputs, including speech.Although these models can be adept at recognizing and analyzing speech, they often fall short of generating appropriate responses.We argue that this is due to the lack of principles on task definition and model development, which requires open-source datasets and metrics suitable for model evaluation.To bridge the gap, we present SD-Eval, a benchmark dataset aimed at multidimensional evaluation of spoken dialogue understanding and generation.SD-Eval focuses on paralinguistic and environmental information and includes 7,303 utterances, amounting to 8.76 hours of speech data. The data is aggregated from eight public datasets, representing four perspectives: emotion, accent, age, and background sound.To assess the SD-Eval benchmark dataset, we implement three different models and construct a training set following a process similar to that of SD-Eval. The training set contains 1,052.72 hours of speech data and 724.4k utterances. We also conduct a comprehensive evaluation using objective evaluation methods (e.g. BLEU and ROUGE), subjective evaluations and LLM-based metrics for the generated responses.Models conditioned with paralinguistic and environmental information outperform their counterparts in both objective and subjective measures.Moreover, experiments demonstrate that LLM-based metrics show a higher correlation with human evaluation compared to traditional metrics.We open-source SD-Eval at https://github.com/amphionspace/SD-Eval.