---
title: "Position: Fundamental Limitations of LLM Censorship Necessitate New Approaches"
source: "https://proceedings.mlr.press/v235/glukhov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/glukhov24a/glukhov24a.pdf"
categories: ['ai-safety-governance-alignment-positions', 'position-papers-on-ml-research-directions']
tags: ['llm-safety', 'censorship', 'adversarial-robustness']
venue: "ICML 2024"
tldr: "This position paper argues that fundamental limitations make LLM censorship approaches insufficient and calls for new safety mechanisms."
---

# Position: Fundamental Limitations of LLM Censorship Necessitate New Approaches

**Source**: [https://proceedings.mlr.press/v235/glukhov24a.html](https://proceedings.mlr.press/v235/glukhov24a.html)

**TLDR**: This position paper argues that fundamental limitations make LLM censorship approaches insufficient and calls for new safety mechanisms.

## Abstract

Large language models (LLMs) have exhibited impressive capabilities in comprehending complex instructions. However, their blind adherence to provided instructions has led to concerns regarding risks of malicious use. Existing defence mechanisms, such as model fine-tuning or output censorship methods have proven to be fallible at ensuring that LLMs do not return semantically impermissible responses. We present fundamental limitations of verifying the semantic properties of LLM outputs and identifying compositional threats, illustrating inherent challenges of current approaches to censoring LLM outputs. Specifically, we demonstrate that semantic censorship can be perceived as an undecidable problem, and semantic properties of LLM outputs can become impossible to verify when the LLM is capable of providing "encrypted" outputs. We further show challenges of censorship can extend beyond just semantic censorship, as attackers can reconstruct impermissible outputs from a collection of permissible ones. Consequently, we call for a re-evaluation of the problem of censorship and its goals, stressing the need for new definitions and approaches to censorship. In addition, we provide an initial attempt toward achieving this goal through syntactic censorship, drawing from a security perspective to design censorship methods that can provide guarantees.