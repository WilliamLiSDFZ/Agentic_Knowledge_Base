# GATE X-E : A Challenge Set for Gender-Fair Translations from Weakly-Gendered Languages

**Source**: https://aclanthology.org/2024.findings-acl.504/

## [POSITIVE] Chain-of-Thought Prompting for GPT-4 Rewriting
Using chain-of-thought prompting to elicit GPT-4 to produce three variant translations (feminine, masculine, neutral) for each input source-translation pair, with detailed step-by-step instructions and clarifications

**Delta**: 0.96–0.99 accuracy on Pronoun-Only subset
**Condition**: GPT-4 rewriting on Pronoun-Only subset across all four language pairs

**Evidence**: "Our solution uses chain-of-thought prompting (Wang et al., 2023) to elicit GPT-4 to produce three variant translations for each input source-target pair... It achieves high accuracy on the pronoun-only subset of GATE X-E."

## [POSITIVE] Explicit Instruction Elaboration in Prompts
Making prompt instructions much more explicit to reduce incorrect assumptions by GPT-4 about which individuals have gender markings in the source or input translation

**Delta**: reduced frequency of incorrect gender assumptions (qualitative)
**Condition**: GPT-4 rewriting task; iterative prompt development on dummy dataset of 100 sentence pairs

**Evidence**: "During early experiments with simpler prompts, we found that GPT-4 would often make incorrect assumptions about what individuals has gender markings in the source or input translation. We found that making instructions much more explicit helped reduce the frequency of these assumptions."

## [POSITIVE] Few-Shot Examples in Prompts (GPT-4)
Including three full examples customized per source language in the GPT-4 prompt, including examples indicating 'None' should be returned when no AGMEs are present

**Delta**: contributed to high accuracy scores (0.96–0.99 on Pronoun-Only)
**Condition**: GPT-4 rewriting solution across all four language pairs

**Evidence**: "The prompt also includes three full examples, customized per source language. The examples indicate that 'None' should be returned in lieu of translation variants when there are no AGMEs present."

## [POSITIVE] Few-Shot Setting for GPT-3.5 Turbo
Adding five examples to the GPT-3.5 Turbo prompt for gender-neutral rewriting, compared to a zero-shot single-sentence prompt

**Delta**: improved accuracy over zero-shot; e.g. tr→en neutral rewriting: 98.90% vs 97.24% accuracy; reduced POS errors and 'them/themselves' errors
**Condition**: GPT-3.5 Turbo gender-neutral rewriting on Pronoun-Only subset

**Evidence**: "In the gender-neutral rewriting task (Table 6), GPT-3.5 Turbo performs better in the few-shot setting compared to the zero-shot setting... The few-shot setting, however, does show an improvement in neutral rewriting errors (such as POS(part-of-speech) errors and them being rewritten as themselves) when compared to the zero-shot setting."

## [NEGATIVE] Gendered-Noun Problem Scope
Expanding rewriting to include translations containing intrinsically gendered nouns, requiring implicit coreference resolution and source-target noun alignment

**Delta**: scores drop to ~0.5–0.8 vs 0.96–0.99 for Pronoun-Only; Finnish mixed→feminine as low as 0.34
**Condition**: GPT-4 rewriting on Gendered-Noun subset across all language pairs

**Evidence**: "Scores on the Gendered-Noun subset are substantially lower than for Pronoun-Only, generally ranging from about 0.5 to 0.8, with Finnish mixed → feminine as an outlier at the low end at 0.34."

## [NEUTRAL] Exact Match Accuracy Metric
Using exact match to reference as the primary evaluation metric instead of BLEU or WER, since only one or two words typically differ between original and correct rewrite

**Delta**: no performance delta; methodological choice
**Condition**: Evaluation of GPT-4 rewriting solution on GATE X-E

**Evidence**: "Following Rarrick et al. (2023), we focus on exact match accuracy to the reference. Frequently only one or two words will be different between an original translation and a correct rewrite. In this context, metrics such as BLEU (Papineni et al., 2002) and WER are not very effective at determining the significance of single extraneous or missed word modifications."

## [POSITIVE] Rule-Based Neutral-to-Gendered Conversion
Using a rule-based algorithm to convert all-neutral GPT-3.5 Turbo rewrites into gendered alternatives, leveraging the observation that neutral pronoun form disambiguates gendered pronoun choices

**Delta**: gendered rewriting accuracy 99.27–99.50% across language pairs
**Condition**: GPT-3.5 Turbo pipeline for gendered alternatives on Pronoun-Only subset

**Evidence**: "A useful simplifying observation is for uniform-gender pronoun only rewrites, we can generate a correct feminine or masculine rewrite from the original target and a correct all-neutral rewrite... we begin with the original translation, and map to pronouns directly to the desired gender where unambiguous."

## [POSITIVE] Rule-Based System (Sun et al. 2021) for Neutral Rewriting
Using a rule-based system with SpaCy and GPT-2 for gender-neutral rewriting as a baseline comparison

**Delta**: higher BLEU and lower WER than GPT-3.5 Turbo (e.g. tr→en: BLEU 99.65 vs 99.30/99.55); lower accuracy than GPT-3.5 Turbo (96.16% vs 97.24%/98.90%)
**Condition**: Gender-neutral rewriting on Pronoun-Only subset; comparison with GPT-3.5 Turbo

