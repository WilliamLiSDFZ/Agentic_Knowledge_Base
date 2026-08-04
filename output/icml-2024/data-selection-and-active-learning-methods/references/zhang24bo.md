---
title: "Candidate Pseudolabel Learning: Enhancing Vision-Language Models by Prompt Tuning with Unlabeled Data"
source: "https://proceedings.mlr.press/v235/zhang24bo.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bo/zhang24bo.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'data-selection-and-active-learning-methods']
tags: ['vision-language-models', 'prompt-tuning', 'pseudo-labels', 'semi-supervised', 'unlabeled-data']
venue: "ICML 2024"
tldr: "Introduces Candidate Pseudolabel Learning to enhance VLM fine-tuning with unlabeled data by mitigating incorrect hard pseudolabels."
---

# Candidate Pseudolabel Learning: Enhancing Vision-Language Models by Prompt Tuning with Unlabeled Data

**Source**: [https://proceedings.mlr.press/v235/zhang24bo.html](https://proceedings.mlr.press/v235/zhang24bo.html)

**TLDR**: Introduces Candidate Pseudolabel Learning to enhance VLM fine-tuning with unlabeled data by mitigating incorrect hard pseudolabels.

## Abstract

Fine-tuning vision-language models (VLMs) with abundant unlabeled data recently has attracted increasing attention. Existing methods that resort to the pseudolabeling strategy would suffer from heavily incorrect hard pseudolabels when VLMs exhibit low zero-shot performance in downstream tasks. To alleviate this issue, we propose a Candidate Pseudolabel Learning method, termed CPL, to fine-tune VLMs with suitable candidate pseudolabels of unlabeled data in downstream tasks. The core of our method lies in the generation strategy of candidate pseudolabels, which progressively generates refined candidate pseudolabels by both intra- and inter-instance label selection, based on a confidence score matrix for all unlabeled data. This strategy can result in better performance in true label inclusion and class-balanced instance selection. In this way, we can directly apply existing loss functions to learn with generated candidate psueudolabels. Extensive experiments on nine benchmark datasets with three learning paradigms demonstrate the effectiveness of our method. Our code can be found here.