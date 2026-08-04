---
title: "Modeling Language Tokens as Functionals of Semantic Fields"
source: "https://proceedings.mlr.press/v235/pei24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pei24c/pei24c.pdf"
categories: ['sequence-models-for-memory-and-state', 'transformer-architecture-efficiency-and-scaling']
tags: ['language-modeling', 'semantic-fields', 'transformer-free', 'state-space-models', 'token-representation']
venue: "ICML 2024"
tldr: "Models language tokens as functionals of semantic fields, offering a transformer-free approach with reduced parameter requirements."
---

# Modeling Language Tokens as Functionals of Semantic Fields

**Source**: [https://proceedings.mlr.press/v235/pei24c.html](https://proceedings.mlr.press/v235/pei24c.html)

**TLDR**: Models language tokens as functionals of semantic fields, offering a transformer-free approach with reduced parameter requirements.

## Abstract

Recent advances in natural language processing have relied heavily on using Transformer-based language models. However, Transformers often require large parameter sizes and model depth. Existing Transformer-free approaches using state-space models demonstrate superiority over Transformers, yet they still lack a neuro-biologically connection to the human brain. This paper proposes ${\it LasF}$, representing ${\bf L}$anguage tokens ${\bf as}$ ${\bf F}$unctionals of semantic fields, to simulate the neuronal behaviors for better language modeling. The ${\it LasF}$ module is equivalent to a nonlinear approximator tailored for sequential data. By replacing the final layers of pre-trained language models with the ${\it LasF}$ module, we obtain ${\it LasF}$-based models. Experiments conducted for standard reading comprehension and question-answering tasks demonstrate that the ${\it LasF}$-based models consistently improve accuracy with fewer parameters. Besides, we use CommonsenseQA’s blind test set to evaluate a full-parameter tuned ${\it LasF}$-based model, which outperforms the prior best ensemble and single models by $0.4%$ and $3.1%$, respectively. Furthermore, our ${\it LasF}$-only language model trained from scratch outperforms existing parameter-efficient language models on standard datasets such as WikiText103 and PennTreebank.