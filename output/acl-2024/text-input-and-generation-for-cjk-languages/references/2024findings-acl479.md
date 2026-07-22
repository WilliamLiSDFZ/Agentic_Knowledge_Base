---
title: "Alignment-Based Decoding Policy for Low-Latency and Anticipation-Free Neural Japanese Input Method Editors"
source: "https://aclanthology.org/2024.findings-acl.479/"
categories: ['text-input-and-generation-for-cjk-languages']
tags: ['Japanese-IME', 'low-latency', 'alignment-based-decoding']
venue: "ACL 2024"
tldr: "An alignment-based decoding policy enables low-latency, anticipation-free neural Japanese input method editors using transformer models."
---

# Alignment-Based Decoding Policy for Low-Latency and Anticipation-Free Neural Japanese Input Method Editors

**Source**: [https://aclanthology.org/2024.findings-acl.479/](https://aclanthology.org/2024.findings-acl.479/)

**TLDR**: An alignment-based decoding policy enables low-latency, anticipation-free neural Japanese input method editors using transformer models.

## Abstract

AbstractJapanese input method editors (IMEs) are essential tools for inputting Japanese text using a limited set of characters such as the kana syllabary. However, despite their importance, the potential of newer attention-based encoder-decoder neural networks, such as Transformer, has not yet been fully explored for IMEs due to their high computational cost and low-quality intermediate output in simultaneous settings, leading to high latencies. In this work, we propose a simple decoding policy to enable the use of attention-based encoder-decoder networks for simultaneous kana-kanji conversion in the context of Japanese IMEs inspired by simultaneous machine translation (SimulMT). We demonstrate that simply decoding by explicitly considering the word boundaries achieves a fairly strong quality-latency trade-off, as it can be seen as equivalent to performing decoding on aligned prefixes and thus achieving an incremental anticipation-free conversion. We further show how such a policy can be applied in practice to achieve high-quality conversions with minimal computational overhead. Our experiments show that our approach can achieve a noticeably better quality-latency trade-off compared to the baselines, while also being a more practical approach due to its ability to directly handle streaming input. Our code is available at https://anonymous.4open.science/r/transformer_ime-D327.