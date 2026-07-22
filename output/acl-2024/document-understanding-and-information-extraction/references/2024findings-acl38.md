---
title: "Towards Better Graph-based Cross-document Relation Extraction via Non-bridge Entity Enhancement and Prediction Debiasing"
source: "https://aclanthology.org/2024.findings-acl.38/"
categories: ['natural-language-processing-information-extraction', 'document-understanding-and-information-extraction']
tags: ['cross-document-relation-extraction', 'graph-based', 'entity-enhancement']
venue: "ACL 2024"
tldr: "Enhances cross-document relation extraction via non-bridge entity augmentation and prediction debiasing in graph-based models."
---

# Towards Better Graph-based Cross-document Relation Extraction via Non-bridge Entity Enhancement and Prediction Debiasing

**Source**: [https://aclanthology.org/2024.findings-acl.38/](https://aclanthology.org/2024.findings-acl.38/)

**TLDR**: Enhances cross-document relation extraction via non-bridge entity augmentation and prediction debiasing in graph-based models.

## Abstract

AbstractCross-document Relation Extraction aims to predict the relation between target entities located in different documents. In this regard, the dominant models commonly retain useful information for relation prediction via bridge entities, which allows the model to elaborately capture the intrinsic interdependence between target entities. However, these studies ignore the non-bridge entities, each of which co-occurs with only one target entity and offers the semantic association between target entities for relation prediction. Besides, the commonly-used dataset–CodRED contains substantial NA instances, leading to the prediction bias during inference. To address these issues, in this paper, we propose a novel graph-based cross-document RE model with non-bridge entity enhancement and prediction debiasing. Specifically, we use a unified entity graph to integrate numerous non-bridge entities with target entities and bridge entities, modeling various associations between them, and then use a graph recurrent network to encode this graph. Finally, we introduce a novel debiasing strategy to calibrate the original prediction distribution. Experimental results on the closed and open settings show that our model significantly outperforms all baselines, including the GPT-3.5-turbo and InstructUIE, achieving state-of-the-art performance. Particularly, our model obtains 66.23% and 55.87% AUC points in the official leaderboard under the two settings, respectively,ranking the first place in all submissions since December 2023. Our code is available at https://github.com/DeepLearnXMU/CoRE-NEPD.