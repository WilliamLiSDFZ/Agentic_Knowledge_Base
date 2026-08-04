---
title: "Linguistic Calibration of Long-Form Generations"
source: "https://proceedings.mlr.press/v235/band24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/band24a/band24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['linguistic-calibration', 'long-form-generation', 'hallucination']
venue: "ICML 2024"
tldr: "A method is proposed for training language models to produce long-form text with verbally calibrated confidence to reduce hallucination-driven poor decisions."
---

# Linguistic Calibration of Long-Form Generations

**Source**: [https://proceedings.mlr.press/v235/band24a.html](https://proceedings.mlr.press/v235/band24a.html)

**TLDR**: A method is proposed for training language models to produce long-form text with verbally calibrated confidence to reduce hallucination-driven poor decisions.

## Abstract

Language models (LMs) may lead their users to make suboptimal downstream decisions when they confidently hallucinate. This issue can be mitigated by having the LM verbally convey the probability that its claims are correct, but existing models cannot produce long-form text with calibrated confidence statements. Through the lens of decision-making, we define linguistic calibration for long-form generations: an LM is linguistically calibrated if its generations enable its users to make calibrated probabilistic predictions. This definition enables a training framework where a supervised finetuning step bootstraps an LM to emit long-form generations with confidence statements such as "I estimate a 30% chance of..." or "I am certain that...", followed by a reinforcement learning step which rewards generations that enable a user to provide calibrated answers to related questions. We linguistically calibrate Llama 2 7B and find in automated and human evaluations of long-form generations that it is significantly more calibrated than strong finetuned factuality baselines with comparable accuracy. These findings generalize under significant domain shifts to scientific and biomedical questions and to an entirely held-out person biography generation task. Our results demonstrate that long-form generations may be calibrated end-to-end by constructing an objective in the space of the predictions that users make in downstream decision-making.