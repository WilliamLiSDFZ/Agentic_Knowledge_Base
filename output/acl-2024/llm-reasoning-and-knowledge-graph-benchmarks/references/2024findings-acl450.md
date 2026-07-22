---
title: "Trust in Internal or External Knowledge? Generative Multi-Modal Entity Linking with Knowledge Retriever"
source: "https://aclanthology.org/2024.findings-acl.450/"
categories: ['multimodal-language-vision-learning-systems', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['multimodal-entity-linking', 'knowledge-retrieval', 'generative-models']
venue: "ACL 2024"
tldr: "A generative multi-modal entity linking approach that balances internal parametric knowledge with external knowledge retrieval."
---

# Trust in Internal or External Knowledge? Generative Multi-Modal Entity Linking with Knowledge Retriever

**Source**: [https://aclanthology.org/2024.findings-acl.450/](https://aclanthology.org/2024.findings-acl.450/)

**TLDR**: A generative multi-modal entity linking approach that balances internal parametric knowledge with external knowledge retrieval.

## Abstract

AbstractMulti-modal entity linking (MEL) is a challenging task that requires accurate prediction of entities within extensive search spaces, utilizing multi-modal contexts. Existing generative approaches struggle with the knowledge gap between visual entity information and the intrinsic parametric knowledge of LLMs. To address this knowledge gap, we introduce a novel approach called GELR, which incorporates a knowledge retriever to enhance visual entity information by leveraging external sources. Additionally, we devise a prioritization scheme that effectively handles noisy retrieval results and manages conflicts arising from the integration of external and internal knowledge. Moreover, we propose a noise-aware instruction tuning technique during training to finely adjust the model’s ability to leverage retrieved information effectively. Through extensive experiments conducted on three benchmarks, our approach showcases remarkable improvements, ranging from 3.0% to 6.5%, across all evaluation metrics compared to strong baselines. These results demonstrate the effectiveness and superiority of our proposed method in tackling the complexities of multi-modal entity linking.