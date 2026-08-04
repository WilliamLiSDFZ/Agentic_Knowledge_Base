---
title: "SceneCraft: An LLM Agent for Synthesizing 3D Scenes as Blender Code"
source: "https://proceedings.mlr.press/v235/hu24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24g/hu24g.pdf"
categories: ['large-language-model-alignment-and-capabilities', '3d-vision-and-scene-understanding']
tags: ['llm-agent', '3d-scene-generation', 'blender', 'code-synthesis', 'spatial-planning']
venue: "ICML 2024"
tldr: "Presents SceneCraft, an LLM agent that converts text descriptions into Blender Python scripts to synthesize complex 3D scenes with spatial reasoning."
---

# SceneCraft: An LLM Agent for Synthesizing 3D Scenes as Blender Code

**Source**: [https://proceedings.mlr.press/v235/hu24g.html](https://proceedings.mlr.press/v235/hu24g.html)

**TLDR**: Presents SceneCraft, an LLM agent that converts text descriptions into Blender Python scripts to synthesize complex 3D scenes with spatial reasoning.

## Abstract

This paper introduces SceneCraft, a Large Language Model (LLM) Agent converting text descriptions into Blender-executable Python scripts which render complex scenes with up to a hundred 3D assets. This process requires complex spatial planning and arrangement. We tackle these challenges through a combination of advanced abstraction, strategic planning, and library learning. SceneCraft first models a scene graph as a blueprint, detailing the spatial relationships among assets in the scene. SceneCraft then writes Python scripts based on this graph, translating relationships into numerical constraints for asset layout. Next, SceneCraft leverages the perceptual strengths of vision-language foundation models like GPT-V to analyze rendered images and iteratively refine the scene. On top of this process, SceneCraft features a library learning mechanism that compiles common script functions into a reusable library, facilitating continuous self-improvement without expensive LLM parameter tuning. Our evaluation demonstrates that SceneCraft surpasses existing LLM-based agents in rendering complex scenes, as shown by its adherence to constraints and favorable human assessments. We also showcase the broader application potential of SceneCraft by reconstructing detailed 3D scenes from the Sintel movie and guiding a video generative model with generated scenes as intermediary control signal.