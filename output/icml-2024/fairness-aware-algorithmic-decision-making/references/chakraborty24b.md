---
title: "MaxMin-RLHF: Alignment with Diverse Human Preferences"
source: "https://proceedings.mlr.press/v235/chakraborty24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chakraborty24b/chakraborty24b.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'fairness-aware-algorithmic-decision-making']
tags: ['RLHF', 'diverse-preferences', 'MaxMin-optimization', 'reward-model']
venue: "ICML 2024"
tldr: "Proposes MaxMin-RLHF to align language models to diverse human preferences by optimizing a mixture of reward models with a maximin objective."
---

# MaxMin-RLHF: Alignment with Diverse Human Preferences

**Source**: [https://proceedings.mlr.press/v235/chakraborty24b.html](https://proceedings.mlr.press/v235/chakraborty24b.html)

**TLDR**: Proposes MaxMin-RLHF to align language models to diverse human preferences by optimizing a mixture of reward models with a maximin objective.

## Abstract

Reinforcement Learning from Human Feedback (RLHF) aligns language models to human preferences by employing a singular reward model derived from preference data. However, the single reward model overlooks the rich diversity of human preferences inherent in data collected from multiple users. In this work, we first derive an impossibility result of alignment with single reward RLHF, thereby highlighting its insufficiency in representing diverse human preferences. Next, we propose to learn a mixture of reward models via an expectation-maximization algorithm and solve a MaxMin alignment objective inspired by the Egalitarian principle in social choice theory to better honor diverse human preferences. We present comprehensive experimental results on small-scale (GPT-2) and large-scale language (with Tulu2-7B)) and show the efficacy of the proposed approach in the presence of diversity among human preferences. We remark that our findings in this work are not only limited to language models but also extend to reinforcement learning in general.