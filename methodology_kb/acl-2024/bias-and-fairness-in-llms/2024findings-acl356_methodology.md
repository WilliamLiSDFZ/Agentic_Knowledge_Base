# Bias in News Summarization: Measures, Pitfalls and Corpora

**Source**: https://aclanthology.org/2024.findings-acl.356/

## [POSITIVE] Rule-based demographic attribute control via name/pronoun replacement
Replacing first names, pronouns, and titles of gendered entities in real news documents to create controlled inputs with specific demographic distributions, rather than using subsampling or LLM-generated data

**Delta**: no systematic degradation in summary quality (scores within one standard deviation of original)
**Condition**: Creating controlled evaluation corpora for bias analysis in summarization

**Evidence**: "Table 4 shows that, while there is a small reduction in score for 4 out of 7 systems, performance is very similar between original and modified documents, with the latter score falling within less than one standard deviation of the original score. This indicates that our modification of the input documents does not lead to meaningful degradation in summary quality."

## [POSITIVE] Input-adjusted reference distribution for inclusion bias
Using the input document's demographic identifier distribution as the reference distribution for measuring inclusion bias, rather than a uniform distribution

**Delta**: corrects misleading bias scores; e.g. Random and Lead drop from 0.15/0.12 to 0.02/0.00 on CNN/DM
**Condition**: Measuring inclusion bias on naturally biased corpora like CNN/DM and XSum

**Evidence**: "Without correction for the input distribution, Random, Lead and Topic appear highly biased, while Sexist the least biased... b) Even our proposed correction, Topic scores higher on bias than Sexist, which clearly does not represent the bias of the underlying algorithms."

## [NEGATIVE] Uniform reference distribution for inclusion bias (Liang et al. approach)
Using a uniform distribution as the reference for measuring gender identifier frequency in summaries, without accounting for input document bias

**Delta**: Random baseline scores 0.15 (CNN/DM) and 0.24 (XSum) bias despite being unbiased by construction; Sexist scores 0.02 and 0.20 despite being clearly biased
**Condition**: Measuring inclusion bias on corpora with skewed input demographics (62-74% male identifiers)

**Evidence**: "Without correction for the input distribution, Random, Lead and Topic appear highly biased, while Sexist the least biased. The latter is a consequence of it barely decreasing female representation in sport documents, where representation is already low in the input, but boosting it in summaries for family related articles."

## [POSITIVE] Entity inclusion bias measure (odds ratio)
Measuring bias as the maximum odds ratio between inclusion probabilities of demographic groups at the entity level, rather than word list frequency

**Delta**: successfully detects near-zero inclusion bias across all 7 models; induced bias detection shows 0.71 score vs near-zero baseline
**Condition**: Evaluating content selection bias in single-document news summarization

**Evidence**: "Table 3 shows that all models score low on both inclusion bias measures, indicating that the content selection of all studied models does not carry any significant gender bias in this particular setting."

## [POSITIVE] Entity hallucination bias measure
Measuring bias as the total variation distance between the demographic distribution of hallucinated entities and a uniform distribution

**Delta**: reveals consistent male hallucination bias across all models (scores 0.31-0.44), not detectable by inclusion measures alone
**Condition**: Evaluating hallucination behavior in abstractive summarization models

**Evidence**: "Remarkably, we find that all models carry a bias towards male entities in their hallucinations. We study this in more detail in Section 9.1."

## [POSITIVE] Distinguishability classifier for representation bias
Using cosine similarity between summaries (bag-of-words and dense Sentence-BERT representations) to classify which demographic group is discussed, after neutralizing pronouns and names

**Delta**: reveals BART XSum has highest distinguishability (0.21-0.24); Llama-2 7b has lowest (0.04-0.05)
**Condition**: Measuring representation bias in summarization across demographic groups

**Evidence**: "All models show some degree of distinguishablity, with BART summaries showing the most pronounced differences between summaries for male and female coded documents."

## [POSITIVE] Pronoun and name neutralization before distinguishability scoring
Replacing all pronouns with gender-neutral variants and names with FIRST_NAME/LAST_NAME markers before computing distinguishability to avoid trivial grammatical cues

**Delta**: enables meaningful representation bias measurement beyond surface-level gender markers
**Condition**: Computing distinguishability scores for representation bias evaluation

**Evidence**: "To avoid distinguishability via simple grammatical cues and names, we replace all pronouns with a gender neutral variant (they/them etc.) and names with the markers FIRST_NAME/LAST_NAME."

## [NEGATIVE] LLM-generated synthetic data for bias evaluation
Using LLM-generated documents (e.g., GPT-2) as inputs for bias evaluation, as done in prior work (Brown and Shokri, 2023)

**Delta**: risk of false positives due to LLM-introduced biases in the generated data itself
**Condition**: Constructing evaluation datasets for summarization bias analysis

**Evidence**: "Similarly, we avoid LLM data, since it is well known that it is subject to biases itself (Liang et al., 2022)."

## [NEGATIVE] Subsampling existing datasets for bias evaluation
Subsampling naturally occurring datasets to create balanced evaluation sets for bias analysis

**Delta**: requires prior knowledge of which biases exist; cannot control for confounding input biases
**Condition**: Constructing evaluation datasets for summarization bias analysis

**Evidence**: "We reject Option 1, since it requires us to know beforehand which biases exist."

## [POSITIVE] Locally balanced gender corpus (C_loc)
Assigning half of entities in each document as male and half as female to create within-document gender competition

**Delta**: enables measurement of inclusion and hallucination bias by creating direct competition between genders within each document
**Condition**: Measuring inclusion and hallucination bias in summarization

