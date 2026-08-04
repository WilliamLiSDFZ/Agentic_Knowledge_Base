---
title: "ArtWhisperer: A Dataset for Characterizing Human-AI Interactions in Artistic Creations"
source: "https://proceedings.mlr.press/v235/vodrahalli24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vodrahalli24a/vodrahalli24a.pdf"
categories: ['human-ai-content-creation-competition', 'data-selection-and-active-learning-methods']
tags: ['human-AI-interaction', 'text-to-image', 'dataset', 'iterative-prompting', 'artistic-creation']
venue: "ICML 2024"
tldr: "Introduces ArtWhisperer, a dataset from an online game characterizing how humans iteratively craft prompts to guide text-to-image models toward target images."
---

# ArtWhisperer: A Dataset for Characterizing Human-AI Interactions in Artistic Creations

**Source**: [https://proceedings.mlr.press/v235/vodrahalli24a.html](https://proceedings.mlr.press/v235/vodrahalli24a.html)

**TLDR**: Introduces ArtWhisperer, a dataset from an online game characterizing how humans iteratively craft prompts to guide text-to-image models toward target images.

## Abstract

In this work, we investigate how people use text-to-image models to generate desired target images. To study this interaction, we created ArtWhisperer, an online game where users are given a target image and are tasked with iteratively finding a prompt that creates a similar-looking image as the target. Through this game, we recorded over 50,000 human-AI interactions; each interaction corresponds to one text prompt created by a user and the corresponding generated image. The majority of these are repeated interactions where a user iterates to find the best prompt for their target image, making this a unique sequential dataset for studying human-AI collaborations. In an initial analysis of this dataset, we identify several characteristics of prompt interactions and user strategies. People submit diverse prompts and are able to discover a variety of text descriptions that generate similar images. Interestingly, prompt diversity does not decrease as users find better prompts. We further propose a new metric to quantify AI model steerability using our dataset. We define steerability as the expected number of interactions required to adequately complete a task. We estimate this value by fitting a Markov chain for each target task and calculating the expected time to reach an adequate score. We quantify and compare AI steerability across different types of target images and two different models, finding that images of cities and nature are more steerable than artistic and fantasy images. We also evaluate popular vision-language models to assess their image understanding and ability to incorporate feedback. These findings provide insights into human-AI interaction behavior, present a concrete method of assessing AI steerability, and demonstrate the general utility of the ArtWhisperer dataset.