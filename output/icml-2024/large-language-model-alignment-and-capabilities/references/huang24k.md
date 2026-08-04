---
title: "InstructSpeech: Following Speech Editing Instructions via Large Language Models"
source: "https://proceedings.mlr.press/v235/huang24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24k/huang24k.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'audio-and-music-generation-diffusion-models']
tags: ['speech-editing', 'instruction-following', 'large-language-models']
venue: "ICML 2024"
tldr: "Proposes InstructSpeech, a multi-task LLM-based model for instruction-guided manipulation of speech semantic and acoustic attributes."
---

# InstructSpeech: Following Speech Editing Instructions via Large Language Models

**Source**: [https://proceedings.mlr.press/v235/huang24k.html](https://proceedings.mlr.press/v235/huang24k.html)

**TLDR**: Proposes InstructSpeech, a multi-task LLM-based model for instruction-guided manipulation of speech semantic and acoustic attributes.

## Abstract

Instruction-guided speech editing aims to follow the user’s natural language instruction to manipulate the semantic and acoustic attributes of a speech. In this work, we construct triplet paired data (instruction, input speech, output speech) to alleviate data scarcity and train a multi-task large language model named InstructSpeech. To mitigate the challenges of accurately executing user’s instructions, we 1) introduce the learned task embeddings with a fine-tuned Flan-T5-XL to guide the generation process towards the correct generative task; 2) include an extensive and diverse set of speech editing and processing tasks to enhance model capabilities; 3) investigate chain-of-thought reasoning for free-form semantic content editing; and 4) propose a hierarchical adapter that effectively updates a small portion of parameters for generalization to new tasks. To assess instruction speech editing in greater depth, we introduce a benchmark evaluation with contrastive instruction-speech pre-training (CISP) to test the speech quality and instruction-speech alignment faithfulness. Experimental results demonstrate that InstructSpeech achieves state-of-the-art results in eleven tasks, for the first time unlocking the ability to edit speech’s acoustic and semantic attributes following a user’s instruction. Audio samples are available at https://InstructSpeech.github.io