# Classist Tools: Social Class Correlates with Performance in NLP

**Source**: https://aclanthology.org/2024.acl-long.682/

## [NEGATIVE] Lexical Feature Regression for SES Classification
Multi-class logistic regression using surface, syntax, readability, and style features to predict socioeconomic class of speakers

**Delta**: macro F1 of 0.16 vs baseline of 0.07
**Condition**: Social class prediction from TV/movie utterances

**Evidence**: "Our best model achieves a macro F1 of 0.16, only slightly better than a most-frequent label baseline (macro-F1 of 0.07)."

## [POSITIVE] TF-IDF Text Representation for SES Classification
Logistic regression using TF-IDF unigram and bigram features instead of hand-crafted lexical features for social class prediction

**Delta**: F1 of 0.52 vs 0.29 for lexical features (x1.8 improvement)
**Condition**: Social class prediction from TV/movie utterances

**Evidence**: "Logistic regression based on TF-IDF achieves an F1 of 0.52 (x1.8 lexical features)."

## [POSITIVE] Sentence Embeddings for SES Classification
Using sentence-transformers (all-mpnet-base-v2) embeddings with logistic regression for social class prediction

**Delta**: F1 of 0.454 on test set vs 0.290 for lexical features
**Condition**: Social class prediction from TV/movie utterances

**Evidence**: "Sentence Embed[dings achieve] 0.457 [val] 0.454 [test]"

## [NEGATIVE] TF-IDF + Lexical Feature Combination
Combining TF-IDF features with hand-crafted lexical features for social class prediction

**Delta**: F1 of 0.290 on test, same as lexical alone
**Condition**: Social class prediction from TV/movie utterances; combination does not improve over TF-IDF alone

**Evidence**: "TF-IDF + Lexical [achieves] 0.297 [val] 0.290 [test]"

## [NEGATIVE] Wav2Vec2 ASR on Sociolect Data
Using Wav2Vec2 self-supervised speech model for automatic speech recognition across different socioeconomic and racial groups

**Delta**: clear trends showing lower ASR accuracy for lower SES and non-white speakers; stronger disparities than Whisper
**Condition**: ASR on US TV shows with varying SES and race

**Evidence**: "We find clear trends across models, with effects from both race and class: lower ASR error rates are associated with higher SES and with whiteness. These trends are stronger for the Wav2Vec2 model."

## [NEGATIVE] Whisper ASR on Sociolect Data
Using Whisper-medium model for automatic speech recognition across different socioeconomic and racial groups

**Delta**: lower ASR error rates associated with higher SES and whiteness, but weaker disparities than Wav2Vec2
**Condition**: ASR on US TV shows with varying SES and race

**Evidence**: "We find clear trends across models, with effects from both race and class: lower ASR error rates are associated with higher SES and with whiteness. These trends are stronger for the Wav2Vec2 model."

## [NEGATIVE] XLS-R ASR on Sociolect Data
Using XLS-R cross-lingual self-supervised speech model for automatic speech recognition across socioeconomic groups

**Delta**: shows performance disparities correlated with SES and race (consistent with other models)
**Condition**: ASR on US TV shows with varying SES and race

**Evidence**: "We find clear trends across models, with effects from both race and class: lower ASR error rates are associated with higher SES and with whiteness."

## [NEGATIVE] Llama 2 Perplexity as Sociolect Measure
Using Llama 2 7B language model perplexity to measure how well the model represents different socioeconomic groups' language

**Delta**: Low class mean perplexity 189.804 vs Middle-Upper 164.807
**Condition**: Language modelling perplexity across SES groups

**Evidence**: "lower SES leads to higher perplexity... models show significantly higher perplexities for Lower class speakers than for higher prestige groups."

## [NEGATIVE] Mistral-7B Perplexity as Sociolect Measure
Using Mistral-7B language model perplexity to measure representation of different socioeconomic groups

**Delta**: Low class mean 294.606 vs Middle-Upper 241.923; significant differences p<0.05
**Condition**: Language modelling perplexity across SES groups for white speakers

**Evidence**: "In the case of Mistral, lower-class and lower-middle class speakers have significantly higher perplexities than Mid-Upper and Middle class speakers."

## [NEGATIVE] Zephyr-7B (Aligned Model) Perplexity as Sociolect Measure
Using Zephyr-7B, a chat-aligned version of Mistral-7B, to test whether alignment affects sociolect representation disparities

**Delta**: Low class mean 415.641 vs Middle-Upper 332.224; significant differences p<0.01 for upper class
**Condition**: Language modelling perplexity across SES groups; alignment does not mitigate SES disparity

**Evidence**: "In the case of Zephyr, the model shows higher perplexities for lower classes than it does for Middle, Mid-Upper and Upper class speakers."

## [NEGATIVE] Grammar Error Correction on Sociolect Data
Applying grammar correction models (HappyTransformer T5, Gramformer, CoEdit-large, Flan-T5) to utterances from different SES groups to measure correction frequency

**Delta**: models produce corrections more frequently for lower SES speakers; Flan-T5 corrects 66.42% of utterances overall
**Condition**: Grammar error correction across SES groups

**Evidence**: "we can see a clear pattern: models produce corrections more frequently for those of lower SES."

## [POSITIVE] Coleman-Liau Index (CLI) as SES Feature
Using the Coleman-Liau readability index as a feature for socioeconomic class prediction

**Delta**: strongest coefficient among readability features (0.467 for class)
**Condition**: Lexical feature regression for SES classification

**Evidence**: "Although CLI and the number of characters have strong coefficients, the overall performance is very low."

## [POSITIVE] Character Count as SES Feature
Using mean word length (number of characters per word) as a feature for socioeconomic class prediction

**Delta**: coefficient of -0.437 for class, strongest among surface features
**Condition**: Lexical feature regression for SES classification

**Evidence**: "Although CLI and the number of characters have strong coefficients, the overall performance is very low."

## [NEUTRAL] Group-level vs Character-level ASR/Perplexity Analysis
Aggregating all utterances from a show/episode together rather than separating by individual character due to computational constraints

**Delta**: expected to underestimate disparities; character-level would likely show stronger effects
**Condition**: All NLP evaluation tasks in this study

**Evidence**: "Although this is a limitation in terms of the accuracy of the results, we expect that character-level annotations would strengthen our findings rather than negate them."

## [NEUTRAL] Fictional TV/Movie Data as Sociolect Proxy
Using scripted TV shows and movies as a proxy for real speakers of different socioeconomic backgrounds to avoid privacy issues

**Delta**: provides reasonable proxy supported by sociolinguistics literature but requires validation with real speakers
**Condition**: Dataset construction for sociolect NLP evaluation

**Evidence**: "Quaglio (2008) found important similarities between real and TV show dialogue... we therefore have reason to believe our dataset provides a reasonable proxy for real speakers."

## [NEUTRAL] Perplexity Lower-bound Filtering (min 5 tokens)
Excluding turns shorter than five tokens when calculating perplexity to reduce noise

**Delta**: not quantified; described as reducing non-differentiating utterances
**Condition**: Language modelling perplexity calculation

**Evidence**: "We exclude turns shorter than five tokens as they generally do not differentiate between classes."

## [NEGATIVE] Grammar Correction of In-group Slang/Regional Phenomena
Grammar correction models modifying regional slang and non-standard linguistic features as if they were errors

**Delta**: qualitative examples show erasure of legitimate linguistic variation (e.g., Scottish slang, AAE features)
**Condition**: Grammar error correction applied to lower SES and non-standard dialect speakers

**Evidence**: "we notice that often some of these corrections are performed on in-group slang or regional linguistic phenomena"
