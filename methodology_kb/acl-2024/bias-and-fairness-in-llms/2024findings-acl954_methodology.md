# Ask LLMs Directly, “What shapes your bias?”: Measuring Social Bias in Large Language Models

**Source**: https://aclanthology.org/2024.findings-acl.954/

## [POSITIVE] Direct QA-based Social Perception Measurement
Directly quantifying social perceptions using a QA format with multiple-choice questions, assigning scores based on model responses without requiring additional sentiment analysis or classifier steps

**Delta**: outperforms baseline
**Condition**: Compared to indirect methods that use sentiment analysis or toxicity classifiers to measure bias

**Evidence**: "Our QA-based approach, by contrast, is designed to compute bias scores directly based on the options selected."

## [POSITIVE] Persona-Assigning Prompting Strategy
Assigning demographic personas to LLMs via system prompts to elicit perspective-specific responses and measure how social perceptions vary across different identity viewpoints

**Delta**: outperforms baseline
**Condition**: Applied to instruction-following LLMs for bias measurement across demographic identities

**Evidence**: "Prompt-based methods are effective at eliciting persona-relevant responses from the recent instruction-following LLMs (Gupta et al., 2023) and efficient to be easily adjusted to the various demographic personas, unlike the alternative approaches that necessitate training a model for each specific persona assignment."

## [POSITIVE] Counter-Scoring Strategy
Assigning counter-reward or counter-penalty scores to non-selected options in addition to reward/penalty scores for selected options, to capture relative preferences among all targets

**Delta**: descriptive improvement in capturing preference rankings
**Condition**: When a model selects UNKNOWN/correct answer but still implicitly ranks non-selected targets differently depending on option combinations

**Evidence**: "If bias scores are not assigned to both targets, they would be assessed as having an equal rank and deemed not to have been discriminated against. To reflect the ranks of preference appropriately, we give a counter-penalty score to Hindu."

## [POSITIVE] TARGET BIAS (TB) Metric
A metric measuring the polarity of bias toward a target by a persona, computed by summing perception scores normalized by the number of times the target appears as an option

**Delta**: captures bias polarity not detectable by Bias Score (BS)
**Condition**: When evaluating directional/polarity aspects of bias across personas and targets

**Evidence**: "A shift in response tendency based on the persona was observed, yet it could not be captured with BS. Although the BS scores of a kid and an elder are equivalent, our metric PB_p accurately reflects the degree of perception shifting."

## [POSITIVE] BIAS AMOUNT (BAMT) Metric
A metric measuring the quantity of bias regardless of polarity, computed by summing absolute values of perception scores, capturing how frequently a model makes biased decisions

**Delta**: reveals bias patterns invisible to TB alone
**Condition**: When distinguishing between models that are biased in balanced vs. skewed directions (e.g., Llama-2 family type 2 vs. GPT3.5 type 3)

**Evidence**: "TB and BAMT categorize the shape of bias in LMs... simultaneously analyzing bias with TB and BAMT metrics can discover various aspects of bias within LLMs."

## [POSITIVE] PERSONA BIAS (PB) Metric
A metric measuring variance in social perceptions influenced by different personas, computed as the average absolute difference in TB scores between a persona-assigned model and the default model

**Delta**: captures perception shifts not detectable by Bias Score
**Condition**: When evaluating how much persona assignment changes model bias relative to the default model

**Evidence**: "Although the BS scores of a kid and an elder are equivalent, our metric PB_p accurately reflects the degree of perception shifting. These observations indicate that TB_p→t and PB_p have the ability to capture differences in perception, depending on the personas."

## [POSITIVE] Multi-Metric Combined Interpretation
Using TB, BAMT, and PB together to categorize LLMs into four bias types (ideal, balanced-vast, skewed-scarce, skewed-vast) for comprehensive bias analysis

**Delta**: enables fine-grained categorization vs. single-dimensional BS
**Condition**: When performing comprehensive bias analysis across multiple LLMs and domains

**Evidence**: "our proposed metrics capture multi-dimensional aspects of bias with social perceptions, compared to the BS score, which can capture only a single-dimensional aspect."

## [NEUTRAL] Larger Model Size (Llama-2 scaling)
Increasing model size from 7B to 13B to 70B parameters in the Llama-2-Chat family

**Delta**: bar size decreases with scale but BAMT remains high relative to GPT models
**Condition**: Within the Llama-2-Chat model family on the BBQ dataset bias evaluation

**Evidence**: "In Figure 5, we observe that, as the model size increases, the size of the bar decreases. Also, llama-7b, the smallest model, has the highest BAMT line among others."

## [POSITIVE] GPT-4 as Evaluated Model
Using GPT-4 (gpt-4-1106-preview) as the LLM under evaluation

**Delta**: lowest bias scores across all domains and metrics
**Condition**: Compared to GPT-3.5 and Llama-2 family models on bias metrics TB, BAMT, PB, and BS

**Evidence**: "GPT4 shows scores that fit type (1), recording the lowest scores across all domains... GPT4 not only has the ability to avoid biased speech toward targeted demographic groups but also refrains from biased role-playing in relation to the assigned persona."

## [NEGATIVE] Indirect Bias Measurement via Sentiment/Toxicity Classifiers
Prior approach of measuring bias by analyzing sentiment or toxicity in model-generated text using external classifiers

**Delta**: descriptive limitation
**Condition**: When used as the primary method for quantifying social bias in LLMs

**Evidence**: "These approaches may face challenges due to confounding factors from the context or the imperfect performance of toxicity and sentiment classifiers, which could lead to misleading results."

## [NEGATIVE] Fixed Stereotype QA Evaluation
Prior QA-based evaluation approach that measures model agreement with fixed stereotypical vs. anti-stereotypical options rooted in English-speaking cultures

**Delta**: descriptive limitation
**Condition**: When evaluating bias across diverse demographic identities and perspectives

**Evidence**: "Most of the QA-based evaluations examined the model's adherence to fixed stereotypes, mainly rooted in English-speaking cultures, by offering choices between stereotypical and anti-stereotypical options. This approach has not fully considered that perceptions of each individual toward a target may be different, depending on their unique viewpoints."

## [POSITIVE] Multiple Prompt Iterations for Persona Assignment
Using five different persona-assigning prompts across five test iterations and averaging results to reduce prompt sensitivity

**Delta**: reduces variance across prompt formulations
**Condition**: Applied to all persona-assigned LLM experiments to improve robustness

**Evidence**: "We use five prompts to assign a persona to a model. Each of the five iterations uses a different prompt... We conducted five iterations of testing on all models and averaged the results."

## [NEUTRAL] In-group Favoritism Pattern Detection
Observing that persona-assigned LLMs exhibit higher positive perception toward their own demographic group, analogous to human in-group bias

**Delta**: descriptive finding
**Condition**: Observed across all domains and most models, intensified in llama-70b and GPT3.5 compared to smaller Llama models

**Evidence**: "Each persona has an exceptional love for itself... TB toward the non-old group is positive for a boy, a girl, and a kid persona... but that of an elder persona is as negative as -0.08. Conversely, the elder persona perceives their own age group positively."

## [POSITIVE] Ambiguous vs. Disambiguated Context Conditions
Dividing the BBQ dataset into ambiguous and disambiguated context conditions to measure bias under different levels of contextual information

**Delta**: higher bias scores in ambiguous condition vs. disambiguated
**Condition**: Applied across all five domains and all five LLMs evaluated

**Evidence**: "To measure bias in different context scenarios, we conducted our experiments by dividing the dataset into two different context conditions... The first row is the results on the dataset of ambiguous contexts, and the second one is those on disambiguated data."
