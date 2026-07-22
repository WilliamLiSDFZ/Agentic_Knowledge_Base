---
title: "EcoRank: Budget-Constrained Text Re-ranking Using Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.773/"
pdf_url: ""
categories: ['llm-based-ranking-and-recommendation']
tags: ['text-reranking', 'budget-constraint', 'llm-prompting']
venue: "ACL 2024"
tldr: "Proposes EcoRank, a budget-constrained text re-ranking framework that optimizes cost-effectiveness across pointwise, listwise, and pairwise LLM prompting strategies."
---

# EcoRank: Budget-Constrained Text Re-ranking Using Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.773/](https://aclanthology.org/2024.findings-acl.773/)

**TLDR**: Proposes EcoRank, a budget-constrained text re-ranking framework that optimizes cost-effectiveness across pointwise, listwise, and pairwise LLM prompting strategies.

## Abstract

AbstractLarge Language Models (LLMs) have achieved state-of-the-art performance in text re-ranking. This process includes queries and candidate passages in the prompts, utilizing pointwise, listwise, and pairwise prompting strategies. A limitation of these ranking strategies with LLMs is their cost: the process can become expensive due to API charges, which are based on the number of input and output tokens. We study how to maximize the re-ranking performance given a budget, by navigating the vast search spaces of prompt choices, LLM APIs, and budget splits. We propose a suite of budget-constrained methods to perform text re-ranking using a set of LLM APIs. Our most efficient method, called EcoRank, is a two-layered pipeline that jointly optimizes decisions regarding budget allocation across prompt strategies and LLM APIs. Our experimental results on four popular QA and passage reranking datasets show that EcoRank outperforms other budget-aware supervised and unsupervised baselines.