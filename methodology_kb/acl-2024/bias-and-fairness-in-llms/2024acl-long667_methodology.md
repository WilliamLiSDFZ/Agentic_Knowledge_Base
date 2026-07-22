# ViSAGe: A Global-Scale Analysis of Visual Stereotypes in Text-to-Image Generation

**Source**: https://aclanthology.org/2024.acl-long.667/

## [POSITIVE] Visual vs. Non-Visual Stereotype Distinction
Annotating stereotypical attributes from SeeGULL on a Likert scale to distinguish 'visual' attributes (explicitly identifiable in images, e.g., 'sombrero') from 'non-visual' attributes (e.g., 'intelligent'), retaining only 385 out of 1994 attributes where all annotators agreed on visual nature.

**Delta**: 385 visual attributes selected from 1994 total; automated methods detect more objectively visual stereotypes with this grounding
**Condition**: Applied during both human annotation and automated stereotype detection phases

**Evidence**: "Without visual stereotypes to ground the evaluations, the automated techniques detect non-visual attributes like 'attractive', 'smart', etc., for identity groups. However, using visual attributes as a reference, our approach uncovers more objectively visual stereotypes for identity groups."

## [POSITIVE] Grounding Evaluation in Existing Textual Stereotype Resource (SeeGULL)
Using the SeeGULL dataset (containing ~7000 stereotypes for 175 nationality-based identity groups) as a reference to ground visual stereotype evaluation, rather than deriving stereotypes from scratch.

**Delta**: Coverage of 135 nationalities; described as 'significantly larger than prior work'
**Condition**: Applied throughout the ViSAGe evaluation framework

**Evidence**: "This grounding in existing social stereotype resources aids the critical distinction between spurious correlations in models and stereotypical tendencies which are necessary for model safety interventions."

## [POSITIVE] Strict Consensus Threshold for Visual Attribute Selection
Excluding all attributes where any annotator expressed uncertainty, disagreement, or strong disagreement, requiring unanimous agreement or strong agreement from all 3 annotators for an attribute to be deemed 'visual'.

**Delta**: Reduced from 1994 to 385 attributes (19.3% retention); annotator-marked likelihood of 44.69%
**Condition**: Applied to visual attribute annotation task to ensure reliability

**Evidence**: "For our subsequent analysis, we exclude all attributes where any annotator expressed uncertainty or disagreement regarding the visual nature. Consequently, we deem terms where all annotators at least agreed about their visual nature, as 'visual' resulting in a selection of 385 out of the original 1994 attributes."

## [POSITIVE] Diverse Annotator Pool by Geographic Identity
Recruiting annotators identifying with different geographical origin identities (Asian, European, and North American) for each attribute annotation to capture cross-cultural perspectives on visual nature of stereotypes.

**Delta**: 3 annotators per attribute from different geographic backgrounds
**Condition**: Applied during visual attribute annotation task

**Evidence**: "For each attribute, we get annotations from 3 annotators that identify with different geographical origin identities - Asian, European, and North American."

## [POSITIVE] Multiple Prompt Templates for Image Generation
Using three distinct prompt formats per identity group ('a photo of id person', 'a portrait of id person', 'an id person') and generating 5 images per prompt, yielding 15 images per identity group.

**Delta**: 15 images per identity group; 2,025 identity-image pairs annotated
**Condition**: Applied during image generation with Stable Diffusion v1.4

**Evidence**: "For each prompt Pi (i = 1, 2, 3) and each identity term id, we generate 5 images, resulting in an output set of images I = {Ii,1, Ii,2, . . . , Ii,5} for a combination of prompt and identity term."

## [NEUTRAL] Automated Stereotype Detection via CLIP + BART Captioning
Using CLIP embeddings scored against n-gram caches, with top-k embeddings passed to BART to generate candidate captions, then performing string matching against visual stereotypes to detect stereotypical attributes at scale.

**Delta**: 44.69% likelihood of automated detections being confirmed by human annotators; also identified false positives like 'cow', 'elephant' for Indians
**Condition**: Applied as a scalable alternative to human annotation for stereotype detection

**Evidence**: "This approach also identified stereotypical attributes which were not necessarily depicted in the images, e.g., attributes like 'cow', 'elephant' for Indians. This could be a limitation in our automated approach or existing errors/biases in the generated captions themselves."

