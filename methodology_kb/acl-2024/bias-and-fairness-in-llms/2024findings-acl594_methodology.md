# More than Minorities and Majorities: Understanding Multilateral Bias in Language Generation

**Source**: https://aclanthology.org/2024.findings-acl.594/

## [POSITIVE] Language Model Debiasing (LMD)
An auxiliary loss based on Jensen-Shannon divergence that penalizes the model when it assigns different probabilities to target terms of different demographic groups, encouraging equal generation probability across all demographics in a multi-demographic setting.

**Delta**: F-statistic reduced to 0.08 (Gender), 0.40 (Orientation); best t-value 0.81 (Orientation)
**Condition**: Most effective for Gender and Orientation bias dimensions; less effective or counterproductive for Race and Age bias dimensions

**Evidence**: "LMD and ADD methods are very effective at reducing the whole bias among all demographics, and the 'F-statistic' tends to be 0 on the test sets."

## [NEGATIVE] LMD on Race/Age bias
Applying the LMD auxiliary loss to race and age bias dimensions, where the t-value metric is used to measure pairwise demographic bias.

**Delta**: t-value increased from 1.71 (baseline) to 2.64 (Race); from 1.07 to 2.18 (Age)
**Condition**: Race and Age bias dimensions when measured by pairwise t-value

**Evidence**: "However, some results show that the debiasing method enlarged biases, such as the LMD method on race bias and age bias. This may be because the 't-value' of some demographic pairs changes from negative to positive and vice versa after debiasing, which leads to the increase of bias."

## [POSITIVE] Attribute Distance Debiasing (ADD)
An auxiliary loss that equalizes the cosine similarity distance between negative attribute feature representations and all demographic target term representations, extended from pairwise to multi-demographic settings.

**Delta**: F-statistic reduced to 0.02 (Gender best), t-value reduced to 0.14 (Gender best); best overall across most dimensions
**Condition**: Most effective for Gender bias; effective for Race and Religion; counterproductive for Orientation (t-value increased to 3.03)

**Evidence**: "LMD and ADD methods are very effective at reducing the whole bias among all demographics, and the 'F-statistic' tends to be 0 on the test sets."

## [NEGATIVE] ADD on Age bias - DST performance
Applying ADD debiasing to the age bias dimension and measuring downstream dialogue state tracking performance.

**Delta**: F1 dropped from 94.58 to 68.79; Accuracy dropped from 94.72 to 52.42
**Condition**: Age bias dimension on Dialogue State Tracking (DST) task

**Evidence**: "We note that the ADD reduces the performance of the DialoGPT on the DST dialogue task when reducing the age bias. We speculate that this is because age bias is more implicit than gender bias, race bias, etc... Perhaps the ADD method is too violent for age bias, which mitigates the bias but damages its language generative performance."

## [POSITIVE] Counter Target Data Augmentation (CTDA)
A data augmentation method that replaces all target demographic terms in training data with terms from all other demographic groups in B_multi, increasing training data size by (N-1) times where N is the number of demographics.

**Delta**: Best F-statistic for Religion (0.94) and best t-value for Religion (1.04); F-statistic 0.46 for Orientation
**Condition**: Most effective for Religion and Age bias dimensions; less effective for Race and Orientation

**Evidence**: "Data augmentation-based CADA and CTDA methods also perform well in mitigating the gender and religion bias dimensions."

## [POSITIVE] Counter Attribute Data Augmentation (CADA)
A data augmentation method that replaces attribute terms in training data according to B_multi, doubling the training data size, to balance attribute associations across demographic groups.

**Delta**: Best F-statistic for Gender (0.41), best t-value for Race (1.05); F-statistic 0.72 for Orientation
**Condition**: Most effective for Gender and Race bias dimensions

**Evidence**: "Data augmentation-based CADA and CTDA methods also perform well in mitigating the gender and religion bias dimensions."

## [POSITIVE] Multi-demographic debiasing (transfer to unseen groups)
Training debiasing methods on 3-4 demographic groups instead of just 2 (paired), then evaluating transfer to unseen demographic groups not seen during training.

