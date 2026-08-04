# Token-Specific Watermarking with Enhanced Detectability and Semantic Coherence for Large Language Models

**Source**: https://proceedings.mlr.press/v235/huo24a.html

## [POSITIVE] Token-Specific Splitting Ratio (γ-Generator)
A lightweight MLP that takes the embedding of the preceding token as input and generates a token-specific splitting ratio γt for each token, replacing the fixed splitting ratio used in KGW.

**Delta**: outperforms baseline (improved Pareto frontier over KGW)
**Condition**: Applied during LLM text generation for watermarking; evaluated on OPT-1.3B and LLAMA2 7B/13B/70B

**Evidence**: "Our method uniquely learns token-specific splitting ratios and watermark logits, which take into account the distinct context and semantics of each token... Our method has the adaptability that allows for token-specific adjustments in splitting ratios and watermark logits, while KGW employs uniform values across all tokens."

## [POSITIVE] Token-Specific Watermark Logit (δ-Generator)
A lightweight MLP that takes the embedding of the preceding token as input and generates a token-specific watermark logit δt for each token, replacing the fixed constant watermark logit used in KGW.

**Delta**: outperforms baseline (improved Pareto frontier over KGW)
**Condition**: Applied during LLM text generation for watermarking; evaluated on OPT-1.3B and LLAMA2 7B/13B/70B

**Evidence**: "Our method outperforms EXP-edit in both detectability and SimCSE, demonstrating that learning token-specific parameters to watermark enables appropriately shifting the output distribution to enhance detectability without significantly affecting semantics."

## [POSITIVE] Multi-Objective Optimization (MGDA)
Uses the Multiple-Gradient Descent Algorithm (MGDA) to simultaneously optimize detection loss and semantic loss, finding Pareto optimal solutions where improving one objective does not detrimentally affect the other.

**Delta**: outperforms baseline (improved Pareto frontier over KGW and other baselines)
**Condition**: Used during training of γ- and δ-generator networks

**Evidence**: "The second factor distinguishing our approach is the incorporation of multi-objective optimization, which enables simultaneous maximization of detectability and semantic integrity. This is achieved by concurrently optimizing a differentiable detection loss and a semantic loss. In contrast, the KGW method cannot explicitly optimize for these two objectives together."

## [POSITIVE] Differentiable Detection Loss (Relaxed Z-Score)
A differentiable surrogate for the non-differentiable z-score used in watermark detection, relaxing |s|G (count of green tokens) as the sum of probabilities of selecting green tokens, enabling gradient-based optimization.

**Delta**: outperforms baseline (enables direct optimization of detectability)
**Condition**: Used during training as part of the detection loss objective

**Evidence**: "Since this metric is inherently non-differentiable, we introduce a differentiable surrogate that allows for direct optimization through gradient-based techniques during training."

## [POSITIVE] Semantic Loss via SimCSE Cosine Similarity
Measures semantic coherence by computing cosine similarity between SimCSE (RoBERTa-base) embeddings of watermarked and non-watermarked texts, used as a training objective to preserve semantic integrity.

**Delta**: outperforms baseline (improved SimCSE scores vs. KGW and EXP-edit)
**Condition**: Used during training as part of the semantic loss objective

**Evidence**: "Our method outperforms EXP-edit in both detectability and SimCSE... our method directly maximizes differentiable metrics of semantic coherence and detectability through multi-objective optimization, inherently improving them."

## [POSITIVE] Gumbel-Softmax Differentiable Sampling
Uses Gumbel-Softmax reparameterization to enable differentiable approximation of the Bernoulli sampling process for vocabulary splitting into green/red lists, allowing gradient-based updates of the γ-generator.

**Delta**: enables gradient-based training (no quantitative delta reported)
**Condition**: Applied in the γ-generator during training

**Evidence**: "However, the sampling process from a Bernoulli distribution is non-differentiable, which prevents the gradient-based updating of the parameters in Gγ. To address this issue, we utilize the Gumbel-Softmax method for differentiable sampling."

## [POSITIVE] Weaker Watermark After Adjectives/Determiners
The learned γ and δ generators assign lower splitting ratios and watermark logits when the preceding token is an adjective (ADJ) or determiner (DET), reducing watermark strength to preserve semantic coherence before likely noun tokens.

**Delta**: enhances both semantic coherence and syntactic consistency (qualitative)
**Condition**: Automatically learned behavior when preceding token is ADJ or DET

**Evidence**: "One observation is that when the preceding token is an adjective (ADJ) or a determiner (DET), γ and δ tend to be assigned lower values... Applying a weaker watermark to tokens following ADJs and DETs promotes the selection of the next token with the highest model logit, which is most likely to be a noun. This approach thereby enhances both semantic coherence and syntactic consistency."

## [POSITIVE] Stronger Watermark After Punctuation
The learned γ and δ generators assign higher splitting ratios and watermark logits when the preceding token is punctuation (PUNCT), exploiting the minimal constraints on subsequent tokens to embed a stronger watermark.

**Delta**: improved robustness against paraphrase attacks (superior Pareto frontier vs. KGW)
**Condition**: Automatically learned behavior when preceding token is PUNCT; particularly beneficial under paraphrase attacks

**Evidence**: "Our approach inserts strong watermarks around punctuations. These watermarks remain intact even after paraphrasing, ensuring the detectability of the watermark in the altered text. Such a mechanism is lacking in KGW."

