# Energy-based Backdoor Defense without Task-Specific Samples and Model Retraining

**Source**: https://proceedings.mlr.press/v235/gao24b.html

## [POSITIVE] EBBA - Energy-Based Backdoor Detection
Computes energy scores for each label using task-agnostic internet images (no task-specific samples required). Detects backdoored models by identifying labels with abnormally high energy scores using mean and variance thresholding.

**Delta**: detects backdoored model in all cases (BadNets, Blend, WaNet, FIBA, DUBA) without task-specific samples
**Condition**: Backdoored model detection without task-specific samples

**Evidence**: "Under conditions where there are no poisoned or clean samples, only our method performs effectively, while TeCo and SCALE become entirely ineffective."

## [POSITIVE] Maximum Logit Normalization (Setting Max Logit to Zero)
Sets the maximum logit value for each sample to zero before computing energy scores, preventing the dominant ground-truth label from overwhelming the statistical significance of other labels.

**Delta**: prevents target label energy from being masked by high-confidence predictions
**Condition**: Energy computation for backdoored model detection

**Evidence**: "Hence, we propose setting the maximum value of the logits to 0... Even though the target label consistently has the highest or second-highest probability, the ultimately calculated energy is the lowest [without this fix]."

## [POSITIVE] Uniform Output Distribution Filtering
Selects a subset of internet images that produces a uniformly distributed model output (equal number of samples per pseudo-label class) to avoid skewed statistical results.

**Delta**: prevents illogical statistical outcomes from skewed distributions
**Condition**: Preprocessing step for EBBA backdoor model detection

**Evidence**: "we first refine the test set to achieve a uniformly distributed output, addressing concerns about skewed distributions that would lead to illogical statistical outcomes."

## [POSITIVE] EBBA+ - Transferred Energy for Poisoned Image Detection and Backdoor Removal
Applies multiple image corruption methods to candidate poisoned images and measures the Normalized Transferred Energy (NTE) shift from target label to ground-truth label to identify poisoned samples and recover their true labels without model retraining.

**Delta**: outperforms all other methods in PDR and F1 score across Cifar10, GTSRB, and ImageNet; achieves best BA in backdoor removal
**Condition**: Poisoned image detection and backdoor removal without model retraining

**Evidence**: "EBBA+ exhibits excellent performance in two aspects. First, it can detect all the triggers with high probability... Secondly, EBBA+ can achieve better or competitive detection performance than the baselines on three datasets."

## [POSITIVE] Normalized Transferred Energy (NTE)
Quantifies the energy transfer from the target label to the original clean label after image corruption of poisoned samples. The NTE score of the original label significantly surpasses others for poisoned images.

**Delta**: enables recovery of original clean label for poisoned images; ground-truth label has highest NTE score
**Condition**: Poisoned image detection and backdoor removal

**Evidence**: "if image x is poisoned, the transfer of output probability from the target to the original label leads to the NTE of the original label significantly surpassing that of other labels, while the NTE of the target label is much lower than that of other labels."

## [POSITIVE] Image Corruption for Output Analysis
Applies 80 different image corruption methods (Gaussian noise, raindrop effects, division by positive integers, etc.) to candidate images and analyzes logit-level changes rather than final output changes.

**Delta**: ground-truth label shifts to top results in over 90% of corruptions for poisoned images
**Condition**: Poisoned image detection via EBBA+

**Evidence**: "After the poisoned image undergoes image corruption, its ground-truth label in the output has clearly shifted forward to the top results (with the portion less than 6 exceeding 90%)."

## [POSITIVE] Logit-Level Analysis Instead of Final Output
Shifts focus from final classification output to logits when analyzing corrupted poisoned images, since final output may not change even when logits do change.

**Delta**: improves robustness over output-only methods like TeCo
**Condition**: Poisoned image detection under strong backdoor attacks

**Evidence**: "We find that even when the final output of a poisoned sample remains unchanged after corruption, its logits will be changed... only observing the final output may result in low robustness of defense."

## [POSITIVE] t-SNE Clustering for Poisoned Image Separation
Projects perturbed images into a feature space using t-SNE and applies clustering to distinguish clean images of the target class from poisoned images redirected to clean classes.

**Delta**: successfully distinguishes clean samples belonging to class t from poisoned samples belonging to class k
**Condition**: Final stage of EBBA+ for poisoned image detection and backdoor removal

