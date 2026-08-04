---
title: "An Independence-promoting Loss for Music Generation with Language Models"
source: "https://proceedings.mlr.press/v235/lemercier24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lemercier24a/lemercier24a.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'generative-models-and-variational-inference']
tags: ['music-generation', 'language-models', 'independence-loss', 'multi-stage-quantizers', 'audio-tokens']
venue: "ICML 2024"
tldr: "Introduces an independence-promoting loss to improve token prediction in language model-based music generation using multi-stage quantizers."
---

# An Independence-promoting Loss for Music Generation with Language Models

**Source**: [https://proceedings.mlr.press/v235/lemercier24a.html](https://proceedings.mlr.press/v235/lemercier24a.html)

**TLDR**: Introduces an independence-promoting loss to improve token prediction in language model-based music generation using multi-stage quantizers.

## Abstract

Music generation schemes using language modeling rely on a vocabulary of audio tokens, generally provided as codes in a discrete latent space learnt by an auto-encoder. Multi-stage quantizers are often employed to produce these tokens, therefore the decoding strategy used for token prediction must be adapted to account for multiple codebooks: either it should model the joint distribution over all codebooks, or fit the product of the codebook marginal distributions. Modelling the joint distribution requires a costly increase in the number of auto-regressive steps, while fitting the product of the marginals yields an inexact model unless the codebooks are mutually independent. In this work, we introduce an independence-promoting loss to regularize the auto-encoder used as the tokenizer in language models for music generation. The proposed loss is a proxy for mutual information based on the maximum mean discrepancy principle, applied in reproducible kernel Hilbert spaces. Our criterion is simple to implement and train, and it is generalizable to other multi-stream codecs. We show that it reduces the statistical dependence between codebooks during auto-encoding. This leads to an increase in the generated music quality when modelling the product of the marginal distributions, while generating audio much faster than the joint distribution model.