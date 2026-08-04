---
title: "Provable Interactive Learning with Hindsight Instruction Feedback"
source: "https://proceedings.mlr.press/v235/misra24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/misra24a/misra24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['interactive-learning', 'hindsight-feedback', 'instruction-following']
venue: "ICML 2024"
tldr: "Studies provable interactive learning where agents receive hindsight instruction feedback rather than rewards or expert supervision."
---

# Provable Interactive Learning with Hindsight Instruction Feedback

**Source**: [https://proceedings.mlr.press/v235/misra24a.html](https://proceedings.mlr.press/v235/misra24a.html)

**TLDR**: Studies provable interactive learning where agents receive hindsight instruction feedback rather than rewards or expert supervision.

## Abstract

We study interactive learning in a setting where the agent has to generate a response (e.g., an action or trajectory) given a context and an instruction. In contrast, to typical approaches that train the system using reward or expert supervision on response, we study learning with hindsight labeling where a teacher provides an instruction that is most suitable for the agent’s generated response. This hindsight labeling of instruction is often easier to provide than providing expert supervision of the optimal response which may require expert knowledge or can be impractical to elicit. We initiate the theoretical analysis of interactive learning with hindsight labeling. We first provide a lower bound showing that in general, the regret of any algorithm must scale with the size of the agent’s response space. Next, we study a specialized setting where the underlying instruction-response distribution can be decomposed as a low-rank matrix. We introduce an algorithm called LORIL for this setting and show that it is a no-regret algorithm with the regret scaling with $\sqrt{T}$ and depends on the intrinsic rank but does not depend on the agent’s response space. We provide experiments showing the performance of LORIL in practice for 2 domains.