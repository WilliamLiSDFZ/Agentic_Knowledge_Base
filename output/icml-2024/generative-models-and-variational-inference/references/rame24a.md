---
title: "WARM: On the Benefits of Weight Averaged Reward Models"
source: "https://proceedings.mlr.press/v235/rame24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/rame24a/rame24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'generative-models-and-variational-inference']
tags: ['reward-hacking', 'RLHF', 'reward-model', 'weight-averaging', 'alignment', 'LLM']
venue: "ICML 2024"
tldr: "Weight averaging of reward models reduces reward hacking and improves LLM alignment robustness in RLHF."
---

# WARM: On the Benefits of Weight Averaged Reward Models

**Source**: [https://proceedings.mlr.press/v235/rame24a.html](https://proceedings.mlr.press/v235/rame24a.html)

**TLDR**: Weight averaging of reward models reduces reward hacking and improves LLM alignment robustness in RLHF.

## Abstract

Aligning large language models (LLMs) with human preferences through reinforcement learning (RLHF) can lead to reward hacking, where LLMs exploit failures in the reward model (RM) to achieve seemingly high rewards without meeting the underlying objectives. We identify two primary challenges when designing RMs to mitigate reward hacking: distribution shifts during the RL process and inconsistencies in human preferences. As a solution, we propose Weight Averaged Reward Models (WARM), first fine-tuning multiple RMs, then averaging them in the weight space. This strategy follows the observation that fine-tuned weights remain linearly mode connected when sharing the same pre-training. By averaging weights, WARM improves efficiency compared to the traditional ensembling of predictions, while improving reliability under distribution shifts and robustness to preference inconsistencies. Our experiments on summarization tasks, using best-of-N and RL methods, shows that WARM improves the overall quality and alignment of LLM predictions; for example, a policy RL fine-tuned with WARM has a 79.4% win rate against a policy RL fine-tuned with a single RM.