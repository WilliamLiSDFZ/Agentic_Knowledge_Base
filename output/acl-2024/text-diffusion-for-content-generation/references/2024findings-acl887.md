---
title: "Diffusion Guided Language Modeling"
source: "https://aclanthology.org/2024.findings-acl.887/"
categories: ['text-diffusion-for-content-generation', 'llm-security-robustness-and-detection']
tags: ['text-diffusion', 'controllable-generation', 'sentiment-control']
venue: "ACL 2024"
tldr: "Combines diffusion guidance with language models to control text attributes like sentiment and toxicity during generation."
---

# Diffusion Guided Language Modeling

**Source**: [https://aclanthology.org/2024.findings-acl.887/](https://aclanthology.org/2024.findings-acl.887/)

**TLDR**: Combines diffusion guidance with language models to control text attributes like sentiment and toxicity during generation.

## Abstract

AbstractCurrent language models demonstrate remarkable proficiency in text generation. However, for many applications it is desirable to control attributes, such as sentiment, or toxicity, of the generated language—ideally tailored towards each specific use case and target audience. For auto-regressive language models, existing guidance methods are prone to decoding errors that cascade during generation and degrade performance. In contrast, text diffusion models can easily be guided with, for example, a simple linear sentiment classifier—however they do suffer from significantly higher perplexity than auto-regressive alternatives. In this paper we use a guided diffusion model to produce a latent proposal that steers an auto-regressive language model to generate text with desired properties. Our model inherits the unmatched fluency of the auto-regressive approach and the plug-and-play flexibility of diffusion. We show that it outperforms previous plug-and-play guidance methods across a wide range of benchmark data sets. Further, controlling a new attribute in our framework is reduced to training a single logistic regression classifier.