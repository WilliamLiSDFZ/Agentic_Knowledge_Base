# Noise Correction on Subjective Datasets

**Source**: https://aclanthology.org/2024.acl-long.294/

## [POSITIVE] Multitask Learning for Individual Annotators
Creating A separate fully-connected task heads (one per annotator) to predict each annotator's individual label, replacing a single majority-vote output head.

**Delta**: GHC: F1 45.57 (Multitask) vs 47.95 (Baseline); GoEmotions: e.g. Anger 56.31 (Multitask) vs 42.21 (Baseline)
**Condition**: Subjective datasets with multiple annotators (GabHateCorpus, GoEmotions)

**Evidence**: "For GoEmotions results, we see that for Multitask+LC, all six cases exceed the multitask results... Most notably, there is a significant improvement in performance between the majority and annotator (multitask) conditions."

## [POSITIVE] Loss-Based Label Correction (Multitask + LC)
Combining multitask learning with loss-based noise correction that uses a two-component mixture model to weight samples by their likelihood of being mislabeled, then re-parameterizes labels as a weighted sum of the network's prediction and the ground truth.

**Delta**: GHC F1: 50.3 (Multitask+LC) vs 45.57 (Multitask); GoEmotions Anger: 66.68 (Multitask+LC) vs 56.31 (Multitask)
**Condition**: Applied to subjective datasets in both single and multi-annotator settings

**Evidence**: "As can be seen in the GHC results, our method demonstrates improvements across all metrics when compared against the baselines... For GoEmotions results, we see that for Multitask+LC, all six cases exceed the multitask results."

## [POSITIVE] Subjectivity Parameter ψ
A hyperparameter that scales the network's self-guess loss term to control the degree of label correction, balancing agreement with disagreement. Higher ψ pushes more disagreeing labels toward the majority class; lower ψ encourages diversity.

**Delta**: GHC No Noise: ψ=0.5 gives F1 50.3 vs ψ=1 gives 47.86 vs ψ=0.25 gives 48.13
**Condition**: Multitask + Label Correction setting on GabHateCorpus and GoEmotions

**Evidence**: "Our investigation into the optimal setting for the subjectivity parameter (ψ) across GHC and GoEmotions datasets demonstrates that a ψ value of 0.5 consistently achieves the highest performance (relative to the majority vote) for our experimental setup."

## [POSITIVE] Manifold Mixup
Applying mixup at the embedding level by selecting a random layer from BERT and interpolating hidden states, addressing the challenge of direct input interpolation for textual data.

**Delta**: outperforms baseline
**Condition**: Applied to both Baseline + Loss Correction and Multitask + Loss Correction scenarios

**Evidence**: "While we observed an improvement in the multitask scenario, we believe the application of manifold mixup is also contributory to this, our multitask results exceed the results presented in the previous work."

## [POSITIVE] Entropy-Based Penalty Warmup
A warmup period using an entropy-based penalty on the confidence term during the initial training epochs to prevent noise overfitting during warm-up and stabilize training.

**Delta**: descriptive: stabilizes training and mitigates poor initialization
**Condition**: Loss correction training on GoEmotions and GabHateCorpus

**Evidence**: "A warmup period using an entropy-based penalty on the confidence term has been found useful to prevent noise overfitting during warm-up periods... We designated a warm-up period of 2 epochs for the GoEmotions and GabHateCorpus datasets. This was necessary to stabilize the training, mitigate poor initialization."

## [POSITIVE] Regularization to Prevent Class Collapse
Regularization following Tanaka et al. (2018) and Arazo et al. (2019) to deter the model from allocating all samples to a single class during label correction training.

**Delta**: descriptive: prevents degenerate solutions
**Condition**: Loss correction training on subjective datasets

**Evidence**: "We utilized regularization following Tanaka et al. (2018) and Arazo et al. (2019) aiming to deter the allocation of all samples to a singular class."

## [NEGATIVE] Majority Vote Aggregation (Baseline)
Standard approach of aggregating multiple annotations into a single ground truth label via majority voting, used as the baseline training target.

