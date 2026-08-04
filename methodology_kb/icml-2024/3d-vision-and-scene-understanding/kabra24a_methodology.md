# Leveraging VLM-Based Pipelines to Annotate 3D Objects

**Source**: https://proceedings.mlr.press/v235/kabra24a.html

## [POSITIVE] ScoreAgg (Score-Based Aggregation)
A probabilistic aggregation method that uses VLM joint image-text log-likelihoods to marginalize over factors like viewpoint, combining scores across multiple queries using log-sum-exp instead of merging text responses via an LLM.

**Delta**: outperforms baseline
**Condition**: Multi-view 3D object type annotation on Objaverse-LVIS

**Evidence**: "Fig 3-L shows that all VLM pipelines outperform tags from the original dataset. PaLI captions (using ScoreAgg) outperform CAP3D substantially."

## [NEGATIVE] GPT4 Text-Based Aggregation (CAP3D)
Using an LLM (GPT4) to summarize multi-view captions into a single object-level description by feeding all per-view captions as text input.

**Delta**: caption blow-up ratios as high as 5.6
**Condition**: Multi-view 3D object captioning aggregation

**Evidence**: "This text-based aggregation is susceptible to hallucinations as it merges potentially contradictory descriptions... For CAP3D, we find caption blow-up ratios as high as 5.6, implying that GPT4 accumulated the words of at least 5 single-view captions for that particular object."

## [POSITIVE] Log-Sum-Exp Aggregation Function
Using log-sum-exp (LSE) as the aggregation function in ScoreAgg to combine scores across occurrences of a response in distinct queries, rather than using max.

**Delta**: small but significant margin over max-score aggregation
**Condition**: ScoreAgg aggregation function selection for type annotation

**Evidence**: "The LSE outperforms the max-score aggregation by a small but significant margin—the latter performs worse than several views individually, because overconfident responses might dominate the aggregate. This validates our algorithmic choice."

## [NEGATIVE] Max-Score Aggregation Function
Using the maximum score across queries as the aggregation function in ScoreAgg instead of log-sum-exp.

**Delta**: performs worse than several individual views
**Condition**: ScoreAgg aggregation function selection for type annotation

**Evidence**: "The LSE outperforms the max-score aggregation by a small but significant margin—the latter performs worse than several views individually, because overconfident responses might dominate the aggregate."

## [POSITIVE] Multi-View Aggregation
Aggregating VLM responses across multiple (up to 8) views of a 3D object using ScoreAgg.

**Delta**: outperforms any individual view
**Condition**: Type annotation on Objaverse-LVIS with increasing number of views Iv

**Evidence**: "Fig 5a shows the accuracy of individual object views versus all-view ScoreAgg responses. The log-sum-exp (LSE) aggregate performs better than any individual view, underscoring why our captions are more reliable than CAP3D's."

## [POSITIVE] Multi-Prompt Aggregation
Using multiple VQA prompts (4 different questions) in addition to multiple views, aggregated via ScoreAgg.

**Delta**: further boosts accuracy over view-only aggregation
**Condition**: Type annotation on Objaverse-LVIS; helps avoid mode collapse and reduces question-specific biases

**Evidence**: "Prompt-aggregation further boosts the accuracy of type prediction, as we show qualitatively in Fig 6. Using multiple questions smoothens the ScoreAgg response distribution and widens the support."

## [POSITIVE] Increasing Number of VLM Responses per Probe (J)
Sampling more candidate responses per VLM query (beam search with up to J=5 parallel decodings) to increase overlap in the response-score matrix.

**Delta**: monotonically increasing accuracy with J
**Condition**: ScoreAgg scaling with compute budget J on Objaverse-LVIS

**Evidence**: "Figures 5b and 5c underscore that ScoreAgg benefits from more candidate captions and views. The intuition is that increasing I and J increases the overlap in the response-view score matrix, thus producing a more reliable aggregate score for each candidate caption."

## [POSITIVE] Increasing Number of VLM Probes (I)
Running more VLM queries (more views or prompts) to increase overlap and reliability of the aggregated output.

**Delta**: monotonically increasing accuracy with Iv
**Condition**: ScoreAgg scaling with compute budget I on Objaverse-LVIS

**Evidence**: "Figures 5b and 5c underscore that ScoreAgg benefits from more candidate captions and views."

## [POSITIVE] PaLI VQA Annotations
Using a VQA variant of PaLI-X with four different question prompts to infer object type, aggregated via ScoreAgg.

**Delta**: top-∞ accuracy 0.67 vs 0.26 for PaLI captioning; two-thirds of Objaverse-LVIS covered
**Condition**: Type annotation on Objaverse-LVIS compared to captioning-based approaches

**Evidence**: "PaLI VQA annotations perform significantly better than the rest. They match ground-truth string labels on a large fraction of validation data without being trained for the task: our output distributions contain the exact expected type on two-thirds of Objaverse-LVIS (Fig 3-R)."

## [POSITIVE] Conditional Inference via Prompt-Chaining (Type as Auxiliary Input)
Providing the inferred object type as auxiliary text input when querying the VLM for downstream properties like material (e.g., 'what material is the spoon made of' vs 'what material is this made of').

**Delta**: PaLI-X top-1 acc: 0.60 (type+appearance) vs 0.56 (appearance only); BLIP-2 top-1 acc: 0.56 (type+appearance) vs 0.57 (appearance only)
**Condition**: Material inference with PaLI-X and BLIP-2 on material test set

