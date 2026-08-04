# Instruction Tuning for Secure Code Generation

**Source**: https://proceedings.mlr.press/v235/he24k.html

## [POSITIVE] SafeCoder Joint Optimization
Combining security-specific instruction tuning with standard instruction tuning in a single training run, applying different loss functions depending on whether the sample comes from the security dataset or standard dataset

**Delta**: +~30% secure code generation rate, reaching ~90% security
**Condition**: Applied during instruction tuning phase across coding and general-purpose LMs

**Evidence**: "using SafeCoder during instruction tuning yields LMs that reach a secure code generation rate of ∼90%, surpassing their pretrained versions and their instruction-tuned counterparts without SafeCoder by ∼30%"

## [POSITIVE] Masked Language Modeling Loss on Secure Programs
Applying a negative log-likelihood loss masked by m_sec to focus training signal only on security-critical tokens of secure programs

**Delta**: ~10% improvement in security when masks are used vs. not used
**Condition**: Ablation study on StarCoder-1B and Phi-2-2.7B

**Evidence**: "This change results in about 10% decrease in security when compared to our full method. Therefore, focusing on security-tokens during training is essential for achieving the best security."

## [POSITIVE] Unlikelihood Loss on Insecure Programs
Applying a masked unlikelihood loss to penalize generation of security-critical tokens that lead to insecure code, providing a negative learning signal

**Delta**: -5.1% security for StarCoder-1B and -10.6% for Phi-2-2.7B when removed
**Condition**: Ablation study on StarCoder-1B and Phi-2-2.7B

**Evidence**: "In the last ablation study, we do not use the unlikelihood loss in Equation (4) during instruction tuning. This decreases security by 5.1% for StarCoder-1B and 10.6% for Phi-2-2.7B, which highlights the importance of performing negative training on insecure programs."

## [POSITIVE] Security-token Masking (m_sec and m_vul)
Using token-level diff between secure and insecure programs to identify and mask only security-relevant tokens during training, computed via Python difflib library

**Delta**: ~10% improvement in security vs. training on all tokens
**Condition**: Ablation study on StarCoder-1B and Phi-2-2.7B

**Evidence**: "we exclude masks m_sec and m_vul from the loss functions... As a result, the LM is trained on all tokens of o_sec and o_vul. This change results in about 10% decrease in security when compared to our full method."

## [POSITIVE] Automated Two-Step Data Collection Pipeline
First applying lightweight heuristic filtering (keyword matching, commit size limits) to GitHub commits, then using CodeQL static analysis to verify vulnerability fixes, reducing 145M commits to 465 high-quality samples

**Delta**: ~20% improvement in security vs. using only He & Vechev (2023) manual dataset
**Condition**: Ablation study on StarCoder-1B and Phi-2-2.7B

**Evidence**: "The comparison results show that 'no collected data' is about 20% less secure than our full method. Moreover, Table 10 in Appendix B provides breakdown results, showing that 'no collected data' performs poorly on CWEs not covered by He & Vechev (2023)'s training data."

## [POSITIVE] Oversampling Minority Classes
Oversampling minority CWE-language pair classes to exactly k samples to address data imbalance within the security dataset

**Delta**: Improves mean security rate and reduces variance; diminishing returns beyond k=20
**Condition**: Applied to StarCoder-1B with k=20 for coding LMs and k=40 for general-purpose LMs

**Evidence**: "We find that our oversampling scheme is strongly beneficial for both improving security and for stabilizing the training by reducing the variance. When k is larger than 20, the return is diminishing."

## [POSITIVE] GPT-4 Instruction Generation
Using GPT-4 to automatically generate functional instructions for secure/insecure program pairs, excluding security-specific features from the instruction

**Delta**: outperforms baseline
**Condition**: Used during dataset construction in the automated pipeline

**Evidence**: "we prompt GPT-4 to generate an instruction i that describes the common functionality of o_sec and o_vul... Our prompt specifies that i should describe the common functionality of o_sec and o_vul, excluding any mentions of security-specific features."

## [NEUTRAL] Security-Aware Prompting (Generic)
Adding a generic security instruction to the prompt asking the model to generate secure code without vulnerabilities

