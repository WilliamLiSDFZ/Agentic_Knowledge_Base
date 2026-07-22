# SeeGULL Multilingual: a Dataset of Geo-Culturally Situated Stereotypes

**Source**: https://aclanthology.org/2024.acl-short.75/

## [POSITIVE] LLM-based stereotype generation with few-shot prompting
Using PaLM-2 in a few-shot setting to generate candidate (identity, attribute) stereotype tuples across multiple languages at scale

**Delta**: 25,861 stereotypes across 23 language-region pairs
**Condition**: Multilingual stereotype dataset creation at scale

**Evidence**: "Using few shot examples of stereotypes from existing datasets (Nadeem et al., 2021; Klineberg, 1951), we instruct the model to produce candidate tuples in the format (id, attr)"

## [POSITIVE] Culturally situated human annotations
Obtaining annotations from annotators who reside in the specific country/region where the language is commonly used, rather than general crowd workers

**Delta**: Captures geo-cultural subjectivity; e.g., 45.4% vs 74.6% stereotype agreement rates for Portuguese in Portugal vs Brazil
**Condition**: Stereotype validation and offensiveness annotation tasks

**Evidence**: "We adopt this approach since region of annotator residence impacts socially subjective tasks like stereotype annotations (Davani et al., 2022)"

## [POSITIVE] Separate annotations per language-country pair
For languages spoken in multiple countries (Spanish, Portuguese, Bengali), collecting separate annotations from each country independently

**Delta**: Revealed 45.4% vs 74.6% stereotype marking rates for Portuguese in Portugal vs Brazil
**Condition**: Languages common in multiple countries (Spanish, Portuguese, Bengali)

**Evidence**: "of the 1138 common tuples annotated in Portuguese in Portugal and Brazil, 45.4% of the tuples were marked as stereotypical by at least 2 annotators in Portugal compared to 74.6% tuples marked as such in Brazil"

## [POSITIVE] Gendered demonym inclusion
Including all gendered forms of demonyms for languages with grammatical gender (Spanish, Italian, Portuguese, Dutch)

**Delta**: Captures intersectional stereotypes; e.g., Bragantinos (male) associated with 'party-goers' vs Bragantinas (female) with 'conservative'
**Condition**: Languages with grammatical gender

**Evidence**: "In languages such as Spanish, Italian, and Portuguese, where demonyms are gendered...we use all gendered versions...SGM records these for languages Spanish, Portuguese, Italian, and Dutch"

## [POSITIVE] Regional demonym inclusion
Sourcing sub-national regional demonyms within each country from established online sources in respective languages, in addition to nationality-based demonyms

**Delta**: Added 10,292 new regional stereotypes not present in English SeeGULL
**Condition**: Dataset construction for all 23 language-region pairs

**Evidence**: "10,292 regional demonym based stereotypes are all newly introduced in SGM, making the overall dataset overlap with SGE about 5%"

## [POSITIVE] Attribute-level offensiveness annotation
Annotating offensiveness at the attribute term level (rather than full tuple level) using a Likert scale, then averaging to estimate tuple offensiveness

**Delta**: Annotated 7,159 unique attribute terms; revealed Italian and Swahili have ~22% offensive stereotypes vs Hindi at 1.83%
**Condition**: Offensiveness estimation for all stereotypes in SGM

**Evidence**: "we obtain human annotations on how offensive it is...by obtaining three in-language, globally situated annotations for each attribute term in the dataset on its degree of offensiveness on a Likert scale"

## [POSITIVE] Multilingual in-language evaluation queries
Evaluating foundation models using queries in the native language of the stereotype rather than English-translated queries

**Delta**: English-translated queries missed significant stereotype endorsements: GPT-4 Turbo +9.4%, Mixtral +5.7%, PaLM 2 +2.4% more endorsements in native language
**Condition**: Foundation model evaluation for stereotype endorsement

**Evidence**: "Our results also show that English-translated queries would have missed a significant fraction of stereotype endorsements in three out of four models"

## [POSITIVE] Disabling safety guardrails during evaluation
Running inference without additional safety guardrails or mitigation layers to measure base model stereotype endorsement

**Delta**: All four models endorsed stereotypes; PaLM 2 at 61.3%, GPT-4 Turbo at 43.0%, Gemini Pro at 39.7%, Mixtral at 21.0%
**Condition**: Foundation model evaluation protocol

**Evidence**: "we run inference without additional safety guardrails or mitigation layers that are typically used by downstream application developers"

## [NEUTRAL] Scoping stereotypes to nationality and regional demonyms only
Limiting identity terms to national and regional demonyms to enable reliable large-scale collection, excluding other identity types

**Delta**: Enabled scale of 1,190 unique identities but excludes other identity categories
**Condition**: Dataset scope and coverage decisions

**Evidence**: "we limit the identity terms of recorded stereotypes to be demonyms associated with nationalities and regions within each nation...These are design choices for reliably collecting stereotypes at scale"

## [NEUTRAL] Minimum 1-annotator threshold for stereotype inclusion
Including any tuple with at least 1 out of 3 annotators marking it as a stereotype in the published dataset, leaving filtering to users

**Delta**: Results in 25,861 stereotypes included in dataset
**Condition**: Dataset inclusion criteria

**Evidence**: "we consider any associations with at least 1 annotation (of 3 annotators) as stereotype to be sufficient for the tuple to be included in the published dataset. The filtering of the data for usage is left to the user"

## [NEGATIVE] English-only evaluation baseline comparison
Using English-only stereotype resources (SGE) as a comparison point, revealing low overlap with multilingual dataset

**Delta**: Only 5% overlap between SGM and English SeeGULL; Tamil had only 4.8% overlap
**Condition**: Comparison of English-only vs multilingual stereotype resources

**Evidence**: "of which, only 949 stereotypes are in common with SGE...The maximum overlap is seen in the Spanish dataset collected in Spain (13.2%)...while the least overlap was for Tamil (4.8%), and Hindi (5.37%)"

## [NEUTRAL] Machine translation for nationality demonyms
Using Google Translate to convert English nationality demonyms into target languages

**Delta**: Enables coverage of 179 nationality demonyms across 20 languages but may lose cultural nuance
**Condition**: Nationality demonym collection step

**Evidence**: "We use a list of 179 nationality based demonyms in English, and translate them to target languages"

## [POSITIVE] Generative (open-ended) evaluation task format
Using a generative multiple-choice question format rather than discriminative format to evaluate model stereotype endorsement

**Delta**: Captures nuanced safety policy responses and unexpected model outputs across all four evaluated models
**Condition**: Foundation model evaluation task design

**Evidence**: "The task is generative, as generative models and systems are increasingly common in downstream applications, and they can produce unexpected answers to questions"
