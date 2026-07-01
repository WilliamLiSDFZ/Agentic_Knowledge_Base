---
title: "Bias and Volatility: A Statistical Framework for Evaluating Large Language Model's Stereotypes and the Associated Generation Inconsistency"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c6ec4a25a11393f277cfd64b7ea4d106-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-values-ethics-alignment-evaluation', 'statistical-inference-and-text-generation-methods\n\nhmm,-let-me-reconsider---looking-more-carefully-at-the-cluster:\n\n**score-matching-and-sampling-methods**']
tags: ['llm-bias', 'stereotype-evaluation', 'generation-inconsistency']
venue: "NeurIPS 2024"
tldr: "Presents a statistical framework quantifying bias and generation volatility in LLM stereotypes by modeling randomness in model outputs."
---

# Bias and Volatility: A Statistical Framework for Evaluating Large Language Model's Stereotypes and the Associated Generation Inconsistency

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c6ec4a25a11393f277cfd64b7ea4d106-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c6ec4a25a11393f277cfd64b7ea4d106-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents a statistical framework quantifying bias and generation volatility in LLM stereotypes by modeling randomness in model outputs.

## Abstract

We present a novel statistical framework for analyzing stereotypes in large language models (LLMs) by systematically estimating the bias and variation in their generation. Current evaluation metrics in the alignment literature often overlook the randomness of stereotypes caused by the inconsistent generative behavior of LLMs. For example, this inconsistency can result in LLMs displaying contradictory stereotypes, including those related to gender or race, for identical professions across varied contexts. Neglecting such inconsistency could lead to misleading conclusions in alignment evaluations and hinder the accurate assessment of the risk of LLM applications perpetuating or amplifying social stereotypes and unfairness.This work proposes a Bias-Volatility Framework (BVF) that estimates the probability distribution function of LLM stereotypes. Specifically, since the stereotype distribution fully captures an LLM's generation variation, BVF enables the assessment of both the likelihood and extent to which its outputs are against vulnerable groups, thereby allowing for the quantification of the LLM's aggregated discrimination risk. Furthermore, we introduce a mathematical framework to decompose an LLM’s aggregated discrimination risk into two components: bias risk and volatility risk, originating from the mean and variation of LLM’s stereotype distribution, respectively. We apply BVF to assess 12 commonly adopted LLMs and compare their risk levels. Our findings reveal that:  i) Bias risk is the primary cause of discrimination risk in LLMs; ii) Most LLMs exhibit significant pro-male stereotypes for nearly all careers; iii) Alignment with reinforcement learning from human feedback lowers discrimination by reducing bias, but increases volatility; iv) Discrimination risk in LLMs correlates with key sociol-economic factors like professional salaries. Finally, we emphasize that BVF can also be used to assess other dimensions of generation inconsistency's impact on LLM behavior beyond stereotypes, such as knowledge mastery.