**Evidence**: "Although GPT-3.5 Turbo provides slightly higher accuracy compared to the rule-based system proposed by Sun et al. (2021), the rule-based system performs better based on BLEU and WER. This is because GPT-3.5 Turbo makes modifications unrelated to neutral rewriting."

## [NEGATIVE] GPT-3.5 Turbo Unrelated Modifications
GPT-3.5 Turbo making modifications to text unrelated to gender-neutral rewriting, degrading precision

**Delta**: majority of errors in both zero-shot and few-shot settings attributed to unrelated modifications
**Condition**: GPT-3.5 Turbo zero-shot and few-shot gender-neutral rewriting

**Evidence**: "In both settings, the majority of errors stem from modifications unrelated to gender-neutral rewriting and from instances where the model suggests no changes are necessary to render the input text gender-neutral."

## [NEGATIVE] Longer Input Sentences
Longer source sentences (particularly Finnish data) increasing the scope for unrelated text modifications during rewriting

**Delta**: Finnish has highest error rate among four languages in GPT-3.5 Turbo experiments
**Condition**: GPT-3.5 Turbo rewriting on Finnish→English Pronoun-Only subset

**Evidence**: "Upon closer examination of the Finnish data, which has the highest error rate, we found that the errors are primarily due to the longer input length. This increases the scope for modifications of the text that are unrelated to gender-neutral rewriting."

## [NEGATIVE] Mixed-Gender 2-AGME Instances
Test cases where the original target has mixed gender assignments across two AGMEs, which tend to be longer and more complex sentences

**Delta**: slightly lower accuracy than uniform-gender instances; e.g. tr→en mixed Pronoun-Only: 0.78–0.82 vs 0.86 for uniform
**Condition**: GPT-4 rewriting on mixed-gender original target instances

**Evidence**: "Test cases where the original target has mixed gender all come from 2-AGME instances. These skew towards longer and more complicated sentence, which thus leads to slightly lower accuracy."

## [NEGATIVE] Masculine Pronoun Preference in GPT-4
GPT-4 showing a slight tendency to prefer masculine pronoun phrasing, leading to marginally higher accuracy on masculine rewrites than feminine rewrites

**Delta**: up to 5 percentage points gap between masculine and feminine rewrites on Hungarian mixed-gender Pronoun-Only
**Condition**: GPT-4 Pronoun-Only rewriting, particularly Hungarian mixed-gender instances

**Evidence**: "On most language pairs we see that Pronoun-Only rewrites into masculine outperform rewrites into feminine by a few percentage points. The largest gap is 5 points for mixed-gender original target on Hungarian. This may indicate a slight general tendency of GPT-4 to prefer phrasing using masculine pronouns."

## [NEGATIVE] Europarl Domain Data with Titles
Inclusion of Europarl data containing formal titles (Mr., Mrs., Mr. President) creating mismatches in gender-neutral and feminine rewrites

**Delta**: Finnish mixed→feminine Gendered-Noun accuracy as low as 0.34
**Condition**: GPT-4 rewriting on Finnish Gendered-Noun mixed-gender original target subset

**Evidence**: "This subset contains a large amount of data from Europarl that includes titles such as Mr. and Mrs. and addresses to Mr. President. The feminine rewrites often choose a mismatched form, such as Ms. Müller rather than Mrs. Müller, or Mrs. President rather than Madam President."

## [POSITIVE] Relaxed Neutral Negative Matching Criteria
Allowing neutral outputs that modify pronouns to neutral forms even when source-marked gender nouns are present, as an alternative evaluation criterion

**Delta**: neutral negative accuracy increases to 0.91 (Farsi), 0.92 (Turkish), 0.95 (Finnish), 0.95 (Hungarian) from baseline 0.53–0.84
**Condition**: Evaluation of GPT-4 on negative instances with neutral output

**Evidence**: "If we relax matching criteria to allow this variant, neutral negative accuracy increases to 0.91 for Farsi, 0.92 for Turkish, 0.95 for Finnish and 0.95 for Hungarian."

## [NEUTRAL] Temperature T=0 for GPT Models
Setting temperature to 0 for all GPT-based rewrites to ensure deterministic outputs

**Delta**: no quantitative delta reported
**Condition**: All GPT-3.5 Turbo experiments

**Evidence**: "For all GPT-based rewrites we set temperature T = 0"

## [POSITIVE] Dual Annotator Review with Consensus
Having a second annotator review all data to correct errors and inconsistencies, with consensus discussion for disagreements

**Delta**: 95% inter-annotator agreement rate
**Condition**: GATE X-E dataset construction across all four language pairs

**Evidence**: "For each language, a second annotator then reviewed the data to correct errors and inconsistencies. Across pairs language pairs, the second annotator agreed with the first annotator's assessment 95% of the time."

## [NEGATIVE] Missing Pronoun/Noun Changes (Error Pattern)
GPT-4 failing to change required pronouns or nouns in positive rewriting cases, with missing possessive determiners being the most common error

**Delta**: missing noun changes: 55.5% (gendered) / 51.9% (neutral) of errors; missing pronoun changes: 37.5% (gendered) / 38.6% (neutral) of errors in Gendered-Noun subset
**Condition**: Human error analysis on Turkish→English GPT-4 outputs, Gendered-Noun subset

**Evidence**: "For positive test cases, missing noun and pronoun changes were far more common than extraneous changes. For cases containing gendered nouns, noun changes were missed more often than pronoun changes... Among missing pronoun errors, missing possessive determiners was by far the most common."
