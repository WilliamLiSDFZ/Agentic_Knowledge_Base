# Disperse-Then-Merge: Pushing the Limits of Instruction Tuning via Alignment Tax Reduction

**Source**: https://aclanthology.org/2024.findings-acl.175/

## [POSITIVE] Disperse-Then-Merge (DTM) Framework
A three-step framework that disperses instruction-following data into K non-overlapping clusters, trains separate sub-models on each cluster, then merges sub-models via weight averaging to cancel out data-specific biases while retaining generalizable knowledge.

**Delta**: GSM8K: 20.62 vs 18.50 (Vanilla), MMLU: 50.43 vs 49.74, BBH: 44.46 vs 42.78, ARC-c: 48.72 vs 46.93, HumanEval: 18.29 vs 17.68, MBPP: 23.60 vs 21.40, TruthfulQA: 29.13 vs 25.83
**Condition**: Applied to Llama-2-7b with TÜLU-V2-mix instruction-following data, K=4 clusters with equal weight merging

**Evidence**: "our proposed approach outperforms its peers on most evaluation benchmarks, proving the effectiveness of our DTM framework"

## [NEUTRAL] Random Data Splitting for Clustering
Randomly distributing instruction-following data into K equal portions instead of using sophisticated embedding-based clustering methods like K-means with sentence embeddings.

**Delta**: No significant difference vs. embedding-based clustering methods
**Condition**: Compared against MiniLM and MPNet-based K-means clustering on instruction/response/both encodings

**Evidence**: "none of those sophisticated clustering methods have an obvious advantage over simple random clustering"

## [NEUTRAL] Embedding-based K-means Clustering (Response encoding)
Using sentence embeddings of responses (R) with K-means clustering to partition instruction-following data into clusters for DTM.

**Delta**: Marginally better on some benchmarks (e.g., OBQA: 34.20, RACE: 42.39 for MiniLM-R) but not consistently superior
**Condition**: Compared against instruction-only and combined instruction+response encoding schemes

**Evidence**: "although the dense representation obtained via encoding response (R) is slightly better than other encoding schemes for clustering, none of those sophisticated clustering methods have an obvious advantage over simple random clustering"

## [POSITIVE] Average Weight Merging
Simple weighted average of K sub-model parameters with equal weights (αj = 1/K) as the model fusion strategy in DTM.

**Delta**: Best or near-best across most benchmarks compared to Fisher, Task Vector, Tie Merge, and DARE merging methods
**Condition**: Compared against Fisher merging, Task Vector, Tie Merge, and DARE on 9 benchmarks

**Evidence**: "it seems that no single merging method is apparently superior to others, and simple average weight merging is sufficient"

## [NEUTRAL] Fisher Merging
Uses approximated Fisher information matrix to find the fused model with highest joint probability across sub-models.

**Delta**: GSM8K: 19.64, MMLU: 50.41, BBH: 44.28 vs DTM average: 20.62, 50.43, 44.46
**Condition**: Applied as alternative merging method in DTM framework on 9 benchmarks

**Evidence**: "it seems that no single merging method is apparently superior to others, and simple average weight merging is sufficient"

## [NEUTRAL] Task Vector Merging
Subtracts base LLM weights from instruction-tuned model to obtain task vectors, then merges via vector arithmetic.

**Delta**: GSM8K: 19.71, MMLU: 49.85, BBH: 43.58 vs DTM average: 20.62, 50.43, 44.46
**Condition**: Applied as alternative merging method in DTM framework on 9 benchmarks

**Evidence**: "it seems that no single merging method is apparently superior to others, and simple average weight merging is sufficient"

## [NEGATIVE] Tie Merge
Trims and prunes models before merging and resolves interference between multiple models before conducting weight averaging.

**Delta**: GSM8K: 18.42, MMLU: 49.32, BBH: 42.90 — lowest among merging methods tested
**Condition**: Applied as alternative merging method in DTM framework; performs worst among merging strategies tested

**Evidence**: "it seems that no single merging method is apparently superior to others, and simple average weight merging is sufficient"

## [NEUTRAL] DARE Merging
Refines task vectors by dropout and rescaling before conducting vector arithmetic for model merging.

