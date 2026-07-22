# Whose Preferences? Differences in Fairness Preferences and Their Impact on the Fairness of AI Utilizing Human Feedback

**Source**: https://aclanthology.org/2024.acl-long.509/

## [POSITIVE] Unlikeability-based sentence pair selection
Selecting sentence pairs with the highest unlikeability coefficients (a measure of variability in categorical responses) to focus on contentious fairness judgments

**Delta**: median unlikeability increased from 0.198 in Do to 0.558 in Dn for personal opinion
**Condition**: Dataset construction for studying disagreements in fairness preferences

**Evidence**: "As our new dataset Dn contains the sentence pairs from Do with the highest unalikeability coefficients, we expect increased variability in responses. Indeed, while Do had an overall median unalikeability of 0.198 for both personal opinion and predictions of the average American opinion, Dn reached a median of 0.558 and 0.481 respectively."

## [POSITIVE] Label binarization
Aggregating annotation options 2, 3, and 4 into a single 'Not Unfair' label to address class imbalance and ensure enough samples per class

**Delta**: enables robust statistical analysis and classifier training
**Condition**: Statistical analysis and classifier training with imbalanced annotation data

**Evidence**: "We often binarize our labels by aggregating options 2, 3, and 4 to ensure each considered class contains enough labels for both learning and statistical analysis."

## [POSITIVE] Using all annotations instead of majority vote for training
Training classifiers using all individual annotations rather than aggregating them into a majority vote label

**Delta**: majority vote classifiers performed worse
**Condition**: Training BERT-based classifiers to predict fairness preferences

**Evidence**: "Instead of aggregating individual annotations (e.g. into majority vote) in the training set, we used all the annotations for training the classifiers (Wei et al., 2023). In Appendix E, we discuss that the accuracy of classifiers trained with only majority vote was worse and that was the reason for using all annotations for training."

## [POSITIVE] Supplementing Dn with Do for classifier training
Combining the new high-unlikeability dataset Dn with the prior dataset Do to provide sufficient training data for classifiers

**Delta**: Dn alone did not beat random baseline; combined dataset enabled meaningful classifier training
**Condition**: Training downstream fairness preference classifiers

**Evidence**: "As Dn was specifically selected to only include sentence pairs with high unalikeability coefficients, which are plausibly particularly hard to classify, we found that Dn alone was not sufficient for training classifiers that clearly beat the random baseline. Correspondingly, we decided to supplement Dn with all sentence pairs from Do."

## [POSITIVE] Demographic-stratified classifier training
Training separate BERT-based classifiers on annotation subsets grouped by annotator demographic categories (gender, race, age, politics)

**Delta**: statistically significant differences in balanced accuracy across demographic training sets (gender P<.05, race P<.001, age P<.001)
**Condition**: Studying the effect of annotator demographics on downstream ML models

**Evidence**: "pairwise Kolmogorov-Smirnov tests comparing the population of trained models ϕκ ϕκ′ for different demographics κ and κ′ in terms of balanced accuracy on the control test set yield statistically significant differences for gender (P < .05), race (P < .001), and age (P < .001)."

## [POSITIVE] Ensemble classifier with equal demographic weighting
Aggregating predictions from classifiers trained on different demographic groups via majority voting, giving equal weight to each demographic group rather than each annotation

**Delta**: significant improvement for 9 out of 24 demographic intersections; control model had 0 significant improvements; coarse demographics showed improvement in 8 out of 9 categories
**Condition**: Predicting fairness preferences for underrepresented demographic intersections

**Evidence**: "The ensemble classifier ϕ¯ provides significantly better (p<0.05) results for 9 out of 24 demographic intersections while the Control model did not provide significantly higher scores for any demographic intersection (and non-significantly better results for 5 out of 24 intersections)."

## [POSITIVE] Ensemble improvement for smallest demographic intersections
The ensemble classifier providing disproportionate gains for the smallest and most underrepresented demographic intersections

**Delta**: +10 percentage points balanced accuracy for Non-White, older, Republican women
**Condition**: Demographic intersections with very few annotators in training data

**Evidence**: "while our approach provides much better scores for our smallest demographic intersection (Non-White, older, Republican women), improving its balanced accuracy score by more than 10 percentage points, we also observe a performance improvement for White, older, Democrat women (our largest demographic intersection)."

## [POSITIVE] Threshold optimization on demographic-specific validation sets
Optimizing the classification threshold for each model on the validation set of the target demographic to maximize balanced accuracy for that group

