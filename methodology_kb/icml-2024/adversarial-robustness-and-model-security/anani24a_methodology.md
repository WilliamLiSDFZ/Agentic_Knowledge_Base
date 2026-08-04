# Adaptive Hierarchical Certification for Segmentation using Randomized Smoothing

**Source**: https://proceedings.mlr.press/v235/anani24a.html

## [POSITIVE] Adaptive Hierarchical Certification (ADAPTIVECERTIFY)
A certification algorithm that adaptively relaxes pixel-level certification to coarser semantic hierarchy levels for unstable components, rather than abstaining from them entirely. Uses a pre-defined class hierarchy DAG and maps fluctuating components to parent nodes.

**Delta**: +1.1% to +12.9% CIG improvement; 19.4% to 35% abstain rate reduction depending on dataset and noise level
**Condition**: Applied across all four datasets (Cityscapes, ACDC, PASCAL-Context, COCO-Stuff-10K) at various noise levels σ and sample counts n

**Evidence**: "ADAPTIVECERTIFY consistently has a higher CIG and lower %⊘ than SEGCERTIFY. The improvement in CIG and %⊘ is highest on the COCO-Stuff-10K dataset, at 3.4% and 35%."

## [NEGATIVE] Flat Hierarchy Certification (SEGCERTIFY baseline)
The state-of-the-art certification method that certifies pixels using a flat set of fine-grained classes and abstains from any component whose top-class probability is below threshold τ.

**Delta**: Up to 61% abstain rate on COCO-Stuff-10K at higher noise levels
**Condition**: Baseline comparison; performs worse as number of classes increases and noise level increases

**Evidence**: "Common certification methods for segmentation use a flat set of fine-grained classes, leading to high abstain rates due to model uncertainty across many classes."

## [POSITIVE] Independent Pilot Samples for Component Level Assignment
Drawing an initial set of n0 independent samples (separate from the hypothesis test samples) to identify fluctuating/unstable components and assign them to hierarchy levels, avoiding invalidation of the statistical test.

**Delta**: Enables valid hierarchical certification without violating i.i.d. sample requirements
**Condition**: Required for correctness of the certification guarantee; applied during GETCOMPONENTLEVELS step

**Evidence**: "To avoid invalidating our hypotheses test, we use the initial set of n0 independent samples drawn in GETCOMPONENTLEVELS to both decide on the assigned component levels indices l1,...,lN, as well as the top class indices cA1,...,cAN."

## [POSITIVE] Posterior Difference Thresholding for Hierarchy Level Assignment
Using the difference between the top two class mean posteriors (ΔPi) from pilot samples to determine which hierarchy level a component is assigned to via a threshold function T_thresh.

**Delta**: Enables parameterized tradeoff between certification rate and CIG; best parameters found via grid search
**Condition**: Applied per-dataset with parameters tuned via grid search to maximize CIG on first 100 samples

**Evidence**: "We calculate the posterior difference ΔPi between the top two classes... We use thresholds to determine its hierarchy level index l by invoking a threshold function T_thresh."

## [POSITIVE] Certified Information Gain (CIG) Metric
A novel evaluation metric proportional to class granularity level. Assigns higher scores to certifications at finer-grained hierarchy levels and lower scores to coarser-level certifications. Reduces to certified accuracy for flat hierarchies.

**Delta**: Provides more informative evaluation than certified accuracy; CIG=1 for all leaf-node certifications
**Condition**: Used as primary evaluation metric for hierarchical certification; equivalent to certified accuracy when hierarchy is flat

**Evidence**: "certified accuracy does not take the loss of information into account for coarser classes, we introduce the Certified Information Gain (CIG) metric, which is proportional to the class granularity level."

## [POSITIVE] Semantic Class Hierarchy DAG
A pre-defined Directed Acyclic Graph organizing classes from fine-grained leaf nodes to coarser parent nodes (e.g., car/truck/bus → vehicle → dynamic obstacle). Used to group semantically related fluctuating classes.

**Delta**: Maximum CIG improvement of +0.23 for class 'hair drier' in COCO-Stuff-10K; +65 percentage points certification rate for class 'toaster'
**Condition**: Effectiveness scales with number of classes; most beneficial on COCO-Stuff-10K (171 classes)

**Evidence**: "Almost all of the classes lie in the quadrant where ADAPTIVECERTIFY outperforms SEGCERTIFY across both metrics (upper right quadrant), reaching a maximum improvement in CIG of +0.23 in the class hair drier in COCO-Stuff-10K."

## [POSITIVE] Adaptive Sampling via Hierarchy Mapping Function K
Transforming flat model outputs to hierarchical labels using mapping function K(class, level) that maps a leaf class to its ancestor at the assigned hierarchy level, enabling black-box use of flat segmentation models.

**Delta**: Enables hierarchical certification without retraining the base model
**Condition**: Applied during HSAMPLE step; works with any flat segmentation model as black-box

**Evidence**: "The construction of g^τ deals with the model f as a black-box, that is, by plugging in any different version of f, the same guarantees in Theorem 3.1 hold."

## [NEUTRAL] Multiple Hypothesis Testing with Bonferroni Correction
Applying Bonferroni correction across all N pixel hypothesis tests to bound the family-wise type I error rate to α, ensuring overall certification confidence of 1-α.

