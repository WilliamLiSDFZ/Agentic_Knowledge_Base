# SceneCraft: An LLM Agent for Synthesizing 3D Scenes as Blender Code

**Source**: https://proceedings.mlr.press/v235/hu24g.html

## [POSITIVE] Relational Scene Graph Abstraction
Models the scene as a bipartite relational graph G(s) = (A, R, E) where assets and spatial relations are nodes, serving as an intermediate abstraction layer before code generation

**Delta**: Constraint score drops from 88.9 to 3.2 when removed; CLIP SIM drops from 69.8 to 19.4
**Condition**: Synthetic query evaluation with annotated constraints

**Evidence**: "removing one component after the other: – Relation Graph: CLIP SIM 19.4, Constraint Score 3.2"

## [POSITIVE] Inner-Loop Visual Feedback Optimization
Iterative self-improvement loop where GPT-4V reviews rendered images, identifies unsatisfied constraints, and revises the Blender script accordingly

**Delta**: Removing inner-loop drops constraint score by 38.4 (from 64.5 to 26.1) and CLIP SIM from 48.3 to 32.8
**Condition**: Per-scene layout optimization on synthetic queries

**Evidence**: "Among these components, inner-loop optimization provides the most important leaps; removing it leads to 38.4 drop on constraint score"

## [POSITIVE] Outer-Loop Library Learning
Reviews incremental code changes across inner-loop iterations over a batch of queries, identifies common patterns, and merges them into a reusable spatial skill library without LLM parameter tuning

**Delta**: Removing learned library drops CLIP SIM from 69.8 to 48.3 and constraint score from 88.9 to 64.5
**Condition**: Evaluated on unseen synthetic queries after library built from 20 training examples

**Evidence**: "– Learned Library: CLIP SIM 48.3, Constraint Score 64.5 (vs full SceneCraft 69.8 / 88.9)"

## [POSITIVE] Dual-Loop Self-Improving Pipeline
Combination of inner-loop per-scene refinement and outer-loop library learning forming a complete self-improvement framework

**Delta**: +45.1% CLIP score improvement over BlenderGPT on synthetic queries; +40.9% on Sintel; constraint score 88.9 vs 5.6
**Condition**: Both synthetic queries and real-world Sintel movie dataset

**Evidence**: "SceneCraft achieves over 45.1% and 40.9% improvement on generated scenes' CLIP score, compared with another popular LLM agent baseline BlenderGPT, over both unseen synthetic queries and real-world movies like Sintel. SceneCraft also achieves significantly better constraint passing score (88.9 against 5.6)"

## [POSITIVE] Scene Decomposition into Sub-Scenes
Decomposes complex scenes with up to 100 assets into a sequence of sub-scenes, each with a subset of assets and description, to reduce planning complexity

**Delta**: Enables handling scenes with up to 100 assets; each sub-scene reduced to 10-20 assets
**Condition**: Complex scenes with large numbers of assets

**Evidence**: "Some scenes might contain up to a hundred assets, making the layout planning very difficult. Therefore, SceneCraft agent decomposes the scene into a set of sub-scenes, each representing a part of the entire scene."

## [POSITIVE] CLIP-Based Asset Retrieval with Re-ranking
Retrieves top-10 assets by text description using CLIP, then renders each and selects the one with highest text-to-image CLIP score

**Delta**: Not quantified separately
**Condition**: Asset retrieval from Turbosquid repository

**Evidence**: "The retrieval process first finds the top-10 assets based on the text description of each asset. Then each retrieved asset is rendered as an image and the one with the highest text-to-image score is selected."

## [POSITIVE] Constraint-Based Layout Optimization
Translates spatial relations into numerical scoring functions F_r and solves for optimal layout by maximizing sum of constraint satisfaction scores

**Delta**: Constraint score 88.9 vs BlenderGPT 5.6
**Condition**: Scene layout planning for all evaluated scenes

**Evidence**: "This enables SceneCraft to simultaneously balance multiple constraints, ensuring a comprehensive and contextually accurate scene layout planning."

## [POSITIVE] Non-Parametric Skill Updates via Python Code
All learning updates are made to Python code (non-parametric knowledge) rather than LLM parameters, avoiding backpropagation costs

**Delta**: Library built from only 20 synthetic examples
**Condition**: Library learning phase; contrasted with traditional fine-tuning

**Evidence**: "updates are made to non-parametric knowledge represented as Python code, avoiding the computational cost and inaccessibility issues associated with back-propagation in large language models"

## [POSITIVE] GPT-4V as Visual Reviewer
Uses GPT-4V's multimodal perception to analyze rendered images and identify which constraints are lacking or incorrectly satisfied

**Delta**: Inner-loop with GPT-4V reviewer contributes the largest single improvement (+38.4 constraint score)
**Condition**: Inner-loop refinement for each scene

**Evidence**: "We iteratively improve the initially generated scene layout in a visual feedback loop by taking advantage of the perception capabilities of a multimodal LLM (GPT-V (OpenAI, 2023)). We render the generated scene into an image, then feed the rendered image and the scene description directly to the LLM+V-Reviewer"

## [NEUTRAL] Asset Height Canonicalization
Preprocessing step that normalizes each asset's default height to 1, with LLM predicting realistic heights during retrieval

**Delta**: Not quantified; noted as imperfect for flat objects like carpets
**Condition**: All asset imports; limitation noted for very flat objects

**Evidence**: "we add a preprocessing step to set each asset's default height to be 1 (canonicalized), and then when the LLM retrieves an asset, it will predict its height to make it realistic in the scene. We didn't do further height adjustment in the refinement procedure, so there are certain cases where some objects' heights are actually wrong"

## [NEUTRAL] Fixed 4-Step Inner-Loop Refinement
Hard-coded 4 refinement iterations without early stopping, chosen to balance quality and computational efficiency

**Delta**: More steps continue improving performance but 4 steps sufficient given a good library
**Condition**: After library is learned; early generation without library requires 10+ steps

**Evidence**: "In our refinement algorithm, the average number of iterations is hard-coded as 4 steps without early stopping. We have tried different values and find having more steps can continue improving the per-scene performance."

## [POSITIVE] Scene-Guided Video Generation
Using SceneCraft-generated 3D scenes as conditional input to a fine-tuned VideoPoet model for video generation

**Delta**: FVD 317 vs BlenderGPT 574; CLIP-based RM 46.2 vs BlenderGPT 69.1; both better than text-to-video baseline (FVD 531)
**Condition**: Sintel movie dataset with fine-tuned VideoPoet model

**Evidence**: "the generated scene helps the video generation and outperform the vanilla text-to-video baseline... SceneCraft (Dual-Loop): Scene CLIP SIM 82.7, CLIP-based RM 46.2, FVD 317"

## [POSITIVE] Universal Self-Consistency for Library Merging
Reviews all per-query function updates and finds a consensus representative to merge into the global skill library, inspired by universal self-consistency

**Delta**: Enables library generalization from 20 training queries to unseen queries
**Condition**: Outer-loop library learning over batch of queries

**Evidence**: "SceneCraft reviews all these updates, try to find one that represents the consensus of all, and merge it into the global skill library. This procedure shares similar intuition as universal self-consistency (Chen et al., 2023)."
