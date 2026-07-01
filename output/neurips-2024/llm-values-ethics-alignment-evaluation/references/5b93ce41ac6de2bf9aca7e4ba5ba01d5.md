---
title: "Incentivizing Quality Text Generation via Statistical Contracts"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5b93ce41ac6de2bf9aca7e4ba5ba01d5-Abstract-Conference.html"
categories: ['statistical-inference-and-text-generation-methods\n\nhmm,-let-me-reconsider---looking-more-carefully-at-the-cluster:\n\n**score-matching-and-sampling-methods**', 'llm-values-ethics-alignment-evaluation']
tags: ['statistical-contracts', 'llm-incentives', 'text-quality']
venue: "NeurIPS 2024"
tldr: "Proposes statistical contracts to align incentives for quality text generation, addressing moral hazard in pay-per-token LLM pricing schemes."
---

# Incentivizing Quality Text Generation via Statistical Contracts

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5b93ce41ac6de2bf9aca7e4ba5ba01d5-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/5b93ce41ac6de2bf9aca7e4ba5ba01d5-Abstract-Conference.html)

**TLDR**: Proposes statistical contracts to align incentives for quality text generation, addressing moral hazard in pay-per-token LLM pricing schemes.

## Abstract

While the success of large language models (LLMs) increases demand for machine-generated text, current pay-per-token pricing schemes create a misalignment of incentives known in economics as moral hazard: Text-generating agents have strong incentive to cut costs by preferring a cheaper model over the cutting-edge one, and this can be done “behind the scenes” since the agent performs inference internally. In this work, we approach this issue from an economic perspective, by proposing a pay-for-performance, contract-based framework for incentivizing quality. We study a principal-agent game where the agent generates text using costly inference, and the contract determines the principal’s payment for the text according to an automated quality evaluation. Since standard contract theory is inapplicable when internal inference costs are unknown, we introduce cost-robust contracts. As our main theoretical contribution, we characterize optimal cost-robust contracts through a direct correspondence to optimal composite hypothesis tests from statistics, generalizing a result of Saig et al. (NeurIPS’23). We evaluate our framework empirically by deriving contracts for a range of objectives and LLM evaluation benchmarks, and find that cost-robust contracts sacrifice only a marginal increase in objective value compared to their cost-aware counterparts.