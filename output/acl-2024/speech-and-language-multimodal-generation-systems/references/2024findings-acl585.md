---
title: "Self-Supervised Singing Voice Pre-Training towards Speech-to-Singing Conversion"
source: "https://aclanthology.org/2024.findings-acl.585/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems', 'multimodal-language-vision-learning-systems']
tags: ['speech-to-singing', 'self-supervised', 'voice-conversion']
venue: "ACL 2024"
tldr: "A self-supervised singing voice pre-training approach addresses data scarcity and quality challenges in speech-to-singing conversion."
---

# Self-Supervised Singing Voice Pre-Training towards Speech-to-Singing Conversion

**Source**: [https://aclanthology.org/2024.findings-acl.585/](https://aclanthology.org/2024.findings-acl.585/)

**TLDR**: A self-supervised singing voice pre-training approach addresses data scarcity and quality challenges in speech-to-singing conversion.

## Abstract

AbstractSpeech-to-singing voice conversion (STS) task always suffers from data scarcity, because it requires paired speech and singing data. Compounding this issue are the challenges of content-pitch alignment and the suboptimal quality of generated outputs, presenting significant hurdles in STS research. This paper presents SVPT, an STS approach boosted by a self-supervised singing voice pre-training model.We leverage spoken language model techniques to tackle the rhythm alignment problem and the in-context learning capability to achieve zero-shot conversion. We adopt discrete-unit random resampling and pitch corruption strategies, enabling training with unpaired singing data and thus mitigating the issue of data scarcity. SVPT also serves as an effective backbone for singing voice synthesis (SVS), offering insights into scaling up SVS models. Experimental results indicate that SVPT delivers notable improvements in both STS and SVS endeavors. Audio samples are available at https://speech2sing.github.io.