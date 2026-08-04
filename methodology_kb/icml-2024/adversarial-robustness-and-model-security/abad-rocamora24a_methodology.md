# Revisiting Character-level Adversarial Attacks for Language Models

**Source**: https://proceedings.mlr.press/v235/abad-rocamora24a.html

## [POSITIVE] Greedy Character Perturbation Selection
At each iteration, Charmer greedily selects the single-character perturbation (replacement, insertion, or deletion) with the highest loss, rather than exhaustively searching all combinations.

**Delta**: >95% ASR in every studied TextAttack benchmark
**Condition**: Applied across all benchmarks including BERT, RoBERTa, Llama 2, and Vicuna

**Evidence**: "Our attack is able to achieve >95% ASR (Attack success rate) in every studied TextAttack benchmark and LLMs Llama-2 and Vicuna, obtaining up to a 23%-point ASR improvement with respect to the runner-up method."

## [POSITIVE] Top-n Position Pre-selection (Algorithm 1)
A heuristic that selects the top-n most important positions by replacing each character with a test character (whitespace) and measuring the change in loss, reducing the search space from O(|S|) to n positions.

**Delta**: Greatly improves ASR over random selection for all studied n, with only ~0.25s additional runtime
**Condition**: Applied during position selection phase; evaluated on BERT SST-2 at k=1

**Evidence**: "When compared with the random position selection, our method greatly improves the ASR for all the studied n, while introducing a minor time increase of 0.25 seconds on average."

## [POSITIVE] n=20 Candidate Positions
Setting the number of candidate positions n to 20 as a balance between ASR and runtime efficiency.

**Delta**: ASR increase less noticeable for n>20, making n=20 the optimal trade-off
**Condition**: Standard Charmer configuration for most benchmarks

**Evidence**: "In Fig. 2, we can observe that the ASR consistently grows when increasing the number of candidate positions. However, the increase is less noticeable for n>20, therefore, the increase in runtime does not pay off the increase in ASR. This leads us to choose n=20 for the rest of our experiments."

## [NEGATIVE] Charmer-Fast (n=1)
A faster variant of Charmer that uses only n=1 candidate position, trading attack quality for speed.

**Delta**: Higher d_lev and lower ASR compared to full Charmer
**Condition**: When speed is prioritized over attack quality; also used for LLM attacks due to inference cost

**Evidence**: "If speed is preferred to adversarial example quality, we can set n=1 (Charmer-Fast), which attains a runtime closer to DeepWordBug at the cost of a higher d_lev and lower ASR."

## [POSITIVE] Levenshtein Distance Constraint
Constraining adversarial perturbations using Levenshtein (edit) distance to ensure semantics-preserving and imperceptible adversarial examples.

**Delta**: Charmer achieves lowest d_lev among competitive methods while maintaining highest ASR; e.g., d_lev of 1.47 on SST-2 BERT vs 17.17 for TextFooler
**Condition**: Applied across all character-level attack experiments

**Evidence**: "our method obtains the lowest Levenshtein distance (d_lev). Regarding the similarity (Sim), our Charmer attains the highest or runner up similarity in 8/10 cases, proving its ability to generate highly similar adversarial examples."

## [POSITIVE] Carlini-Wagner Loss (unclipped)
Using the Carlini-Wagner loss for attack optimization, without clipping the value to 0 at maximum (unlike the original formulation), to handle cases where loss is positive for different adversarial examples.

**Delta**: Enables handling of cases where loss is positive for different adversarial examples
**Condition**: Used in both classifier and LLM attack formulations

**Evidence**: "In the original paper, Carlini & Wagner (2017) clip the value of the loss to be 0 at maximum. We do not clip in order to deal with cases where the loss is positive for different adversarial examples."

## [POSITIVE] Expansion-Contraction Operator for Insertions/Deletions
Using expansion (phi) and contraction (psi) operators to unify character insertions, deletions, and replacements into a single replacement operation on an expanded sentence, enabling a unified search over all edit operations.

**Delta**: Enables character insertions and deletions in addition to replacements, unlike prior work (Yang et al., 2020) which only considered replacements
**Condition**: Core algorithmic component of Charmer

**Evidence**: "Similarly to (Yang et al., 2020), our method measures the importance of every position plus insertions. After a perturbation is done, importances are updated to consider the interaction between perturbations."

## [POSITIVE] Iterative Perturbation with Importance Update
After each perturbation step, the importance of positions is recomputed to account for interactions between perturbations, unlike methods that compute importance only once.

**Delta**: Outperforms prior art by 4.84% ASR and 8% USE similarity on BERT SST-2
**Condition**: Applied during multi-step attack (k>1)

**Evidence**: "After a perturbation is done, importances are updated to consider the interaction between perturbations... Charmer improves the ASR in 4.84% points and the USE similarity in 8% points with respect to the previous art."

## [POSITIVE] Token-level Pre-filtering for LLM Attacks
For LLM attacks, first tokenizing the input and masking each token to find the most important token, then applying Algorithm 1 only within positions of those important tokens, to reduce the number of forward passes.

