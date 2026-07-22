# Large Language Models are not Fair Evaluators

**Source**: https://aclanthology.org/2024.acl-long.511/

## [NEGATIVE] Vanilla LLM Evaluation (Conclusion-First Template)
Standard evaluation template where LLM outputs scores first, then provides explanation. Used as baseline in prior work (e.g., Vicuna benchmark).

**Delta**: GPT-4: 52.7% accuracy, kappa 0.24; ChatGPT: 44.4% accuracy, kappa 0.06
**Condition**: LLM-as-evaluator pairwise comparison; baseline condition

**Evidence**: "Compared to the commonly used VANILLA evaluation method, our proposed automatic calibration strategies (i.e., EC, MEC and BPC) significantly enhance the alignment between GPT-4 and ChatGPT with human judgments"

## [POSITIVE] Evidence Calibration (EC)
Modified evaluation template that requires the LLM to generate evaluation evidence/explanation first before assigning scores, leveraging the auto-regressive nature of causal language models.

**Delta**: GPT-4: 52.7% -> 56.5% accuracy, kappa 0.24 -> 0.29; ChatGPT: 44.4% -> 52.6% accuracy, kappa 0.06 -> 0.23
**Condition**: Single-sample evidence generation (k=1); both GPT-4 and ChatGPT as evaluators

**Evidence**: "we design an evidence calibration (EC) evaluation template T_EC(Q, R1, R2) that requires the model to generate the explanation (evaluation evidence) first and then give the score. In this way, the score can be calibrated with the evaluation evidence."

## [POSITIVE] Multiple Evidence Calibration (MEC)
Samples k evaluation results using the evidence calibration template and ensembles them to improve reliability and reduce positional bias.

**Delta**: GPT-4 MEC k=3: 58.7% accuracy, kappa 0.30; GPT-4 MEC k=6: 60.9% accuracy, kappa 0.33; ChatGPT MEC k=3: 53.2% accuracy, kappa 0.24; ChatGPT MEC k=6: 55.6% accuracy, kappa 0.27
**Condition**: Applied to both GPT-4 and ChatGPT; optimal k=3 balancing performance and cost

**Evidence**: "our proposed automatic calibration strategies (i.e., EC, MEC and BPC) significantly enhance the alignment between GPT-4 and ChatGPT with human judgments"

## [POSITIVE] Balanced Position Calibration (BPC)
Evaluates each candidate response in both positions (swapping order across two runs) and computes the final score as the average, directly counteracting positional bias.

**Delta**: GPT-4 MEC(k=3)+BPC(k=3): 62.5% accuracy, kappa 0.37; ChatGPT MEC(k=3)+BPC(k=3): 58.8% accuracy, kappa 0.31; ChatGPT accuracy improved by 14.3% over VANILLA
**Condition**: Combined with MEC; applied to both GPT-4 and ChatGPT evaluators

**Evidence**: "the accuracy is improved by 14.3%, and the kappa correlation coefficient is increased from 0.06 to 0.31"

## [POSITIVE] MEC+BPC vs. MEC alone (k=6)
Combining MEC(k=3) with BPC(k=3) versus simply increasing evidence samples to k=6 without position swapping.

**Delta**: GPT-4: MEC(k=3)+BPC(k=3) = 62.5% vs MEC(k=6) = 60.9%; ChatGPT: MEC(k=3)+BPC(k=3) = 58.8% vs MEC(k=6) = 55.6%
**Condition**: Comparison showing BPC adds value beyond simply increasing sample count

**Evidence**: "'MEC (k = 3) + BPC (k = 3)' outperforms 'MEC (k = 6)', demonstrating that LLMs are affected by positional bias, and BPC effectively ensures that LLMs serve as fair evaluators"

## [POSITIVE] Human-in-the-Loop Calibration (HITLC)
Uses BPDE score to identify the most likely biased evaluations and selectively incorporates human annotations only for those cases, combining automated and human evaluation.

**Delta**: GPT-4 with 20% human annotation: 73.8% accuracy, kappa 0.56; ChatGPT with 20% human annotation: 71.3% accuracy, kappa 0.52; reduces annotation cost by 39% (from $30 to $18.3)
**Condition**: Applied on top of MEC+BPC; β=20% threshold for human annotation selection

**Evidence**: "by incorporating just 20% (β = 20%) human assistance, ChatGPT attains comparable Human Average accuracy, while reducing the annotation cost from $30 to $18.3, a 39% reduction"

## [POSITIVE] Balanced Position Diversity Entropy (BPDE)
Entropy-based score computed from evaluation results of both MEC and BPC (across both position orderings) to identify examples most likely affected by positional bias for human review.

**Delta**: BPDE outperforms Vanilla Diversity Entropy and Random selection across all human annotation thresholds
**Condition**: Used within HITLC to select examples for human annotation; compared against random selection and single-position diversity entropy