**Delta**: GSM8K: 18.95, MMLU: 49.89, BBH: 43.37 vs DTM average: 20.62, 50.43, 44.46
**Condition**: Applied as alternative merging method in DTM framework on 9 benchmarks

**Evidence**: "it seems that no single merging method is apparently superior to others, and simple average weight merging is sufficient"

## [NEUTRAL] Model Ensemble (vs. Model Merging)
Aggregating multiple sub-models by combining their output logits at inference time, rather than merging weights in parameter space.

**Delta**: MMLU overall: Ensemble 50.39 vs Merge 50.43 for DTM; computation cost is K times larger
**Condition**: Compared against weight merging for both Uniform Soup and DTM on MMLU benchmark

**Evidence**: "model ensemble is almost on par with model fusion except that model fusion is marginally better than ensemble overall. However, the computation required by model ensemble is K (the number of sub-models) times larger than the model fusion"

## [NEUTRAL] L2 Regularization (L2-norm)
Incorporates L2 regularization into the SFT training objective to prevent overfitting on instruction-following data and interference with parametric knowledge.

**Delta**: MMLU: 49.98, BBH: 43.61 — second-best on BBH but below DTM overall
**Condition**: Applied to Llama-2-7b SFT on TÜLU-V2-mix; competitive on some benchmarks but not consistently better than DTM

**Evidence**: "the performance of L2-norm and EWC also attains impressive performance on two benchmarks respectively, possibly due to the retention of pre-training knowledge through regularization techniques"

## [NEGATIVE] Elastic Weight Consolidation (EWC)
Continual learning regularization technique applied during SFT to mitigate catastrophic forgetting of pre-training knowledge by penalizing changes to important weights.

**Delta**: GSM8K: 15.77, MMLU: 49.02, BBH: 41.80 — below Vanilla SFT on most benchmarks
**Condition**: Applied to Llama-2-7b SFT on TÜLU-V2-mix; knowledge forgetting is not the main cause of alignment tax so EWC provides limited benefit

**Evidence**: "the performance of L2-norm and EWC also attains impressive performance on two benchmarks respectively, possibly due to the retention of pre-training knowledge through regularization techniques"

## [NEUTRAL] Replay (Pre-training Data Mixing)
Mixes pre-training data from Redpajama into instruction-following corpus in 1:1 ratio for multi-task learning to retain pre-training knowledge during SFT.

**Delta**: MMLU: 49.46, BBH: 43.05 — comparable to Vanilla but below DTM
**Condition**: Applied to Llama-2-7b on TÜLU-V2-mix; alignment tax persists despite replay, suggesting forgetting is not the main cause

**Evidence**: "Although a significant amount of pre-training data is mixed into the pre-training corpus to alleviate the forgetting and intervention of parametric knowledge, from Figure 3 we can see the drop in performance of traditional knowledge and reasoning benchmarks can hardly be removed"

## [POSITIVE] Uniform Soup
Merges multiple models trained on the full instruction-following corpus with different hyperparameter configurations via weight averaging.

**Delta**: MMLU: 50.24, second-best on three benchmarks; MT-bench: 5.04 vs DTM 5.19; Vicuna-bench: 7.48 vs DTM 6.60
**Condition**: Applied to Llama-2-7b on TÜLU-V2-mix; strong on instruction-following but weaker on knowledge/reasoning vs DTM

**Evidence**: "the performance of Uniform Soup is notable, achieving the second-best results on three benchmarks. The difference between Uniform Soup and ours lies in that their sub-models for merging are trained on the full volume of data with different hyper-parameters. Consequently, the data biases of its sub-models are more likely to be overlapped and cannot be removed at merging"

## [NEGATIVE] MoE (LoRAMoE)
Combines Mixture of Experts with parameter-efficient fine-tuning to enable expert coordination for task utilization and leverage of parametric knowledge.

**Delta**: GSM8K: 14.48, MMLU: 47.36, BBH: 40.39 — worst or near-worst on most benchmarks; MT-bench: 3.67
**Condition**: Applied to Llama-2-7b on TÜLU-V2-mix; underperforms even Vanilla SFT on most benchmarks

**Evidence**: "the performance of Uniform Soup is notable, achieving the second-best results on three benchmarks... [MoE results shown in Table 1 as consistently lower]"

