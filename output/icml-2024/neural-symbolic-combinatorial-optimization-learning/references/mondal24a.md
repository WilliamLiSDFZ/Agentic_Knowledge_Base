---
title: "Slot Abstractors: Toward Scalable Abstract Visual Reasoning"
source: "https://proceedings.mlr.press/v235/mondal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mondal24a/mondal24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'graph-neural-networks-and-topology']
tags: ['abstract-visual-reasoning', 'slot-attention', 'relational-learning', 'systematic-generalization']
venue: "ICML 2024"
tldr: "Slot Abstractors combine slot-based object representations with abstractor mechanisms to achieve scalable abstract visual reasoning over relational patterns."
---

# Slot Abstractors: Toward Scalable Abstract Visual Reasoning

**Source**: [https://proceedings.mlr.press/v235/mondal24a.html](https://proceedings.mlr.press/v235/mondal24a.html)

**TLDR**: Slot Abstractors combine slot-based object representations with abstractor mechanisms to achieve scalable abstract visual reasoning over relational patterns.

## Abstract

Abstract visual reasoning is a characteristically human ability, allowing the identification of relational patterns that are abstracted away from object features, and the systematic generalization of those patterns to unseen problems. Recent work has demonstrated strong systematic generalization in visual reasoning tasks involving multi-object inputs, through the integration of slot-based methods used for extracting object-centric representations coupled with strong inductive biases for relational abstraction. However, this approach was limited to problems containing a single rule, and was not scalable to visual reasoning problems containing a large number of objects. Other recent work proposed Abstractors, an extension of Transformers that incorporates strong relational inductive biases, thereby inheriting the Transformer’s scalability and multi-head architecture, but it has yet to be demonstrated how this approach might be applied to multi-object visual inputs. Here we combine the strengths of the above approaches and propose Slot Abstractors, an approach to abstract visual reasoning that can be scaled to problems involving a large number of objects and multiple relations among them. The approach displays state-of-the-art performance across four abstract visual reasoning tasks, as well as an abstract reasoning task involving real-world images.