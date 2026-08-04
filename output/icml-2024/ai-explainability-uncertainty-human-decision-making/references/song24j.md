---
title: "Latent Logic Tree Extraction for Event Sequence Explanation from LLMs"
source: "https://proceedings.mlr.press/v235/song24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/song24j/song24j.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['LLMs', 'event-sequences', 'logic-trees', 'explainability']
venue: "ICML 2024"
tldr: "A plug-and-play method is proposed to extract logic tree-based explanations from LLMs for observed event sequences in high-stakes streaming systems."
---

# Latent Logic Tree Extraction for Event Sequence Explanation from LLMs

**Source**: [https://proceedings.mlr.press/v235/song24j.html](https://proceedings.mlr.press/v235/song24j.html)

**TLDR**: A plug-and-play method is proposed to extract logic tree-based explanations from LLMs for observed event sequences in high-stakes streaming systems.

## Abstract

Modern high-stakes systems, such as healthcare or robotics, often generate vast streaming event sequences. Our goal is to design an efficient, plug-and-play tool to elicit logic tree-based explanations from Large Language Models (LLMs) to provide customized insights into each observed event sequence. Built on the temporal point process model for events, our method employs the likelihood function as a score to evaluate generated logic trees. We propose an amortized Expectation-Maximization (EM) learning framework and treat the logic tree as latent variables. In the E-step, we evaluate the posterior distribution over the latent logic trees using an LLM prior and the likelihood of the observed event sequences. LLM provides a high-quality prior for the latent logic trees, however, since the posterior is built over a discrete combinatorial space, we cannot get the closed-form solution. We propose to generate logic tree samples from the posterior using a learnable GFlowNet, which is a diversity-seeking generator for structured discrete variables. The M-step employs the generated logic rules to approximate marginalization over the posterior, facilitating the learning of model parameters and refining the tunable LLM prior parameters. In the online setting, our locally built, lightweight model will iteratively extract the most relevant rules from LLMs for each sequence using only a few iterations. Empirical demonstrations showcase the promising performance and adaptability of our framework.