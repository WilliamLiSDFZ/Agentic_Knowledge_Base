---
title: "Exploring Defeasibility in Causal Reasoning"
source: "https://aclanthology.org/2024.findings-acl.384/"
pdf_url: ""
categories: ['causal-reasoning-and-explanation-in-nlp', 'moral-figurative-language-nlp-analysis']
tags: ['causal-reasoning', 'defeasibility', 'strengthening', 'weakening', 'argumentation']
venue: "ACL 2024"
tldr: "Explores defeasibility in causal reasoning by examining how supporting or weakening arguments affect causal strength between cause and effect."
---

# Exploring Defeasibility in Causal Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.384/](https://aclanthology.org/2024.findings-acl.384/)

**TLDR**: Explores defeasibility in causal reasoning by examining how supporting or weakening arguments affect causal strength between cause and effect.

## Abstract

AbstractDefeasibility in causal reasoning implies that the causal relationship between cause and effect can be strengthened or weakened. Namely, the causal strength between cause and effect should increase or decrease with the incorporation of strengthening arguments (supporters) or weakening arguments (defeaters), respectively. However, existing works ignore defeasibility in causal reasoning and fail to evaluate existing causal strength metrics in defeasible settings. In this work, we present 𝛿-CAUSAL, the first benchmark dataset for studying defeasibility in causal reasoning. 𝛿-CAUSAL includes around 11K events spanning ten domains, featuring defeasible causality pairs, namely, cause-effect pairs accompanied by supporters and defeaters. We further show that current causal strength metrics fail to reflect the change of causal strength with the incorporation of supporters or defeaters in 𝛿-CAUSAL. To this end, we propose CESAR (Causal Embedding aSsociation with Attention Rating), a metric that measures causal strength based on token-level causal relationships. CESAR achieves a significant 69.7% relative improvement over existing metrics, increasing from 47.2% to 80.1% in capturing the causal strength change brought by supporters and defeaters. We further demonstrate even Large Language Models (LLMs) like GPT-3.5 still lag 4.5 and 10.7 points behind humans in generating supporters and defeaters, emphasizing the challenge posed by 𝛿-CAUSAL.