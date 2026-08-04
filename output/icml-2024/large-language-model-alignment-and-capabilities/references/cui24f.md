---
title: "ULTRAFEEDBACK: Boosting Language Models with Scaled AI Feedback"
source: "https://proceedings.mlr.press/v235/cui24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cui24f/cui24f.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'learning-with-imperfect-data-and-bias']
tags: ['llm-alignment', 'ai-feedback', 'preference-learning']
venue: "ICML 2024"
tldr: "Introduces ULTRAFEEDBACK, a large-scale AI feedback dataset to boost LLM alignment by scaling preference data collection using AI annotations."
---

# ULTRAFEEDBACK: Boosting Language Models with Scaled AI Feedback

**Source**: [https://proceedings.mlr.press/v235/cui24f.html](https://proceedings.mlr.press/v235/cui24f.html)

**TLDR**: Introduces ULTRAFEEDBACK, a large-scale AI feedback dataset to boost LLM alignment by scaling preference data collection using AI annotations.

## Abstract

Learning from human feedback has become a pivot technique in aligning large language models (LLMs) with human preferences. However, acquiring vast and premium human feedback is bottlenecked by time, labor, and human capability, resulting in small sizes or limited topics of current datasets. This further hinders feedback learning as well as alignment research within the open-source community. To address this issue, we explore how to go beyond human feedback and collect high-quality AI feedback automatically for a scalable alternative. Specifically, we identify scale and diversity as the key factors for feedback data to take effect. Accordingly, we first broaden instructions and responses in both amount and breadth to encompass a wider range of user-assistant interactions. Then, we meticulously apply a series of techniques to mitigate annotation biases for more reliable AI feedback. We finally present UltraFeedback, a large-scale, high-quality, and diversified AI feedback dataset, which contains over 1 million GPT-4 feedback for 250k user-assistant conversations from various aspects. Built upon UltraFeedback, we align a LLaMA-based model by best-of-$n$ sampling and reinforcement learning, demonstrating its exceptional performance on chat benchmarks. Our work validates the effectiveness of scaled AI feedback data in constructing strong open-source chat language models, serving as a solid foundation for future feedback learning research.