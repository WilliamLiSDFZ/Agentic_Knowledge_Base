---
title: "Failures Are Fated, But Can Be Faded: Characterizing and Mitigating Unwanted Behaviors in Large-Scale Vision and Language Models"
source: "https://proceedings.mlr.press/v235/sagar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sagar24a/sagar24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'large-language-model-alignment-and-capabilities']
tags: ['failure-characterization', 'bias-mitigation', 'vision-language-models', 'alignment', 'safety']
venue: "ICML 2024"
tldr: "A framework is proposed to characterize and mitigate failure modes—including biases and misalignment—in large-scale vision and language models before deployment."
---

# Failures Are Fated, But Can Be Faded: Characterizing and Mitigating Unwanted Behaviors in Large-Scale Vision and Language Models

**Source**: [https://proceedings.mlr.press/v235/sagar24a.html](https://proceedings.mlr.press/v235/sagar24a.html)

**TLDR**: A framework is proposed to characterize and mitigate failure modes—including biases and misalignment—in large-scale vision and language models before deployment.

## Abstract

In large deep neural networks that seem to perform surprisingly well on many tasks, we also observe a few failures related to accuracy, social biases, and alignment with human values, among others. Therefore, before deploying these models, it is crucial to characterize this failure landscape for engineers to debug and legislative bodies to audit models. Nevertheless, it is infeasible to exhaustively test for all possible combinations of factors that could lead to a model’s failure. In this paper, we introduce a post-hoc method that utilizes deep reinforcement learning to explore and construct the landscape of failure modes in pre-trained discriminative and generative models. With the aid of limited human feedback, we then demonstrate how to restructure the failure landscape to be more desirable by moving away from the discovered failure modes. We empirically show the effectiveness of the proposed method across common Computer Vision, Natural Language Processing, and Vision-Language tasks.