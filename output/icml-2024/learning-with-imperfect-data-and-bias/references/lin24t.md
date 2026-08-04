---
title: "Distributionally Robust Data Valuation"
source: "https://proceedings.mlr.press/v235/lin24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24t/lin24t.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['data-valuation', 'distributional-robustness', 'machine-learning']
venue: "ICML 2024"
tldr: "A distributionally robust data valuation framework that addresses practical limitations of validation-based data contribution estimation."
---

# Distributionally Robust Data Valuation

**Source**: [https://proceedings.mlr.press/v235/lin24t.html](https://proceedings.mlr.press/v235/lin24t.html)

**TLDR**: A distributionally robust data valuation framework that addresses practical limitations of validation-based data contribution estimation.

## Abstract

Data valuation quantifies the contribution of each data point to the performance of a machine learning model. Existing works typically define the value of data by its improvement of the validation performance of the trained model. However, this approach can be impractical to apply in collaborative machine learning and data marketplace since it is difficult for the parties/buyers to agree on a common validation dataset or determine the exact validation distribution a priori. To address this, we propose a distributionally robust data valuation approach to perform data valuation without known/fixed validation distributions. Our approach defines the value of data by its improvement of the distributionally robust generalization error (DRGE), thus providing a worst-case performance guarantee without a known/fixed validation distribution. However, since computing DRGE directly is infeasible, we propose using model deviation as a proxy for the marginal improvement of DRGE (for kernel regression and neural networks) to compute data values. Furthermore, we identify a notion of uniqueness where low uniqueness characterizes low-value data. We empirically demonstrate that our approach outperforms existing data valuation approaches in data selection and data removal tasks on real-world datasets (e.g., housing price prediction, diabetes hospitalization prediction).