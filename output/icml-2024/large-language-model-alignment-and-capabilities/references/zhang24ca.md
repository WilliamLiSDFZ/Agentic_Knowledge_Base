---
title: "PARDEN, Can You Repeat That? Defending against Jailbreaks via Repetition"
source: "https://proceedings.mlr.press/v235/zhang24ca.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ca/zhang24ca.pdf"
categories: ['adversarial-robustness-and-model-security', 'large-language-model-alignment-and-capabilities']
tags: ['jailbreak-defense', 'LLM-safety', 'repetition-based-detection']
venue: "ICML 2024"
tldr: "Proposes PARDEN, a repetition-based defense mechanism to protect safety-aligned LLMs against jailbreak attacks."
---

# PARDEN, Can You Repeat That? Defending against Jailbreaks via Repetition

**Source**: [https://proceedings.mlr.press/v235/zhang24ca.html](https://proceedings.mlr.press/v235/zhang24ca.html)

**TLDR**: Proposes PARDEN, a repetition-based defense mechanism to protect safety-aligned LLMs against jailbreak attacks.

## Abstract

Large language models (LLMs) have shown success in many natural language processing tasks. Despite rigorous safety alignment processes, supposedly safety-aligned LLMs like Llama 2 and Claude 2 are still susceptible to jailbreaks, leading to security risks and abuse of the models. One option to mitigate such risks is to augment the LLM with a dedicated "safeguard", which checks the LLM’s inputs or outputs for undesired behaviour. A promising approach is to use the LLM itself as the safeguard. Nonetheless, baseline methods, such as prompting the LLM to self-classify toxic content, demonstrate limited efficacy. We hypothesise that this is due to domain shift: the alignment training imparts a self-censoring behaviour to the model ("Sorry I can’t do that"), while the self-classify approach shifts it to a classification format ("Is this prompt malicious"). In this work, we propose PARDEN, which avoids this domain shift by simply asking the model to repeat its own outputs. PARDEN neither requires finetuning nor white box access to the model. We empirically verify the effectiveness of our method and show that PARDEN significantly outperforms existing jailbreak detection baselines for Llama-2 and Claude-2. We find that PARDEN is particularly powerful in the relevant regime of high True Positive Rate (TPR) and low False Positive Rate (FPR). For instance, for Llama2-7B, at TPR equal to 90%, PARDEN accomplishes a roughly 11x reduction in the FPR from 24.8% to 2.0% on the harmful behaviours dataset. Code and data are available at https://github.com/Ed-Zh/PARDEN.