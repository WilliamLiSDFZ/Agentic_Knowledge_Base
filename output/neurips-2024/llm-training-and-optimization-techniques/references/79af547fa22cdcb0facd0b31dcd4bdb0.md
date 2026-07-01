---
title: "Model Decides How to Tokenize: Adaptive DNA Sequence Tokenization with MxDNA"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/79af547fa22cdcb0facd0b31dcd4bdb0-Abstract-Conference.html"
categories: ['machine-learning-for-molecular-biology', 'llm-training-and-optimization-techniques']
tags: ['DNA-tokenization', 'genomic-language-models', 'adaptive-tokenization', 'foundation-models', 'sequence-modeling']
venue: "NeurIPS 2024"
tldr: "MxDNA introduces an adaptive tokenization strategy tailored to DNA sequences for genomic foundation models."
---

# Model Decides How to Tokenize: Adaptive DNA Sequence Tokenization with MxDNA

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/79af547fa22cdcb0facd0b31dcd4bdb0-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/79af547fa22cdcb0facd0b31dcd4bdb0-Abstract-Conference.html)

**TLDR**: MxDNA introduces an adaptive tokenization strategy tailored to DNA sequences for genomic foundation models.

## Abstract

Foundation models have made significant strides in understanding the genomic language of DNA sequences. However, previous models typically adopt the tokenization methods designed for natural language, which are unsuitable for DNA sequences due to their unique characteristics. In addition, the optimal approach to tokenize DNA remains largely under-explored, and may not be intuitively understood by humans even if discovered. To address these challenges, we introduce MxDNA, a novel framework where the model autonomously learns an effective DNA tokenization strategy through gradient decent. MxDNA employs a sparse Mixture of Convolution Experts coupled with a deformable convolution to model the tokenization process, with the discontinuous, overlapping, and ambiguous nature of meaningful genomic segments explicitly considered. On Nucleotide Transformer Benchmarks and Genomic Benchmarks, MxDNA demonstrates superior performance to existing methods with less pretraining data and time, highlighting its effectiveness. Finally, we show that MxDNA learns unique tokenization strategy distinct to those of previous methods and captures genomic functionalities at a token level during self-supervised pretraining. Our MxDNA aims to provide a new perspective on DNA tokenization, potentially offering broad applications in various domains and yielding profound insights. Code is available at https://github.com/qiaoqiaoLF/MxDNA.