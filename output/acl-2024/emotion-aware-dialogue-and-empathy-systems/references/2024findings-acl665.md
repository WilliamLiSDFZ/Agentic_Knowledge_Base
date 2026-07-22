---
title: "Both Matter: Enhancing the Emotional Intelligence of Large Language Models without Compromising the General Intelligence"
source: "https://aclanthology.org/2024.findings-acl.665/"
categories: ['emotion-aware-dialogue-and-empathy-systems', 'llm-training-alignment-and-evaluation']
tags: ['emotional-intelligence', 'llm-alignment', 'conversational-ai']
venue: "ACL 2024"
tldr: "Enhances LLMs' emotional intelligence across perception, cognition, and expression dimensions without degrading their general reasoning capabilities."
---

# Both Matter: Enhancing the Emotional Intelligence of Large Language Models without Compromising the General Intelligence

**Source**: [https://aclanthology.org/2024.findings-acl.665/](https://aclanthology.org/2024.findings-acl.665/)

**TLDR**: Enhances LLMs' emotional intelligence across perception, cognition, and expression dimensions without degrading their general reasoning capabilities.

## Abstract

AbstractEmotional Intelligence (EI), consisting of emotion perception, emotion cognition and emotion expression, plays the critical roles in improving user interaction experience for the current large language model (LLM) based conversational general AI assistants. Previous works mainly focus on raising the emotion perception ability of them via naive fine-tuning on EI-related classification or regression tasks. However, this leads to the incomplete enhancement of EI and catastrophic forgetting of the general intelligence (GI). To this end, we first introduce EiBench, a large-scale collection of EI-related tasks in the text-to-text format with task instructions that covers all three aspects of EI, which lays a solid foundation for the comprehensive EI enhancement of LLMs. Then a novel Modular Emotional Intelligence enhancement method (**MoEI**), consisting of Modular Parameter Expansion and intra-inter modulation, is proposed to comprehensively enhance the EI of LLMs without compromise their GI. Extensive experiments on two representative LLM-based assistants, Flan-T5 and LLaMA-2-Chat, demonstrate the effectiveness of MoEI to improving EI while maintain GI.