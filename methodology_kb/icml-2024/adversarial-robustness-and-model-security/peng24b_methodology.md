# UPAM: Unified Prompt Attack in Text-to-Image Generation Models Against Both Textual Filters and Visual Checkers

**Source**: https://proceedings.mlr.press/v235/peng24b.html

## [POSITIVE] Sphere-Probing Learning (SPL)
A gradient estimation scheme that samples points on a sphere around current model parameters, queries the black-box API for Pass/Deny outcomes, and estimates optimization gradients by moving away from Deny-labeled points toward the decision boundary, enabling training even when no image results are returned.

**Delta**: R-1 drops from 38.37% to 0.22% without SPL; R-3 drops from 41.83% to 0.37% without SPL
**Condition**: Pre-training stage; critical when the API returns no images due to defense mechanisms blocking malicious prompts

**Evidence**: "Comparing (a) and (b) in Tab. 2, it can be seen that when UPAM does not employ SPL, both R-1 precision and R-3 precision drop to almost 0. This is because SPL is designed to deceive textual and visual defenses. In the absence of SPL, black-box T2I models hardly return images, resulting in poor R-precision performance."

## [POSITIVE] Semantic-Enhancing Learning (SEL)
A fine-tuning scheme based on Zeroth-Order Optimization (ZOO) that uses CLIP-based image-text and image-image similarity losses to align the semantics of returned images with target harmful images.

**Delta**: R-1 drops from 38.37% to 23.25% without SEL (-15.12%); R-3 drops from 41.83% to 28.36% without SEL (-13.47%)
**Condition**: Fine-tuning stage; applies after SPL has enabled the API to reliably return images

**Evidence**: "When comparing (a) and (c) in Tab. 2, we can see that our UPAM without SEL leads to a significant R-precision decrease of 15.12% (R-1) and 13.47% (R-3), demonstrating the effect of SEL."

## [POSITIVE] Gradient Harmonization (GH) in SEL
A method that removes the boundary-directed component from SEL's gradient by projecting out the SPL gradient direction, preventing SEL from pushing model parameters into the Deny region and disrupting SPL's achievements.

**Delta**: R-1 drops from 38.37% to 33.82% without GH; R-3 drops from 41.83% to 35.08% without GH; Textual Similarity worsens from 0.17 to 0.35 without GH
**Condition**: Fine-tuning stage; necessary to maintain compatibility between SEL and SPL when both are used together

**Evidence**: "when removing GH, SEL could disrupt SPL's optimization achievements, thus leading to worse performances in terms of R-1, R-3, and Textual Similarity. This demonstrates the effectiveness of gradient harmonization in SEL."

## [POSITIVE] Moving Closer to Boundary (MCB) in SPL
After optimizing model parameters into the Pass region, gradually reducing the sphere radius to move parameters back toward the Pass/Deny decision boundary, increasing the likelihood of generating target harmful images rather than genuinely safe ones.

**Delta**: R-1 drops from 38.37% to 35.76% without MCB; R-3 drops from 41.83% to 39.31% without MCB; Textual Similarity worsens from 0.17 to 0.22 without MCB
**Condition**: Pre-training stage SPL; applies after initial optimization has moved parameters into the Pass region

**Evidence**: "By comparing (i) and (ii) in Tab. 3, when removing MCB in SPL, obvious performance degradation is observed in terms of R-1, R-3, and Textual Similarity. This demonstrates the effectiveness of further moving closer to the boundary in SPL."

## [POSITIVE] LLM-based Prompt Generation (Pre-trained LLM)
Using a pre-trained Large Language Model (LLaMA) as the backbone for generating adversarial prompts, leveraging its language organization capability to produce human-readable, spelling-correct, and natural adversarial prompts.

**Delta**: PPL worsens dramatically from 706.32 to 3954.85 without pre-trained LLM (using untrained transformer instead)
**Condition**: Attack stealthiness; applies throughout training and inference for naturalness of generated adversarial prompts

**Evidence**: "Comparing (i) and (ii) in Tab. 5, we can see the transformer performs much worse in terms of PPL, demonstrating the effect of adopting knowledge of LLM."

## [POSITIVE] LoRA Adapter Optimization
Instead of fine-tuning the entire pre-trained LLM, only a low-rank adaptation (LoRA) adapter with rank 8 is updated, preserving the LLM's pre-trained language knowledge while allowing task-specific optimization.

**Delta**: PPL worsens from 706.32 to 2848.52 when directly optimizing the full LLM instead of LoRA
**Condition**: Attack stealthiness; preserving naturalness of adversarial prompts while enabling gradient-based optimization

