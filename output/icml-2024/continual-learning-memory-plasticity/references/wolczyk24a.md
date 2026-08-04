---
title: "Fine-tuning Reinforcement Learning Models is Secretly a Forgetting Mitigation Problem"
source: "https://proceedings.mlr.press/v235/wolczyk24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wolczyk24a/wolczyk24a.pdf"
categories: ['continual-learning-memory-plasticity', 'online-learning-and-sequential-decision-making']
tags: ['fine-tuning', 'reinforcement-learning', 'catastrophic-forgetting', 'continual-learning']
venue: "ICML 2024"
tldr: "Reframes fine-tuning challenges in RL as a forgetting mitigation problem and proposes methods to preserve pre-trained capabilities during adaptation."
---

# Fine-tuning Reinforcement Learning Models is Secretly a Forgetting Mitigation Problem

**Source**: [https://proceedings.mlr.press/v235/wolczyk24a.html](https://proceedings.mlr.press/v235/wolczyk24a.html)

**TLDR**: Reframes fine-tuning challenges in RL as a forgetting mitigation problem and proposes methods to preserve pre-trained capabilities during adaptation.

## Abstract

Fine-tuning is a widespread technique that allows practitioners to transfer pre-trained capabilities, as recently showcased by the successful applications of foundation models. However, fine-tuning reinforcement learning (RL) models remains a challenge. This work conceptualizes one specific cause of poor transfer, accentuated in the RL setting by the interplay between actions and observations: forgetting of pre-trained capabilities. Namely, a model deteriorates on the state subspace of the downstream task not visited in the initial phase of fine-tuning, on which the model behaved well due to pre-training. This way, we lose the anticipated transfer benefits. We identify conditions when this problem occurs, showing that it is common and, in many cases, catastrophic. Through a detailed empirical analysis of the challenging NetHack and Montezuma’s Revenge environments, we show that standard knowledge retention techniques mitigate the problem and thus allow us to take full advantage of the pre-trained capabilities. In particular, in NetHack, we achieve a new state-of-the-art for neural models, improving the previous best score from $5$K to over $10$K points in the Human Monk scenario.