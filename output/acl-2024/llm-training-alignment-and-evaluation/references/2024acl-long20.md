---
title: "Confidence Under the Hood: An Investigation into the Confidence-Probability Alignment in Large Language Models"
source: "https://aclanthology.org/2024.acl-long.20/"
categories: ['llms-for-biomedical-and-clinical-nlp', 'llm-training-alignment-and-evaluation']
tags: ['confidence-calibration', 'LLM-reliability', 'probability-alignment']
venue: "ACL 2024"
tldr: "An investigation into the alignment between LLMs' expressed confidence and actual probability estimates for their outputs."
---

# Confidence Under the Hood: An Investigation into the Confidence-Probability Alignment in Large Language Models

**Source**: [https://aclanthology.org/2024.acl-long.20/](https://aclanthology.org/2024.acl-long.20/)

**TLDR**: An investigation into the alignment between LLMs' expressed confidence and actual probability estimates for their outputs.

## Abstract

AbstractAs the use of Large Language Models (LLMs) becomes more widespread, understanding their self-evaluation of confidence in generated responses becomes increasingly important as it is integral to the reliability of the output of these models. We introduce the concept of Confidence-Probability Alignment, that connects an LLM’s internal confidence, quantified by token probabilities, to the confidence conveyed in the model’s response when explicitly asked about its certainty. Using various datasets and prompting techniques that encourage model introspection, we probe the alignment between models’ internal and expressed confidence. These techniques encompass using structured evaluation scales to rate confidence, including answer options when prompting, and eliciting the model’s confidence level for outputs it does not recognize as its own. Notably, among the models analyzed, OpenAI’s GPT-4 showed the strongest confidence-probability alignment, with an average Spearman’s  ̂𝜌 of 0.42, across a wide range of tasks. Our work contributes to the ongoing efforts to facilitate risk assessment in the application of LLMs and to further our understanding of model trustworthiness.