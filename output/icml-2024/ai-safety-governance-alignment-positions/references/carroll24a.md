---
title: "AI Alignment with Changing and Influenceable Reward Functions"
source: "https://proceedings.mlr.press/v235/carroll24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/carroll24a/carroll24a.pdf"
categories: ['ai-safety-governance-alignment-positions', 'large-language-model-alignment-and-capabilities']
tags: ['AI-alignment', 'dynamic-rewards', 'influenceable-preferences', 'Markov-decision-process']
venue: "ICML 2024"
tldr: "Introduces Dynamic Reward MDPs to study AI alignment when reward functions change and can be influenced by AI interactions."
---

# AI Alignment with Changing and Influenceable Reward Functions

**Source**: [https://proceedings.mlr.press/v235/carroll24a.html](https://proceedings.mlr.press/v235/carroll24a.html)

**TLDR**: Introduces Dynamic Reward MDPs to study AI alignment when reward functions change and can be influenced by AI interactions.

## Abstract

Existing AI alignment approaches assume that preferences are static, which is unrealistic: our preferences change, and may even be influenced by our interactions with AI systems themselves. To clarify the consequences of incorrectly assuming static preferences, we introduce Dynamic Reward Markov Decision Processes (DR-MDPs), which explicitly model preference changes and the AI’s influence on them. We show that despite its convenience, the static-preference assumption may undermine the soundness of existing alignment techniques, leading them to implicitly reward AI systems for influencing user preferences in ways users may not truly want. We then explore potential solutions. First, we offer a unifying perspective on how an agent’s optimization horizon may partially help reduce undesirable AI influence. Then, we formalize different notions of AI alignment that account for preference change from the outset. Comparing the strengths and limitations of 8 such notions of alignment, we find that they all either err towards causing undesirable AI influence, or are overly risk-averse, suggesting that a straightforward solution to the problems of changing preferences may not exist. As there is no avoiding grappling with changing preferences in real-world settings, this makes it all the more important to handle these issues with care, balancing risks and capabilities. We hope our work can provide conceptual clarity and constitute a first step towards AI alignment practices which explicitly account for (and contend with) the changing and influenceable nature of human preferences.