**Delta**: enables fair cross-demographic evaluation
**Condition**: Cross-demographic evaluation of fairness preference classifiers

**Evidence**: "in order to account for label imbalances, we optimized the classification threshold used by ϕκi on Dival(κ′) to maximize the models' balanced accuracy (sklearn, 2007) on the demographic κ′."

## [POSITIVE] Logistic regression for demographic effect analysis
Using logistic regression with all demographic variables as predictors to estimate odds ratios for fairness label outcomes per demographic group

**Delta**: significant effects found for age (P<.001), politics (P<.001), education (P<.001) on personal opinion; all demographics except gender significant for average American opinion
**Condition**: Analyzing the influence of annotator demographics on fairness preferences

**Evidence**: "We observe significant effects of age, politics, and education on annotators' personal fairness judgments, and significant effects of all considered demographic variables except for gender on the predicted average American's opinion."

## [NEUTRAL] Bonferroni correction for multiple hypothesis testing
Applying Bonferroni's correction to all reported p-values to account for multiple hypothesis testing

**Delta**: controls false positive rate in significance testing
**Condition**: Statistical significance testing across multiple demographic variables

**Evidence**: "We account for multiple hypothesis testing using Bonferroni's correction (Armstrong, 2014) in all reported p-values."

## [NEGATIVE] MTurk qualification filter
Adding a qualification test requiring workers to correctly answer two multiple-choice questions before accessing the survey to filter out bots and low-effort workers

**Delta**: approval rate increased from 28% to 65% but data collection speed dropped dramatically (4 hours for 500 submissions vs. 3 weeks for 203 submissions)
**Condition**: MTurk data collection quality control

**Evidence**: "While the first 500 submissions -regardless of their quality or approval rate- were collected in a lapse of 4 hours, we required approximately 3 weeks to collect 203 more participations once the Qualification was installed. Such a filter increased the quality of the responses drastically, raising to a 65% approval rate instead of the original 28%."

## [NEUTRAL] Dual-platform data collection (MTurk + Prolific)
Collecting annotations from both Amazon Mechanical Turk and Prolific, then merging datasets due to similar demographic distributions and unlikeability coefficients

**Delta**: similar demographic distributions and unlikeability coefficients across platforms
**Condition**: Crowdsourced data collection for fairness preference annotations

**Evidence**: "As the demographic distributions and unalikeability coefficients among the labels collected on MTurk and Prolific were very similar to each other, we merged them into one large dataset (henceforth referred to as Dn)."

## [POSITIVE] Asking for both personal opinion and average American prediction
Eliciting two types of judgments from each annotator: their personal fairness opinion and their prediction of what the average American would think

**Delta**: stronger demographic effects found for average American predictions than personal opinions
**Condition**: Eliciting fairness preferences in crowdsourcing survey

**Evidence**: "We generally obtain more significant results (i.e. lower p-values) for the prediction of average American's opinion compared to annotators' personal judgments. Thus, we have stronger evidence that their demographics affect annotators' perception of the average American's judgment rather than their own judgments."

## [POSITIVE] Pre-trained BERT-based classifier
Using pre-trained multi-headed BERT models fine-tuned on fairness preference annotations to predict fairness judgments

**Delta**: classifiers trained on different demographic subsets show statistically significant performance differences
**Condition**: Training downstream models to predict human fairness preferences

**Evidence**: "we fitted pre-trained multiheaded BERT based classifiers (Devlin et al., 2019) building upon the code by Dorner et al., 2022."

## [POSITIVE] Manual filtering of low-quality sentence pairs
Manually removing sentence pairs where the original and modified sentences are not semantically similar before selecting high-unlikeability pairs

**Delta**: improves dataset quality by removing incoherent or factually incorrect pairs
**Condition**: Dataset construction and quality control

**Evidence**: "After manually filtering out low quality pairs, for which the original and modified sentences s and s′ are not semantically similar, we collect labels for the 1500 sentence pairs with the largest unlikeability"

## [POSITIVE] Equal category representation per annotator
Ensuring each annotator saw an equal number of comment pairs from each focus category (Gender, Race, Religion, Mixed)

**Delta**: controls for category exposure bias across annotators
**Condition**: Survey design for crowdsourced annotation collection

**Evidence**: "The sentence pairs shown to annotators were split, such that each annotator saw an equal number of comment pairs from each category."
