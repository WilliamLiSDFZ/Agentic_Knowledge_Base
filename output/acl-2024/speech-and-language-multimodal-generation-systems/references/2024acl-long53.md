---
title: "Prompt Refinement with Image Pivot for Text-to-Image Generation"
source: "https://aclanthology.org/2024.acl-long.53/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'speech-and-language-multimodal-generation-systems']
tags: ['text-to-image', 'prompt-refinement', 'image-pivot']
venue: "ACL 2024"
tldr: "An image-pivoted approach automatically refines user prompts into keyword-enriched prompts for improved text-to-image generation."
---

# Prompt Refinement with Image Pivot for Text-to-Image Generation

**Source**: [https://aclanthology.org/2024.acl-long.53/](https://aclanthology.org/2024.acl-long.53/)

**TLDR**: An image-pivoted approach automatically refines user prompts into keyword-enriched prompts for improved text-to-image generation.

## Abstract

AbstractFor text-to-image generation, automatically refining user-provided natural language prompts into the keyword-enriched prompts favored by systems is essential for the user experience. Such a prompt refinement process is analogous to translating the prompt from “user languages” into “system languages”. However, the scarcity of such parallel corpora makes it difficult to train a prompt refinement model. Inspired by zero-shot machine translation techniques, we introduce Prompt Refinement with Image Pivot (PRIP). PRIP innovatively uses the latent representation of a user-preferred image as an intermediary “pivot” between the user and system languages. It decomposes the refinement process into two data-rich tasks: inferring representations of user-preferred images from user languages and subsequently translating image representations into system languages. Thus, it can leverage abundant data for training. Extensive experiments show that PRIP substantially outperforms a wide range of baselines and effectively transfers to unseen systems in a zero-shot manner.