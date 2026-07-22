---
title: "Description Boosting for Zero-Shot Entity and Relation Classification"
source: "https://aclanthology.org/2024.findings-acl.562/"
categories: ['natural-language-processing-information-extraction', 'concept-embedding-taxonomy-hierarchy-representation']
tags: ['zero-shot-classification', 'entity-relation', 'description-boosting']
venue: "ACL 2024"
tldr: "Enhances zero-shot entity and relation classification by leveraging textual descriptions to boost model generalization to unseen classes."
---

# Description Boosting for Zero-Shot Entity and Relation Classification

**Source**: [https://aclanthology.org/2024.findings-acl.562/](https://aclanthology.org/2024.findings-acl.562/)

**TLDR**: Enhances zero-shot entity and relation classification by leveraging textual descriptions to boost model generalization to unseen classes.

## Abstract

AbstractZero-shot entity and relation classification models leverage available external information of unseen classes – e.g., textual descriptions – to annotate input text data. Thanks to the minimum data requirement, Zero-Shot Learning (ZSL) methods have high value in practice, especially in applications where labeled data is scarce. Even though recent research in ZSL has demonstrated significant results, our analysis reveals that those methods are sensitive to provided textual descriptions of entities (or relations). Even a minor modification of descriptions can lead to a change in the decision boundary between entity (or relation) classes. In this paper, we formally define the problem of identifying effective descriptions for zero shot inference. We propose a strategy for generating variations of an initial description, a heuristic for ranking them and an ensemble method capable of boosting the predictions of zero-shot models through description enhancement. Empirical results on four different entity and relation classification datasets show that our proposed method outperform existing approaches and achieve new SOTA results on these datasets under the ZSL settings. The source code of the proposed solutions and the evaluation framework are open-sourced.