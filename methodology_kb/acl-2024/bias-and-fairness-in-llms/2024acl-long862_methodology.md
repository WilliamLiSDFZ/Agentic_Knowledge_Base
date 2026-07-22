# Having Beer after Prayer? Measuring Cultural Bias in Large Language Models

**Source**: https://aclanthology.org/2024.acl-long.862/

## [NEUTRAL] Culturally-Contextualized Prompts (CAMeL-Co)
Naturally occurring prompts from Twitter/X that embed explicit Arab cultural references, designed to provide contexts uniquely suited for Arab entities

**Delta**: CBS 40-60% despite explicit Arab cultural context
**Condition**: Text infilling evaluation of LMs on culturally-specific Arabic prompts

**Evidence**: "existing LMs show high average CBS (40-60%), which is on par with their performance on CAMeL-Ag prompts where contexts are neutral. This indicates a struggle in localizing to the appropriate culture in context"

## [NEUTRAL] Culture Token Prompt Adaptation
Prepending a special token meaning 'Arab' to prompts to help localize LMs to the relevant Arab culture

**Delta**: little effect
**Condition**: Text infilling with BERT-type and GPT-type LMs on CAMeL-Co prompts

**Evidence**: "introducing a special culture token had little effect"

## [POSITIVE] N-shot Arab Entity Demonstrations
Prepending randomly sampled Arab entities as demonstrations to prompts to help localize LMs to Arab cultural context

**Delta**: reduced CBS for most LMs
**Condition**: Text infilling evaluation; entity being evaluated is excluded from demonstrations

**Evidence**: "prepending Arab demonstrations reduced CBS for most LMs"

## [NEGATIVE] Multilingual LM Training
Training language models on data from multiple languages simultaneously

**Delta**: higher CBS compared to monolingual LMs
**Condition**: Cultural bias measurement on Arabic prompts; Arab vs. Western entity preference

**Evidence**: "Most multilingual LMs showed a higher CBS compared with monolingual LMs. This implies that multilingual training could impact cultural relevance of LMs in non-Western languages."

## [POSITIVE] Monolingual Arabic LM Training
Training language models exclusively on Arabic-language data

**Delta**: lower CBS than multilingual LMs; embeddings of Arab and Western entities grouped into distinct clusters
**Condition**: Cultural bias score evaluation on CAMeL-Co prompts

**Evidence**: "We find that embeddings of Arab and Western entities are grouped into distinct clusters by monolingual LMs while mixed up in multilingual LMs"

## [NEGATIVE] Wikipedia as Pre-training Corpus
Using Arabic Wikipedia as a source for pre-training language models

**Delta**: highest CBS among all corpora tested
**Condition**: 4-gram LM training and CBS evaluation on CAMeL-Co prompts

**Evidence**: "Arabic Wikipedia is the most Western-centric among all corpora, despite being often considered as one of the highest-quality sources for pre-training data. This is mostly because a large portion of Arabic Wikipedia articles discuss Western content."

## [NEGATIVE] International News as Pre-training Corpus
Using international news sources (OSIAN) as Arabic pre-training data

**Delta**: second highest CBS among corpora tested
**Condition**: 4-gram LM training and CBS evaluation on CAMeL-Co prompts

**Evidence**: "International news had the second highest CBS."

## [NEGATIVE] Web-Crawled Data as Pre-training Corpus
Using web-crawled Arabic data (OSCAR/CommonCrawl) as pre-training corpus

**Delta**: third most Western-centric source
**Condition**: 4-gram LM training and CBS evaluation; potentially affected by machine-translated content

**Evidence**: "web-crawled data was the third most Western-centric source. This could explain the prevalence of Western content as it may get translated into Arabic from languages such as English."

## [POSITIVE] Local News as Pre-training Corpus
Using local Arabic news corpora (1.5B corpus, Assafir) as pre-training data

**Delta**: lowest CBS among corpora tested
**Condition**: 4-gram LM training and CBS evaluation on CAMeL-Co prompts

**Evidence**: "Local news and Twitter/X corpora had the lowest CBS, suggesting that future work may consider these sources for training more culturally adapted LMs."

## [POSITIVE] Twitter/X Social Media as Pre-training Corpus
Using Arabic tweets corpus as pre-training data for language models

**Delta**: lowest CBS among corpora tested
**Condition**: 4-gram LM training and CBS evaluation on CAMeL-Co prompts

**Evidence**: "Local news and Twitter/X corpora had the lowest CBS, suggesting that future work may consider these sources for training more culturally adapted LMs."

