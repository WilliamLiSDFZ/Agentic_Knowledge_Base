---
title: "Interactive Text-to-Image Retrieval with Large Language Models: A Plug-and-Play Approach"
source: "https://aclanthology.org/2024.acl-long.46/"
categories: ['multimodal-language-vision-learning-systems', 'speech-and-language-multimodal-generation-systems']
tags: ['interactive-retrieval', 'text-to-image', 'LLM-plug-in']
venue: "ACL 2024"
tldr: "PlugIR addresses dialogue-based interactive text-to-image retrieval by leveraging LLMs' instruction-following capabilities as a plug-and-play module."
---

# Interactive Text-to-Image Retrieval with Large Language Models: A Plug-and-Play Approach

**Source**: [https://aclanthology.org/2024.acl-long.46/](https://aclanthology.org/2024.acl-long.46/)

**TLDR**: PlugIR addresses dialogue-based interactive text-to-image retrieval by leveraging LLMs' instruction-following capabilities as a plug-and-play module.

## Abstract

AbstractIn this paper, we primarily address the issue of dialogue-form context query within the interactive text-to-image retrieval task. Our methodology, PlugIR, actively utilizes the general instruction-following capability of LLMs in two ways. First, by reformulating the dialogue-form context, we eliminate the necessity of fine-tuning a retrieval model on existing visual dialogue data, thereby enabling the use of any arbitrary black-box model. Second, we construct the LLM questioner to generate non-redundant questions about the attributes of the target image, based on the information of retrieval candidate images in the current context. This approach mitigates the issues of noisiness and redundancy in the generated questions. Beyond our methodology, we propose a novel evaluation metric, Best log Rank Integral (BRI), for a comprehensive assessment of the interactive retrieval system. PlugIR demonstrates superior performance compared to both zero-shot and fine-tuned baselines in various benchmarks. Additionally, the two methodologies comprising PlugIR can be flexibly applied together or separately in various situations.