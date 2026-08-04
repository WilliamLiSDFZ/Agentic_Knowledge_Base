---
title: "Incorporating Information into Shapley Values: Reweighting via a Maximum Entropy Approach"
source: "https://proceedings.mlr.press/v235/biparva24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/biparva24a/biparva24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'ai-explainability-uncertainty-human-decision-making']
tags: ['Shapley-values', 'causal-inference', 'maximum-entropy', 'variable-ordering']
venue: "ICML 2024"
tldr: "This paper proposes a maximum entropy reweighting approach to incorporate causal information into Shapley value computation by addressing variable ordering choices."
---

# Incorporating Information into Shapley Values: Reweighting via a Maximum Entropy Approach

**Source**: [https://proceedings.mlr.press/v235/biparva24a.html](https://proceedings.mlr.press/v235/biparva24a.html)

**TLDR**: This paper proposes a maximum entropy reweighting approach to incorporate causal information into Shapley value computation by addressing variable ordering choices.

## Abstract

Both the marginal contributions needed for the computation of Shapley values and the graph produced by Pearl-Verma theorem rely on the choice of an ordering of the variables. For Shapley values, the marginal contributions are averaged over all orderings, while in causal inference methods, the typical approach is to select orderings producing a graph with a minimal number of edges. We reconcile both approaches by reinterpreting them from a maximum entropy perspective. Namely, Shapley values assume no prior knowledge about the orderings and treat them as equally likely, while causal inference approaches apply Occam’s razor and consider only orderings producing the simplest explanatory graphs. We find that the blind application of Occam’s razor to Shapley values does not produce fully satisfactory explanations. Hence, we propose two variations of Shapley values based on entropy maximization to appropriately incorporate prior information about the model. Hence, we propose a variation of Shapley values based on entropy maximization to appropriately incorporate prior information about the model.