## [POSITIVE] TF-IDF Salience Score for Attribute-Identity Association
Computing a modified TF-IDF metric as a salience score S(attrs, id) = tf(attrs, id) · idf(attrs, C) to measure how uniquely a stereotypical attribute is associated with a specific identity group in generated captions.

**Delta**: Identified most salient visual stereotypes per identity group (e.g., 'sombrero', 'dark', 'brown' for Mexicans)
**Condition**: Applied in automated stereotype detection pipeline

**Evidence**: "To further understand how uniquely a stereotypical attribute attrs is present in the caption of the images of an identity group, we compute a salience score of the attributes w.r.t. the identity group S(attrs, id). We use a modified tf-idf metric."

## [POSITIVE] Stereotypical Tendency Ratio (θid)
Computing the ratio of mean likelihood of stereotypical attributes appearing in images to mean likelihood of randomly selected non-stereotypical attributes appearing, to quantify how stereotypically an identity group is represented.

**Delta**: On average, visual stereotypical attributes are 3x more likely to appear than non-stereotypical attributes; Nigerians 27x more likely
**Condition**: Applied across 135 identity groups for Study 1

**Evidence**: "We observe that on average, the visual representation of any identity group is thrice as likely to be stereotypical than non-stereotypical, i.e., the visual stereotypical attributes associated with an identity group are thrice as likely to appear in their visual representation when compared to randomly selected visual non-stereotypical attributes."

## [POSITIVE] Stereotypical Pull Analysis via CLIP Cosine Similarity
Measuring mean pairwise cosine similarity between CLIP embeddings of default, stereotypical, and non-stereotypical image sets to quantify a model's tendency to generate stereotypical images even when prompted neutrally or with non-stereotypical attributes.

**Delta**: 121 out of 135 identity groups show higher similarity to stereotyped than non-stereotyped representations
**Condition**: Applied in Study 2 across 135 identity groups

**Evidence**: "For 121 out of 135 identity groups, the default representation of an identity group has a higher similarity score with the 'stereotyped' images compared to the 'non-stereotyped' images indicating an overall 'pull' towards generating stereotypical looking images."

## [POSITIVE] Offensiveness Score Inference from SeeGULL Ratings
Using pre-existing offensiveness ratings of stereotypical attributes in SeeGULL to compute a mean offensiveness score O(id) for each identity group based on which stereotypical attributes were identified as present in generated images.

**Delta**: Identified that Africa, South America, and South East Asia identity groups have comparatively more offensive representations
**Condition**: Applied to assess offensiveness of T2I generations across identity groups

**Evidence**: "We observe that the representations of people from countries in Africa, South America, and South East Asia, are comparatively more offensive. Jordanians, Uruguayans, Gabonese, Laotian, and Albanians have the most offensive representation."

## [POSITIVE] Equal Number of Stereotypical and Non-Stereotypical Attributes in Annotation
Presenting annotators with an equal number of stereotypical and randomly selected non-stereotypical attributes per image to enable fair comparison of likelihood scores.

**Delta**: Enables fair computation of stereotypical tendency ratio θid
**Condition**: Applied during human annotation task for stereotype detection

**Evidence**: "We select an equal number, k, of stereotypical and random attributes for any given identity group for a fair comparison."

## [POSITIVE] Bounding Box Annotation for Visual Markers
Requiring annotators to draw bounding boxes around specific regions, objects, or indicators in images that support their selection of a visual attribute, providing spatial grounding for stereotype identification.

**Delta**: 40,057 image-attribute pairs annotated with spatial markers
**Condition**: Applied during human annotation of stereotype detection task

**Evidence**: "Additionally, they are also asked to draw bounding boxes to highlight specific regions, objects, or other indicators that support their selection of the visual attribute within the image."

## [POSITIVE] Global South vs. Global North Stratification
Analyzing stereotypical pull and offensiveness scores stratified by geo-political regions (8 regions from SeeGULL) to reveal differential treatment of identity groups from the Global South versus Global North.

**Delta**: Global South identity groups show higher mean similarity scores across all three image sets (d, s, ns), indicating less diversity and stronger stereotypical pull
**Condition**: Applied in both Study 1 and Study 2 analyses

**Evidence**: "Moreover, for identity groups from global south, the similarity between stereotypes and non-stereotyped image sets S(s, ns) is also very high, indicating an overall lack of diversity in the sets of generated images."