**Evidence**: "Instead of optimizing LoRA, we directly optimize the pre-trained LLM. Comparing (i) and (iii) in Tab. 5, the significant change in PPL demonstrates the effect of using LoRA adapter."

## [POSITIVE] Gradient-Based Optimization (vs. Enumeration)
Training a parameterized attack model (UPAM) using gradient-based optimization instead of enumeration-based search, enabling efficient inference-time conversion of naive prompts to adversarial ones.

**Delta**: UPAM achieves R-1 of 38.37% vs. best baseline RIATIG at 8.65% on DALL-E Protocol A; inference time of 5.03s vs. 301.52s for RIATIG
**Condition**: Both Protocol A and Protocol B; especially effective under dual defense (textual filter + visual checker)

**Evidence**: "our UPAM significantly outperforms other methods by an average of 35.31% (R-1) and 38.90% (R-3), respectively... Furthermore, UPAM exhibits a significantly shorter inference time compared to other methods, showcasing superior efficiency."

## [POSITIVE] Improved ZOO Gradient with Momentum (g2)
An improved zeroth-order gradient estimator that incorporates the previous update direction and an adaptive adjustment along the previous gradient path, reducing stochastic randomness and improving gradient consistency over standard ZOO.

**Delta**: described as overcoming poor convergence of standard ZOO in practical applications
**Condition**: SEL fine-tuning stage; addresses convergence issues of standard zeroth-order optimization

**Evidence**: "The advantage of this design is that it encourages the model to update along previously effective directions with necessary adjustments, thereby increasing the gradient consistency and reducing the incidental randomness of optimization."

## [POSITIVE] Boundary-Region Optimization Objective in SPL
Positioning SPL's optimization objective at the boundary region between Pass and Deny cases (slightly toward Pass) rather than at the center of the Pass region, to increase the chance of generating harmful images rather than genuinely safe ones.

**Delta**: motivates MCB design which yields +2.61% R-1 and +2.52% R-3 improvement over version without boundary approach
**Condition**: Pre-training stage SPL; critical design choice distinguishing UPAM from model inversion methods that optimize toward class center

**Evidence**: "Motivated by the observation that misclassifications often occur at the boundary between two classes in classifiers, we propose situating the SPL's optimization objective at the boundary region of the two cases, with a slight inclination towards the 'Pass' side. This choice is guided by the notion that, when positioned at the boundary region, the black box exhibits less confidence in its decisions, significantly enhancing the chances of successfully generating target 'harmful' images."

## [POSITIVE] Two-Stage Training Decomposition
Decomposing the attack goal into two sequential stages: (1) pre-training with SPL to ensure the API reliably returns images, and (2) fine-tuning with SEL to align returned images with target semantics.

**Delta**: outperforms all baselines on R-1, R-3, Textual Similarity, Inference Time, and PPL across all three T2I models
**Condition**: Overall UPAM framework; addresses the challenge of simultaneously bypassing defenses and achieving semantic alignment

**Evidence**: "Considering it is non-trivial to simultaneously prompt the API to return images and also ensure their harmfulness, here we decompose the goal into two learning stages to address the challenges separately: the first stage enables the API to reliably return images, and the second stage finetunes these images to be harmful."

## [POSITIVE] CLIP-Based Semantic Measurement Loss (LSM)
A combined loss function using CLIP encoders to measure both image-text similarity (between returned image and naive prompt) and image-image similarity (between returned image and target image), used to guide SEL fine-tuning.

**Delta**: SEL with LSM improves R-1 by +15.12% and R-3 by +13.47% over UPAM without SEL
**Condition**: SEL fine-tuning stage; requires the API to be returning images (i.e., after SPL pre-training)

**Evidence**: "Motivated by the powerful semantic representation capability of CLIP, we utilize its pre-trained image/text encoders to measure the semantics of the returned image I*. The semantic measurement is comprehensively handled from the following two perspectives: Image-Text similarity... Image-Image similarity."

## [POSITIVE] Adaptive Sphere Radius Adjustment
Dynamically increasing the sphere radius when no boundary is detected (all sampled points are Deny) and decreasing it during boundary approach, with learning rate tied to radius (alpha = r/k).

**Delta**: enables effective boundary detection and gradual approach; removing MCB (which uses radius reduction) degrades R-1 by -2.61%
**Condition**: SPL pre-training stage; necessary for stable optimization without crossing back into the Deny region

**Evidence**: "If all points are predicted as 'Deny' (meaning no boundary are detected in the sphere), we increase the sphere radius r to probe the boundary... By decreasing the radius incrementally, we ensure effective boundary approaching."
