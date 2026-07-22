---
title: "SumSurvey: An Abstractive Dataset of Scientific Survey Papers for Long Document Summarization"
source: "https://aclanthology.org/2024.findings-acl.574/"
categories: ['state-memory-replay-sequence-modeling']
tags: ['long-document-summarization', 'scientific-surveys', 'abstractive-summarization']
venue: "ACL 2024"
tldr: "Presents SumSurvey, a large abstractive dataset of scientific survey papers for long document summarization."
---

# SumSurvey: An Abstractive Dataset of Scientific Survey Papers for Long Document Summarization

**Source**: [https://aclanthology.org/2024.findings-acl.574/](https://aclanthology.org/2024.findings-acl.574/)

**TLDR**: Presents SumSurvey, a large abstractive dataset of scientific survey papers for long document summarization.

## Abstract

AbstractWith the popularity of large language models (LLMs) and their ability to handle longer input documents, there is a growing need for high-quality long document summarization datasets. Although many models already support 16k input, current lengths of summarization datasets are inadequate, and salient information is not evenly distributed. To bridge these gaps, we collect a new summarization dataset called SumSurvey, consisting of more than 18k scientific survey papers. With an average document length exceeding 12k and a quarter exceeding 16k, as well as the uniformity metric outperforming current mainstream long document summarization datasets, SumSurvey brings new challenges and expectations to both fine-tuned models and LLMs. The informativeness of summaries and the models supporting the evaluation of long document summarization warrant further attention. Automatic and human evaluation results on this abstractive dataset confirm this view. Our dataset and code are available at https://github.com/Oswald1997/SumSurvey.