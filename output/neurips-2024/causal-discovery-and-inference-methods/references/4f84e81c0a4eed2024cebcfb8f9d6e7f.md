---
title: "Data-faithful Feature Attribution: Mitigating Unobservable Confounders via Instrumental Variables"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4f84e81c0a4eed2024cebcfb8f9d6e7f-Abstract-Conference.html"
categories: ['causal-discovery-and-inference-methods', 'machine-learning-theory-and-evaluation-methods']
tags: ['feature-attribution', 'instrumental-variables', 'confounders', 'causal-inference', 'explainability']
venue: "NeurIPS 2024"
tldr: "Proposes a data-faithful feature attribution method that uses instrumental variables to mitigate the effects of unobservable confounders on model interpretation."
---

# Data-faithful Feature Attribution: Mitigating Unobservable Confounders via Instrumental Variables

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4f84e81c0a4eed2024cebcfb8f9d6e7f-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/4f84e81c0a4eed2024cebcfb8f9d6e7f-Abstract-Conference.html)

**TLDR**: Proposes a data-faithful feature attribution method that uses instrumental variables to mitigate the effects of unobservable confounders on model interpretation.

## Abstract

The state-of-the-art feature attribution methods often neglect the influence of unobservable confounders, posing a risk of misinterpretation, especially when it is crucial for the interpretation to remain faithful to the data. To counteract this, we propose a new approach, data-faithful feature attribution, which trains a confounder-free model using instrumental variables. The cluttered effects of unobservable confounders in a model trained as such are decoupled from input features, thereby aligning the output of the model with the contribution of input features to the target feature in the data generation. Furthermore, feature attribution results produced by our method are more robust when focusing on attributions from the perspective of data generation. Our experiments on both synthetic and real-world datasets demonstrate the effectiveness of our approaches.