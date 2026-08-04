# Watermark Stealing in Large Language Models

**Source**: https://proceedings.mlr.press/v235/jovanovic24a.html

## [POSITIVE] Watermark Stealing via API Querying
Querying the watermarked LLM API with a set of prompts to build an approximate model of the secret watermarking rules (scoring function s*) by analyzing token frequency differences between watermarked and base distributions

**Delta**: over 80% spoofing and scrubbing success rate for under $50
**Condition**: Applied to distribution-modifying watermarking schemes (KGW2-SELFHASH, KGW-SOFT, UNIGRAM, KGW2-SUM) in blackbox API access setting

**Evidence**: "We show that for a one-time query cost of below $50, the attacker can reliably produce arbitrarily many natural-looking texts that are detected as watermarked with over 80% success rate."

## [POSITIVE] Partial Context Score Utilization
Supplementing the full 3-gram context score s(T, {T1,T2,T3}) with partial context scores s(T, {Ti,Tj}), s(T, {Ti}), and s(T, {}) to address sparsity of full-context observations, weighted by w1=0.5 and w2=0.25

**Delta**: from below 50% to ~80% average spoofing success at n=30,000 queries
**Condition**: Ablation study on KGW2-SELFHASH spoofing; partial contexts are especially useful for schemes using min-aggregation like KGW2-SELFHASH

**Evidence**: "We see that this significantly degrades the attack, reducing the average success from around 80% to below 50% for n=30,000 queries, validating our algorithmic choices."

## [POSITIVE] Dominant Context Token Heuristic (T_min identification)
Identifying the token with minimal hash value among the 3-gram context tokens to determine which partial context score carries the same signal as the full context score, exploiting the min-aggregation property of KGW2-SELFHASH

**Delta**: contributes to overall ~80% attack success (part of partial context improvement)
**Condition**: Specific to KGW2-SELFHASH and schemes using min-aggregation in PRF seeding

**Evidence**: "We first leverage the above observation by using the following heuristic to determine T_min, the token with minimal hash value among T1, T2, and T3... smaller hash values of a token lead to more informative partial context scores, as those more often use the same V_green as the corresponding scores for the full context."

## [POSITIVE] Context-Independent Distribution Score
Adding s(T, {}) (context-independent score) to the unified score to account for cases where T itself is minimal in the PRF seed, exploiting the self-seeding property of KGW2-SELFHASH

**Delta**: part of the combined improvement from below 50% to ~80% (w2=0.25 weight)
**Condition**: Specific to self-seeding schemes like KGW2-SELFHASH

**Evidence**: "We also account for cases where T is minimal in Eq. (1), i.e., V_green depends only on T. This implies that tokens that have small H(T) and are members of their corresponding V_green will generally appear more often, so we add s(T, {}) to our unified score."

## [POSITIVE] Logit Promotion for Spoofing (positive delta_att)
Modifying the auxiliary LM's logit vector at each generation step to promote tokens proportionally to their stolen watermark scores s*, increasing likelihood of generating green tokens

**Delta**: over 80% FPR* @1e-3 spoofing success across multiple model pairs
**Condition**: Spoofing attacks on all tested distribution-modifying watermarking schemes

**Evidence**: "To mount a spoofing attack, our attacker modifies the text generation procedure of LM_att to promote tokens proportionally to their scores s*, as high-scoring tokens are estimated more likely to be 'green' in the given context... we modify the logit vector l such that for each candidate token T we have [logit modification with delta_att > 0]."

## [POSITIVE] Logit Demotion for Scrubbing (negative delta_att)
Using the same stolen scoring function s* but with delta_att < 0 to demote green tokens during paraphrasing, reducing watermark strength in the output text

**Delta**: DIPPER scrubbing boosted from ~0-2% to over 80% FNR* @1e-3 on KGW2-SELFHASH
**Condition**: Scrubbing attacks on long texts (>1000 tokens) with KGW2-SELFHASH; also effective on UNIGRAM, KGW-SOFT, KGW2-SUM

**Evidence**: "To mount a scrubbing attack, our attacker uses the same procedure as above, setting delta_att < 0 to demote tokens based on their score under s*, i.e., make it less likely to output tokens that strengthen the watermark... our attacker can use the result of stealing (s*) to significantly boost the success of DIPPER, from around 0 to above 80% on average."

## [POSITIVE] Duplicate N-gram Penalty
Penalizing tokens that would complete a duplicate (h+1)-gram by dividing their logit by parameter rho_att, since duplicate contexts cannot contribute new green tokens but increase text length, reducing effective watermark strength

**Delta**: contributes to overall spoofing success (no isolated ablation reported)
**Condition**: Spoofing attacks on schemes that ignore duplicate n-grams in detection

