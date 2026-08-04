---
title: "Safety Fine-Tuning at (Almost) No Cost: A Baseline for Vision Large Language Models"
source: "https://proceedings.mlr.press/v235/zong24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zong24a/zong24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'adversarial-robustness-and-model-security']
tags: ['safety-fine-tuning', 'vision-language-models', 'jailbreak', 'harmful-content', 'alignment']
venue: "ICML 2024"
tldr: "This paper proposes a cost-effective safety fine-tuning baseline for vision large language models to mitigate harmful content generation and jailbreaking vulnerabilities."
---

# Safety Fine-Tuning at (Almost) No Cost: A Baseline for Vision Large Language Models

**Source**: [https://proceedings.mlr.press/v235/zong24a.html](https://proceedings.mlr.press/v235/zong24a.html)

**TLDR**: This paper proposes a cost-effective safety fine-tuning baseline for vision large language models to mitigate harmful content generation and jailbreaking vulnerabilities.

## Abstract

Current vision large language models (VLLMs) exhibit remarkable capabilities yet are prone to generate harmful content and are vulnerable to even the simplest jailbreaking attacks. Our initial analysis finds that this is due to the presence of harmful data during vision-language instruction fine-tuning, and that VLLM fine-tuning can cause forgetting of safety alignment previously learned by the underpinning LLM. To address this issue, we first curate a vision-language safe instruction-following dataset VLGuard covering various harmful categories. Our experiments demonstrate that integrating this dataset into standard vision-language fine-tuning or utilizing it for post-hoc fine-tuning effectively safety aligns VLLMs. This alignment is achieved with minimal impact on, or even enhancement of, the models’ helpfulness. The versatility of our safety fine-tuning dataset makes it a valuable resource for safety-testing existing VLLMs, training new models or safeguarding pre-trained VLLMs. Empirical results demonstrate that fine-tuned VLLMs effectively reject unsafe instructions and substantially reduce the success rates of several black-box adversarial attacks, which approach zero in many cases. The code and dataset will be open-sourced.