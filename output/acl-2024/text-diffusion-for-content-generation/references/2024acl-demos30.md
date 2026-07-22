---
title: "CharPoet: A Chinese Classical Poetry Generation System Based on Token-free LLM"
source: "https://aclanthology.org/2024.acl-demos.30/"
categories: ['text-input-and-generation-for-cjk-languages', 'text-diffusion-for-content-generation']
tags: ['chinese-poetry', 'token-free-llm', 'classical-generation']
venue: "ACL 2024"
tldr: "Presents CharPoet, a token-free LLM-based system for controllable Chinese classical poetry generation at the character level."
---

# CharPoet: A Chinese Classical Poetry Generation System Based on Token-free LLM

**Source**: [https://aclanthology.org/2024.acl-demos.30/](https://aclanthology.org/2024.acl-demos.30/)

**TLDR**: Presents CharPoet, a token-free LLM-based system for controllable Chinese classical poetry generation at the character level.

## Abstract

AbstractAutomatic Chinese classical poetry generation has attracted much research interest, but achieving effective control over format and content simultaneously remains challenging. Traditional systems usually accept keywords as user inputs, resulting in limited control over content. Large language models (LLMs) improve content control by allowing unrestricted user instructions, but the token-by-token generation process frequently makes format errors. Motivated by this, we propose CharPoet, a Chinese classical poetry generation system based on token-free LLM, which provides effective control over both format and content. Our token-free architecture generates in a character-by-character manner, enabling precise control over the number of characters. Pruned from existing token-based LLMs, CharPoet inherits their pretrained capabilities and can generate poetry following instructions like “Write me a poem for my mother’s birthday.” CharPoet achieves format accuracy above 0.96, outperforming Jiuge-GPT-2 (0.91) and GPT-4 (0.38). In terms of content quality, CharPoet surpasses traditional systems including Jiuge, and is comparable to other LLMs. Our system is open source and available at https://modelscope.cn/models/CharPoet/CharPoet. A video demonstration of CharPoet is available at https://youtu.be/voZ25qEp3Dc.