**Evidence**: "Table 1 reveals that class-conditional inference can boost material prediction abilities in both VLMs (PaLI-X and BLIP-2). Although the effect is stronger in (the significantly larger) PaLI-X, using a type annotation as well as the object's appearance generally outperforms using one or the other."

## [POSITIVE] CAP3D Captions as Type Input for Material Inference
Using CAP3D's detailed captions (which often explicitly contain material labels) as the auxiliary type input for conditional material inference.

**Delta**: LLM mode top-1 acc 0.46 vs 0.33 for PaLI-VQA types; but VLM mode 0.61 vs 0.60
**Condition**: Material inference in LLM mode (text-only); CAP3D captions contain target material label 43% of the time vs 12% for PaLI types

**Evidence**: "Predictions from text alone (see 'From Type' subcolumns) confirm that CAP3D captions contain more material information than PaLI-VQA types. Yet PaLI types are on par or better than CAP3D captions when we do use the object's appearance."

## [POSITIVE] PaLI-VQA Types as Auxiliary Input for Material Inference (VLM mode)
Using succinct PaLI VQA type annotations as auxiliary input for conditional material inference with visual input.

**Delta**: on par or better than CAP3D captions in VLM mode (0.60 vs 0.61 top-1 acc for PaLI-X)
**Condition**: Material inference in VLM mode (with visual input) using PaLI-X

**Evidence**: "Yet PaLI types are on par or better than CAP3D captions when we do use the object's appearance (see 'From Type and Appearance' subcolumns). This is likely explained by hallucinations or specious details in CAP3D captions which hinder VLM reasoning."

## [POSITIVE] String Post-Processing Map (f)
A canonical string normalization function applied to VLM responses to deduplicate responses that are identical up to punctuation, case, uninformative tokens, or common suffixes like 'on/against a white background'.

**Delta**: ablated as beneficial
**Condition**: ScoreAgg deduplication step for PaLI captions on Objaverse

**Evidence**: "We compare results with and without a post-processing map f (Eq 1) to ignore suffixes of the form 'on/against a white background.'"

## [POSITIVE] Visual Sensitivity Metric (Hellinger Distance)
An unsupervised metric measuring the Hellinger distance between VLM predictions with and without visual input, used to quantify how much visual context changes predictions and correlate with accuracy gains.

**Delta**: significant correlation with gains in supervised soft accuracy
**Condition**: Unsupervised evaluation of material inference quality on material test set

**Evidence**: "We find significant correlation between the visual sensitivity metric and gains in (supervised) soft accuracy. The correlation is likely underestimated due to noise in the material labels."

## [POSITIVE] Caption Blow-Up Ratio as Hallucination Measure
An unsupervised metric dividing the word count of an aggregated caption by the maximum word count of any single-view caption, used to detect hallucination in text-based aggregation methods.

**Delta**: CAP3D ratios up to 5.6; ScoreAgg always 1.0
**Condition**: Hallucination detection for CAP3D vs ScoreAgg on Objaverse

**Evidence**: "For CAP3D, we find caption blow-up ratios as high as 5.6, implying that GPT4 accumulated the words of at least 5 single-view captions for that particular object. On the other hand, if we computed caption blow-up ratios for ScoreAgg, we would always get a ratio of 1.0, because our final caption is always one of the single-view captions."

## [POSITIVE] PaLI-X over BLIP-2
Using the larger PaLI-X (55B parameters, 756^2 image resolution) instead of BLIP-2 T5 XL for VLM inference.

**Delta**: PaLI-X top-1 material acc 0.56 vs BLIP-2 0.57 (appearance only); stronger conditional inference effect in PaLI-X
**Condition**: Material inference and type annotation tasks on Objaverse

**Evidence**: "Although the effect is stronger in (the significantly larger) PaLI-X, using a type annotation as well as the object's appearance generally outperforms using one or the other... So it is surprising that PaLI-X outperforms BLIP-2 nonetheless. Besides model size, a reason for the performance gap could be that BLIP-2 operates with images of size 224^2."

## [POSITIVE] Length-Normalized Scoring
Applying length normalization (alpha=0.6) to PaLI-X output scores to avoid disadvantaging longer outputs during beam search.

**Delta**: described as necessary for fair scoring
**Condition**: PaLI-X VLM scoring during ScoreAgg

**Evidence**: "PaLI scoring is length normalized as originally described in Eq 14 of (Wu et al., 2016)... This is to help ensure that longer outputs are not disadvantaged."

## [POSITIVE] Providing More Context in Conditional Questions
Including both material and type information in the question prompt (e.g., 'Is this M T fragile?' vs 'Is this T fragile?') to reduce the gap between VLM and LLM mode predictions.

**Delta**: Hellinger distance reduced (e.g., fragility: 0.110 to 0.103; lift-ability: 0.133 to 0.124)
**Condition**: Unsupervised visual sensitivity analysis for binary properties (fragility, lift-ability)

**Evidence**: "We also find that providing more information in the question (both material and type rather than type alone) consistently reduces the gap (i.e., mean Hellinger distance) between VLM and LLM mode responses."

## [POSITIVE] Zero-Shot VLM Inference (No Fine-Tuning)
Running all VLMs zero-shot without any task-specific fine-tuning or in-context learning examples.

**Delta**: two-thirds of Objaverse-LVIS covered at top-∞ accuracy
**Condition**: Type annotation on Objaverse-LVIS using PaLI VQA with ScoreAgg

**Evidence**: "They match ground-truth string labels on a large fraction of validation data without being trained for the task: our output distributions contain the exact expected type on two-thirds of Objaverse-LVIS (Fig 3-R)."
