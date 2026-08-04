# GeoReasoner: Geo-localization with Reasoning in Street Views using a Large Vision-Language Model

**Source**: https://proceedings.mlr.press/v235/li24ch.html

## [POSITIVE] Locatability-Enhanced Data Curation
A CLIP-based visual-text pairing network that quantifies the degree of locatability in street-view images using semantic segmentation masks and textual clue similarity, filtering out low-quality images below a threshold of 0.4

**Delta**: country-level accuracy from 0.63 to 0.72, city-level from 0.47 to 0.51 (0% to 100% high-locatability images)
**Condition**: Training the location tuning component of GeoReasoner on GSV images

**Evidence**: "the results reveal that as the proportion of high-locatability GSV images in the training dataset increases, the performance of the fine-tuned location component improves in both country- and city-level geo-localization. Specifically, the country- and city-level geo-localization accuracy increases from 0.63 & 0.47 for 0% high-locatability GSV images, to 0.72 & 0.51 for 100% high-locatability GSV images"

## [POSITIVE] Two-Stage Supervised Fine-Tuning (Reasoning + Location Tuning)
A two-stage fine-tuning process: Stage 1 (reasoning tuning) uses 3K game-derived text-image pairs to teach country-level reasoning; Stage 2 (location tuning) uses 70K high-locatability GSV images for fine-grained city-level prediction

**Delta**: +25.02% F1 on country-level, +38.61% F1 on city-level over Qwen-VL baseline
**Condition**: Compared against Qwen-VL (Qwen-7B) baseline on the custom test dataset

**Evidence**: "GeoReasoner outperforms it 25.02% on country-level geo-localization and 38.61% on city-level geo-localization, in terms of F1 value"

## [POSITIVE] Reasoning Tuning Stage
Fine-tuning the LVLM with LoRA on 3K text-image pairs from geo-localization games (GeoGuessr, Tuxun) to incorporate human inference knowledge for country-level reasoning

**Delta**: F1 from 0.8766 to 0.9033 (country-level), 0.8255 to 0.8584 (city-level) when added on top of location tuning
**Condition**: Ablation study comparing GeoReasoner w/o reasoning tuning vs. full GeoReasoner

**Evidence**: "The reasoning tuning component also plays a significant role in the performance improvement, as evidenced by the superior performance of the full GeoReasoner (row 4)"

## [POSITIVE] Location Tuning Stage
Fine-tuning the LVLM with a second LoRA stacked on the first, using 70K high-locatability GSV images with geo-tags for fine-grained city-level geo-localization

**Delta**: F1 from 0.8215 to 0.9033 (country-level), 0.5813 to 0.8584 (city-level) when added on top of reasoning tuning
**Condition**: Ablation study; especially critical for city-level prediction

**Evidence**: "the location tuning component is essential for geo-localization, as GeoReasoner w/o reasoning tuning (row 3) achieves much higher accuracy than GeoReasoner w/o location tuning (row 2), especially for fine-grained city-level prediction"

## [POSITIVE] Stacked LoRA Adapters
Using two stacked LoRA modules: LoRA1 for reasoning tuning and LoRA2 for location tuning, both applied on top of the pre-trained Qwen-VL model

**Delta**: outperforms baseline Qwen-VL by +25.02% country F1 and +38.61% city F1
**Condition**: Applied to Qwen-VL (9.6B base model) with 112.19M LoRA parameters each

**Evidence**: "Both stages are fine-tuned from the pre-trained Qwen-VL with LoRA, which contributes to the overall performance improvement of Qwen-VL in both the reasoning and location tuning stages, allowing the model to better capture complex relationships within the image-text pairs"

## [POSITIVE] External Knowledge from Geo-localization Games
Collecting 3K+ text-image pairs from GeoGuessr and Tuxun communities containing human-curated geo-localization clues (e.g., 'houses in central Chile are more likely to have terracotta tiled roofs'), cleaned with BERT-based NER

**Delta**: contributes to >25% country-level and >38% city-level F1 improvement over Qwen-VL
**Condition**: Used in reasoning tuning stage; provides country-level reasoning granularity

