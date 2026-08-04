---
title: "LoRA+: Efficient Low Rank Adaptation of Large Models"
source: "https://proceedings.mlr.press/v235/hayou24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hayou24a/hayou24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['lora', 'learning-rate', 'fine-tuning']
venue: "ICML 2024"
tldr: "LoRA+ improves fine-tuning of large-width models by using different learning rates for the two adapter matrices, addressing suboptimality of the original LoRA."
---

# LoRA+: Efficient Low Rank Adaptation of Large Models

**Source**: [https://proceedings.mlr.press/v235/hayou24a.html](https://proceedings.mlr.press/v235/hayou24a.html)

**TLDR**: LoRA+ improves fine-tuning of large-width models by using different learning rates for the two adapter matrices, addressing suboptimality of the original LoRA.

## Abstract

In this paper, we show that Low Rank Adaptation (LoRA) as originally introduced in (Hu et al., 2021) leads to suboptimal finetuning of models with large width. This is due to the fact that adapter matrices A and B in LoRA are updated with the same learning rate in ADAM. Using scaling arguments for large width networks, we demonstrate that the same learning rate does not allow efficient feature learning. We then show that this suboptimality of LoRA can be corrected simply by setting different learning rates for the LoRA adapter matrices A and B with a well-chosen fixed ratio. We call this proposed algorithm LoRA+. In our extensive experiments, LoRA+ improves finetuning speed (up to ∼ 2X SpeedUp) and performance (1% − 2% improvements), at the same computational cost as LoRA. The code is available at https://github.com/nikhil-ghosh-berkeley/loraplus