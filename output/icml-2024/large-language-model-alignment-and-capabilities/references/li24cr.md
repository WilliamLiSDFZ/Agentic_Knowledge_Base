---
title: "DecisionNCE: Embodied Multimodal Representations via Implicit Preference Learning"
source: "https://proceedings.mlr.press/v235/li24cr.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24cr/li24cr.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['multimodal-pretraining', 'imitation-learning', 'representation-learning']
venue: "ICML 2024"
tldr: "DecisionNCE uses implicit preference learning to develop multimodal representations for autonomous robot decision-making."
---

# DecisionNCE: Embodied Multimodal Representations via Implicit Preference Learning

**Source**: [https://proceedings.mlr.press/v235/li24cr.html](https://proceedings.mlr.press/v235/li24cr.html)

**TLDR**: DecisionNCE uses implicit preference learning to develop multimodal representations for autonomous robot decision-making.

## Abstract

Multimodal pretraining is an effective strategy for the trinity of goals of representation learning in autonomous robots: $1)$ extracting both local and global task progressions; $2)$ enforcing temporal consistency of visual representation; $3)$ capturing trajectory-level language grounding. Most existing methods approach these via separate objectives, which often reach sub-optimal solutions. In this paper, we propose a universal unified objective that can simultaneously extract meaningful task progression information from image sequences and seamlessly align them with language instructions. We discover that via implicit preferences, where a visual trajectory inherently aligns better with its corresponding language instruction than mismatched pairs, the popular Bradley-Terry model can transform into representation learning through proper reward reparameterizations. The resulted framework, DecisionNCE, mirrors an InfoNCE-style objective but is distinctively tailored for decision-making tasks, providing an embodied representation learning framework that elegantly extracts both local and global task progression features, with temporal consistency enforced through implicit time contrastive learning, while ensuring trajectory-level instruction grounding via multimodal joint encoding. Evaluation on both simulated and real robots demonstrates that DecisionNCE effectively facilitates diverse downstream policy learning tasks, offering a versatile solution for unified representation and reward learning. Project Page: https://2toinf.github.io/DecisionNCE/