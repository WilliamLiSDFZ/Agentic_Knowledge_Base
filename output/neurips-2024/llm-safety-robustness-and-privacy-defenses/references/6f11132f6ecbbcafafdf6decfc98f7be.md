---
title: "ColJailBreak: Collaborative Generation and Editing for Jailbreaking Text-to-Image Deep Generation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6f11132f6ecbbcafafdf6decfc98f7be-Abstract-Conference.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'generative-models-for-visual-style-and-appearance']
tags: ['jailbreaking', 'text-to-image', 'safety-filter-bypass']
venue: "NeurIPS 2024"
tldr: "ColJailBreak uses collaborative generation and editing to bypass safety filters in commercial text-to-image generation models."
---

# ColJailBreak: Collaborative Generation and Editing for Jailbreaking Text-to-Image Deep Generation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6f11132f6ecbbcafafdf6decfc98f7be-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/6f11132f6ecbbcafafdf6decfc98f7be-Abstract-Conference.html)

**TLDR**: ColJailBreak uses collaborative generation and editing to bypass safety filters in commercial text-to-image generation models.

## Abstract

The commercial text-to-image deep generation models (e.g. DALL·E) can produce high-quality images based on input language descriptions. These models incorporate a black-box safety filter to prevent the generation of unsafe or unethical content, such as violent, criminal, or hateful imagery. Recent jailbreaking methods generate adversarial prompts capable of bypassing safety filters and producing unsafe content, exposing vulnerabilities in influential commercial models. However, once these adversarial prompts are identified, the safety filter can be updated to prevent the generation of unsafe images. In this work, we propose an effective, simple, and difficult-to-detect jailbreaking solution: generating safe content initially with normal text prompts and then editing the generations to embed unsafe content. The intuition behind this idea is that the deep generation model cannot reject safe generation with normal text prompts, while the editing models focus on modifying the local regions of images and do not involve a safety strategy. However, implementing such a solution is non-trivial, and we need to overcome several challenges: how to automatically confirm the normal prompt to replace the unsafe prompts, and how to effectively perform editable replacement and naturally generate unsafe content. In this work, we propose the collaborative generation and editing for jailbreaking text-to-image deep generation (ColJailBreak), which comprises three key components: adaptive normal safe substitution, inpainting-driven injection of unsafe content, and contrastive language-image-guided collaborative optimization. We validate our method on three datasets and compare it to two baseline methods. Our method could generate unsafe content through two commercial deep generation models including GPT-4 and DALL·E 2.