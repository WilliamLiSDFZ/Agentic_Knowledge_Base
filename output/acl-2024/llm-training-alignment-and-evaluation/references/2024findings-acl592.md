---
title: "Direct Preference Optimization with an Offset"
source: "https://aclanthology.org/2024.findings-acl.592/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'continuous-discrete-representation-tradeoffs']
tags: ['direct-preference-optimization', 'alignment', 'fine-tuning']
venue: "ACL 2024"
tldr: "An extension of DPO that incorporates an offset term to better handle varying degrees of preference in human alignment data."
---

# Direct Preference Optimization with an Offset

**Source**: [https://aclanthology.org/2024.findings-acl.592/](https://aclanthology.org/2024.findings-acl.592/)

**TLDR**: An extension of DPO that incorporates an offset term to better handle varying degrees of preference in human alignment data.

## Abstract

AbstractDirect preference optimization (DPO) is a successful fine-tuning strategy for aligning large language models with human preferences without the need to train a reward model or employ reinforcement learning. DPO, as originally formulated, relies on binary preference data and fine-tunes a language model to increase the likelihood of a preferred response over a dispreferred response. However, not all preference pairs are equal. Sometimes, the preferred response is only slightly better than the dispreferred one. In other cases, the preference is much stronger. For instance, if a response contains harmful or toxic content, the annotator will have a strong preference for that response. In this paper, we propose a generalization of DPO, termed DPO with an offset (ODPO), that does not treat every preference pair equally during fine-tuning. Intuitively, ODPO requires the difference between the likelihood of the preferred and dispreferred response to be greater than an offset value. The offset is determined based on the extent to which one response is preferred over another. Our experiments on various tasks suggest that ODPO significantly outperforms DPO in aligning language models, especially when the number of preference pairs is limited.