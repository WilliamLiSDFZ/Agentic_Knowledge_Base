# Causal-Guided Active Learning for Debiasing Large Language Models

**Source**: https://aclanthology.org/2024.acl-long.778/

## [POSITIVE] Causal Invariance-Based Biased Instance Identification
Identifies biased instances by finding counter example pairs where model hidden states are similar but generated outputs differ significantly, violating causal invariance between semantic content and subsequent text.

**Delta**: outperforms baseline
**Condition**: Applied to multiple-choice QA tasks with LLMs (llama2-13B-chat, vicuna-13B-v1.5) across generalizability and unharmfulness benchmarks

**Evidence**: "Compared with vanilla zero-shot baselines, zero-shot CAL can consistently improve model performance on all the datasets, and even surpass the performance of few-shot methods on part of benchmarks. The effectiveness of zero-shot CAL suggests that the biased patterns induced by CAL are typical and truly exist in the datasets."

## [POSITIVE] Influential Criterion for Biased Instance Selection
Selects counter example pairs where the predicted probability of the gold subsequent text is low, indicating that dataset bias significantly hinders the LLM on those instances.

**Delta**: outperforms baseline
**Condition**: Used in combination with the typical criterion to select informative biased instances for bias pattern induction

**Evidence**: "for any input text Xi, if the probability that Yi is properly generated is rather low, it suggests that biased information significantly hinders the LLM. Hence, such examples would contain a high level of bias and could be informative biased instances."

## [POSITIVE] Typical Criterion for Biased Instance Selection
Selects counter example pairs where the LLM's generations for both instances in the pair are similar, making it easier to summarize a unified bias pattern.

**Delta**: outperforms baseline
**Condition**: Applied during informative biased instance selection to enable coherent bias pattern induction

**Evidence**: "if Yˆi and Yˆj are similar, it would be easier to conclude the influence caused by the bias, as the influence of dataset bias is typical... by utilizing the causal invariance together with the influential and typical criterion, a set of typical biased instances could be selected, so that the biased patterns could be effectively induced."

## [POSITIVE] PCA Dimensionality Reduction for Bias Representations
Applies Principal Component Analysis to reduce bias representation vectors to two dimensions before clustering, retaining over 96% of total variance and removing noise.

**Delta**: neutral (enabling step)
**Condition**: Applied before DBSCAN clustering of bias representation vectors

**Evidence**: "We find that the first two principal components can explain over 96% of the total variance. Thus, the left part may mainly be noise and would disturb the process of clustering. Hence, we perform the DBSCAN based on the first two PCA components."

## [POSITIVE] DBSCAN Clustering of Bias Representations
Uses density-based clustering (DBSCAN) on dimension-reduced bias representation vectors to group counter example pairs into clusters for bias pattern induction.

**Delta**: neutral (enabling step)
**Condition**: Applied to bias representation vectors after PCA reduction to group biased instances by type

**Evidence**: "bias representations are concentrated in several distinct groups after dimensionality reduction through PCA. Moreover, the bias patterns summarized based on different clustering categories are also distinguished. This indicates that our method could discover different types of biased instances and then induce bias patterns."

## [POSITIVE] Zero-Shot ICL Bias Suppression via Induced Patterns
Appends automatically induced bias pattern descriptions (e.g., 'X is not related to the goal of the task') to the original prompt to prevent LLMs from using biased information during zero-shot inference.

**Delta**: outperforms vanilla zero-shot baseline
**Condition**: Zero-shot setting across Chatbot, MT-Bench, MNLI, HANS, BBQ, UNQOVER datasets

**Evidence**: "Compared with vanilla zero-shot baselines, zero-shot CAL can consistently improve model performance on all the datasets, and even surpass the performance of few-shot methods on part of benchmarks."

## [POSITIVE] Counterfactual Few-Shot ICL (FS-CAL)
Provides automatically derived counterfactual examples (instances where bias leads to incorrect generation) as few-shot demonstrations to implicitly inform LLMs that biased information is not predictive.

**Delta**: outperforms vanilla few-shot baseline
**Condition**: Few-shot setting across Chatbot, MT-Bench, MNLI, HANS, BBQ, UNQOVER datasets

**Evidence**: "few-shot CAL achieves consistent performance improvement on the two categories of benchmarks. This demonstrates that, CAL can improve both the generalizability and the unharmfulness of LLMs, and suggests that by utilizing the essential differences between semantic information, CAL can identify a set of biased instances, and the counterfactual ICL-based prompts can effectively leverage the biased counterfactual examples to debias LLMs."

## [POSITIVE] ICL-Based Debiasing vs. Fine-Tuning
Uses in-context learning instead of fine-tuning for debiasing to avoid over-optimization and generalizability degradation associated with fine-tuning-based approaches.

**Delta**: avoids in-distribution performance degradation
**Condition**: Applied to generative LLMs where fine-tuning risks over-optimization

**Evidence**: "through ICL, LLMs can both effectively debias themselves and avoid the in-distribution performance degradation which is always associated with fine-tuning-based approaches (Du et al., 2023), suggesting the superiority of ICL-based debiasing methods."

## [POSITIVE] Cross-LLM Bias Pattern Generalization
Applies bias patterns induced from one LLM (llama2-13b-chat) to debias a different LLM (GPT-4), exploiting shared pretraining corpus biases.

