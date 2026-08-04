# Recovering the Pre-Fine-Tuning Weights of Generative Models

**Source**: https://proceedings.mlr.press/v235/horwitz24a.html

## [POSITIVE] Spectral DeTuning
An iterative, gradient-free algorithm for pre-fine-tuning weight recovery using low-rank matrix factorization (SVD-based coordinate descent) to recover the original pre-trained model weights from multiple LoRA fine-tuned models.

**Delta**: W-Error -17.816 vs -7.540 (Mean LoRA baseline) for Stable Diffusion; LPIPS 0.009 vs 0.482 for Stable Diffusion
**Condition**: Applied to LoRA fine-tuned models including ViT, Stable Diffusion, and Mistral

**Evidence**: "Spectral DeTuning recovers the Pre-Fine-Tuning images with high precision, even when using 'in the wild' LoRAs, essentially reversing the personalization finetuning of the LoRA model"

## [POSITIVE] Rank Scheduler
A progressive rank scheduling strategy that starts with a lower rank r* < r and increases it according to an 'Increase on Plateau' schedule, forcing the optimization to focus on the most significant principal components first before increasing complexity.

**Delta**: Over 95% of layers converge with precision of at least -16 with scheduler vs less than 40% without
**Condition**: Applied during Spectral DeTuning optimization on Stable Diffusion; also used with per-LoRA rank schedulers when ranks vary

**Evidence**: "When using the rank scheduler, over 95% of the layers converge with a precision of at least −16, in contrast to less than 40% when not using the scheduler."

## [POSITIVE] Mean LoRA Initialization
Initializing the estimated pre-fine-tuning weight matrix W* as the average of all n fine-tuned weight matrices at iteration 0.

**Delta**: Used as starting point; enables convergence of the iterative algorithm
**Condition**: Used as initialization step in Spectral DeTuning before M-step/W-step iterations

**Evidence**: "At iteration 0, we set W* as the average of n all the fine-tuned matrices, i.e., W* = 1/n sum W'_i."

## [NEGATIVE] Mean LoRA Baseline
A baseline method that simply averages the weights across all LoRA fine-tuned models, based on the assumption that the mean of the LoRA residuals is approximately zero.

**Delta**: W-Error -7.540 vs -17.816 (Spectral DeTuning) for Stable Diffusion; LPIPS 0.482 vs 0.009
**Condition**: Applied as a baseline across ViT, Stable Diffusion, and Mistral experiments

**Evidence**: "As expected, the LoRA fine-tuned models are indeed different from the Pre-FT model. Averaging over several LoRA models slightly improves the results, but is still far from recovering the Pre-FT activations."

## [POSITIVE] LoRA Rank Estimation Heuristic
A method to estimate unknown LoRA ranks by subtracting pairs of fine-tuned models (Wi' - Wj' = Mi - Mj) and using the rank of the difference as an upper bound, formulated as a linear programming problem.

**Delta**: 100% accuracy on hundreds of combinations of LoRAs with different ranks
**Condition**: Applied when LoRA ranks are unknown or varying across models

**Evidence**: "We tested the LoRA rank estimation heuristic presented in Section 5.4 on hundreds of combinations of LoRAs with different ranks. The heuristic achieved an accuracy of 100%."

## [POSITIVE] Per-Layer Independent Optimization
Performing the pre-FT weight recovery optimization independently on each layer, enabling high parallelization of the attack across GPUs.

**Delta**: Recovers Mistral-7B weights in under five minutes on a cluster of RTX2080 GPUs
**Condition**: Applied to all fine-tuned layers of large-scale models like Mistral-7B

**Evidence**: "it is highly parallelizable, e.g., on a cluster of desktop GPUs such as RTX2080 our method can recover the Pre-FT weights of a Mistral-7B model in under five minutes."

## [POSITIVE] Log-Space W-Error Metric
Using log-transformed mean squared weight error as the evaluation metric to be robust to outlier layers that fail to converge, providing a more representative summary of convergence quality.

