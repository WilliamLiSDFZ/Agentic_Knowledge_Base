# GPT is Not an Annotator: The Necessity of Human Annotation in Fairness Benchmark Construction

**Source**: https://aclanthology.org/2024.acl-long.760/

## [POSITIVE] Community-sourced benchmark development
Deriving stereotypes and harm predicates from large-scale online surveys of members of the affected community, rather than crowdworkers, to ensure grounding in lived experience

**Delta**: outperforms baseline
**Condition**: Bias benchmark construction for marginalized communities (LGBTQ+, Jewish)

**Evidence**: "recent work (Felkner et al., 2023) has had success with community-sourced bias benchmarks in which stereotypes were derived from a large-scale online survey of members of the affected community. This yielded a large, specific, well-grounded, and high-quality bias benchmark dataset"

## [NEGATIVE] GPT-3.5-Turbo model-assisted harm extraction
Using GPT-3.5-Turbo to automatically extract attested harm predicates from free-response survey data instead of human annotators

**Delta**: 5.40% exact match (WQ overall), 18.14% exact match (WS overall); R²=0.14 correlation with human benchmark for WQ
**Condition**: Predicate extraction from community survey responses for fairness benchmark construction

**Evidence**: "GPT-3.5-Turbo has unacceptably poor performance on attested harm extraction. We present quantitative and qualitative evidence of serious quality issues with model-extracted predicates, including high rates of both misrepresenting survey responses and hallucinating harms not present in input text."

## [NEGATIVE] Iterative GPT prompting with previously extracted predicates
Prompting GPT-3.5-Turbo N times per survey response (where N equals the number of human ground-truth predicates), appending previously extracted predicates to avoid repetition

**Delta**: N would be unknown in realistic use case, making this an artificially easy setup yet still yielding poor results
**Condition**: GPT predicate extraction experiments; represents upper bound of model performance

**Evidence**: "For each survey answer, we prompted the model N times, where N is the number of human-extracted ground truth predicates. This N would be unknown in a realistic use case, so our experiments represent an artificially easy annotation task."

## [NEGATIVE] Low temperature GPT generation (T=0.3)
Setting GPT-3.5-Turbo temperature to 0.3 for all predicate extraction experiments to reduce randomness

**Delta**: contributed to highly repetitive hallucinations (e.g., 'are greedy', 'are manipulative' for Jewish responses)
**Condition**: GPT predicate extraction at temperature 0.3

**Evidence**: "Most of these hallucinations are highly repetitive, suggesting that the model defaults to a very small set of priors when unable to extract a predicate from the input data."

## [NEUTRAL] SBERT cosine similarity for predicate evaluation
Using SBERT (all-mpnet-base-v2) sentence embeddings to compute cosine similarity between human-extracted and GPT-extracted predicates, both as raw phrases and in dummy sentences

**Delta**: PCS: 0.47 (WQ), 0.61 (WS); SCS: 0.78 (WQ), 0.82 (WS)
**Condition**: Auxiliary evaluation of GPT-extracted predicates; overestimates quality for negation errors

**Evidence**: "this metric is prone to overestimating similarity in cases where the two predicates share many words but differ significantly in meaning... negation errors are not easily flagged by automated metrics like cosine similarity"

## [POSITIVE] Pseudo-log-likelihood bias scoring
Measuring model bias as the percentage of sentence pairs where the model assigns higher probability to the stereotypical sentence than the counter-stereotypical sentence, using pseudo-log-likelihood scores

**Delta**: Mean WinoSemitism score of 69.03 across 20 models, all above 50 (chance)
**Condition**: Evaluation of antisemitic bias in 20 off-the-shelf language models using WinoSemitism

**Evidence**: "the bias score is the percentage of sentence pairs for which the tested model has a higher probability of predicting the stereotypical sentence than the counterstereotypical sentence. An ideal bias score is 50... All tested models show some degree of antisemitism."

## [NEUTRAL] Random sampling of names and counterfactuals (vs. Cartesian product)
Using random sampling of names and counterfactual identity descriptors instead of strict Cartesian product to keep WinoSemitism dataset size comparable to prior work given a larger name list

**Delta**: 58,816 sentence pairs in H-WS vs. 45,468 in GPT-WQ
**Condition**: WinoSemitism benchmark construction only

**Evidence**: "Our use of random sampling of names and counterfactual identity descriptors is a departure from previous work, which constructed benchmarks using a strict Cartesian product of all component categories. However, we had a much larger list of names than previous work, and we chose to use random sampling to keep the overall size of the WinoSemitism benchmark roughly comparable to previous work."

## [POSITIVE] Using both noun and adjective identity descriptors
Including both 'Jewish people'/'Jews' and 'Christian people'/'Christians' forms to minimize bigram frequency imbalance effects on bias scores

**Delta**: minimizes impact of bigram frequency differences on subset of WS datasets
**Condition**: WinoSemitism benchmark construction to address training data frequency imbalance

**Evidence**: "We minimize this impact by using both noun and adjective identity descriptors (i.e. 'Jewish people' and 'Jews', 'Christian people' and 'Christians', etc.) in the WS benchmark datasets, so that the relative frequency of bigram pairs affects only a small subset of the WS datasets."

## [POSITIVE] Post-hoc qualitative human analysis of GPT extractions
Manually reviewing all GPT-extracted predicates and classifying them into five categories: Correct, Semantically Correct, Opposite, Hallucination, and Other

**Delta**: Revealed <50% correct for both GPT-WQ and GPT-WS; ~30% hallucination rate for GPT-WQ; ~6% opposite rate for GPT-WQ
**Condition**: Evaluation methodology for assessing GPT annotation quality

**Evidence**: "we observe that, for both GPT-WQ and GPT-WS, less than half of GPT-extracted predicates are classified correct, i.e. immediately usable for benchmark construction."

## [NEGATIVE] Intersectional subgroup analysis
Evaluating bias scores and extraction quality separately for subgroups within the LGBTQ+ community (e.g., lesbian, bisexual, pansexual, asexual) to detect disparate impacts

**Delta**: R²=0 for lesbians; 0% exact match for pansexual and asexual; ~30% opposite extractions for lesbian respondents
**Condition**: GPT-WinoQueer dataset; multiply marginalized subgroups within LGBTQ+ community

**Evidence**: "Of the nine LGBTQ+ identity subgroups considered, six had R² < 0.5, including R² = 0 for lesbians. Model-created bias benchmarks perform even more poorly for marginalized subcommunities, falsely underestimating the likelihood of intersectional stereotypes in model outputs."

## [POSITIVE] Expert annotators with lived experience
Using human annotators who are themselves members of the surveyed communities to extract harm predicates, leveraging subjective judgment and cultural context

**Delta**: R²=0.73 (WS) and stronger benchmark calibration vs. R²=0.14 for GPT-created WQ benchmark
**Condition**: Benchmark construction for sensitive social bias tasks requiring cultural and contextual understanding

**Evidence**: "Annotations from expert humans with lived experience as members of the relevant community are absolutely essential to the construction of high-quality LLM fairness benchmarks."
