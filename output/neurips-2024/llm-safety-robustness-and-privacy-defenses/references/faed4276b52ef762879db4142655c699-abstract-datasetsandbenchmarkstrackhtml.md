---
title: "Evaluating Copyright Takedown Methods for Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/faed4276b52ef762879db4142655c699-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-safety-robustness-and-privacy-defenses']
tags: ['copyright', 'machine-unlearning', 'language-models', 'memorization']
venue: "NeurIPS 2024"
tldr: "Evaluates existing copyright takedown and machine unlearning methods for language models that may memorize and reproduce copyrighted training data."
---

# Evaluating Copyright Takedown Methods for Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/faed4276b52ef762879db4142655c699-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/faed4276b52ef762879db4142655c699-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Evaluates existing copyright takedown and machine unlearning methods for language models that may memorize and reproduce copyrighted training data.

## Abstract

Language models (LMs) derive their capabilities from extensive training on diverse data, including copyrighted material. These models can memorize and generate content similar to their training data, potentially risking legal issues like copyright infringement.Therefore, model creators are motivated to develop mitigation methods that prevent generating particular copyrighted content, an ability we refer to as copyright takedowns. This paper introduces the first evaluation of the feasibility and side effects of copyright takedowns for LMs. We propose CoTaEval, an evaluation framework to assess the effectiveness of copyright takedown methods,the impact on the model's ability to retain uncopyrightable factual knowledge from the copyrighted content, and how well the model maintains its general utility and efficiency.We examine several strategies, including adding system prompts, decoding-time filtering interventions, and unlearning approaches. Our findings indicate that no method excels across all metrics, showing significant room for research in this unique problem setting and indicating potential unresolved challenges for live policy proposals.