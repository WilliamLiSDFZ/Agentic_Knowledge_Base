---
title: "DiffusPoll: Conditional Text Diffusion Model for Poll Generation"
source: "https://aclanthology.org/2024.findings-acl.54/"
pdf_url: ""
categories: ['text-diffusion-for-content-generation', 'social-ai-temporal-dynamics-evaluation']
tags: ['text-diffusion', 'poll-generation', 'social-media']
venue: "ACL 2024"
tldr: "A conditional text diffusion model generates polls from social media context to reduce manual labor for media workers."
---

# DiffusPoll: Conditional Text Diffusion Model for Poll Generation

**Source**: [https://aclanthology.org/2024.findings-acl.54/](https://aclanthology.org/2024.findings-acl.54/)

**TLDR**: A conditional text diffusion model generates polls from social media context to reduce manual labor for media workers.

## Abstract

AbstractOnline social media platforms often gather user feedback through polls to enhance user engagement. Automatically generating polls from social media and its context can decrease the labor expenses of media workers and enhance workplace productivity. However, on social media platforms, there are internet water armies that manipulate public opinion through sheer numbers and causing the comments to be biased, drowning out minority views. In such circumstances, polls created based on biased comments often have limited types of options and poor coverage. Therefore, it is crucial to diversify the poll options and try to listen to the voices of the minority. To achieve this, we introduce DiffusPoll, a novel paradigm for poll generation based on a non-autoregressive diffusion model that can generate diversified and high-quality samples. Under the new paradigm, we design a task-specific mask strategy tailored to the inherent logic of polls to optimize controlled generation. Furthermore, we also leverage additional attribute tags from comments to enhance the generation quality. Experimental results indicate that DiffusPoll has achieved state-of-the-art performance in both the quality and diversity of poll generation tasks, and is more likely to hit the voices of minority.