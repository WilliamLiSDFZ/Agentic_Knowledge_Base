---
title: "TELLER: A Trustworthy Framework for Explainable, Generalizable and Controllable Fake News Detection"
source: "https://aclanthology.org/2024.findings-acl.919/"
categories: ['computational-misinformation-narrative-framing-detection', 'llm-hallucination-detection-and-mitigation']
tags: ['fake-news-detection', 'explainability', 'controllable-classification']
venue: "ACL 2024"
tldr: "TELLER is a trustworthy fake news detection framework that improves explainability, generalizability, and controllability over existing deep-learning approaches."
---

# TELLER: A Trustworthy Framework for Explainable, Generalizable and Controllable Fake News Detection

**Source**: [https://aclanthology.org/2024.findings-acl.919/](https://aclanthology.org/2024.findings-acl.919/)

**TLDR**: TELLER is a trustworthy fake news detection framework that improves explainability, generalizability, and controllability over existing deep-learning approaches.

## Abstract

AbstractThe proliferation of fake news has emerged as a severe societal problem, raising significant interest from industry and academia. While existing deep-learning based methods have made progress in detecting fake news accurately, their reliability may be compromised caused by the non-transparent reasoning processes, poor generalization abilities and inherent risks of integration with large language models (LLMs). To address this challenge, we propose TELLER, a novel framework for trustworthy fake news detection that prioritizes explainability, generalizability and controllability of models. This is achieved via a dual-system framework that integrates cognition and decision systems, adhering to the principles above. The cognition system harnesses human expertise to generate logical predicates, which guide LLMs in generating human-readable logic atoms. Meanwhile, the decision system deduces generalizable logic rules to aggregate these atoms, enabling the identification of the truthfulness of the input news across diverse domains and enhancing transparency in the decision-making process. Finally, we present comprehensive evaluation results on four datasets, demonstrating the feasibility and trustworthiness of our proposed framework.