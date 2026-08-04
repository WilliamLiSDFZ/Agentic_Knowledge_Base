---
title: "When is Transfer Learning Possible?"
source: "https://proceedings.mlr.press/v235/phan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/phan24a/phan24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'causal-inference-and-discovery-methods']
tags: ['transfer-learning', 'framework', 'supervised-learning', 'reinforcement-learning', 'imitation-learning']
venue: "ICML 2024"
tldr: "Introduces a unified framework characterizing when transfer learning succeeds across supervised, reinforcement, and imitation learning settings."
---

# When is Transfer Learning Possible?

**Source**: [https://proceedings.mlr.press/v235/phan24a.html](https://proceedings.mlr.press/v235/phan24a.html)

**TLDR**: Introduces a unified framework characterizing when transfer learning succeeds across supervised, reinforcement, and imitation learning settings.

## Abstract

We present a general framework for transfer learning that is flexible enough to capture transfer in supervised, reinforcement, and imitation learning. Our framework enables new insights into the fundamental question of when we can successfully transfer learned information across problems. We model the learner as interacting with a sequence of problem instances, or environments, each of which is generated from a common structural causal model (SCM) by choosing the SCM’s parameters from restricted sets. We derive a procedure that can propagate restrictions on SCM parameters through the SCM’s graph structure to other parameters that we are trying to learn. The propagated restrictions then enable more efficient learning (i.e., transfer). By analyzing the procedure, we are able to challenge widely-held beliefs about transfer learning. First, we show that having sparse changes across environments is neither necessary nor sufficient for transfer. Second, we show an example where the common heuristic of freezing a layer in a network causes poor transfer performance. We then use our procedure to select a more refined set of parameters to freeze, leading to successful transfer learning.