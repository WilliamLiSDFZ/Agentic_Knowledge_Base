---
title: "ChatMusician: Understanding and Generating Music Intrinsically with LLM"
source: "https://aclanthology.org/2024.findings-acl.373/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems', 'code-llm-generation-and-evaluation']
tags: ['music-generation', 'llm-continual-pretraining', 'music-reasoning']
venue: "ACL 2024"
tldr: "ChatMusician integrates intrinsic music understanding and generation into an LLM via continual pre-training on music notation data."
---

# ChatMusician: Understanding and Generating Music Intrinsically with LLM

**Source**: [https://aclanthology.org/2024.findings-acl.373/](https://aclanthology.org/2024.findings-acl.373/)

**TLDR**: ChatMusician integrates intrinsic music understanding and generation into an LLM via continual pre-training on music notation data.

## Abstract

AbstractWhile LLMs demonstrate impressive capabilities in musical knowledge, we find that music reasoning is still an unsolved task.We introduce ChatMusician, an open-source large language model (LLM) that integrates intrinsic musical abilities. It is based on continual pre-training and finetuning LLaMA2 on a text-compatible music representation, ABC notation, and the music is treated as a second language.ChatMusician can understand and generate music with a pure text tokenizer without external multi-modal neural structures or tokenizers. Interestingly, endowing musical abilities does not harm language abilities, even achieving a slightly higher MMLU score.ChatMusician is capable of composing well-structured, full-length music, condition on texts, chords, melodies, motifs, musical forms, etc.On our meticulously curated college-level music understanding benchmark, MusicTheoryBench, ChatMusician surpasses LLaMA2 and GPT-3.5 by a noticeable margin. We show that ChatMusician preserves or even surpasses the original LLaMA2 7B’s language abilities by evaluating on MMLU benchmark.Our work reveals that LLMs can be an excellent compressor for music, which can be seen as humanity’s creative language, but there remains significant territory to be conquered.We release our 5B token music-language corpora MusicPiles, the collected MusicTheoryBench, code, model and demo.