**Delta**: GHC Baseline F1: 47.95 (no noise) drops to 41.67 (20% noise); large drop under noise
**Condition**: Under 20% label noise injection on GabHateCorpus and GoEmotions

**Evidence**: "It is also interesting to note that both the majority-based methods for aggregating labels (Baseline Majority and Baseline + Label Correction), showed a large drop in performance. This highlights the importance of training multiple annotators as a way to mitigate the effect of noise."

## [NEGATIVE] Naive Loss-Based Noise Correction on Subjective Data
Directly applying standard loss-based noise correction (treating high-loss samples as mislabeled) to subjective datasets without accounting for minority opinions.

**Delta**: descriptive: erases diverse minority opinions
**Condition**: Applied directly to subjective datasets without the subjectivity parameter adjustment

**Evidence**: "a main challenge we try to overcome is that naive applications of these methods can erase the diverse perspectives of annotators. This is because the original technique makes use of a sample's loss to determine whether it is correctly or incorrectly labeled. On a dataset with subjective labels, we find that higher loss samples are associated with minority opinions which complicates the noisy sample detection process."

## [NEGATIVE] High ψ Value (ψ=1)
Setting the subjectivity parameter to its maximum value, causing the network to strongly push disagreeing labels toward the majority class.

**Delta**: GHC F1: 47.86 (ψ=1) vs 50.3 (ψ=0.5); GoEmotions Anger: 55.05 (ψ=1) vs 66.68 (ψ=0.5)
**Condition**: Multitask + Label Correction on GabHateCorpus and GoEmotions

**Evidence**: "Setting the value too high may lead the network to make incorrect guesses and may lead to increased variance and inaccuracies."

## [POSITIVE] Network Memorization Effect Exploitation
Leveraging the two-phase deep network learning behavior where networks first learn correct/simple patterns before memorizing noisy/complex ones, using early-phase loss distributions to separate agreeing from disagreeing annotations.

**Delta**: descriptive: clear bimodal separation of agreeing vs disagreeing samples observed
**Condition**: Multitask learning on GabHateCorpus and GoEmotions during training

**Evidence**: "We showcase a clear bimodal distribution to illustrate the challenge of separating noise and opinion in Figure 1. We see that for a specific annotator, there are peaks for agreeing and disagreeing samples... Arpit et al. (2017) demonstrated that networks tended to learn correct samples first before memorizing the incorrect samples. In our problem, the semantics of this changes to agreeing versus disagreeing samples."

## [POSITIVE] Multitask Learning Under Noise Injection
Using multiple annotator task heads instead of majority-vote aggregation when 20% label noise is injected into the dataset.

**Delta**: GHC 20% noise: Multitask+LC F1 51.55 vs Baseline+LC F1 45.97; GoEmotions 20% noise: Multitask+LC consistently outperforms Baseline+LC across all emotions
**Condition**: 20% label noise injection on GabHateCorpus and GoEmotions

**Evidence**: "We see that for the results of GoEmotions in Table 5, there is a significant drop in the majority label annotations. However, the multitask cases all showcase a smaller drop in performance than the majority label techniques. This highlights the need to account for multiple annotator opinions."

## [POSITIVE] ψ=0.5 Balanced Subjectivity Setting
Setting the subjectivity parameter to 0.5 to achieve a balanced trade-off between noise correction and preservation of diverse minority opinions.

**Delta**: GHC: 18% increase in agreement between model predictions and majority labels; GoEmotions: ~14% improvement in prediction consistency
**Condition**: Multitask + Label Correction on both GabHateCorpus and GoEmotions

**Evidence**: "For the GHC Multitask model depicted on the left of Figure 2, there is a visible trend where the variance decreases to its lowest point at ψ=0.5. This represents an 18% increase in the agreement between the model's predictions and the majority labels. The GoEmotion Multitask model shown on the right shows a corresponding improvement of approximately 14% improvement in prediction consistency."