**Delta**: W-Error -17.634 (Spectral DeTuning) vs -7.437 (Mean LoRAs); MSE values 3.395e-09 vs 1.525e-07 are misleading due to outliers
**Condition**: Used as evaluation metric across all LoWRA Bench experiments

**Evidence**: "We use log-space as when errors are very small, the average mean squared weight error is determined by outliers, e.g., a single non-converging layer when all other layers converge. Log transforming the mean squared error is robust to such outliers."

## [POSITIVE] Data-Free Unsupervised Optimization
The optimization objective requires no training data and makes no assumptions about the data used to train the model, operating purely on the weight matrices of fine-tuned models.

**Delta**: Enables attack without any training data or prior knowledge of source model
**Condition**: Applied across all model types (ViT, Stable Diffusion, Mistral)

**Evidence**: "First, it is training-free, meaning, it requires no data, nor does it make any assumptions with regards to the data used to train the model. Moreover, the optimization is performed on a per-layer basis, enabling high parallelization of the attack."

## [NEGATIVE] High LoRA Rank Usage
Using higher LoRA ranks (e.g., r=32, r=64) during fine-tuning, which increases the difficulty of pre-FT weight recovery.

**Delta**: W-Error degrades from -15.636 at rank 8 to -4.817 at rank 32 (5 LoRAs); from -15.822 to -9.639 (10 LoRAs)
**Condition**: Applied to ViT experiments with fixed number of LoRAs (5 or 10)

**Evidence**: "In Tables 6 and 7 we show the results for the ViT model when using different LoRA ranks and fixing the number of LoRAs. [rank 8: -15.636, rank 32: -4.817 for 5 LoRAs]"

## [POSITIVE] Increasing Number of LoRAs
Using more LoRA fine-tuned models as input to Spectral DeTuning, providing additional constraints on the pre-FT weight estimation.

**Delta**: Monotonically improves W-Error convergence across all model types as number of LoRAs increases from 2 to 15
**Condition**: Applied across ViT, Stable Diffusion, Mistral SFT, and Mistral DPO experiments

**Evidence**: "In Figure 7 we illustrate the impact of the number of fine-tuned LoRA models on the W-Error convergence... Mistral DPO obtains a lowest W-Error but only semantically converges when using 8 LoRAs"

## [POSITIVE] Mixed-Source LoRA Detection
Using the rank estimation heuristic to detect and remove LoRA models that originated from a different pre-trained source model, by identifying full-rank differences between the mixed model and others.

**Delta**: Successfully detected the SD 1.4 LoRA mixed into a set of SD 1.5 LoRAs
**Condition**: Applied when a LoRA from a different pre-trained model (SD 1.4) is mixed into a set of same-source LoRAs (SD 1.5)

**Evidence**: "Indeed, the above steps indicated the LoRA that originated from Stable Diffusion 1.4 has a full rank difference from any other LoRA (while the pairwise rank between the LoRAs that used the same Pre-FT model were low rank, as expected)."

## [POSITIVE] Coordinate Descent Optimization
Alternating between M-step (fixing W* and solving for each Mi via SVD truncation) and W-step (fixing all Mi and solving for W* as the mean of residuals) to iteratively solve the non-convex optimization problem with closed-form sub-solutions.

**Delta**: Achieves near-perfect correlation between loss and W-Error (rho=0.994)
**Condition**: Core optimization procedure of Spectral DeTuning applied to all model types

**Evidence**: "While the optimization problem in Equation (3) is non-convex, it can be iteratively broken down into a set of simple sub-problems which have closed-form solutions."

## [POSITIVE] Varying Rank LoRA Robustness
Using a dedicated rank scheduler per LoRA model when input LoRAs have different ranks, allowing Spectral DeTuning to handle heterogeneous fine-tuned models.

**Delta**: W-Error -14.453 vs -6.969 (Mean LoRA) with ranks [8,32,32,32,64,100]; LPIPS 0.073 vs 0.307
**Condition**: Applied to Stable Diffusion with n=6 LoRAs of varying ranks [8,32,32,32,64,100] from CivitAI

**Evidence**: "Spectral DeTuning is robust to the varying ranks, exhibiting only a minor decrease in performance despite the higher rank of the LoRAs."
