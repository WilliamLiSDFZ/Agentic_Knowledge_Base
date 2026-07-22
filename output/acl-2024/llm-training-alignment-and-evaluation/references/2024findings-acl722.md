---
title: "Prefix Text as a Yarn: Eliciting Non-English Alignment in Foundation Language Model"
source: "https://aclanthology.org/2024.findings-acl.722/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'language-technology-cultural-linguistic-diversity']
tags: ['non-english-alignment', 'prefix-prompting', 'foundation-models']
venue: "ACL 2024"
tldr: "Shows that prefix text can elicit non-English alignment in foundation LLMs without supervised fine-tuning, questioning the depth of SFT-based alignment."
---

# Prefix Text as a Yarn: Eliciting Non-English Alignment in Foundation Language Model

**Source**: [https://aclanthology.org/2024.findings-acl.722/](https://aclanthology.org/2024.findings-acl.722/)

**TLDR**: Shows that prefix text can elicit non-English alignment in foundation LLMs without supervised fine-tuning, questioning the depth of SFT-based alignment.

## Abstract

AbstractWhile supervised fine-tuning (SFT) has been a straightforward approach for tailoring the output of foundation large language model (LLM) to specific preferences, concerns have been raised about the depth of this alignment, with some critiques suggesting it is merely “superficial”. We critically examine this hypothesis within the scope of cross-lingual generation tasks, proposing that the effectiveness of SFT may be constrained by its reliance on prior tokens to guide cross-lingual generation. Based on this crucial insight, and in response to the challenges posed by the costly and limited availability of non-English data for SFT, we introduce a novel training-free alignment method named PreTTY, which employs minimal task-related prior tokens to bridge the foundation LLM and the SFT LLM, achieving comparable performance without training. Experiments on machine translation and part-of-speech tagging across seven languages demonstrate the efficacy of PreTTY in cross-lingual settings. Remarkably, by initiating the decoding process with only one or two prior tokens, foundation LLMs can attain up to 98% of the performance metrics of their SFT counterparts. This method presents a cost-effective alternative to traditional SFT and advances the democratization of multilingual LLMs.