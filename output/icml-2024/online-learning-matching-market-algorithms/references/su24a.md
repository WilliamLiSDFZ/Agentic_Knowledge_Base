---
title: "Learning from Streaming Data when Users Choose"
source: "https://proceedings.mlr.press/v235/su24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/su24a/su24a.pdf"
categories: ['online-learning-matching-market-algorithms', 'generative-models-and-variational-inference']
tags: ['streaming-data', 'user-choice', 'competing-services', 'online-learning', 'market-dynamics']
venue: "ICML 2024"
tldr: "A framework is studied for learning from streaming user data when users choose between competing service providers based on model quality."
---

# Learning from Streaming Data when Users Choose

**Source**: [https://proceedings.mlr.press/v235/su24a.html](https://proceedings.mlr.press/v235/su24a.html)

**TLDR**: A framework is studied for learning from streaming user data when users choose between competing service providers based on model quality.

## Abstract

In digital markets comprised of many competing services, each user chooses between multiple service providers according to their preferences, and the chosen service makes use of the user data to incrementally improve its model. The service providers’ models influence which service the user will choose at the next time step, and the user’s choice, in return, influences the model update, leading to a feedback loop. In this paper, we formalize the above dynamics and develop a simple and efficient decentralized algorithm to locally minimize the overall user loss. Theoretically, we show that our algorithm asymptotically converges to stationary points of of the overall loss almost surely. We also experimentally demonstrate the utility of our algorithm with real world data.