**Delta**: Multi ADD achieves F-statistic 0.98 vs Pair ADD 4.61 for Race; Multi ADD achieves F-statistic 0.70 vs Pair ADD 3.91 for Religion; 'diamond' symbol (Multi less biased than Pair) appears in majority of comparisons
**Condition**: Transfer evaluation on unseen demographic groups (Native Hawaiian, American Indian for Race; Muslim, Atheist for Religion; Asexual for Orientation)

**Evidence**: "Our debiasing methods have better transfer ability than traditional methods among unknown demographic groups... In the dimension of religious bias, our method is very effective in mitigating overall bias (ΔF-statistic=3.58) and the bias in the 'Muslim-Atheist' pair (Δt-value=3.06)."

## [NEGATIVE] Paired (traditional) LMD on transfer to unseen groups
Applying the traditional paired-demographic LMD debiasing method and evaluating its transfer to unseen demographic groups.

**Delta**: F-statistic increased from 4.54 (baseline) to 9.20 (Pair LMD) for Race; from 4.28 to 5.06 for Religion; from 0.83 to 9.06 for Orientation
**Condition**: Transfer evaluation on unseen demographic groups across Race, Religion, and Orientation dimensions

**Evidence**: "We also find that the traditional LMD method enlarges the whole bias and the bias in unknown demographic pairs in three bias dimensions. It can be explained in this way: this method makes the model output the two targets with the same probability, which reduces the model's bias towards these two demographics but may increase the bias between other demographics besides them."

## [NEUTRAL] ANOVA F-statistic for multi-demographic bias evaluation
Using Analysis of Variance (ANOVA) F-statistic to measure overall bias across multiple demographic groups simultaneously, complementing pairwise t-value measurements.

**Delta**: Enables detection of multi-group bias not captured by pairwise metrics
**Condition**: Multi-demographic bias evaluation across all five bias dimensions

**Evidence**: "To analyze the model's bias against multiple demographic groups more comprehensively and clearly, we utilize Analysis of variance (ANOVA) to evaluate the bias degree in the model... The 'F-statistic' shows the difference between the within-group variances and the between-group variances."

## [NEUTRAL] Perplexity-based bias measurement
Using language model perplexity scores over demographically-varied test sentences to quantify bias; lower perplexity indicates higher model confidence and thus potential bias toward generating that content.

**Delta**: Reveals that Asians (29.3) and Latinos (129.3) receive lower perplexity than Blacks (159.7) and Whites (196.6) for crime-related sentences in DialoGPT
**Condition**: Bias detection across racial groups in DialoGPT small

**Evidence**: "The results show that DialoGPT small is not only racially biased against traditional Blacks-Whites pairs, but also significantly biased against Asians and Latinos, which are usually ignored by existing studies."

## [POSITIVE] Multi-demographic debiasing - DST task performance
Evaluating whether multi-demographic debiasing methods degrade downstream dialogue state tracking (DST) performance on MultiWoZ 2.0.

**Delta**: Most methods show very small decreases or even improvements; e.g., CTDA achieves 94.75 F1 vs 94.58 baseline for Gender
**Condition**: Downstream DST task performance across all five bias dimensions (except ADD on Age)

**Evidence**: "Most of the results of the four methods show very small decreases in F1 scores and accuracy (Acc), and some even improve the performance of the baseline. This result demonstrates the robustness of our bias mitigation methods on multi-demographic groups."

## [POSITIVE] Real data collection (vs. synthetic data)
Collecting bias examples from real Reddit comments using PushShift API rather than generating synthetic data by replacing demographic terms in an existing single-demographic dataset.

**Delta**: Enables identification of more diverse forms of bias across multiple demographic groups
**Condition**: Dataset construction for multi-demographic bias

**Evidence**: "To ensure the authenticity of bias in the dataset and identify more forms of bias that may be present, we avoided the use of synthetic data generation methods that rely on replacing demographic terms within a dataset related to only one demographic group. Instead, we collect data from multiple demographic groups to ensure that as many types of bias as possible are identified and addressed."

## [POSITIVE] Balanced demographic sampling in dataset
Ensuring equal numbers of biased sentences for each demographic group in the dataset to prevent skewing toward any particular group.

**Delta**: Prevents dataset-level bias from confounding debiasing experiments
**Condition**: Dataset construction across all five bias dimensions

**Evidence**: "Specifically, we ensured that the number of biased sentences for each demographic group was equal. This ensures that any biases in the dataset are not skewed towards a particular demographic group."
