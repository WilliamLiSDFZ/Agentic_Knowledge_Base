---
title: "Detecting Any instruction-to-answer interaction relationship:Universal Instruction-to-Answer Navigator for Med-VQA"
source: "https://proceedings.mlr.press/v235/wu24ac.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24ac/wu24ac.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'ai-explainability-uncertainty-human-decision-making']
tags: ['medical-VQA', 'visual-question-answering', 'instruction-following', 'multimodal', 'medical-imaging']
venue: "ICML 2024"
tldr: "Introduces Uni-Med, a universal instruction-to-answer navigation framework for medical visual question answering across diverse inadequately annotated medical images."
---

# Detecting Any instruction-to-answer interaction relationship:Universal Instruction-to-Answer Navigator for Med-VQA

**Source**: [https://proceedings.mlr.press/v235/wu24ac.html](https://proceedings.mlr.press/v235/wu24ac.html)

**TLDR**: Introduces Uni-Med, a universal instruction-to-answer navigation framework for medical visual question answering across diverse inadequately annotated medical images.

## Abstract

Medical Visual Question Answering (Med-VQA) interprets complex medical imagery using user instructions for precise diagnostics, yet faces challenges due to diverse, inadequately annotated images. In this paper, we introduce the Universal Instruction-Vision Navigator (Uni-Med) framework for extracting instruction-to-answer relationships, facilitating the understanding of visual evidence behind responses. Specifically, we design the Instruct-to-Answer Clues Interpreter (IAI) to generate visual explanations based on the answers and mark the core part of instructions with "real intent" labels. The IAI-Med VQA dataset, produced using IAI, is now publicly available to advance Med-VQA research. Additionally, our Token-Level Cut-Mix module dynamically aligns visual explanations with image patches, ensuring answers are traceable and learnable. We also implement intention-guided attention to minimize non-core instruction interference, sharpening focus on ’real intent’. Extensive experiments on SLAKE datasets show Uni-Med’s superior accuracies (87.52% closed, 86.12% overall), outperforming MedVInT-PMC-VQA by 1.22% and 0.92%. Code and dataset are available at: https://github.com/zhongzee/Uni-Med-master.