**Evidence**: "we integrate external knowledge obtained from real geo-localization games, tapping into valuable human inference capabilities... Despite the relatively small dataset, a noticeable improvement in performance has been achieved"

## [POSITIVE] MaskFormer Semantic Segmentation for Locatability
Using MaskFormer to predict segmentation masks for various classes (buildings, sky, vehicles, etc.) in GSV images to compute area ratios used in the locatability metric

**Delta**: enables filtering that improves accuracy from 0.63 to 0.72 (country) and 0.47 to 0.51 (city)
**Condition**: Part of the locatability quantization network pipeline

**Evidence**: "we first use MaskFormer to predict segmentation masks for various classes in GSV images, such as buildings, sky, and vehicles. We then compute an n-length vector I_seg, which quantifies the area ratio of each mask class"

## [POSITIVE] Sentence-BERT for Textual Clue Weighting
Using Sentence-BERT to measure similarity between textual clues and semantic segmentation labels, producing a weight vector that reflects the importance of each semantic class for geo-localization

**Delta**: enables locatability metric computation that improves dataset quality
**Condition**: Part of the locatability quantization network; used to weight segmentation classes

**Evidence**: "we utilize Sentence-BERT to measure the similarity between textual clues and semantic segmentation labels, yielding an m × n matrix M... This vector represents the importance of each semantic segmentation label for geo-localization"

## [POSITIVE] Locatability Threshold of 0.4
Empirically chosen threshold to filter high-locatability images from the 130K+ collected GSV images, resulting in 70K+ high-locatability images for training

**Delta**: filters to 70K high-locatability images; model trained on 70K achieves significantly higher accuracy than 10K
**Condition**: Setting threshold too high (e.g., 0.7) reduces image count; too low (e.g., 0.1) introduces noise

**Evidence**: "Empirically, we selected a threshold value of 0.4 for filtering locatable GSV images. This resulted in over 70k highly locatable images with geo-tags passing to the next stage for training an LVLM"

## [POSITIVE] Training Data Quantity (70K vs 10K)
Using the full 70K high-locatability GSV images for training versus a subset of 10K images

**Delta**: model trained with 70K achieves significantly higher accuracy than 10K (exact delta not specified for this comparison)
**Condition**: Applies when high-locatability images are used; quantity matters alongside quality

**Evidence**: "the quantity of high-locatability images is vital, as the model trained with 70K images (as in Sect. 4.2.2) achieves significantly higher accuracy than the one trained with 10K images (Sect. 4.1.2)"

## [POSITIVE] BERT-based NER Filtering for Textual Clues
Using a BERT-based Named Entity Recognition model to clean and filter collected game text, removing entries that lack specific geographical location information

**Delta**: results in 3K+ high-quality geo-localization textual clues from raw game community data
**Condition**: Applied during data curation of textual clues from GeoGuessr and Tuxun communities

**Evidence**: "we utilized the BERT-based Named Entity Recognition (NER) model to clean and filter text that lacked specific geographical location information. In this way, we collected a total of over 3K textual clues that encapsulate rich geo-localization information"

## [POSITIVE] GeoReasoner vs StreetCLIP (resource efficiency)
GeoReasoner trained on 70K street views achieves comparable or slightly better performance than StreetCLIP trained on 1.1 million images

**Delta**: GeoReasoner F1: 0.9033 (country), 0.8585 (city) vs StreetCLIP F1: 0.8854 (country), 0.8543 (city)
**Condition**: GeoReasoner trained on 70K images vs StreetCLIP on 1.1M images; GeoReasoner also provides reasoning

**Evidence**: "GeoReasoner performs slightly better than StreetCLIP, which was trained on a substantially larger dataset of 1.1 million geo-tagged street-view images"

## [NEGATIVE] GPT-4V Low Recall due to Safety Restrictions
GPT-4V frequently refuses to answer geo-localization queries due to privacy/security measures, resulting in very low recall despite high accuracy on answered queries

