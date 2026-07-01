---
title: "InterDreamer: Zero-Shot Text to 3D Dynamic Human-Object Interaction"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5eca2e4fe7858cbbfef4e08573cfcb25-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning', 'neural-geometric-shape-representation-learning']
tags: ['text-to-3d', 'human-object-interaction', 'zero-shot-generation']
venue: "NeurIPS 2024"
tldr: "Presents InterDreamer, a zero-shot framework for generating 3D dynamic human-object interactions from text by combining motion and interaction priors without paired training data."
---

# InterDreamer: Zero-Shot Text to 3D Dynamic Human-Object Interaction

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5eca2e4fe7858cbbfef4e08573cfcb25-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/5eca2e4fe7858cbbfef4e08573cfcb25-Abstract-Conference.html)

**TLDR**: Presents InterDreamer, a zero-shot framework for generating 3D dynamic human-object interactions from text by combining motion and interaction priors without paired training data.

## Abstract

Text-conditioned human motion generation has experienced significant advancements with diffusion models trained on extensive motion capture data and corresponding textual annotations. However, extending such success to 3D dynamic human-object interaction (HOI) generation faces notable challenges, primarily due to the lack of large-scale interaction data and comprehensive descriptions that align with these interactions. This paper takes the initiative and showcases the potential of generating human-object interactions without direct training on text-interaction pair data. Our key insight in achieving this is that interaction semantics and dynamics can be decoupled. Being unable to learn interaction semantics through supervised training, we instead leverage pre-trained large models, synergizing knowledge from a large language model and a text-to-motion model. While such knowledge offers high-level control over interaction semantics, it cannot grasp the intricacies of low-level interaction dynamics. To overcome this issue, we introduce a world model designed to comprehend simple physics, modeling how human actions influence object motion. By integrating these components, our novel framework, InterDreamer, is able to generate text-aligned 3D HOI sequences without relying on paired text-interaction data. We apply InterDreamer to the BEHAVE, OMOMO, and CHAIRS datasets, and our comprehensive experimental analysis demonstrates its capability to generate realistic and coherent interaction sequences that seamlessly align with the text directives.