**Delta**: outperforms vanilla zero-shot in most cases for GPT-4
**Condition**: Cross-model transfer: bias patterns from llama2-13b-chat applied to GPT-4 on Chatbot, MT-Bench, MNLI, HANS, BBQ, UNQOVER

**Evidence**: "compared to vanilla zero-shot, ZS-CAL achieves higher performance in most cases. This demonstrated that different LLMs might share similar bias patterns and we can debias an LLM based on the bias pattern identified from other LLMs."

## [POSITIVE] Open-Source LLM for Bias Pattern Induction (Qwen-72B)
Uses Qwen1.5-72B-Chat instead of GPT-4 to summarize bias patterns from clustered counter example pairs.

**Delta**: outperforms baseline but slightly inferior to GPT-4
**Condition**: Bias pattern induction step when using open-source model as alternative to GPT-4

**Evidence**: "the results still outperform the baseline methods with the biased patterns induced by free open-source LLM, while slightly inferior to that of GPT-4."

## [NEUTRAL] Subset-Based Bias Pattern Induction (20% Data)
Runs CAL on only 20% of the dataset rather than the full corpus to reduce computational cost while maintaining effectiveness.

**Delta**: performance keeps relatively stable with 20% data
**Condition**: Applied to MNLI dataset with llama2-13b-chat; useful when data is scarce or computation is limited

**Evidence**: "the performance of CAL keeps relatively stable with 20% data. Moreover, our approach still far outperforms the baseline method on the HANS dataset, which demonstrates the effectiveness of our approach to debias LLMs."

## [POSITIVE] Predictive Criterion Filtering
Filters out counter example pairs where the LLM has not captured any predictive information (both instances generate improper outputs), ensuring identified pairs truly reflect bias rather than model confusion.

**Delta**: neutral (quality control step)
**Condition**: Applied during biased instance identification to improve purity of detected bias instances

**Evidence**: "To rule out such instances, we introduce an additional filtering process using a Predictive Criterion, which requires that M should at least make a proper generation for the instance i or j, since if on both i and j model generation are improper, it is rather probable that M has not captured any predictive information in Xi or Xj."

## [NEGATIVE] Providing More Than Two Bias Patterns in Zero-Shot Prompt
Including more than two bias patterns in the zero-shot debiasing prompt during inference.

**Delta**: decline in performance
**Condition**: Zero-shot debiasing prompt construction when multiple bias patterns are available

**Evidence**: "In zero-shot scenarios, we discovered that providing debiasing prompt containing more than two bias patterns may lead to a decline in performance, even if using any of these bias patterns individually would improve performance."

## [POSITIVE] Prior Knowledge-Based Zero-Shot Debiasing (ZS-known)
Uses manually crafted debiasing prompts based on researchers' prior knowledge of specific biases (e.g., swapping positions, avoiding stereotype language).

**Delta**: improved performance over vanilla zero-shot on all datasets
**Condition**: Zero-shot setting; limited by dependence on manual identification of biases

**Evidence**: "in general, the prior knowledge-based zero-shot debiasing methods show improved performance on all the datasets. This indicates that through ICL, LLMs can both effectively debias themselves and avoid the in-distribution performance degradation which is always associated with fine-tuning-based approaches."

## [POSITIVE] Bias Representation Vector Extraction via Element-Wise Similarity
Extracts bias representation vectors by identifying element-wise similar components between hidden states of counter example pairs, using a strict threshold (0.15) to ensure purity of bias information.

**Delta**: neutral (enabling step)
**Condition**: Applied during bias representation extraction for clustering in the MNLI dataset with llama2-13B-chat

**Evidence**: "We set a strict threshold of 0.15 for the ratio to ensure that the bias representation vectors of the counter example pairs have purer bias information."

## [NEGATIVE] Zero-Shot CAL on Constituent Bias Category
Applying zero-shot CAL debiasing to the constituent bias subcategory of the HANS dataset.

**Delta**: not effective for constituent bias (48.1 ZS-CAL vs 50.0 ZS)
**Condition**: Zero-shot setting on HANS constituent bias subcategory with llama2-13B-chat

**Evidence**: "Perhaps because the bias patterns summarized by GPT-4 is not comprehensive enough, zero-shot CAL method is not effective for constituent bias category."

## [POSITIVE] Few-Shot CAL on Constituent Bias Category
Applying few-shot counterfactual ICL debiasing to the constituent bias subcategory of the HANS dataset.

**Delta**: +0.6 accuracy (48.6 FS vs 49.2 FS-CAL)
**Condition**: Few-shot setting on HANS constituent bias subcategory with llama2-13B-chat

**Evidence**: "few-shot CAL method is effective for all the three bias categories, especially on the lexical overlap and subsequence bias categories."

## [NEUTRAL] Hyperparameter Sensitivity of Counter Example Pair Count
Varying the number of counter example pairs and negative examples across different orders of magnitude to test robustness of CAL.

**Delta**: performance remains relatively stable across magnitudes
**Condition**: Sensitivity analysis on MNLI and HANS datasets with llama2-13B-chat

**Evidence**: "Empirically, the performance of CAL remains relatively stable with different magnitudes for counter example pairs and negative examples. Moreover, our approach generally outperforms the baseline method on the HANS dataset."
