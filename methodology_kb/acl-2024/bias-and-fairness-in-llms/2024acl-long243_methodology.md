# Favi-Score: A Measure for Favoritism in Automated Preference Ratings for Generative AI Evaluation

**Source**: https://aclanthology.org/2024.acl-long.243/

## [NEUTRAL] Sign Accuracy (Sample-Level)
Measures the fraction of individual samples where the automated metric agrees with human preference ratings

**Delta**: Spearman's ρ = -0.01 correlation with Favi-Score
**Condition**: Used as a standalone metric evaluation measure; insufficient alone to capture systematic bias

**Evidence**: "The correlation of the Favi-Score to the sample-level sign accuracy is depicted in Figure 5b, which shows a small correlation (Spearman's-ρ = −0.01)."

## [NEUTRAL] Sign Accuracy (System-Level)
Measures the fraction of system pairs where the automated metric agrees with human evaluation on which system is better overall

**Delta**: Spearman's ρ = -0.25 inverse correlation with Favi-Score
**Condition**: Used as a standalone metric evaluation measure; better than sample-level but still insufficient to detect favoritism

**Evidence**: "there is a low-to-moderate inverse correlation between the two scores of Spearman's-ρ = −0.25"

## [POSITIVE] Favi-Score
A score measuring favoritism in automated preference metrics by computing the expected error cost, weighted by direction and severity of disagreements with human ratings

**Delta**: Identifies ranking errors undetectable by sign accuracy alone
**Condition**: Applied to any preference-based automated metric evaluation; complements sign accuracy scores

**Evidence**: "our main finding is that favoritism causes mistakes in the rankings of systems according to the metric: even a metric with a high sign accuracy can lead to wrong evaluation if it has a strong favoritism."

## [POSITIVE] Directed Error Cost Weighting
Weighting scheme that assigns costs to metric errors based on their severity and direction: switching + to - costs 2, switching + to = costs 1, reflecting impact on outcome margin

**Delta**: Enables differentiation between C1 (Φ=2) and C2 (Φ=1) despite both having 10 errors
**Condition**: Core component of Favi-Score computation for three-way preference ratings (+, =, -)

**Evidence**: "Mistaking + for − leads to a change of 2 in the outcome margin, whereas mistaking + with = changes the outcome margin by 1. Thus, we weigh these mistakes accordingly and define the error cost."

## [NEUTRAL] Scalar-to-Preference Conversion
Converting scalar or Likert metric outputs to preference ratings by comparing paired scalar values, assuming higher values indicate higher quality

**Delta**: None
**Condition**: Applied when metrics output scalar values rather than direct preferences; used across all experimental domains

**Evidence**: "Since most metrics return a scalar value, we need to transform them into a preference rating. Similarly, in many cases human ratings are available as scalar or ordinal judgements for a single input and output pair."

## [POSITIVE] ChatGPT as Preference Metric with Chain-of-Thought
Using GPT-3.5-Turbo prompted to provide preference ratings along with feedback and explanation to elicit chain-of-thought reasoning, then discarding the explanations for evaluation

**Delta**: High system-level accuracy in WMT-22
**Condition**: Applied to WMT-22 machine translation evaluation as an additional metric

**Evidence**: "we discard the feedback and explanation texts which were included to elicit behavior analogous to chain of thought (Wei et al., 2022) prompting... ChatGPT has a high system-level accuracy"

## [NEGATIVE] Symmetry Assumption for Preference Ratings
Assuming preference ratings are symmetric with respect to system order, inverting ratings (+ to -) for reversed system pairs rather than collecting new ratings

**Delta**: Overall accuracy of 69% and Krippendorff-α of 0.249 when comparing original vs. flipped ratings
**Condition**: Applied to ChatGPT preference ratings in WMT-22; introduces inconsistency due to position bias

**Evidence**: "we also collected ratings for flipped system pairs and noticed discrepancies. We show the confusion matrix in Figure 7. The overall accuracy is 69% and the intra-rater Krippendorff-α (Krippendorff, 1970) is 0.249."

## [NEUTRAL] DAG-based System Ranking Visualization
Representing system rankings as directed acyclic graphs where edges indicate statistically significant preference between systems based on sign tests at 95% confidence

**Delta**: System-level agreement of 61.1% for COMET-22 vs. human DAG
**Condition**: Used as visualization tool; insufficient alone to detect favoritism when rankings are preserved but margins are distorted

**Evidence**: "Note that only considering the DAG does not reveal the whole story. For example, if a metric unduly favors a system that humans also rank highly, the overall ranking might not change."

## [NEGATIVE] COMET-22 as Automated MT Metric
Neural machine translation evaluation metric used for preference rating in WMT-22, exhibiting systematic favoritism toward certain systems

**Delta**: System-level agreement of 61.1%; strongly disfavors ref-B and favors QUARTZ_TuneReranking
**Condition**: Applied to WMT-22 English-to-German machine translation evaluation

**Evidence**: "according to COMET-22, ref-B is ranked much worse, while QUARTZ_TuneReranking is disproportionately favored by COMET-22 compared to the human ranking. This is a direct consequence of favoritism."

## [NEUTRAL] BertScore for Summarization Evaluation
BERT-based metric for evaluating summarization quality, showing high system-level sign accuracy but very low sample-level accuracy with moderate favoritism

**Delta**: System-level sign accuracy 0.789, sample-level accuracy 0.05, mean Favi-Score 0.29
**Condition**: Applied to SummEval consistency feature evaluation

**Evidence**: "BertScore has a high system-level sign accuracy (0.789), while having an exceptionally low sample level accuracy (0.05). However, since the Favi-Score is low as well (mean of 0.29), it showcases that the Favi-Score is more influential on the final ranking than the sample level accuracy."

## [NEGATIVE] ROUGE Score for Summarization Evaluation
N-gram overlap metric for summarization showing higher favoritism than BertScore despite slightly higher sample-level accuracy

**Delta**: Sample-level accuracy 0.07, average Favi-Score 0.339, system-level sign accuracy 0.633
**Condition**: Applied to SummEval consistency feature evaluation; compared against BertScore

**Evidence**: "the ROUGE score has a slightly higher sample-level accuracy (0.07) while having a higher average Favi-Score (0.339), and a much lower system level sign accuracy (0.633). We also note that the favoritism is more pronounced in the ROUGE score."

## [POSITIVE] One-vs-All Favi-Score per System
Computing Favi-Score for each system against all other systems individually and displaying as box plots to identify which systems are systematically favored or disfavored

**Delta**: Reveals M2M100 disfavoritism invisible in DAG rankings
**Condition**: Used as diagnostic tool for per-system favoritism analysis

**Evidence**: "The M2M100 system is also strongly disfavored. However, this is not visible from the DAGs alone, where it is ranked last, both according to COMET-22 and human judgements. This is a case where the Favi-Score uncovers a potentially undesired outcome that could go unnoticed otherwise."

## [POSITIVE] Complementary Use of Favi-Score and Sign Accuracy
Using Favi-Score alongside existing sign accuracy scores rather than replacing them, as they measure complementary properties of metric behavior

**Delta**: Metrics with low Favi-Score preserve correct ranking regardless of sign accuracy level
**Condition**: Recommended evaluation protocol for any automated preference metric

**Evidence**: "Metrics with a low Favi-Score will tend to preserve the correct ranking regardless of their sign-accuracy... we propose that preference-based metrics ought to be evaluated on both sign accuracy scores and favoritism."