## [NEUTRAL] Deita (Automatic Data Selection)
Automatic data selection strategy that filters instruction-following data based on complexity, quality, and diversity scores, keeping only samples with complexity scores above 2.5.

**Delta**: GSM8K: 18.12, MMLU: 48.50, BBH: 42.90 — below Vanilla SFT on MMLU but best on RACE (41.43)
**Condition**: Applied to Llama-2-7b on TÜLU-V2-mix; data quality filtering does not resolve alignment tax

**Evidence**: "our proposed approach outperforms both (1) data selection methods that filter out low-quality samples (Dou et al., 2023)"

## [NEGATIVE] Data Quality Filtering
Filtering instruction-following corpus to keep only high-quality samples (quality score > 2.5) using an automatic quality evaluator before SFT.

**Delta**: Alignment tax still persists after filtering; performance decline pattern unchanged
**Condition**: Applied to Llama-2-7b on TÜLU-V2-mix high-quality subset; does not eliminate alignment tax

**Evidence**: "Even if we filter out the low-quality samples within the instruction-following corpus with a quality evaluator (Liu et al., 2024), the alignment tax still exists as shown in Figure 2, suggesting that data quality is probably not the main cause behind the performance decline"

## [NEUTRAL] DTM on Small Datasets
Applying the DTM framework to small instruction-following corpora (e.g., LIMA with 1,000 samples).

**Delta**: LIMA: MMLU 46.25 vs Vanilla 46.70 (slight decrease); BBH 40.06 vs 39.46 (slight increase)
**Condition**: Applied to LIMA (1,000 samples); DTM benefit diminishes with very small datasets

**Evidence**: "DTM is not constrained by the domain of the instruction-following data, but its superiority is influenced by the data size"

## [POSITIVE] DTM on Diverse Domains
Applying DTM across instruction-following corpora from different domains (code, STEM, generic, medical, etc.).

**Delta**: Consistent improvements across Alpaca-GPT4, Code-Alpaca, Baize, Camel, Evol-Instruct datasets on MMLU, BBH, ARC-e, ARC-c
**Condition**: Applied across 5 different instruction-following corpora of varying domains and sizes

**Evidence**: "DTM is not constrained by the domain of the instruction-following data, but its superiority is influenced by the data size"

## [POSITIVE] DTM on Stronger Base LLMs
Applying DTM framework to more capable base models (Mistral-7b and Baichuan-2-7b) beyond Llama-2-7b.

**Delta**: Mistral-7b: GSM8K 43.52 vs Vanilla 38.51, MMLU 62.63 vs 62.01, BBH 60.87 vs 59.64; Baichuan-2-7b: GSM8K 26.46 vs 25.63, BBH 42.40 vs 40.53
**Condition**: Applied to Mistral-7b and Baichuan-2-7b with TÜLU-V2-mix; generalizes across different backbone architectures

**Evidence**: "suggesting that DTM is agnostic to the base LLM and able to generalize to more capable LLMs"

## [NEUTRAL] LoRA (Parameter-Efficient Fine-Tuning)
Using Low-Rank Adaptation as the parameter-efficient fine-tuning technique for all SFT experiments including DTM sub-model training.

**Delta**: Not quantified separately; used as standard setup across all methods
**Condition**: Used as default PEFT method for all experiments; other PEFT methods not explored

**Evidence**: "We generally utilize LoRA (Hu et al., 2022) as a parameter-efficient fine-tuning (PEFT) technique for SFT and do not perform experiments with other PEFT techniques"

## [NEGATIVE] Scaling Instruction-Following Data (Vanilla SFT)
Simply increasing the volume of instruction-following data used for standard SFT without any bias mitigation strategy.

**Delta**: Performance peaks then declines; e.g., Llama-2-7b MMLU drops after ~60-80% of data used
**Condition**: Applied to Llama-2-7b and Llama-2-13b on TÜLU-V2-mix; alignment tax emerges at latter stages of SFT

**Evidence**: "with the size of instruction-following data rising, it has been observed that the performance of LLM on standard knowledge and reasoning benchmarks does not always improve but exhibits degradation, i.e., the alignment tax"
