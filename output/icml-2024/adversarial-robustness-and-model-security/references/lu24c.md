---
title: "Position: Exploring the Robustness of Pipeline-Parallelism-Based Decentralized Training"
source: "https://proceedings.mlr.press/v235/lu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24c/lu24c.pdf"
categories: ['adversarial-robustness-and-model-security', 'position-papers-on-ml-research-directions']
tags: ['pipeline-parallelism', 'decentralized-training', 'robustness', 'adversarial-threats', 'position-paper']
venue: "ICML 2024"
tldr: "Position paper examining security vulnerabilities and robustness of pipeline-parallelism-based decentralized training."
---

# Position: Exploring the Robustness of Pipeline-Parallelism-Based Decentralized Training

**Source**: [https://proceedings.mlr.press/v235/lu24c.html](https://proceedings.mlr.press/v235/lu24c.html)

**TLDR**: Position paper examining security vulnerabilities and robustness of pipeline-parallelism-based decentralized training.

## Abstract

Modern machine learning applications increasingly demand greater computational resources for training large models. Decentralized training has emerged as an effective means to democratize this technology. However, the potential threats associated with this approach remain inadequately discussed, posing a hurdle to the development of decentralized training infrastructures. This paper aims to initiate discussion towards this end by exploring the robustness of decentralized training from three primary perspectives. Firstly, we articulate our position on establishing robust decentralized training by outlining potential threats and the corresponding countermeasures. Secondly, we illustrate a nascent poisoning attack targeting decentralized training frameworks, easily executable by malicious stages. To mitigate this security threat and ensure efficient training, we propose a robust training framework, integrating a 100% detection strategy and efficient training mechanisms. Finally, we demonstrate the severity of the proposed attack and the effectiveness of our robust training framework. This position paper emphasizes the urgency of exploring the robustness of decentralized training and proposes a feasible solution. The code is available at https://github.com/dcx001016/pipeline_attack.