## [NEUTRAL] 5-shot In-context Learning for GPT-type LMs
Using 5-shot examples for GPT-type LMs on NER and sentiment analysis tasks instead of fine-tuning

**Delta**: results reported alongside fine-tuned models showing similar Western bias patterns
**Condition**: NER and sentiment analysis fairness evaluation for GPT-3.5 and GPT-4

**Evidence**: "For GPT-type LMs, we perform in-context learning with 5-shot examples"

## [POSITIVE] Pattern-based Entity Extraction from CommonCrawl
Using manually designed patterns of nouns/noun-verb expressions to extract cultural entities from Arabic CommonCrawl, avoiding use of LMs in dataset construction

**Delta**: 5k-10k unique extractions per entity type before filtering
**Condition**: Dataset construction for entity types with limited Wikidata coverage

**Evidence**: "Pattern-matching is a simple yet effective method; and importantly, it avoids using any LMs in the construction of the dataset that will be used for evaluating LMs."

## [NEUTRAL] Dialectal Arabic Training (CAMeLBERT-DA)
Training BERT-type model exclusively on Dialectal Arabic data

**Delta**: compared against MSA and mixed variants; no clear advantage reported
**Condition**: Cultural bias evaluation across all CAMeL tasks

**Evidence**: "we compare CAMeLBERT to its variants trained exclusively on Dialectal Arabic (CAMeLBERT-DA) or Modern Standard Arabic (CAMeLBERT-MSA)"

## [NEUTRAL] Arabic-English Code-Switched Training (GigaBERT-CS)
Further training GigaBERT on synthetic Arabic-English code-switched data

**Delta**: no clear improvement over GigaBERT on cultural bias metrics
**Condition**: NER and cultural bias score evaluation

**Evidence**: "GigaBERT and GigaBERT-CS (Lan et al., 2020), which was further trained on synthetic Arabic-English CodeSwitched data"

## [NEUTRAL] Instruction Tuning on Localized Arabic Instructions (AceGPT)
Instruction-tuning Llama2 on localized Arabic instructions to improve Arabic cultural adaptation

**Delta**: still shows high CBS (40-60% range) similar to other multilingual LMs
**Condition**: Text infilling CBS evaluation on CAMeL-Co prompts

**Evidence**: "AceGPT (Huang et al., 2023), an instruction-tuned version of Llama2 on localized Arabic instructions... existing LMs show high average CBS (40-60%)"

## [POSITIVE] Odds Ratio Analysis for Stereotype Detection
Computing odds ratios of adjective usage in LM-generated stories about Arab vs. Western named characters to identify stereotypical associations

**Delta**: revealed consistent stereotyping: Arab names associated with 'poor' (OR ~0.26-0.47), Western names with 'wealthy' (OR ~2.02-4.10)
**Condition**: Story generation analysis across JAIS-Chat, GPT-3.5, GPT-4 for male and female names

**Evidence**: "Stories about Arab characters more often cover a theme of poverty with adjectives such as 'poor' persistently used across LMs. On the other hand, the adjective 'wealthy' was more likely to appear in Western stories."

## [POSITIVE] Cultural Bias Score (CBS)
Likelihood-based metric computing the percentage of cases where a model assigns higher probability to Western entities over Arab entities for masked token filling

**Delta**: revealed 40-65% Western preference across all 16 LMs tested
**Condition**: Intrinsic evaluation of cultural bias in text infilling across all LM architectures

**Evidence**: "existing LMs show high average CBS (40-60%), which is on par with their performance on CAMeL-Ag prompts where contexts are neutral"

## [POSITIVE] False Negative/False Positive Fairness Analysis for Sentiment
Examining differences in false positive and false negative sentiment predictions between sentences containing Arab vs. Western entities rather than comparing F1 scores

**Delta**: revealed that nearly all LMs show higher false negatives on Arab entity sentences
**Condition**: Sentiment analysis fairness evaluation; F1 scores had minimal differences between groups

**Evidence**: "nearly all LMs achieve higher false negatives on sentences containing Arab entities, suggesting more false association of Arab entities with negative sentiment"

## [NEUTRAL] NER Fine-tuning on ANERCorp
Fine-tuning LMs on ANERCorp dataset for Arabic named entity recognition evaluation

**Delta**: up to 20 F1 point gap between Western and Arab location entities; ~5 F1 point gap for names
**Condition**: NER fairness evaluation on CAMeL-Co prompts filled with Arab vs. Western entities

**Evidence**: "most LMs perform better when tagging Western person names and locations. Larger discrepancies are observed on locations, reaching up to 20 F1 points of difference."
