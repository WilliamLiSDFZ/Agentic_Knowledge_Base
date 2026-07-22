# Variationist: Exploring Multifaceted Variation and Bias in Written Language Data

**Source**: https://aclanthology.org/2024.acl-demos.33/

## [POSITIVE] Normalized Positive Weighted PMI (npw_pmi)
A variant of pointwise mutual information that is normalized, positive, and weighted, used to measure associations between language units and variables

**Delta**: descriptive (reveals geographic distribution of dialectal lexical items and sociodemographic annotation biases)
**Condition**: Computational dialectology and human label variation case studies

**Evidence**: "She selects the normalized, positive, and weighted variant of PMI (npw_pmi) as the metric... As shown in the choropleth map in Figure 3a, the lexical item appears to be mostly used in specific regions in northern Italy"

## [POSITIVE] Stopword Removal
Removing common function words from text before analysis using off-the-shelf multilingual stopword lists or user-provided lists

**Delta**: descriptive (reduces noise in association metrics)
**Condition**: Applied in dialectology, human label variation, and text generation case studies to reduce noise

**Evidence**: "she sets all text characters to lowercase and specifies stopword removal using a default lexicon in Italian, and extends it by providing extra unigrams to remove (i.e., the 'user' and 'url' placeholders)"

## [POSITIVE] Lowercase Normalization
Converting all text characters to lowercase before tokenization and analysis

**Delta**: descriptive (reduces data sparsity)
**Condition**: Human label variation case study with hate speech corpus

**Evidence**: "he sets the conversion of texts to lowercase to reduce data sparsity"

## [POSITIVE] Coordinate-type Spatial Variables
Using latitude and longitude as coordinate-type variables with spatial semantics to enable fine-grained geographic visualization

**Delta**: descriptive (provides finer granularity than administrative region boundaries)
**Condition**: Computational dialectology case study; useful when language varieties cross administrative borders

**Evidence**: "By running VARIATIONIST again and specifying the latitude and longitude variables instead (both with coordinate type and spatial semantics), Alice gets a fine-grained picture of the actual use of the word (Figure 3b)"

## [POSITIVE] Binned Map Visualization
Defining equally-sized intervals for latitude and longitude variables to create binned maps at intermediate geographic granularity

**Delta**: descriptive (intermediate granularity between region-level and municipality-level)
**Condition**: Computational dialectology case study

**Evidence**: "Moreover, by defining 30 equally-sized intervals for the latitude and longitude variables, she obtains a binned map (Figure 3c) that allows her to explore the use of 'ghe' at an intermediate granularity"

## [POSITIVE] Normalized Class Relevance Metric (npw_relevance)
A normalized class relevance metric based on Ramponi and Tonelli (2022) in its positive, weighted, and positive weighted versions for measuring unit-class associations

**Delta**: descriptive (reveals differential annotation patterns across sociodemographic groups)
**Condition**: Human label variation case study with sociodemographic annotation analysis

**Evidence**: "Bob employs the Measuring Hate Speech (MHS; Sachdeva et al., 2022) corpus... he uses VARIATIONIST and specifies text as the column containing the textual data and npw_relevance as the metric... Bob discovers that the lexical item 'gay' is more indicative of the hateful class for annotators who identify as straight compared to those who identify as bisexual, gay, or other"

## [POSITIVE] Root Type-Token Ratio (root_ttr)
A lexical diversity measure that normalizes the type-token ratio by taking the square root of the number of tokens

**Delta**: descriptive (human answers show larger root_ttr and standard deviation than ChatGPT-generated ones)
**Condition**: Text generation case study comparing human vs. ChatGPT-generated texts

**Evidence**: "human-produced answers are more varied in terms of root_ttr, also exhibiting a larger standard deviation compared to ChatGPT-generated ones (cf. Figure 5a)"

## [POSITIVE] Bigram Analysis with npw_pmi
Using bigrams as language units combined with npw_pmi to identify informative two-word sequences associated with different text sources

**Delta**: descriptive (reveals stylistic differences: human texts use everyday language while ChatGPT uses formal bigrams)
**Condition**: Text generation case study comparing human vs. ChatGPT-generated texts

