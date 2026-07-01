---
title: "To Believe or Not to Believe Your LLM: Iterative Prompting for Estimating Epistemic Uncertainty"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6aebba00fff5b6de7b488e496f80edd7-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques']
tags: ['uncertainty-quantification', 'epistemic-uncertainty', 'iterative-prompting']
venue: "NeurIPS 2024"
tldr: "Proposes an iterative prompting approach to jointly estimate epistemic and aleatoric uncertainty in large language model responses."
---

# To Believe or Not to Believe Your LLM: Iterative Prompting for Estimating Epistemic Uncertainty

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6aebba00fff5b6de7b488e496f80edd7-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/6aebba00fff5b6de7b488e496f80edd7-Abstract-Conference.html)

**TLDR**: Proposes an iterative prompting approach to jointly estimate epistemic and aleatoric uncertainty in large language model responses.

## Abstract

We explore uncertainty quantification in large language models (LLMs), with the goal to identify when uncertainty in responses given a query is large. We simultaneously consider both epistemic and aleatoric uncertainties, where the former comes from the lack of knowledge about the ground truth (such as about facts or the language), and the latter comes from irreducible randomness (such as multiple possible answers). In particular, we derive an information-theoretic metric that allows to reliably detect when only epistemic uncertainty is large, in which case the output of the model is unreliable. This condition can be computed based solely on the output of the model obtained simply by some special iterative prompting based on the previous responses. Such quantification, for instance, allows to detect hallucinations (cases when epistemic uncertainty is high) in both single- and multi-answer responses. This is in contrast to many standard uncertainty quantification strategies (such as thresholding the log-likelihood of a response) where hallucinations in the multi-answer case cannot be detected. We conduct a series of experiments which demonstrate the advantage of our formulation. Further, our investigations shed some light on how the probabilities assigned to a given output by an LLM can be amplified by iterative prompting, which might be of independent interest.