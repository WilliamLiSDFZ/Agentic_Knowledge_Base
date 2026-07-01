---
title: "Causal discovery with endogenous context variables"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3fcce87e6df22b2ab6f0be68af3ec714-Abstract-Conference.html"
categories: ['causal-discovery-and-inference-methods', 'physics-informed-neural-operators-and-simulations']
tags: ['causal-discovery', 'context-variables', 'endogenous-variables']
venue: "NeurIPS 2024"
tldr: "A causal discovery framework that handles endogenous context variables representing changing generating mechanisms across different environments or internal system states."
---

# Causal discovery with endogenous context variables

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3fcce87e6df22b2ab6f0be68af3ec714-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/3fcce87e6df22b2ab6f0be68af3ec714-Abstract-Conference.html)

**TLDR**: A causal discovery framework that handles endogenous context variables representing changing generating mechanisms across different environments or internal system states.

## Abstract

Systems with variations of the underlying generating mechanism between different contexts, i.e., different environments or internal states  in which the system operates, are common in the real world, such as soil moisture regimes in Earth science. Besides understanding the shared properties of the system, in practice, the question of context-specific properties, i.e., the change in causal relationships between contexts, arises. For real-world data, contexts are often driven by system variables, e.g., precipitation highly influences soil moisture. Nevertheless, this setup needs to be studied more. To account for such endogenous contexts in causal discovery, our work proposes a constraint-based method that can efficiently discover context-specific causal graphs using an adaptive testing approach. Our approach tests conditional independence on the pooled datasets to infer the dependence between system variables, including the context, to avoid introducing selection bias. To yield context-specific insights, conditional independence is tested on context-specific data. We work out the theoretical framework for this adaptive testing approach and give a detailed discussion of the connection to structural causal models, including sufficiency assumptions, which allow to prove the soundness of our algorithm and to interpret the results causally. A simulation study to evaluate numerical properties shows that our approach  behaves as expected, but also leads to a further understanding of current limitations and viable extensions.