**Evidence**: "It can be observed from them that our method successfully distinguishes clean samples belonging to class t from poisoned samples belonging to class k. Thus, we recover the benign accuracy of the target class and perfectly locate all the poisoned images without any clean sample."

## [NEUTRAL] Choice of Clustering Method
Selection among Hierarchical Clustering (HC), Birch, Mean Shift, and DBSCAN for the binary classification step in EBBA+.

**Delta**: PDR varies minimally: HC=0.972, Birch=0.968, Mean Shift=0.965, DBSCAN=~0.96
**Condition**: Clustering step in EBBA+ on GTSRB dataset

**Evidence**: "since the final result is already easily amenable to binary classification, the choice of clustering method has little impact for EBBA+."

## [POSITIVE] No Model Retraining Constraint
Design choice to avoid model retraining entirely, making the method applicable in cloud-based or resource-constrained settings.

**Delta**: achieves best BA among all methods including those requiring retraining; competitive ASR
**Condition**: Backdoor removal compared to Fine-Pruning, NAD, ANP, RNP, MEDIC, ZIP

**Evidence**: "our method does not need model retraining or pre-training... The BA of EBBA+ is best among all methods while its ASR is only comparable with them."

## [POSITIVE] Task-Agnostic Internet Images for Detection
Uses images downloaded from the internet (any domain) rather than task-specific clean or poisoned samples for backdoored model detection.

**Delta**: enables detection across all 5 attack types without any task-specific data, unlike TeCo and SCALE which fail completely
**Condition**: Backdoored model detection in real-world cloud-based scenarios

**Evidence**: "we develop an enhanced energy-based technique, called EBBA, to detect backdoored models without task-specific samples (i.e., samples from any tasks)."

## [NEGATIVE] Adaptive Attack Modification (Soft Label Suppression of Target Energy)
Adversarial training that reduces target label probability in clean images by modifying soft labels, designed to evade EBBA detection.

**Delta**: significantly reduces the energy value of the target label
**Condition**: Adaptive attack against EBBA

**Evidence**: "We trained on the GTSRB dataset and found that this training method significantly reduces the energy value of the target label."

## [POSITIVE] Modified EBBA Detection Criterion for Adaptive Attacks
Changes the detection condition from Ek' - mu > lambda*sigma to |Ek' - mu| > lambda*sigma to catch both abnormally high and abnormally low target label energies.

**Delta**: EBBA can still detect the anomaly under adaptive attack
**Condition**: Defense against adaptive attacks on EBBA

**Evidence**: "Simply modifying Eq. (8) from Ek′ − µ > λσ to |Ek′ − µ| > λσ in the EBBA formula is sufficient, as the energy of the target label will exhibit an exceptionally low value under this training condition, which can still be captured by EBBA."

## [POSITIVE] Direct Output Filtering Before NTE Application
First filters all images classified into the target class as potentially poisoned before applying NTE, limiting the search space and preserving benign accuracy for non-target classes.

**Delta**: minimum BA guaranteed to be K/(K-1) * ba, surpassing most defense methods; for large K approaches clean model accuracy
**Condition**: Backdoor removal phase of EBBA+

**Evidence**: "since we have identified the target label in EBBA, the minimum value of BA is K/(K−1) × ba, where K is the total number of labels and ba is the benign accuracy of the backdoor model. This already surpasses most defense methods."

## [POSITIVE] Cross-Domain Applicability of EBBA
Applying EBBA energy statistics approach to non-image classification tasks such as speech recognition (ESC-50) and text classification (THUCnews).

**Delta**: energy of target label significantly surpasses other labels in both speech and text domains
**Condition**: Speech recognition on ESC-50 and text classification on THUCnews

**Evidence**: "We find that EBBA is effective not only in image classification but also easily applicable to text and speech classifications... the energy of the two target labels significantly surpasses that of other labels."

## [POSITIVE] Multi-Target Backdoor Defense with EBBA
Applying EBBA to models with two simultaneous backdoor targets, both achieving 99% attack success rate.

**Delta**: energy of both target labels significantly surpasses other labels
**Condition**: Multi-label backdoor attacks with two simultaneous target labels

**Evidence**: "the energy of the two target labels significantly surpasses that of other labels. This provides evidence of EBBA's outstanding defense capabilities against multi-target attacks."
