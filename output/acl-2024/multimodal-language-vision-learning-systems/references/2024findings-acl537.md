---
title: "TextBind: Multi-turn Interleaved Multimodal Instruction-following in the Wild"
source: "https://aclanthology.org/2024.findings-acl.537/"
categories: ['multimodal-language-vision-learning-systems', 'llm-training-alignment-and-evaluation']
tags: ['multimodal-instruction-following', 'interleaved-dialogue', 'dataset']
venue: "ACL 2024"
tldr: "Introduces TextBind, a framework and dataset for multi-turn interleaved multimodal instruction-following with large language models."
---

# TextBind: Multi-turn Interleaved Multimodal Instruction-following in the Wild

**Source**: [https://aclanthology.org/2024.findings-acl.537/](https://aclanthology.org/2024.findings-acl.537/)

**TLDR**: Introduces TextBind, a framework and dataset for multi-turn interleaved multimodal instruction-following with large language models.

## Abstract

AbstractLarge language models with instruction-following abilities have revolutionized the field of artificial intelligence. These models show exceptional generalizability to tackle various real-world tasks through their natural language interfaces. However, their performance heavily relies on high-quality exemplar data, which is often difficult to obtain. This challenge is further exacerbated when it comes to multimodal instruction following. We introduce TextBind, an almost annotation-free framework for empowering LLMs with multi-turn interleaved multimodal instruction-following capabilities. Our approach requires only image-caption pairs and generates multi-turn multimodal instruction-response conversations from a language model. To accommodate interleaved image-text inputs and outputs, we devise MIM, a language model-centric architecture that seamlessly integrates image encoder and decoder models. Extensive quantitative and qualitative experiments demonstrate that MIM trained on TextBind achieves remarkable generation capability in multimodal conversations compared to recent baselines.