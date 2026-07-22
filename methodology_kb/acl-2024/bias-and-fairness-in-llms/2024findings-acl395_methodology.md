# Whose Emotions and Moral Sentiments do Language Models Reflect?

**Source**: https://aclanthology.org/2024.findings-acl.395/

## [NEUTRAL] Affective Alignment Measurement via JSD
Measuring alignment between LM-generated and human-authored tweets using one minus Jensen-Shannon Distance between affect distributions

**Delta**: alignment scores range from ~0.7 to ~1.0 across models
**Condition**: Used as the core evaluation metric across all 36 LMs on both COVID-19 and Roe v. Wade datasets

**Evidence**: "We measure affective alignment on a topic ti as S^ti(f,g) ∈ [0,1], using (1 - Jensen-Shannon Distance) between the distributions D̂(ti) and D(ti)."

## [NEGATIVE] Default Prompting
Prompting LMs to generate responses without providing any additional demographic or ideological context

**Delta**: nearly all LMs fall short of the partisan alignment baseline
**Condition**: Applied to both base LMs and instruction-tuned LMs on COVID-19 and Roe v. Wade topics

**Evidence**: "From Figure 2, it is evident that nearly all LMs fall short of the partisan alignment baseline, indicating weak alignment."

## [POSITIVE] Steered Prompting
Adding ideological context (liberal or conservative persona) to prompts to steer LM outputs toward a specific demographic group's perspective

**Delta**: most instruction-tuned LMs (8 out of 12) are better aligned with the target ideological group after steering
**Condition**: Effective for instruction-tuned LMs; largely ineffective for base LMs

**Evidence**: "for emotions on COVID-19 (Figure 3a), it is evident that most instruction-tuned LMs (8 out of 12) are better aligned with the target ideological group after steering"

## [POSITIVE] Conservative Steering
Specifically prompting LMs to generate content from a conservative viewpoint

**Delta**: improvement in alignment by conservative steering is much more pronounced than that by liberal steering
**Condition**: Applied to instruction-tuned LMs on COVID-19 topics where LMs already exhibit liberal tendencies by default

**Evidence**: "the improvement in alignment by conservative steering is much more pronounced than that by liberal steering, as indicated by the distance between orange right-facing triangle and the orange circle much longer than that between the blue left-facing triangle and the blue circle"

## [POSITIVE] Liberal Steering
Specifically prompting LMs to generate content from a liberal viewpoint

**Delta**: limited improvement due to LMs already exhibiting stronger default alignment with liberals
**Condition**: Applied to instruction-tuned LMs; less effective than conservative steering due to pre-existing liberal tendencies

**Evidence**: "possibly because LMs already exhibit stronger alignment by default with liberals, thus offering limited scope for further liberal alignment enhancement"

## [NEGATIVE] Instruction Tuning and RLHF
Fine-tuning LMs on instruction-following tasks with Reinforcement Learning from Human Feedback to improve alignment with human values

**Delta**: instruction-tuned models do not extend alignment to emotional or moral dimensions; GPT-3.5 exhibits heightened misalignment compared to base models
**Condition**: Evaluated on affective alignment with liberal and conservative ideological groups

**Evidence**: "Instruction-tuned models, despite undergoing instruction-based and RLHF training to foster alignment with human values, do not appear to extend this alignment to emotional or moral dimensions. Notably, even sophisticated models like GPT-3.5 exhibit heightened misalignment compared to base models."

## [POSITIVE] Instruction Tuning for Steerability
Instruction tuning and RLHF making models more responsive to ideological steering prompts

**Delta**: steering is effective for most instruction-tuned LMs but fails for almost all base LMs
**Condition**: When attempting to steer models toward specific ideological personas

**Evidence**: "steering is effective for most instruction-tuned LMs, as indicated by the left-facing and right-facing triangles of the same color positioned apart from each other. However, such failure cases happen for almost all base LMs... This observation demonstrates that instruction-tuning and RLHF make LMs more steerable."

## [POSITIVE] Plutchik Emotion Agreement (PEA) Weighting
Weighting emotion distributions using the Plutchik wheel's spatial proximity model to account for the interrelated nature of emotions before computing alignment

**Delta**: refines alignment measurements by accounting for interconnected emotional expressions
**Condition**: Applied only to emotion distributions, not moral foundations, due to lack of equivalent structural model for moral foundations

**Evidence**: "This methodological adjustment allows us to account for the interconnected nature of emotional expressions, refining our alignment measurements."

## [POSITIVE] SpanEmo Emotion Classifier
BERT-based multi-label emotion classifier fine-tuned on SemEval 2018 Twitter data, used to detect emotions in both human and LM-generated tweets

