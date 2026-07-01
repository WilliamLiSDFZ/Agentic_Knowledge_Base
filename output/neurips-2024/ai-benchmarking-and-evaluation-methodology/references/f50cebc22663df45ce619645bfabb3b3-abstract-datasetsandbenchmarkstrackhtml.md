---
title: "Towards Reliable Model Selection for Unsupervised Domain Adaptation: An Empirical Study and A Certified Baseline"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f50cebc22663df45ce619645bfabb3b3-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['unsupervised-domain-adaptation', 'model-selection', 'hyperparameter-validation']
venue: "NeurIPS 2024"
tldr: "Empirically studies and proposes a certified baseline for reliable model selection in unsupervised domain adaptation."
---

# Towards Reliable Model Selection for Unsupervised Domain Adaptation: An Empirical Study and A Certified Baseline

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f50cebc22663df45ce619645bfabb3b3-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f50cebc22663df45ce619645bfabb3b3-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Empirically studies and proposes a certified baseline for reliable model selection in unsupervised domain adaptation.

## Abstract

Selecting appropriate hyperparameters is crucial for unlocking the full potential of advanced unsupervised domain adaptation (UDA) methods in unlabeled target domains. Although this challenge remains under-explored, it has recently garnered increasing attention with the proposals of various model selection methods. Reliable model selection should maintain performance across diverse UDA methods and scenarios, especially avoiding highly risky worst-case selections—selecting the model or hyperparameter with the worst performance in the pool.\textit{Are existing model selection methods reliable and versatile enough for different UDA tasks?} In this paper, we provide a comprehensive empirical study involving 8 existing model selection approaches to answer this question. Our evaluation spans 12 UDA methods across 5 diverse UDA benchmarks and 5 popular UDA scenarios.Surprisingly, we find that none of these approaches can effectively avoid the worst-case selection. In contrast, a simple but overlooked ensemble-based selection approach, which we call EnsV, is both theoretically and empirically certified to avoid the worst-case selection, ensuring high reliability. Additionally, EnsV is versatile for various practical but challenging UDA scenarios, including validation of open-partial-set UDA and source-free UDA.Finally, we call for more attention to the reliability of model selection in UDA: avoiding the worst-case is as significant as achieving peak selection performance and should not be overlooked when developing new model selection methods.  Code is available at https://github.com/LHXXHB/EnsV.