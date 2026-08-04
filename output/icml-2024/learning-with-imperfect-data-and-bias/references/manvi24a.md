---
title: "Large Language Models are Geographically Biased"
source: "https://proceedings.mlr.press/v235/manvi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/manvi24a/manvi24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'large-language-model-alignment-and-capabilities']
tags: ['geographic-bias', 'large-language-models', 'fairness']
venue: "ICML 2024"
tldr: "An analysis revealing and quantifying geographic biases in large language models stemming from skewed training data distributions."
---

# Large Language Models are Geographically Biased

**Source**: [https://proceedings.mlr.press/v235/manvi24a.html](https://proceedings.mlr.press/v235/manvi24a.html)

**TLDR**: An analysis revealing and quantifying geographic biases in large language models stemming from skewed training data distributions.

## Abstract

Large Language Models (LLMs) inherently carry the biases contained in their training corpora, which can lead to the perpetuation of societal harm. As the impact of these foundation models grows, understanding and evaluating their biases becomes crucial to achieving fairness and accuracy. We propose to study what LLMs know about the world we live in through the lens of geography. This approach is particularly powerful as there is ground truth for the numerous aspects of human life that are meaningfully projected onto geographic space such as culture, race, language, politics, and religion. We show various problematic geographic biases, which we define as systemic errors in geospatial predictions. Initially, we demonstrate that LLMs are capable of making accurate zero-shot geospatial predictions in the form of ratings that show strong monotonic correlation with ground truth (Spearman’s $\rho$ of up to 0.89). We then show that LLMs exhibit common biases across a range of objective and subjective topics. In particular, LLMs are clearly biased against locations with lower socioeconomic conditions (e.g. most of Africa) on a variety of sensitive subjective topics such as attractiveness, morality, and intelligence (Spearman’s $\rho$ of up to 0.70). Finally, we introduce a bias score to quantify this and find that there is significant variation in the magnitude of bias across existing LLMs. Code is available on the project website: https://rohinmanvi.github.io/GeoLLM.