**Delta**: micro-F1 score of 0.713 on SemEval benchmark; average accuracy of over 0.9 across different emotions on Roe v. Wade subset
**Condition**: Used for emotion detection across all LM-generated and human-authored tweets

**Evidence**: "SpanEmo learns the correlations among the emotions and achieves a micro-F1 score of 0.713 on this dataset, outperforming several other baselines and achieving the state-of-the-art in detecting emotions on Twitter data."

## [POSITIVE] DAMF Moral Sentiment Classifier
BERT-based classifier fine-tuned on multiple Twitter datasets for detecting Moral Foundations Theory dimensions in tweets

**Delta**: F1-score of 0.71 on COVID-19 tweet subset
**Condition**: Used for moral sentiment detection across all LM-generated and human-authored tweets

**Evidence**: "Guo et al. (2023b) annotated the moral foundations of a subset of the COVID-19 tweets that we use in our paper, and further evaluated the performance of DAMF on it, which led to F1-score of 0.71."

## [POSITIVE] Multiple Prompt Templates
Using 10 different prompt variants per condition and randomly sampling from them to mitigate sensitivity to specific prompt wording

**Delta**: mitigates effect of model sensitivity to specific wording
**Condition**: Applied to all LMs across both default and steered prompting conditions

**Evidence**: "To mitigate the effect of the model's sensitivity to the specific wording in a prompt, we craft 10 different prompts for the base LMs and instruction-tuned LMs, using default prompting and steered prompting, respectively."

## [NEUTRAL] Partisan Alignment Baseline
Using the affective alignment between liberals and conservatives on Twitter as a reference baseline for evaluating LM alignment strength

**Delta**: nearly all LMs fall below this baseline, indicating misalignment larger than the partisan divide
**Condition**: Used as evaluation reference across all models and both datasets

**Evidence**: "Any alignment falling short of this benchmark could be deemed insufficient, given the profound divisions in contemporary sociopolitical discourse... it is evident that nearly all LMs fall short of the partisan alignment baseline, indicating weak alignment."

## [NEUTRAL] Ideology Estimation via News Sharing
Estimating user political ideology based on the political bias scores of news domains they share on Twitter

**Delta**: enables partitioning of Twitter users into liberal and conservative groups for comparison
**Condition**: Applied to COVID-19 and Roe v. Wade Twitter datasets to identify ideological groups

**Evidence**: "This method uses political bias scores of the domains users share according to Media Bias-Fact Check to estimate the ideology of users. In other words, if a users shares more left-leaning domains, they are considered to be liberal."

## [NEUTRAL] GPT-4 Topic Clustering
Using GPT-4 to cluster keywords within broad issues into fine-grained sub-topics for more granular analysis

**Delta**: produces 26 sub-topics for COVID-19 and 24 for Roe v. Wade
**Condition**: Applied during dataset preparation for both COVID-19 and Roe v. Wade datasets

**Evidence**: "In order to obtain a fine-grained span of topics, we use GPT-4 to cluster the keywords in each issue into sub-topics, such as 'mask mandates and policies' and 'mask health concerns'. We manually validated the clustering results."

## [NEGATIVE] LM Liberal Tendency (Systemic Bias)
Observed systematic tendency of LMs to align more closely with liberal affect, attributed to liberal-dominant pretraining data from social media

**Delta**: all LMs exhibit liberal tendencies on COVID-19; liberal tendencies persist even after conservative steering
**Condition**: Observed on COVID-19 topics; not statistically significant on Roe v. Wade topics

**Evidence**: "all instruction-tuned LMs retain liberal tendencies, after both liberal steering and conservative steering... This suggests that the representational imbalance is deeply entrenched in the instruction-tuned LMs, which cannot be mitigated or reversed simply through steering."

## [NEGATIVE] High Confidence Distribution in LM Outputs
LMs tend to assign high probability mass to a single emotion or moral foundation rather than distributing across multiple categories

**Delta**: LMs show a more focused distribution compared to humans; conservative steering produces smoother distributions more aligned with humans
**Condition**: Observed in both default and liberal steered models; partially mitigated by conservative steering

**Evidence**: "compared to humans, LMs show a more focused distribution across different types of emotions or moral foundations. This is similar to Durmus et al. (2023), where the authors find that LM tends to assign a high confidence to a single option for multi-choice questions."

## [POSITIVE] Conservative Steering Smoothing Effect
Conservative steering redistributes probability mass from positive emotions/moral foundations to more negative ones, producing distributions closer to human-authored tweets

**Delta**: conservative steering better aligns models with both liberals and conservatives
**Condition**: Observed in topic-level analysis of instruction-tuned LMs on COVID-19 mask mandate topic

**Evidence**: "With conservative steering, LMs' generated distribution becomes smoother and more aligned with that from humans. This might be one of the reasons why conservative steering better aligns the models with both liberals and conservatives."
