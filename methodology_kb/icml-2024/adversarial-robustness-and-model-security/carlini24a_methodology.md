# Stealing part of a production language model

**Source**: https://proceedings.mlr.press/v235/carlini24a.html

## [POSITIVE] SVD-based Hidden Dimension Extraction
Querying the model with random prompts to collect logit vectors, then performing SVD on the resulting matrix to identify the hidden dimension via a sharp drop in singular values

**Delta**: 0 or 1 error in 5 out of 6 models tested
**Condition**: When the API exposes full logit vectors and hidden dimension h is less than vocabulary size l

**Evidence**: "our attack recovers the embedding size nearly perfectly, with an error of 0 or 1 in five out of six cases"

## [POSITIVE] Multiplicative Gap Singular Value Identification
Identifying the hidden dimension by finding the largest multiplicative gap between consecutive singular values rather than using absolute thresholds

**Delta**: Spike occurs at exactly 2047th singular value for 2048-dimensional Pythia model
**Condition**: When dealing with floating-point precision limitations in production neural networks

**Evidence**: "we use a practical numerical rank of Q, where we order the singular values λ1 ≥ λ2 ≥ · · · ≥ λn, and identify the largest multiplicative gap λi/λi+1 between consecutive singular values"

## [POSITIVE] Full Projection Matrix Extraction via SVD
Recovering the full embedding projection matrix W (up to an h×h affine transformation) by computing U·Σ from the compact SVD of the query response matrix

**Delta**: RMS error of 3·10^-5 to 8·10^-4 across models, compared to 2·10^-2 for random initialization (100-500x lower error)
**Condition**: When full logit vectors are accessible via API

**Evidence**: "the RMS between a randomly initialized model and the actual weights is 2 · 10^−2, over 100–500× higher than the error of our reconstruction"

## [POSITIVE] Logit Bias with Reference Token Attack (4-logprob)
Using a common reference token to learn relative differences between logits by adding large bias B to push tokens into top-5, recovering K-1 logits per query

**Delta**: 23.0 bits of precision at 0.25 queries per logit
**Condition**: When API returns top-K logprobs and supports logit bias; chosen for production model attacks due to efficiency

**Evidence**: "logprob-4 (§5.3) top-5 23.0 bits of precision 0.25 queries per logit"

## [NEGATIVE] Linear Constraint Logit Recovery (5-logprob)
More sophisticated method treating each logprob as a linear constraint on original logits, recovering K logits per query instead of K-1

**Delta**: 11.5 bits of precision at 0.64 queries per logit vs 23.0 bits at 0.25 queries per logit for simpler attack
**Condition**: Top-5 logprob API; theoretically stronger but practically weaker due to numerical instability

**Evidence**: "theoretical improvements are not always practical: the theoretically stronger attack from §E that learns 5 logprobs per query in practice requires more queries and recovers logits with lower fidelity. This is because this attack is numerically unstable"

## [NEUTRAL] Binary Logit Bias Attack (top-1)
Attack using only top-1 logprob and binary logit bias values {-1, 0}, inferring logit values from the change in top token probability

**Delta**: 6.1 bits of precision at 1.0 queries per logit
**Condition**: Highly constrained API with only top-1 logprob and binary logit bias

**Evidence**: "logprob-1 (§5.4) top-1 6.1 bits of precision 1.0 queries per logit... this attack is much less numerically stable than the previously-discussed attacks, and so may require more queries to reach the same level of accuracy"

## [NEUTRAL] Binary Search Logprob-free Attack
Without logprob access, performing binary search on logit bias values until increasing any token by epsilon makes it most likely, recovering relative logits

**Delta**: 7.2 bits of precision at 10.0 queries per logit
**Condition**: No logprob access, only logit bias available; high query cost

**Evidence**: "binary search (§F.1) 7.2 bits of precision 10.0 queries per logit"

## [POSITIVE] One-of-N Logprob-free Attack
Logprob-free attack recovering logit information through structured queries without any logprob output

