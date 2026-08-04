---
title: "Progressive Inference: Explaining Decoder-Only Sequence Classification Models Using Intermediate Predictions"
source: "https://proceedings.mlr.press/v235/kariyappa24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kariyappa24a/kariyappa24a.pdf"
categories: ['llm-geometry-and-interpretability-research', 'ai-explainability-uncertainty-human-decision-making']
tags: ['transformer-interpretability', 'sequence-classification', 'progressive-inference']
venue: "ICML 2024"
tldr: "Proposes Progressive Inference, a framework explaining decoder-only transformer classification predictions using intermediate predictions from the classification head."
---

# Progressive Inference: Explaining Decoder-Only Sequence Classification Models Using Intermediate Predictions

**Source**: [https://proceedings.mlr.press/v235/kariyappa24a.html](https://proceedings.mlr.press/v235/kariyappa24a.html)

**TLDR**: Proposes Progressive Inference, a framework explaining decoder-only transformer classification predictions using intermediate predictions from the classification head.

## Abstract

This paper proposes Progressive inference–a framework to explain the predictions of decoder-only transformer models trained to perform sequence classification tasks. Our work is based on the insight that the classification head of a decoder-only model can be used to make intermediate predictions by evaluating them at different points in the input sequence. Due to the masked attention mechanism used in decoder-only models, these intermediate predictions only depend on the tokens seen before the inference point, allowing us to obtain the model’s prediction on a masked input sub-sequence, with negligible computational overheads. We develop two methods to provide sub-sequence level attributions using this core insight. First, we propose Single Pass-Progressive Inference (SP-PI) to compute attributions by simply taking the difference between intermediate predictions. Second, we exploit a connection with Kernel SHAP to develop Multi Pass-Progressive Inference (MP-PI); this uses intermediate predictions from multiple masked versions of the input to compute higher-quality attributions that approximate SHAP values. We perform studies on several text classification datasets to demonstrate that our proposal provides better explanations compared to prior work, both in the single-pass and multi-pass settings.