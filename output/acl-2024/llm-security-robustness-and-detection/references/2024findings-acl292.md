---
title: "Evaluating the Validity of Word-level Adversarial Attacks with Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.292/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['adversarial-attacks', 'word-level-perturbation', 'semantic-validity']
venue: "ACL 2024"
tldr: "Evaluates the semantic validity of word-level adversarial attacks in NLP using LLMs to assess whether synonym substitutions preserve meaning."
---

# Evaluating the Validity of Word-level Adversarial Attacks with Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.292/](https://aclanthology.org/2024.findings-acl.292/)

**TLDR**: Evaluates the semantic validity of word-level adversarial attacks in NLP using LLMs to assess whether synonym substitutions preserve meaning.

## Abstract

AbstractDeep neural networks exhibit vulnerability to word-level adversarial attacks in natural language processing. Most of these attack methods adopt synonymous substitutions to perturb original samples for crafting adversarial examples while attempting to maintain semantic consistency with the originals. Some of them claim that they could achieve over 90% attack success rate, thereby raising serious safety concerns. However, our investigation reveals that many purportedly successful adversarial examples are actually invalid due to significant changes in semantic meanings compared to their originals. Even when equipped with semantic constraints such as BERTScore, existing attack methods can generate up to 87.9% invalid adversarial examples. Building on this insight, we first curate a 13K dataset for adversarial validity evaluation with the help of GPT-4. Then, an open-source large language model is fine-tuned to offer an interpretable validity score for assessing the semantic consistency between original and adversarial examples. Finally, this validity score can serve as a guide for existing adversarial attack methods to generate valid adversarial examples. Comprehensive experiments demonstrate the effectiveness of our method in evaluating and refining the quality of adversarial examples.