**Delta**: 18.0 bits of precision at 3.7 queries per logit; within factor of two of theoretical optimum
**Condition**: No logprob access; best performing logprob-free method

**Evidence**: "Our strongest logprob-free attack is highly efficient, and recovers 18 bits of precision at just 3.7 queries per logit. In Appendix G we theoretically analyze how far this is from optimal, and find it is within a factor of two."

## [POSITIVE] Multi-token Expansion Attack
Forcing the model to emit a repeated sequence of tokens to collect multiple logit vectors per query, reducing both query cost and token cost

**Delta**: Query cost of 1/(4m) and token cost of m/(1+m) where m is expansion factor
**Condition**: When model can be forced to emit repeated token sequences via logit bias

**Evidence**: "It is easy to see that the query cost of this attack is 1/(4m), where m is the expansion factor. Further, since each query requires 1 + m tokens, the token cost is m/(1+m)"

## [POSITIVE] Subset Token Logit Extraction
Using only a subset l' < l of tokens for dimension extraction rather than the full vocabulary

**Delta**: Reduces cost proportionally while maintaining correctness as long as l' > h
**Condition**: When vocabulary size is much larger than hidden dimension

**Evidence**: "taking only l′ < l rows of Q does not change the number of nonzero singular values, except in the unlikely case that the resulting submatrix is of smaller rank. Hence, we can choose a subset of l′ tokens and extract the dimension from logits on these tokens alone, as long as l′ > h"

## [POSITIVE] LayerNorm vs RMSNorm Detection via Bias Subtraction
Detecting normalization layer type by subtracting mean logits across queries and observing whether the h-th singular value drops, exploiting the centering property of LayerNorm

**Delta**: Successfully identifies LayerNorm in ada and babbage, RMSNorm in LLaMA-7B and Gopher-7B
**Condition**: When logprob data is available; requires mean subtraction and float64 precision for lower-precision models

**Evidence**: "there is a drop in the hth singular value for the architectures using LayerNorm, but not for architecture using RMSNorm"

## [POSITIVE] Post-hoc Architecture Dimension Expansion Defense
Defense that expands the hidden dimension of W by concatenating orthogonal weight vectors with small singular values and adding Gaussian noise to the hidden vector, misleading attackers about model size

**Delta**: Successfully misleads attack to report 1024 dimensions instead of true 768 for GPT-2 Small
**Condition**: As a defense; applied after model training without retraining

**Evidence**: "we can expand the dimensionality of W by concatenating extra weight vectors that are orthogonal to the original matrix... This misleads the adversary into thinking that the model is wider than it actually is"

## [POSITIVE] Logit Bias XOR Logprobs Mitigation
Defense that prohibits API queries using both logit bias and logprobs simultaneously, forcing attackers to use more expensive attack variants

**Delta**: Attack becomes 10x more expensive
**Condition**: As a defense/mitigation for model providers

**Evidence**: "Our attack is 10× cheaper when an adversary can supply both a logit bias and also view output logprobs. This suggests a natural mitigation: prohibit queries to the API that make use of both logit bias and logprobs at the same time."

## [NEGATIVE] Float16/bfloat16 Quantization Effect on Rank
Lower precision floating point representation causes some singular values to appear negligible, effectively reducing the observable rank of the model

**Delta**: GPT-2 Small reports 757 instead of true 768 dimensions in bfloat16; all 768 dimensions visible in float64
**Condition**: Models stored and run in 16-bit precision; affects dimension extraction accuracy for small models

**Evidence**: "when running the model in higher float64 precision, we find that indeed all dimensions are used, but that the smallest dozen or so singular values are much smaller than the other singular values"

## [POSITIVE] LayerNorm Bias Enabling Full Rank
The presence of a bias term in LayerNorm preserves full rank h of the hidden activation matrix, enabling accurate dimension extraction

**Delta**: All surveyed LLMs with LayerNorm bias achieved full rank h extraction
**Condition**: Models using LayerNorm with bias enabled

**Evidence**: "all LLMs we surveyed enabled the LayerNorm bias, which means the matrices had full rank h (besides GPT-2 Small: see Appendix A)"
