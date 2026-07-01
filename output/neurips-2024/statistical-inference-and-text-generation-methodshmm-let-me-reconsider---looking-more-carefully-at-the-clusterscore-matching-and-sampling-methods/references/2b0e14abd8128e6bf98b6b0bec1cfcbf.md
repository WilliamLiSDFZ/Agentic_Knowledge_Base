---
title: "Uncertainty of Thoughts: Uncertainty-Aware Planning Enhances Information Seeking in LLMs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2b0e14abd8128e6bf98b6b0bec1cfcbf-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'statistical-inference-and-text-generation-methods\n\nhmm,-let-me-reconsider---looking-more-carefully-at-the-cluster:\n\n**score-matching-and-sampling-methods**']
tags: ['uncertainty-aware-planning', 'information-seeking', 'active-questioning']
venue: "NeurIPS 2024"
tldr: "An uncertainty-aware planning framework enhances LLMs' ability to actively seek information through targeted follow-up questions in tasks like medical diagnosis."
---

# Uncertainty of Thoughts: Uncertainty-Aware Planning Enhances Information Seeking in LLMs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2b0e14abd8128e6bf98b6b0bec1cfcbf-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/2b0e14abd8128e6bf98b6b0bec1cfcbf-Abstract-Conference.html)

**TLDR**: An uncertainty-aware planning framework enhances LLMs' ability to actively seek information through targeted follow-up questions in tasks like medical diagnosis.

## Abstract

In the face of uncertainty, the ability to seek information is of fundamental importance. In many practical applications, such as medical diagnosis and troubleshooting, the information needed to solve the task is not initially given, and has to be actively sought by asking follow-up questions (for example, a doctor asking a patient for more details about their symptoms). In this work, we introduce Uncertainty of Thoughts (UoT), an algorithm to augment large language models with the ability to actively seek information by asking effective questions. UoT combines:1. An uncertainty-aware simulation approach which enables the model to simulate possible future scenarios and how likely they are to occur,2. Uncertainty-based rewards motivated by information gain which incentivizes the model to seek information, and3. A reward propagation scheme to select the optimal question to ask in a way that maximizes the expected reward.In experiments on medical diagnosis, troubleshooting and the `20 Questions' game, UoT achieves an average performance improvement of 38.1% in the rate of successful task completion across multiple LLMs compared with direct prompting, and also improves efficiency (i.e., the number of questions needed to complete the task).