## [POSITIVE] Cross-Model Generalizability (Train on OPT, Apply to LLAMA2)
The γ- and δ-generator networks trained on OPT-1.3B are directly applied to LLAMA2 7B, 13B, and 70B without retraining, demonstrating generalizability across LLM architectures and sizes.

**Delta**: better Pareto frontier than KGW on LLAMA2 7B, 13B, and 70B
**Condition**: Generators trained on OPT-1.3B and evaluated on LLAMA2 7B/13B/70B

**Evidence**: "Our model (γ- and δ-generator networks), initially trained on OPT-1.3B, demonstrates a better Pareto frontier when applied to LLAMA2 7B, 13B and 70B. This adaptability is likely because our method learns the watermarking parameters that reflect the general nature of language itself."

## [NEGATIVE] Selective Watermarking (SWEET baseline)
SWEET watermarks only high-entropy tokens and leaves low-entropy tokens un-watermarked (δ=0), aiming to preserve semantics by avoiding watermarking of constrained tokens.

**Delta**: does not achieve 100% TPR at FPR=0%; on average only 7 out of 200 tokens eligible for watermarking
**Condition**: Applied to general domain text (not code); evaluated at FPR=0%

**Evidence**: "At 0% FPR, SWEET is notably less effective compared to our approach and KGW, and does not achieve 100% TPR. This may be due to its selective watermarking strategy, which targets only high-entropy words and leaves low-entropy words un-watermarked (δ=0). For instance, at (γ,δ)=(0.25,3.0), an analysis of LLM-generated texts that SWEET failed to detect at 0% FPR shows that, on average, only 7 out of 200 tokens are high-entropy and eligible for SWEET watermarking."

## [NEGATIVE] Prompt-Dependent Detection (SWEET/SIR with Prompt)
SWEET and SIR use prompts during detection to improve watermark identification, but this is impractical in many real-world scenarios where prompts are unavailable.

**Delta**: SWEETNoPrompt underperforms SWEET; SIRNoPrompt significantly underperforms SIR
**Condition**: When prompts are unavailable during detection

**Evidence**: "Furthermore, SWEETNoPrompt underperforms SWEET, indicating the method's dependence on prompts, which is impractical... SIRNoPrompt significantly underperforms compared to SIR, indicating a strong dependence on prompts while detection. SIR is less robust than SWEET in the no-prompt scenario, as it exhibits a greater performance degradation without prompts compared to SWEET."

## [NEGATIVE] EXP-edit Exponential Minimum Sampling (Distortion-Free)
EXP-edit uses pseudo-random exponential minimum sampling that does not alter the output distribution of LLMs, making watermarked text indistinguishable from non-watermarked text but limiting flexibility.

**Delta**: TPR@0%=0.922 (0.968 with Top-k=50) vs. Ours TPR@0%=1.000; SimCSE=0.655 (0.677 with Top-k=50) vs. Ours SimCSE=0.713
**Condition**: Compared against proposed method on OPT-1.3B with Top-k=50 sampling

**Evidence**: "Our method outperforms EXP-edit in both detectability and SimCSE, demonstrating that learning token-specific parameters to watermark enables appropriately shifting the output distribution to enhance detectability without significantly affecting semantics. This offers more freedom to effectively embed watermark compared to EXP-edit, which lacks this capability."

## [NEGATIVE] Fixed Splitting Ratio and Watermark Logit (KGW baseline)
KGW uses a constant splitting ratio γ and watermark logit δ across all tokens regardless of context or semantics, which compromises semantic coherence.

**Delta**: inferior Pareto frontier compared to proposed method across all evaluated models
**Condition**: Applied to general domain text generation; evaluated on OPT-1.3B and LLAMA2 7B/13B/70B

**Evidence**: "The design of KGW emphasizes easy detection of watermarked texts. However, this approach often compromises the semantic coherence of the texts... One primary cause of this issue is that KGW uses a constant splitting ratio and watermark logit across all tokens, without taking into account the context and semantics of the specific token being generated."

## [NEGATIVE] Balance-Marking Strategy (MultiBit baseline)
MultiBit embeds multi-bit information into LLM-generated texts and uses a Balance-Marking strategy to decrease perplexity of watermarked texts, developed through approximations for practical applicability.

**Delta**: inferior Pareto frontier compared to proposed method
**Condition**: Evaluated on OPT-1.3B

**Evidence**: "Our method achieves a superior Pareto frontier compared to MultiBit... However, embedding multi-bit information often reduces text quality... However, this method is developed through a series of approximations to ensure practical applicability, which might limit its effectiveness. In contrast, our method directly maximizes differentiable metrics of semantic coherence and detectability through multi-objective optimization."

## [POSITIVE] Computational Efficiency of Lightweight Networks
Using lightweight MLPs for the γ- and δ-generators keeps generation and detection speeds comparable to KGW and much faster than EXP-edit, SIR, and MultiBit.

**Delta**: Generation: 3.946s vs. EXP-edit 24.693s, SIR 8.420s, MultiBit 6.500s; Detection: 0.166s vs. EXP-edit 155.045s, SIR 0.337s, MultiBit 0.610s
**Condition**: Measured on OPT-1.3B for generating 200 tokens

**Evidence**: "Our method achieves higher speeds than EXP-edit, SIR, and MultiBit, while achieving speeds comparable to KGW, SWEET, and No Watermarking."