**Evidence**: "For C_loc, we locally balance gender within each input by assigning half of all entities as male and the other half as female. We use it for inclusion and hallucination bias, since it allows competition between genders for inclusion/hallucination."

## [POSITIVE] Globally balanced gender corpus (C_glob)
Assigning all entities in a document the same gender and balancing the number of purely male vs. female documents

**Delta**: enables clean representation bias measurement by making it easy to identify which content is caused by which entity gender assignments
**Condition**: Measuring representation/distinguishability bias in summarization

**Evidence**: "For C_glob, we assign each entity in an input the same gender and instead balance the number of purely male vs. female inputs. We use it for representation bias, since it makes it easy to identify which content is caused by which entity gender assignments."

## [POSITIVE] GPT-3.5 RTS reference-free quality evaluation
Using GPT-3.5 with the RTS prompt as a reference-free metric to assess summary quality differences between demographic groups

**Delta**: finds no quality differences between male and female summaries (max diff 0.07, within confidence intervals)
**Condition**: Investigating whether distinguishability scores are explained by quality differences

**Evidence**: "We report average scores comparing male and female summaries in C_glob in Table 7, finding no quality differences."

## [POSITIVE] Wikipedia-based hallucinated entity gender classification
Determining gender of hallucinated entities by searching Wikipedia and counting gendered pronouns, with US census data as fallback

**Delta**: enables hallucination bias quantification; reveals consistent male bias in hallucinations across all models
**Condition**: Classifying gender of hallucinated named entities in generated summaries

**Evidence**: "Since we expect hallucinated entities to often be well known, we first search for a Wikipedia article with a title that exactly matches the entity. If we find one, we determine entity gender by counting gendered pronouns. Otherwise, we fall back to using US census data."

## [POSITIVE] Last-name-based entity alignment between summary and source
Heuristic cross-document entity alignment using last names to match summary entities to source document entities

**Delta**: manual verification finds procedure performs well (see Appendix E)
**Condition**: Entity inclusion and hallucination bias measurement requiring cross-document coreference

**Evidence**: "We select the token that is most frequently in the last position in mentions of a chain ed ∈ Ed as its last name. We align a summary entity es to an input entity ed if es contains the last name of ed as long as any other token in es is the first name assigned to ed during dataset construction or a title. Manual verification finds this procedure performs well."

## [NEUTRAL] Not modifying gender-specific content words
Leaving gender-specific content words (e.g., 'chairman') unchanged when swapping entity gender, only modifying names, pronouns, and titles

**Delta**: no significant effect on observed bias measures
**Condition**: Creating controlled demographic inputs for bias evaluation

**Evidence**: "We find that this has no significant effect on observed bias measures. We provide detailed results in Appendix J."

## [NEUTRAL] Keeping last names unchanged during name replacement
Only replacing first names (not last names) when swapping apparent gender of entities

**Delta**: changing last names has only a limited effect on hallucination bias results
**Condition**: Gender bias experiments using name replacement methodology

**Evidence**: "We leave last names the same to minimize modifications... We rerun our experiments for the C_loc case with changed last names to see whether this would alter our conclusions. We find that this has only a limited effect on the hallucination bias."

## [POSITIVE] Induced bias detection validation
Appending a biasing instruction to the prompt ('Please put a particular focus on the women mentioned in the text') to verify the measures can detect known inclusion bias

**Delta**: word list inclusion score rises to 0.42 and entity inclusion to 0.71 vs near-zero baseline scores
**Condition**: Validating the sensitivity of inclusion bias measures

**Evidence**: "Results in Table 5 show that we can clearly detect the induced inclusion bias."

## [NEUTRAL] Sentence-BERT dense representations for distinguishability
Using all-MiniLM-L6-v2 Sentence-BERT embeddings for cosine similarity in the distinguishability classifier

**Delta**: dense and count-based distinguishability scores are very similar across all models
**Condition**: Computing representation bias distinguishability scores

**Evidence**: "The metric is parameterized by a similarity function. We use cosine similarity with two representations: A bag of words based representation, and a dense representation derived from Sentence BERT."

## [POSITIVE] OntoNotes gold coreference annotations for corpus construction
Using the newswire portion of OntoNotes with gold named entity and coreference annotations to avoid using potentially biased automatic coreference resolution

**Delta**: avoids introducing coreference resolution bias into the evaluation pipeline
**Condition**: Constructing controlled evaluation corpora for bias analysis

**Evidence**: "We use the newswire portion of OntoNotes so we can avoid the use of coreference resolution that might itself be biased (Rudinger et al., 2018)."

## [POSITIVE] Racial bias evaluation with both first and last name replacement
Changing both first and last names when studying racial bias, since both are relevant in communicating race

**Delta**: reveals BART XSum has entity inclusion bias favoring black-associated names (0.17); most other models show near-zero racial inclusion bias
**Condition**: Extending bias evaluation methodology to racial bias

**Evidence**: "We change both first and last names, since both are relevant in communicating race... Table 8 shows that most models exhibit no entity inclusion bias, with the exception of BART XSum, which prefers to include black-associated names in the summary."

## [NEUTRAL] Random prompt selection for chat models
Randomly selecting one prompt per summary from a list of ten prompts designed to elicit summarizing behavior for Llama-2 chat models

**Delta**: no specific delta reported for this design choice
**Condition**: Evaluating Llama-2 chat models (7b, 13b, 70b) for summarization bias

**Evidence**: "For the chat models, we randomly select one prompt per summary from a list of ten prompts designed to elicit summarizing behavior."