**Delta**: +2.1% for Mistral-Instruct-7B, +1.8% for CodeLlama-Instruct-7B, +3.6% for OctoCoder, +4.5% for GPT-3.5-Turbo-Instruct
**Condition**: Applied to existing instruction-tuned models without SafeCoder fine-tuning

**Evidence**: "security-aware instructions do not significantly improve security for current instruction-tuned models"

## [NEUTRAL] Security-Aware Prompting (CWE-Specific)
Adding a CWE-specific security instruction to the prompt with a description of the target vulnerability type

**Delta**: +2.7% for Mistral-Instruct-7B, +7.5% for CodeLlama-Instruct-7B, +3.2% for OctoCoder, +7.7% for GPT-3.5-Turbo-Instruct
**Condition**: Applied to existing instruction-tuned models without SafeCoder fine-tuning; requires unrealistic assumption of knowing target CWE

**Evidence**: "security-aware instructions do not significantly improve security for current instruction-tuned models"

## [NEUTRAL] LoRA Fine-tuning for 7B Models
Using lightweight Low-Rank Adaptation (LoRA) fine-tuning with r=16, alpha=32, 0.1 dropout for 7B parameter models due to GPU resource constraints

**Delta**: Not separately quantified vs. full fine-tuning
**Condition**: Applied to CodeLlama-7B, Llama2-7B, and Mistral-7B

**Evidence**: "For the 7B LMs, we use lightweight LoRA fine-tuning (Hu et al., 2022) due to constraints on GPU resources. For other smaller LMs, we always perform full fine-tuning."

## [NEGATIVE] Standard Instruction Tuning Without Security
Fine-tuning LMs with standard instruction tuning datasets (e.g., code or chat data) without any security-specific training

**Delta**: Models remain ~60-70% secure, only marginally better than pretrained versions
**Condition**: Baseline condition across all six evaluated LMs

**Evidence**: "even after standard instruction tuning (i.e., w/o SafeCoder), the models remain highly insecure. This is because standard instruction tuning lacks mechanisms for addressing security concerns."

## [NEGATIVE] SVEN-style KL Divergence Regularization
Using KL divergence loss to align fine-tuned LM output probabilities with original LM, creating a trade-off between security improvement and utility preservation

**Delta**: Creates security-utility trade-off; cannot achieve optimal security and functional correctness simultaneously
**Condition**: When applied to instruction tuning setting as comparison baseline

**Evidence**: "We observe that SVEN is unable to achieve optimal security and functional correctness at the same time. Instead, as also noted by He & Vechev (2023), there exists a trade-off between the two aspects, due to the conflicting objectives."

## [NEUTRAL] Training on Unseen CWE Types
Evaluating SafeCoder on CWE vulnerability types not present in the training dataset

**Delta**: No significant improvement; e.g., StarCoder-1B: 61.4% vs 57.4%, CodeLlama-7B: 49.3% vs 50.4%
**Condition**: Testing on CWEs excluded from SafeCoder training set

**Evidence**: "The results indicate that SafeCoder does not significantly improve security for these scenarios, suggesting that it does not achieve strong generalization across different CWEs."

## [POSITIVE] Heuristic Commit Filtering
Applying keyword matching on commit messages and limiting commit size (max 40 lines, 2 files) to reduce candidate commits before expensive static analysis

**Delta**: Reduced 145M+ commits by ~3 orders of magnitude to 150k candidates
**Condition**: First step of automated data collection pipeline

**Evidence**: "heuristicFilter successfully shrank down the commit dataset by about three orders of magnitude, resulting in 150k remaining commits."

## [POSITIVE] CodeQL Static Analysis Verification
Running CodeQL on both pre- and post-commit repository versions to verify that commits genuinely fix security vulnerabilities, requiring pre-commit vulnerabilities to be non-empty and post-commit to be zero

**Delta**: 4.9% of analyzed samples verified as genuine vulnerability fixes, yielding 1211 verified samples
**Condition**: Second step of automated data collection pipeline applied to 25k analyzable repositories

**Evidence**: "A vulnerability fix could be verified for 4.9% of the successfully analyzed samples, or 1211 samples in absolute terms."
