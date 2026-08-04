---
title: "Position: On the Possibilities of AI-Generated Text Detection"
source: "https://proceedings.mlr.press/v235/chakraborty24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chakraborty24a/chakraborty24a.pdf"
categories: ['position-papers-on-ml-research-directions', 'adversarial-robustness-and-model-security']
tags: ['AI-generated-text-detection', 'LLM', 'information-theory', 'human-vs-machine']
venue: "ICML 2024"
tldr: "Provides theoretical evidence and practical arguments that AI-generated text is detectable unless human and machine distributions are fully indistinguishable."
---

# Position: On the Possibilities of AI-Generated Text Detection

**Source**: [https://proceedings.mlr.press/v235/chakraborty24a.html](https://proceedings.mlr.press/v235/chakraborty24a.html)

**TLDR**: Provides theoretical evidence and practical arguments that AI-generated text is detectable unless human and machine distributions are fully indistinguishable.

## Abstract

Our study addresses the challenge of distinguishing human-written text from Large Language Model (LLM) outputs. We provide evidence that this differentiation is consistently feasible, except when human and machine text distributions are indistinguishable across their entire support. Employing information theory, we show that while detecting machine-generated text becomes harder as it nears human quality, it remains possible with adequate text data. We introduce guidelines on the required text data quantity, either through sample size or sequence length, for reliable AI text detection, through derivations of sample complexity bounds. This research paves the way for advanced detection methods. Our comprehensive empirical tests, conducted across various datasets (Xsum, Squad, IMDb, and Kaggle FakeNews) and with several state-of-the-art text generators (GPT-2, GPT-3.5-Turbo, Llama, Llama-2-13B-Chat-HF, Llama-2-70B-Chat-HF), assess the viability of enhanced detection methods against detectors like RoBERTa-Large/Base-Detector and GPTZero, with increasing sample sizes and sequence lengths. Our findings align with OpenAI’s empirical data related to sequence length, marking the first theoretical substantiation for these observations.