**Evidence**: "BPDE outperforms Vanilla DE, which shows LLMs are sensitive to position exchange, and the results of BPC can significantly improve the performance of HITLC compared to relying solely on the results of MEC"

## [POSITIVE] Vanilla Diversity Entropy (single-position)
Entropy calculated using evaluation results from only one position ordering (without swapping), used as a baseline for BPDE comparison.

**Delta**: Outperforms random selection but underperforms BPDE
**Condition**: Baseline within HITLC; inferior to BPDE which uses both position orderings

**Evidence**: "Two Diversity Entropy methods outperform Random, showing the effectiveness of selecting examples based on the diversity entropy"

## [NEGATIVE] Random Example Selection for Human Annotation
Randomly selecting examples for human annotation in the HITLC framework, used as a baseline.

**Delta**: Underperforms both BPDE and Vanilla Diversity Entropy across all thresholds
**Condition**: Baseline for HITLC example selection strategy

**Evidence**: "Two Diversity Entropy methods outperform Random, showing the effectiveness of selecting examples based on the diversity entropy"

## [NEGATIVE] Low Sampling Temperature (t=0.2) for MEC
Using a very low temperature when sampling multiple evidence calibration results.

**Delta**: Sub-optimal evaluation alignment compared to t=0.6 or t=1.0
**Condition**: MEC strategy with ChatGPT as evaluator

**Evidence**: "both low temperature (i.e., 0.2) and high temperature (i.e., 1.4) result in sub-optimal evaluation alignment. We believe that low temperature eliminates the randomness of sampling, weakening the effect of MEC"

## [NEGATIVE] High Sampling Temperature (t=1.4) for MEC
Using a very high temperature when sampling multiple evidence calibration results.

**Delta**: Sub-optimal evaluation alignment compared to t=0.6 or t=1.0
**Condition**: MEC strategy with ChatGPT as evaluator

**Evidence**: "both low temperature (i.e., 0.2) and high temperature (i.e., 1.4) result in sub-optimal evaluation alignment... high temperature compromises the quality of generation results, leading to poor performance"

## [POSITIVE] Optimal Sampling Temperature (t=0.6 or t=1.0) for MEC
Using a moderate temperature for sampling in MEC to balance randomness and generation quality.

**Delta**: Best evaluation alignment among tested temperatures
**Condition**: MEC strategy with ChatGPT as evaluator

**Evidence**: "it is crucial to select an appropriate temperature (e.g., 0.6 or 1.0 in our experiments) for the LLM evaluators"

## [NEUTRAL] Increasing Evidence Count k beyond 3
Increasing the number of sampled evidence results beyond k=3 in MEC.

**Delta**: Performance increases then plateaus or slightly decreases; k=3 identified as optimal
**Condition**: MEC strategy with ChatGPT as evaluator; k values of 1, 3, 5, 7 tested

**Evidence**: "The model's performance increases and then tends to be constant or decreases slightly as k becomes larger. Despite the slight decrease, the enhancement of the model effect by the MCE strategy is still significant"

## [NEGATIVE] Positional Bias Instruction in Prompt
Adding explicit instruction in the evaluation prompt telling the LLM to ensure response order does not affect judgment.

**Delta**: Does not prevent positional bias; conflict rates remain high (e.g., 82.5% for ChatGPT)
**Condition**: Applied to standard Vicuna evaluation template; tested with GPT-4 and ChatGPT

**Evidence**: "Simply changing the order of candidate responses leads to overturned comparison results, even though we add the command 'ensuring that the order in which the responses were presented does not affect your judgment' into the prompt."

## [NEUTRAL] Comparing Template vs. Scoring Template
Using a direct pairwise comparison template (outputting win/tie/lose) instead of a numerical scoring template.

**Delta**: COMPARING VANILLA: 50.2% accuracy vs SCORING VANILLA: 44.4%; both benefit similarly from MEC and BPC calibration
**Condition**: ChatGPT as evaluator; both templates show significant improvement with calibration methods

**Evidence**: "Our proposed methods are applicable to both of these templates, leading to enhanced accuracy and a heightened correlation coefficient for ChatGPT"

## [NEGATIVE] Positional Bias Effect on Close-Quality Responses
The degree of positional bias is stronger when the quality difference between two responses is small.

**Delta**: Score gap ≤1: high conflict rate; score gap ≥3: relatively stable evaluation results
**Condition**: GPT-4 as evaluator; analysis of conflict rate vs. score gap

**Evidence**: "when the score difference between the two responses is small (e.g., score gap ≤ 1), the evaluation results of GPT-4 are significantly affected by the position of the responses. On the other hand, when the score difference between the two responses is large (e.g., score gap ≥ 3), GPT-4's evaluation results are relatively stable."
