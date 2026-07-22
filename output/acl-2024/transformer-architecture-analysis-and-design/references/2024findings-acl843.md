---
title: "Looking Right is Sometimes Right: Investigating the Capabilities of Decoder-only LLMs for Sequence Labeling"
source: "https://aclanthology.org/2024.findings-acl.843/"
pdf_url: ""
categories: ['transformer-architecture-analysis-and-design', 'llm-training-alignment-and-evaluation']
tags: ['decoder-only-llms', 'sequence-labeling', 'causal-language-models']
venue: "ACL 2024"
tldr: "Investigates the capability of decoder-only LLMs for sequence labeling tasks, finding competitive performance with MLM-based encoders in some settings."
---

# Looking Right is Sometimes Right: Investigating the Capabilities of Decoder-only LLMs for Sequence Labeling

**Source**: [https://aclanthology.org/2024.findings-acl.843/](https://aclanthology.org/2024.findings-acl.843/)

**TLDR**: Investigates the capability of decoder-only LLMs for sequence labeling tasks, finding competitive performance with MLM-based encoders in some settings.

## Abstract

AbstractPre-trained language models based on masked language modeling (MLM) excel in natural language understanding (NLU) tasks. While fine-tuned MLM-based encoders consistently outperform causal language modeling decoders of comparable size, recent decoder-only large language models (LLMs) perform on par with smaller MLM-based encoders. Although their performance improves with scale, LLMs fall short of achieving state-of-the-art results in information extraction (IE) tasks, many of which are formulated as sequence labeling (SL). We hypothesize that LLMs’ poor SL performance stems from causal masking, which prevents the model from attending to tokens on the right of the current token. Yet, how exactly and to what extent LLMs’ performance on SL can be improved remains unclear. We explore techniques for improving the SL performance of open LLMs on IE tasks by applying layer-wise removal of the causal mask (CM) during LLM fine-tuning. This approach yields performance gains competitive with state-of-the-art SL models, matching or outperforming the results of CM removal from all blocks. Our findings hold for diverse SL tasks, demonstrating that open LLMs with layer-dependent CM removal outperform strong MLM-based encoders and even instruction-tuned LLMs.