**Evidence**: "by looking at the top-k (k=20) bigrams associated to human and ChatGPT texts (Figure 5b), Carol finds that human answers appear to include terms that are more commonly used in everyday situations (e.g., 'lot people', 'lot money'), while ChatGPT answers tend to include language that is more formal"

## [POSITIVE] Multi-variable Combination Analysis
Simultaneously analyzing multiple variables (e.g., hatespeech label combined with annotator_sexuality or annotator_race) to uncover intersectional patterns

**Delta**: descriptive (uncovers differential annotation behavior for reclaimed words across in-group vs. out-group annotators)
**Condition**: Human label variation case study with intersectional sociodemographic variables

**Evidence**: "Bob gets a similar finding when investigating the association of reclaimed words such as 'n*ggas' to hateful posts across self-reported annotators' race (Figure 4b). The term is less associated to posts labeled as hateful by annotators who identify themselves as black people (in-group members) compared to those annotated as hateful by most out-group members"

## [POSITIVE] Dual Text Column Analysis
Specifying two text columns simultaneously to explore similarities and differences between texts associated to the same labels or metadata

**Delta**: descriptive (enables direct comparison: human answers average 98.26 units vs. ChatGPT 73.66 units; vocabulary size 1.60M vs. 0.87M)
**Condition**: Text generation case study comparing parallel human and LLM-generated text columns

**Evidence**: "Carol specifies two text columns of interest: human_answers and chatgpt_answers... Carol finds that human answers are on average much longer than ChatGPT-generated ones (i.e., 98.26 vs 73.66 units) and that the vocabulary size of human answers is almost two times that of synthetic responses (i.e., 1.60M vs. 0.87M)"

## [POSITIVE] Custom Tokenizer Support
Allowing users to plug in their own tokenization functions beyond the default whitespace tokenizer or Hugging Face tokenizers

**Delta**: descriptive (avoids language-specific assumptions, broadens applicability to diverse language varieties)
**Condition**: General design principle applicable across all use cases and language varieties

**Evidence**: "VARIATIONIST allows the user to leverage i) a default whitespace tokenizer that goes beyond Latin characters, ii) any tokenizer from Hugging Face Tokenizers, or iii) a custom tokenizer. This way we avoid any assumptions on what actually is a language unit, also broaden the applicability of VARIATIONIST to a wide range of language varieties"

## [POSITIVE] JSON Serialization of Analysis Results
Serializing Inspector analysis results to a .json file for deferred visualization, enabling separation of computation and visualization stages

**Delta**: descriptive (especially useful for large datasets with high number of variable combinations)
**Condition**: Large-scale analyses with many variable combinations

**Evidence**: "the second option is especially useful when dealing with large datasets and a high number of variable combinations (and possible values). Indeed, serialization will enable the results to be easily used for visualization in a later stage"

## [NEGATIVE] Lexical-level Only Analysis
Current limitation of VARIATIONIST to lexical-level analysis of written data, excluding grammatical and speech modality features

**Delta**: descriptive (limits scope of linguistic analysis)
**Condition**: All use cases; limitation applies when grammatical or phonetic analysis is needed

**Evidence**: "As a limitation, we acknowledge that VARIATIONIST is currently limited to the lexical level on written data. We aim to extend its functionalities to also cover other linguistic aspects such as grammar as well as the speech modality in the next releases"

## [POSITIVE] Top-k Unit Pre-filtering for Visualization
Limiting visualization to the top-k highest-scoring language units per variable to manage chart complexity

**Delta**: descriptive (focuses visualization on most informative units, e.g., top-20 bigrams)
**Condition**: Text generation case study and any analysis with large vocabularies

**Evidence**: "it allows the user to specify whether to pre-filter the visualization based on selected language units (provided as lists) or top-scoring ones (by specifying a maximum per-variable amount)"

## [POSITIVE] Interactive Chart Filtering with Regex
Enabling interactive filtering of charts by language unit through a search input field supporting regular expressions or a dropdown menu

**Delta**: descriptive (enables smooth exploration of unit-variable associations)
**Condition**: All visualization use cases

**Evidence**: "Charts can be interactively filtered by language unit through a search input field supporting regular expressions or a dropdown menu to smoothly explore associations between units and the variables of interest"
