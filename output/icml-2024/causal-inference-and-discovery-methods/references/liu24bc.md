---
title: "Causal Discovery via Conditional Independence Testing with Proxy Variables"
source: "https://proceedings.mlr.press/v235/liu24bc.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bc/liu24bc.pdf"
categories: ['causal-inference-and-discovery-methods', 'learning-with-imperfect-data-and-bias']
tags: ['causal-discovery', 'conditional-independence', 'proxy-variables']
venue: "ICML 2024"
tldr: "A proxy-variable-based conditional independence testing method for causal discovery that corrects for bias introduced by latent confounders."
---

# Causal Discovery via Conditional Independence Testing with Proxy Variables

**Source**: [https://proceedings.mlr.press/v235/liu24bc.html](https://proceedings.mlr.press/v235/liu24bc.html)

**TLDR**: A proxy-variable-based conditional independence testing method for causal discovery that corrects for bias introduced by latent confounders.

## Abstract

Distinguishing causal connections from correlations is important in many scenarios. However, the presence of unobserved variables, such as the latent confounder, can introduce bias in conditional independence testing commonly employed in constraint-based causal discovery for identifying causal relations. To address this issue, existing methods introduced proxy variables to adjust for the bias caused by unobserveness. However, these methods were either limited to categorical variables or relied on strong parametric assumptions for identification. In this paper, we propose a novel hypothesis-testing procedure that can effectively examine the existence of the causal relationship over continuous variables, without any parametric constraint. Our procedure is based on discretization, which under completeness conditions, is able to asymptotically establish a linear equation whose coefficient vector is identifiable under the causal null hypothesis. Based on this, we introduce our test statistic and demonstrate its asymptotic level and power. We validate the effectiveness of our procedure using both synthetic and real-world data.