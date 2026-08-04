---
title: "RLVF: Learning from Verbal Feedback without Overgeneralization"
source: "https://proceedings.mlr.press/v235/stephan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stephan24a/stephan24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'test-time-adaptation-methods-and-evaluation']
tags: ['RLHF', 'verbal-feedback', 'LLM-alignment', 'overgeneralization', 'preference-learning']
venue: "ICML 2024"
tldr: "RLVF is a method for incorporating high-level verbal feedback into LLMs to customize behaviors without overgeneralizing the specified adjustments."
---

# RLVF: Learning from Verbal Feedback without Overgeneralization

**Source**: [https://proceedings.mlr.press/v235/stephan24a.html](https://proceedings.mlr.press/v235/stephan24a.html)

**TLDR**: RLVF is a method for incorporating high-level verbal feedback into LLMs to customize behaviors without overgeneralizing the specified adjustments.

## Abstract

The diversity of contexts in which large language models (LLMs) are deployed requires the ability to modify or customize default model behaviors to incorporate nuanced requirements and preferences. A convenient interface to specify such model adjustments is high-level verbal feedback, such as “Don’t use emojis when drafting emails to my boss.” However, while writing high-level feedback is far simpler than collecting annotations for reinforcement learning from human feedback (RLHF), we find that simply prompting a model with such feedback leads to $\textbf{overgeneralization}$–applying feedback in contexts where it is not relevant. We propose a new method Contextualized Critiques with Constrained Preference Optimization (C3PO) to learn from high-level verbal feedback while reducing overgeneralization compared to current work. C3PO uses a piece of high-level feedback to generate a small synthetic preference dataset to specify when and how the feedback should (and should not) be applied. It then fine-tunes the model in accordance with the synthetic preference data while minimizing the divergence from the original model for prompts where the feedback does not apply. Our experimental results indicate that our approach effectively applies verbal feedback to relevant scenarios while preserving existing behaviors for other contexts more than current methods. For both human- and GPT-4-generated high-level feedback, C3PO effectively adheres to the given feedback comparably to in-context baselines while reducing overgeneralization by 30%.