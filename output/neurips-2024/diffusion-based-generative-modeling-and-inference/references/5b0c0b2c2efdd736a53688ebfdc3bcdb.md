---
title: "ShowMaker: Creating High-Fidelity 2D Human Video via Fine-Grained Diffusion Modeling"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5b0c0b2c2efdd736a53688ebfdc3bcdb-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference', 'visual-language-multimodal-generation-reasoning']
tags: ['human-video-generation', 'diffusion-models', 'gesture-animation']
venue: "NeurIPS 2024"
tldr: "Proposes ShowMaker, a fine-grained diffusion model for generating high-fidelity conversational human videos with facial and hand animations."
---

# ShowMaker: Creating High-Fidelity 2D Human Video via Fine-Grained Diffusion Modeling

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5b0c0b2c2efdd736a53688ebfdc3bcdb-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/5b0c0b2c2efdd736a53688ebfdc3bcdb-Abstract-Conference.html)

**TLDR**: Proposes ShowMaker, a fine-grained diffusion model for generating high-fidelity conversational human videos with facial and hand animations.

## Abstract

Although significant progress has been made in human video generation, most previous studies focus on either human facial animation or full-body animation, which cannot be directly applied to produce realistic conversational human videos with frequent hand gestures and various facial movements simultaneously.To address these limitations, we propose a 2D human video generation framework, named ShowMaker, capable of generating high-fidelity half-body conversational videos via fine-grained diffusion modeling.We leverage dual-stream diffusion models as the backbone of our framework and carefully design two novel components for crucial local regions (i.e., hands and face) that can be easily integrated into our backbone.Specifically, to handle the challenging hand generation caused by sparse motion guidance, we propose a novel Key Point-based Fine-grained Hand Modeling module by amplifying positional information from raw hand key points and constructing a corresponding key point-based codebook. Moreover, to restore richer facial details in generated results, we introduce a Face Recapture module, which extracts facial texture features and global identity features from the aligned human face and integrates them into the diffusion process for face enhancement. Extensive quantitative and qualitative experiments demonstrate the superior visual quality and temporal consistency of our method.