**Evidence**: "Additionally, for schemes that ignore duplicate (h+1)-grams in detection, we penalize each T that would complete a duplicate by dividing lT by another parameter rho_att ∈ R before adding s*. The intuition behind this is that outputting duplicates has no chance to produce a green token yet prolongs the text, effectively reducing the watermark strength."

## [POSITIVE] Permutation-Invariant Context Modeling
Ignoring token ordering within context sets when estimating conditional distributions, treating {T1,T2,T3} as a set rather than ordered sequence, to improve sample efficiency given the permutation-invariant PRF seeding in target schemes

**Delta**: improves sample efficiency (no isolated quantitative delta reported)
**Condition**: All distribution-modifying watermarking schemes with permutation-invariant PRF seeding

**Evidence**: "As the value seeding the PRF (e.g., Eq. (1)) is permutation-invariant in all prominent schemes of our class, we ignore ordering within ctx to improve sample efficiency."

## [NEUTRAL] Score Clipping and Linear Rescaling Normalization
Normalizing raw token scores to [0,1] by clipping at threshold c=2 to limit outlier influence, followed by linear rescaling

**Delta**: more elaborate normalization may improve results further (no quantitative delta reported)
**Condition**: Applied uniformly in all experiments with c=2; noted as potentially suboptimal

**Evidence**: "The score is normalized to [0,1] by clipping at c to limit the influence of outliers, followed by linear rescaling—more elaborate normalization may improve our results further."

## [POSITIVE] Sparse Context Score Discarding
Setting s(T, ctx) to 0 when the underlying empirical estimates were computed on very few token occurrences, representing lack of reliable evidence rather than belief that token is red

**Delta**: part of sparsity challenge mitigation enabling overall ~80% attack success
**Condition**: Full context (size-3) scores for KGW2-SELFHASH where Θ(|V|^3) possible contexts cause sparsity

**Evidence**: "we explicitly discard the signal in cases when the underlying estimates p_hat_w(T|ctx) and p_hat_b(T|ctx) were computed on a very small number of token occurrences, by setting s(T,ctx) to 0. Note that this represents the lack of reliable evidence that T is green, but not necessarily a belief that it will be red."

## [NEUTRAL] Auxiliary Model as Base Distribution Estimator (B0 setting)
Using the attacker's own auxiliary LM (LM_att) to estimate the non-watermarked base distribution p_hat_b when non-watermarked responses from LM_mo are unavailable, instead of using actual LM_mo base responses

**Delta**: divergence between LMs does not notably affect downstream attack success (App. B)
**Condition**: Most restrictive (B0, D0) threat model setting; relaxing to B1 (available base responses) does not significantly improve results

**Evidence**: "in the more restrictive unavailable base responses setting (our focus in Sec. 6) we prompt the attacker's auxiliary model LM_att with x_1:n. As we show in App. B, the divergence between the LMs used for p_hat_w and p_hat_b does not notably affect the success of downstream attacks."

## [POSITIVE] Top-1 Selection with Detector Access (D1 setting)
Selecting the best of 5 generated responses using detector API feedback to identify the most strongly watermarked (for spoofing) or least watermarked (for scrubbing) output

**Delta**: boosts spoofing success to almost 100%
**Condition**: D1 threat model setting where attacker has binary detector API access

**Evidence**: "In App. B.1 we show that considering top-1 out of 5 generated responses (viable in the (D1) setting) can further boost our results to almost 100%."

## [POSITIVE] Large Query Budget (n=30,000)
Using 30,000 API queries to build the watermark model, costing ~$42 at ChatGPT API prices

**Delta**: curves converge at ~10,000 queries; $42 total cost for full attack capability
**Condition**: One-time stealing cost; attack remains effective with fewer queries but with reduced success rates

**Evidence**: "We obtain n=30,000 responses of token length ≤800... we use n=30,000 queries, resulting in a cost of only $42 assuming current ChatGPT API prices... around 10,000 queries the curves converge to our results from Table 1."

## [NEGATIVE] KGW2-SUM Scheme (larger context with sum aggregation)
Using h=3 context with sum aggregation instead of min aggregation, creating more distinct red/green splits that are harder to reverse-engineer

**Delta**: spoofing success reduced to ~54-63% vs ~80%+ for KGW2-SELFHASH
**Condition**: Spoofing attacks; KGW2-SUM is harder to spoof but easier to scrub without stealing knowledge

**Evidence**: "Confirming prior intuition (see Sec. 2), KGW2-SUM is harder to spoof, even more so as some of our attack's key features are aimed specifically at KGW2-SELFHASH. Despite this, over 50% of attacker's texts are valid spoofs."

## [NEGATIVE] DIPPER Paraphraser Baseline (no stealing)
Using DIPPER paraphraser alone without watermark stealing augmentation as a scrubbing baseline

