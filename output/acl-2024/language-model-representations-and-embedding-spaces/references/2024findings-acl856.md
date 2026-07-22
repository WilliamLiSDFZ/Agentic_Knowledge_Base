---
title: "Fooling the Textual Fooler via Randomizing Latent Representations"
source: "https://aclanthology.org/2024.findings-acl.856/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'language-model-representations-and-embedding-spaces']
tags: ['adversarial-robustness', 'textual-attacks', 'latent-randomization']
venue: "ACL 2024"
tldr: "A defense against textual adversarial attacks by randomizing latent representations to fool adversarial text generators."
---

# Fooling the Textual Fooler via Randomizing Latent Representations

**Source**: [https://aclanthology.org/2024.findings-acl.856/](https://aclanthology.org/2024.findings-acl.856/)

**TLDR**: A defense against textual adversarial attacks by randomizing latent representations to fool adversarial text generators.

## Abstract

AbstractDespite outstanding performance in a variety of Natural Language Processing (NLP) tasks, recent studies have revealed that NLP models are vulnerable to adversarial attacks that slightly perturb the input to cause the models to misbehave. Several attacks can even compromise the model without requiring access to the model architecture or model parameters (i.e., a blackbox setting), and thus are detrimental to existing NLP applications. To perform these attacks, the adversary queries the victim model many times to determine the most important parts in an input text and transform. In this work, we propose a lightweight and attack-agnostic defense whose main goal is to perplex the process of generating an adversarial example in these query-based black-box attacks; that is to fool the textual fooler. This defense, named AdvFooler, works by randomizing the latent representation of the input at inference time. Different from existing defenses, AdvFooler does not necessitate additional computational overhead during training nor does it rely on assumptions about the potential adversarial perturbation set while having a negligible impact on the model’s accuracy. Our theoretical and empirical analyses highlight the significance of robustness resulting from confusing the adversary via randomizing the latent space, as well as the impact of randomization on clean accuracy. Finally, we empirically demonstrate near state-of-the-art robustness of AdvFooler against representative adversarial attacks on two benchmark datasets.