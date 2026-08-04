---
title: "Gradient-based Visual Explanation for Transformer-based CLIP"
source: "https://proceedings.mlr.press/v235/zhao24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24p/zhao24p.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making']
tags: ['CLIP', 'gradient-based-explanation', 'visual-explainability', 'vision-language-models']
venue: "ICML 2024"
tldr: "This paper proposes Grad-ECLIP, a gradient-based visual explanation method tailored for the CLIP vision-language model."
---

# Gradient-based Visual Explanation for Transformer-based CLIP

**Source**: [https://proceedings.mlr.press/v235/zhao24p.html](https://proceedings.mlr.press/v235/zhao24p.html)

**TLDR**: This paper proposes Grad-ECLIP, a gradient-based visual explanation method tailored for the CLIP vision-language model.

## Abstract

Significant progress has been achieved on the improvement and downstream usages of the Contrastive Language-Image Pre-training (CLIP) vision-language model, while less attention is paid to the interpretation of CLIP. We propose a Gradient-based visual Explanation method for CLIP (Grad-ECLIP), which interprets the matching result of CLIP for specific input image-text pair. By decomposing the architecture of the encoder and discovering the relationship between the matching similarity and intermediate spatial features, Grad-ECLIP produces effective heat maps that show the influence of image regions or words on the CLIP results. Different from the previous Transformer interpretation methods that focus on the utilization of self-attention maps, which are typically extremely sparse in CLIP, we produce high-quality visual explanations by applying channel and spatial weights on token features. Qualitative and quantitative evaluations verify the superiority of Grad-ECLIP compared with the state-of-the-art methods. A series of analysis are conducted based on our visual explanation results, from which we explore the working mechanism of image-text matching, and the strengths and limitations in attribution identification of CLIP. Codes are available here: https://github.com/Cyang-Zhao/Grad-Eclip.