**Delta**: ~0-2% FNR* @1e-3 on KGW2-SELFHASH long texts
**Condition**: Scrubbing long texts (>1000 tokens) with KGW2-SELFHASH; DIPPER alone is insufficient

**Evidence**: "In Table 3 we see that our attacker can use the result of stealing (s*) to significantly boost the success of DIPPER, from around 0 to above 80% on average... the best of which can not achieve more than 30% on average."

## [NEGATIVE] Recursive DIPPER Baseline
Applying DIPPER paraphraser recursively for 5 rounds as a scrubbing baseline without watermark stealing

**Delta**: at most ~30% FNR* @1e-3, far below the 80%+ achieved with stealing
**Condition**: Scrubbing KGW2-SELFHASH long texts; all baselines including recursive DIPPER fail to reach 25% average

**Evidence**: "Beyond DIPPER, we include the PEGASUS paraphraser (that we also boost with our method), paraphrasing with CHATGPT, and a recursive variant of DIPPER (Sadasivan et al., 2023) with 5 paraphrasing rounds... the best of which can not achieve more than 30% on average, with median p-values several orders of magnitude below ours."

## [POSITIVE] PEGASUS Paraphraser Boosted with Stealing
Augmenting PEGASUS paraphraser with stolen watermark scores s* to demote green tokens during paraphrasing

**Delta**: from at best 15% to 84% FNR* @1e-3 on KGW2-SELFHASH
**Condition**: Scrubbing KGW2-SELFHASH; less effective than DIPPER+stealing but still substantial improvement

**Evidence**: "While boosting PEGASUS is not as effective, it is a significant improvement over the baseline (at best 15% to 84%)."

## [POSITIVE] Watermark Stealing for Paraphrase-based Spoofing
Using DIPPER paraphraser augmented with stolen scores to imprint a watermark on an existing non-watermarked text while preserving its content

**Delta**: ≥74% spoofing success at FPR of 1e-3
**Condition**: Spoofing via paraphrasing existing non-watermarked text; applicable to KGW2-SELFHASH and KGW-SOFT

**Evidence**: "we explore a variant of the spoofing attack, where the attacker uses the DIPPER paraphraser to imprint the watermark on a given non-watermarked text. Across several scenarios on KGW2-SELFHASH and KGW-SOFT we achieve ≥74% spoofing success at expected FPR of 10^-3."

## [NEUTRAL] Low FPR Evaluation Threshold (f=1e-3)
Evaluating watermark detection at very low false positive rate (FPR=1e-3) rather than high FPR or ROC-AUC, to reflect realistic deployment conditions where false positive costs are high

**Delta**: many prior works evaluated at higher FPR, potentially overestimating watermark robustness
**Condition**: Evaluation methodology choice; stricter than most prior work, reveals vulnerabilities not apparent at higher FPR

**Evidence**: "In all our experiments, we set f ≤ 10^-3, arguing that this represents the practical watermarking setup, where costs of false positives are very high... we find that many works mainly evaluate watermarks on high FPR values or average-case metrics (ROC-AUC), which may not well reflect the way watermarks would be deployed."

## [NEUTRAL] GPT-4 as Text Quality Judge
Using GPT-4 to evaluate attacker-generated text quality on accuracy, consistency, and style (scale 1-10), filtering out low-quality texts (score below 6.5) from attack success metrics

**Delta**: ensures reported success rates reflect only high-quality attacks (no quality-success tradeoff reported)
**Condition**: Spoofing attack evaluation; ensures practical relevance of reported success rates

**Evidence**: "we consider spoofing unsuccessful if the attacker generates responses poorly rated by GPT4 as a judge of accuracy, consistency, and style on a scale of 1 to 10. Similar approaches were shown to be viable as a proxy for human preference."

## [NEGATIVE] KGW-HARD Scheme Exclusion from Scrubbing
KGW-HARD prevents LM from using red tokens entirely, which harms text quality and makes it unable to consistently produce high-quality watermarked texts as scrubbing targets

**Delta**: excluded from scrubbing experiments due to inability to produce consistent high-quality targets
**Condition**: KGW-HARD watermarking scheme; acknowledged as impractical in original paper as well

**Evidence**: "We exclude KGW-HARD as it is unable to consistently produce high-quality watermarked texts as scrubbing targets."

## [POSITIVE] Multiple Secret Keys Robustness Test
Testing whether spoofing remains successful when the model owner uses multiple secret keys (rotating or per-user keys) as a potential mitigation

**Delta**: spoofing success remains consistent across key variations (App. B.2, C)
**Condition**: Potential mitigation scenario; stealing still effective against multiple-key deployments

**Evidence**: "In App. B.2 we further show that our results stay consistent when varying the secret key ξ of the model owner... we present an additional experiment that demonstrates spoofing success even when the server uses multiple secret keys."