**Delta**: Enables practical attack on LLMs achieving >93% ASR across benchmarks
**Condition**: Applied specifically for LLM (Llama 2, Vicuna) attacks where inference is costly

**Evidence**: "we first tokenize the input sentence and mask each token to determine the most important one based on the loss. Next, we perform Algorithm 1 for the position in these important tokens."

## [POSITIVE] Charmer Adversarial Training Defense
Using Charmer as the inner maximization attack within the TRADES adversarial training objective to improve character-level robustness.

**Delta**: Reduces character-level ASR from 64.02% (standard) to 20.34%; minimally affects clean accuracy (92.43% -> 87.20%)
**Condition**: Adversarial training on BERT-base SST-2 with k=1

**Evidence**: "Charmer does not improve the token-level robustness and TextGrad hinders the character-level robustness... our results indicate character-level robustness is less conflicted with clean accuracy."

## [NEGATIVE] TextGrad Adversarial Training Defense
Using TextGrad (token-level attack) as the inner maximization attack within TRADES adversarial training to improve token-level robustness.

**Delta**: Increases character-level ASR from 64.02% to 67.34%; reduces clean accuracy from 92.43% to 80.94%
**Condition**: Adversarial training on BERT-base SST-2

**Evidence**: "TextGrad hinders the character-level robustness, i.e., increasing the ASR in 3.32% points when compared to standard training... TextGrad hinders the character-level robustness and clean accuracy to improve token-level robustness."

## [POSITIVE] Relaxing LowEng Constraint
Removing the constraint that only lowercase English letters can be perturbed (part of Pruthi-Jones Constraints), allowing attacks on any character.

**Delta**: ASR increases from 0.96% to 98.09% against robust encoding defense (Jones et al., 2020)
**Condition**: Against robust word recognition defenses (Jones et al., 2020 and Pruthi et al., 2019)

**Evidence**: "by relaxing any of the LowEng, End or Start constraints, performance grows considerably for both defenses, e.g., from 0.96% to 98.09% ASR when relaxing LowEng in the robust encoding case."

## [POSITIVE] Relaxing Start/End Character Constraints
Removing the constraints that prohibit perturbing the first or last character of a word (part of Pruthi-Jones Constraints).

**Delta**: Removing End constraint: ASR 70.34%->93.91% (Pruthi) and 0.96%->71.72% (Jones); Removing Start: 70.34%->98.58% (Pruthi) and 0.96%->88.93% (Jones)
**Condition**: Against robust word recognition defenses with PJC constraints

**Evidence**: "The ASR drastically increases when removing the LowEng, End or Start constraints, proving the fragility of existing robust word recognition defenses."

## [NEGATIVE] Pruthi-Jones Constraints (PJC)
A set of attack constraints (no repeat perturbation per word, no first/last character perturbation, no short word perturbation, only lowercase English letters) assumed by typo-corrector defenses.

**Delta**: With PJC, ASR drops to 0.96% against Jones et al. defense; without PJC, ASR is 100%
**Condition**: When evaluating against typo-corrector and robust encoding defenses

**Evidence**: "Charmer attains 100% ASR when not considering the PJC constraints. It is only when considering PJC that robust word recognition defenses are effective."

## [NEGATIVE] Projected Gradient Ascent (PGA) Attack
An alternative gradient-based attack approach considered for character-level adversarial examples.

**Delta**: Worse performance compared to Charmer's greedy strategy
**Condition**: Compared against Charmer on character-level attack benchmarks

**Evidence**: "We note that alternative design decisions can enable the usage of projected gradient ascent (PGA) attacks. However, we observed a worse performance in comparison with our strategy, see Appendix D."

## [POSITIVE] Dataset-specific Alphabet
Using only characters present in each evaluation dataset as the attack alphabet, to avoid introducing out-of-distribution characters.

**Delta**: Ensures in-distribution perturbations; contributes to high similarity scores
**Condition**: Applied across all Charmer experiments

**Evidence**: "For the alphabet Sigma, in order to not introduce out-of-distribution characters, we take the characters present in each evaluation dataset."

## [NEUTRAL] Hypothesis-only Perturbation for Text Pairs
For text pair classification tasks (MNLI-m, RTE, QNLI), only the hypothesis sentence is perturbed rather than both sentences.

**Delta**: Standard experimental practice; enables fair comparison
**Condition**: Applied to MNLI-m, RTE, and QNLI datasets

**Evidence**: "In the text pair classification tasks (MNLI-m, RTE, and QNLI), we perturb only the hypothesis sentence."

## [POSITIVE] Increased k for Long Sentences (AG-News)
Using k=20 maximum Levenshtein distance for AG-News dataset instead of the default k=10, due to the much longer sentences present in that dataset.

**Delta**: Charmer achieves 98.51% ASR on AG-News BERT, highest among all methods
**Condition**: Applied specifically to AG-News dataset

**Evidence**: "For Charmer we use n=20 positions (see Algorithm 1) and k=10 except for AG-news where we use k=20 because of the much longer sentences present in the dataset."