**Delta**: Recall of 0.34 (country) and 0.31 (city), F1 of 0.4923 (country) and 0.3851 (city)
**Condition**: GPT-4V applied to geo-localization task without fine-tuning

**Evidence**: "the recall performance of GPT-4V for the geo-localization task was notably low. Most of the responses were mainly: 'I'm sorry, I can't provide assistance with that request.' We speculate that GPT-4V has undergone extensive measures to ensure the model's security and privacy"

## [NEGATIVE] High Building Proportion in Street Views
Street-view images with very high building proportions (close-up views) have lower locatability because they transition from panoramic to close-up views, reducing available information

**Delta**: locatability peaks at ~0.2 building proportion and decreases as proportion increases further
**Condition**: Applies to the locatability metric computation for GSV images

**Evidence**: "The locatability metric slightly increases as the building proportion ranges from 0 to 0.2, but decreases as the building proportion continues to increase. As the proportion of buildings increases, the street-view images transition from panoramic to close-up views, leading to reduced information availability and consequently diminishing the degree of locatability"

## [NEGATIVE] Reasoning Only (without Location Tuning)
Fine-tuning with only reasoning tuning (LoRA1) without the location tuning stage

**Delta**: F1 of 0.8215 (country) and 0.5813 (city) vs full model 0.9033 and 0.8584
**Condition**: Ablation: reasoning tuning alone is insufficient, especially for city-level prediction

**Evidence**: "GeoReasoner w/o reasoning tuning (row 3) achieves much higher accuracy than GeoReasoner w/o location tuning (row 2), especially for fine-grained city-level prediction"

## [POSITIVE] Flickr Image Fine-tuning for Generalizability
Fine-tuning GeoReasoner on only 10K highly locatable Flickr images to evaluate generalizability on Im2GPS and Im2GPS3k benchmarks

**Delta**: Im2GPS3k: 0.10 street / 0.38 city / 0.83 country (comparable to GeoCLIP trained on millions of images)
**Condition**: Evaluated on Im2GPS and Im2GPS3k benchmarks with locatability filtering applied to test set

**Evidence**: "despite being fine-tuned solely on a smaller number of Flickr images, GeoReasoner achieves results comparable to ISNs and GeoCLIP trained on millions of Flickr images, particularly in terms of city- and country-level accuracy"

## [POSITIVE] Locatability Filtering on Test Set
Applying the locatability filter to benchmark test sets (Im2GPS, Im2GPS3k) to evaluate only on highly locatable images

**Delta**: Im2GPS country-level: ISNs improves from 0.67 to 0.78; GeoCLIP improves from baseline to 0.87
**Condition**: Applied to Im2GPS and Im2GPS3k benchmark evaluation

**Evidence**: "GeoReasoner trained on the filtered, highly locatable Flickr images also show improvements in the city- and country-level geo-localization, demonstrating the generalizability of our proposed locatability module"

## [NEGATIVE] Architectural Style Overfitting (Failure Case)
GeoReasoner over-relies on architectural style (e.g., Eiffel Tower) as a geo-localization cue, failing to distinguish between original landmarks and their replicas in other countries

**Delta**: misclassifies Eiffel Tower replicas in New York and Hangzhou as Paris, France
**Condition**: When input images contain replica landmarks or architecturally similar structures from different locations

**Evidence**: "GeoReasoner comprehends architectural style as a pivotal factor in geo-localization. However, the model can be misled by the learned significance of architectural style... GeoReasoner fails to distinguish between them, predicting all instances as located in Paris, France"

## [NEUTRAL] Country-Level Reasoning Granularity Limitation
The reasoning tuning stage only provides country-level reasoning due to the granularity of game-derived text-image pairs, not city-level reasoning

**Delta**: city-level reasoning not directly available from Stage 1, but Stage 2 location tuning compensates
**Condition**: Reasoning tuning stage using GeoGuessr/Tuxun data; city-level reasoning inferred indirectly

**Evidence**: "we can only provide reasoning at the country level due to the granularity exhibited in the image-text pairs. Nevertheless, this reasoning procedure is sufficient to facilitate the second stage of location tuning"
