# Building Bridges: A Dataset for Evaluating Gender-Fair Machine Translation into German

**Source**: https://aclanthology.org/2024.findings-acl.448/

## [NEGATIVE] Masculine Generic Default in MT
All tested MT systems default to masculine gender forms when translating gender-neutral English person-referring nouns into German

**Delta**: 93–96% masculine forms in words-in-isolation
**Condition**: Words in isolation, singular and plural, across all 8 systems tested

**Evidence**: "all models are heavily biased towards masculine forms (93–96% of all translations)"

## [POSITIVE] Plural Form Translation
Translating plural forms instead of singular forms yields slightly more gender-neutral outputs, because some nouns have gender-neutral plural alternatives in German

**Delta**: Gender-neutral forms increase from ~0–2% (singular) to 4–8% (plural)
**Condition**: Words in isolation, plural vs. singular comparison

**Evidence**: "Gender-neutral forms occur slightly more frequently (4–8% of all translations), probably because of two reasons. First, while some nouns, e.g., 'practitioner' are gender-specific in the singular, gender-neutral alternatives are common for plural"

## [NEUTRAL] Natural Context (Multi-Sentence Passages)
Providing surrounding sentence context when translating person-referring nouns, rather than translating words in isolation

**Delta**: Gender-neutral forms ~15% in context vs. 4–8% in isolation for plural; masculine still dominates at ~85%
**Condition**: RQ2, words-in-context vs. words-in-isolation comparison across Europarl and Wikipedia domains

**Evidence**: "additional context does not yield a significantly higher portion of GFL translations"

## [NEGATIVE] Zero-Shot GPT GFL Detection
Prompting GPT 3.5 or GPT 4 in zero-shot to automatically detect gender-fair language forms in German MT outputs

**Delta**: Recall of 11.5% for gender-neutral cases for both GPT 3.5 and GPT 4
**Condition**: Automatic evaluation of GFL in German translations, Europarl EN-DE passages

**Evidence**: "Both GPT 3.5 and GPT 4 achieve an extremely low recall (11.5%) for gender-neutral cases... zero-shot automatic detection of GFL in German with recent GPT models is hard"

## [POSITIVE] GPT 4 vs GPT 3.5 for GFL Detection Precision
Using GPT 4 instead of GPT 3.5 for zero-shot GFL detection improves precision on gender-neutral forms

**Delta**: Precision improves from 30% (GPT 3.5) to 75% (GPT 4) for gender-neutral detection
**Condition**: Zero-shot GFL detection task, gender-neutral class, Europarl EN-DE

**Evidence**: "GPT 4's precision is relatively high (75%) compared to GPT 3.5 (30%), showing an improvement model generations"

## [NEGATIVE] Flan-T5 for MT
Using Flan-T5 (multi-task instruction fine-tuned model) for English-to-German translation

**Delta**: 39 mistranslations out of 115 singular words vs. near-zero for dedicated MT systems
**Condition**: Words in isolation, singular, compared to dedicated MT systems like DeepL and Google Translate

**Evidence**: "Interestingly, Flan-T5 produced many mistranslations. For instance, the seed noun 'traveller' was translated to 'Reisenden' with a grammatical mistake in the noun declension... The model also created non-existing words"

## [POSITIVE] Community-Enriched GFL Dictionary
Starting from a community-created gender-fair language dictionary (Genderwörterbuch) and enriching it with masculine, feminine, gender-inclusive, and gender-neutral forms in singular and plural, plus English translations

**Delta**: Final dictionary of 115 nouns covering professions and common person-referring nouns
**Condition**: Resource creation for benchmarking GFL in EN-DE MT

**Evidence**: "One of the authors—experienced with GFL and translation—enriched every noun with its masculine, feminine, gender-inclusive, and gender-neutral form in singular and plural... Our final dictionary counts 115 nouns in their singular and plural forms"

## [NEUTRAL] Multi-Domain Passage Sampling (Europarl + Wikipedia)
Sampling test passages from two distinct domains—parliamentary speeches (Europarl) and encyclopedic text (Wikipedia)—to study GFL in natural contexts

**Delta**: No significant domain-based difference in GFL output rates reported
**Condition**: RQ2, context-based translation evaluation

**Evidence**: "Across two domains (encyclopedic and parliament speeches) we show that additional context does not yield a significantly higher portion of GFL translations"

## [NEUTRAL] Multi-Sentence Context Window
For Wikipedia passages, extracting the matching sentence along with two preceding sentences and one following sentence to provide cross-sentence gender resolution context

**Delta**: No significant improvement in GFL output compared to single-sentence or isolated word translation
**Condition**: Wikipedia domain passages only; compared to single-sentence Europarl passages

**Evidence**: "The seed's gender assignment might require cross-sentence resolution. Thus, limited to Wikipedia, we extract the matching sentence along with two preceding sentences and one following"

## [POSITIVE] Focusing on Plural Occurrences for Ambiguity
Restricting context passage collection to plural occurrences of seed nouns to maximize gender-ambiguous cases

**Delta**: More challenging and realistic evaluation scenario; plural yields more gender-neutral translations (4–8%) than singular (0–2%)
**Condition**: Passage retrieval and context-based evaluation setup

**Evidence**: "We focus on plural occurrences because they yield to gender-ambiguous cases more frequently, providing a more challenging scenario for translation systems"

## [NEUTRAL] Beam Search Decoding for Supervised MT Models
Using beam search decoding (n=5) for OPUS MT, NLLB, and Flan-T5 during translation

**Delta**: Not separately quantified against other decoding strategies
**Condition**: Decoding configuration for open-weight supervised MT and instruction-tuned models

**Evidence**: "We used the default generation configuration for GPTs, beam search decoding (n=5) for OPUS MT, NLLB, and Flan-T5, and nucleus sampling (top p=1, top k=50, temperature=0) for Llama 2"

## [NEUTRAL] Instruction Prompt for LLM Translation
Using a minimal instruction prompt ('Translate the following sentence into German. Reply only with the translation.') for Llama 2 and GPT models

**Delta**: GPT 3.5 and DeepL produced the highest non-masculine translations among all systems, but GFL still rare
**Condition**: LLM-based translation (GPT 3.5, GPT 4, Llama 2)

**Evidence**: "For all open-weight models... for Llama 2 and GPTs we used: 'Translate the following sentence into German. Reply only with the translation. Sentence: {sentence}'"
