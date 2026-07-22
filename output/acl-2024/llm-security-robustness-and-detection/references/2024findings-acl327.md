---
title: "Subtle Signatures, Strong Shields: Advancing Robust and Imperceptible Watermarking in Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.327/"
categories: ['llm-security-robustness-and-detection', 'continuous-discrete-representation-tradeoffs']
tags: ['watermarking', 'LLM', 'AI-generated-text', 'imperceptible', 'robustness']
venue: "ACL 2024"
tldr: "Proposes an advanced watermarking approach for LLMs that is both robust and imperceptible, helping distinguish AI-generated from human-written text."
---

# Subtle Signatures, Strong Shields: Advancing Robust and Imperceptible Watermarking in Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.327/](https://aclanthology.org/2024.findings-acl.327/)

**TLDR**: Proposes an advanced watermarking approach for LLMs that is both robust and imperceptible, helping distinguish AI-generated from human-written text.

## Abstract

AbstractThe widespread adoption of Large Language Models (LLMs) has led to an increase in AI-generated text on the Internet, presenting a crucial challenge to differentiate AI-created content from human-written text. This challenge is critical to prevent issues of authenticity, trust, and potential copyright violations. Current research focuses on watermarking LLM-generated text, but traditional techniques struggle to balance robustness with text quality. We introduce a novel watermarking approach, Robust and Imperceptible Watermarking (RIW) for LLMs, which leverages token prior probabilities to improve detectability and maintain watermark imperceptibility. RIW methodically embeds watermarks by partitioning selected tokens into two distinct groups based on their prior probabilities and employing tailored strategies for each group. In the detection stage, the RIW method employs the ‘voted z-test’ to provide a statistically robust framework to identify the presence of a watermark accurately. The effectiveness of RIW is evaluated across three key dimensions: success rate, text quality, and robustness against removal attacks. Our experimental results on various LLMs, including GPT2-XL, OPT-1.3B, and LLaMA2-7B, indicate that RIW surpasses existing models, and also exhibits increased robustness against various attacks and good imperceptibility, thus promoting the responsible use of LLMs.