**Delta**: Maintains same theoretical guarantee as SEGCERTIFY baseline
**Condition**: Applied in HYPOTHESESTESTING step; inherited from SEGCERTIFY framework

**Evidence**: "We apply multiple hypothesis testing, similar to Fischer et al. (2021), following the Bonferroni method to reject (certify) or accept (abstain by overwriting v̂i with ⊘) the null hypotheses of components while maintaining an overall type I error probability of α."

## [NEUTRAL] Gaussian Noise Training (σ=0.25)
Training the HrNetV2 base model with added Gaussian noise of σ=0.25 to improve robustness for randomized smoothing certification.

**Delta**: Clean accuracy: 90% Cityscapes, 61% ACDC, 58% PASCAL-Context, 62.77% mean per-pixel accuracy on COCO-Stuff-10K
**Condition**: Used as the base model for all certification experiments; same model used for Cityscapes and ACDC to evaluate under domain shift

**Evidence**: "We use the weights provided by (Fischer et al., 2021) in their official paper PyTorch implementation, which is the result of training the model on a Gaussian noise of σ=0.25."

## [NEGATIVE] Increasing Noise Level σ
Using higher noise levels σ during certification, which increases the certified radius R but degrades model prediction quality.

**Delta**: CIG drops from ~0.89 at σ=0.25 to ~0.41 at σ=0.50 for SEGCERTIFY on Cityscapes; abstain rate increases from 7% to 26%
**Condition**: Applies to both ADAPTIVECERTIFY and SEGCERTIFY; ADAPTIVECERTIFY degrades less severely

**Evidence**: "Although increasing the noise level σ degrades the performance in both algorithms, ADAPTIVECERTIFY abstains much less than SEGCERTIFY, while maintaining a higher CIG, at higher noise levels."

## [NEGATIVE] Boundary Pixel Handling
Certifying boundary pixels (pixels at label transitions in segmentation maps) which are inherently harder to certify due to model uncertainty at object boundaries.

**Delta**: Boundary abstain rate up to 35% (ACDC baseline) vs 20.2% non-boundary; boundary CIG lower in both methods
**Condition**: Boundary pixels are harder for both methods; ADAPTIVECERTIFY's relative improvement is on average higher for boundary than non-boundary pixels (except PASCAL-Context)

**Evidence**: "A higher percentage of boundary pixels is abstained from by both methods compared to the non-boundary pixels, with a maximum of 35% in the challenging ACDC dataset by the baseline. Similarly, the CIG of the boundary pixels is lower in both methods."

## [POSITIVE] Large Number of Classes
Applying hierarchical certification to datasets with many fine-grained classes (e.g., COCO-Stuff-10K with 171 classes), where flat certification suffers most from high abstain rates.

**Delta**: Highest improvement on COCO-Stuff-10K: +3.4% CIG and 35% abstain rate reduction
**Condition**: Benefit of hierarchical certification scales with number of classes in the dataset

**Evidence**: "COCO-Stuff-10K has a large number of classes –171– best highlighting the efficacy of our hierarchical certification approach."

## [POSITIVE] Non-Mandatory Leaf-Node Prediction (NMLNP) Certification
Allowing certification at any level of the hierarchy (not just leaf/fine-grained nodes), enabling coarser but still semantically meaningful certificates for uncertain pixels.

**Delta**: 2% to 7% additional pixels certified at higher hierarchy levels where SEGCERTIFY abstains
**Condition**: Most beneficial on challenging datasets ACDC, PASCAL-Context, and COCO-Stuff-10K with more fluctuating components

**Evidence**: "both methods certify a comparable number of pixels at the finest level H0. However, due the hierarchical structure of ADAPTIVECERTIFY, there is a notable advantage in certifying additional percentages (ranging from 2% to 7%) of pixels at higher hierarchy levels in the 4 datasets, where SEGCERTIFY opts to abstain."

## [NEUTRAL] Single-Level Hierarchy (Flat) Reduction
When a class has no parent vertices at coarser hierarchy levels (e.g., 'road' in ACDC), ADAPTIVECERTIFY reduces to SEGCERTIFY with no improvement.

**Delta**: ΔCIG = 0, Δ%certified = 0 for leaf classes with no coarser parents
**Condition**: Applies only to classes that are isolated leaf nodes with no semantic grouping in the hierarchy

**Evidence**: "The performance remains the same (with a Δ of 0) for leaf classes with no parent vertices at coarser hierarchy levels, such as road in ACDC (hierarchy in Figure 2), since by definition ADAPTIVECERTIFY is reduced to SEGCERTIFY in a single-level hierarchy."

## [NEUTRAL] Class-Average CIG (cCIG) Metric
A per-class variant of CIG that computes CIG for each fine-grained class separately and averages, providing balanced evaluation across classes regardless of pixel frequency.

**Delta**: Complementary metric to CIG; reported in appendix tables
**Condition**: Used as supplementary evaluation metric alongside CIG and abstain rate

**Evidence**: "We also consider the class-average CIG, namely cCIG, which evaluates the performance on a per-class basis. It is defined by measuring the per-class CIG for all classes in Y and then getting the average."
