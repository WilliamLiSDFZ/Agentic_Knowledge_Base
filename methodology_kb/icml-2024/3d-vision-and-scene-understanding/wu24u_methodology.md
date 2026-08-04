# VoroNav: Voronoi-based Zero-shot Object Navigation with Large Language Model

**Source**: https://proceedings.mlr.press/v235/wu24u.html

## [POSITIVE] Reduced Voronoi Graph (RVG) for Waypoint Selection
Extracts intersection points and viable pathways from a real-time semantic map using the Generalized Voronoi Diagram, selecting waypoints at topological intersections rich in observational data rather than at fixed intervals or frontier points.

**Delta**: +2.8% Success, +3.7% SPL on HM3D; +2.6% Success, +3.8% SPL on HSSD over best competitor
**Condition**: Zero-Shot Object Navigation on HM3D and HSSD datasets

**Evidence**: "our approach outperforms the best-performing competitor (+2.8% Success and +3.7% SPL on HM3D, +2.6% Success and +3.8% SPL on HSSD)"

## [POSITIVE] Path Description Generation
Generates textual descriptions of scenes along navigable paths by collecting objects and their coordinates from the semantic map along exploratory paths, then using GPT-3.5 to create coherent scene descriptions.

**Delta**: +1.3% Success, +0.9% SPL on HM3D; +0.3% Success, +0.8% SPL on HSSD over Voronoi baseline
**Condition**: Ablation study comparing Voro-path vs. Voronoi baseline on HM3D and HSSD

**Evidence**: "both Voro-path and Voro-farsight show higher Success and SPL than Voronoi, indicating the benefits of integrating semantic information to augment navigation capabilities"

## [POSITIVE] Farsight Description via BLIP Image Captioning
Captures panoramic RGB images at each RVG node, selects images oriented toward each neighbor node, and uses BLIP to generate captions representing the egocentric view beyond the depth camera range.

**Delta**: +2.5% Success, +1.9% SPL on HM3D; +0.5% Success, +0.5% SPL on HSSD over Voronoi baseline
**Condition**: Ablation study comparing Voro-farsight vs. Voronoi baseline on HM3D and HSSD

**Evidence**: "both Voro-path and Voro-farsight show higher Success and SPL than Voronoi, indicating the benefits of integrating semantic information to augment navigation capabilities"

## [POSITIVE] Combined Path and Farsight Descriptions (Fused Prompt)
Integrates both path descriptions (scenes along traversable paths) and farsight descriptions (egocentric view images) into a single fused prompt for LLM reasoning, mimicking human exploratory behavior from two perspectives.

**Delta**: +0.8% Success, +0.8% SPL on HM3D over Voro-farsight; +0.2% Success, +0.5% SPL on HSSD over Voro-farsight
**Condition**: Ablation study on HM3D and HSSD; full VoroNav vs. single-description variants

**Evidence**: "VoroNav exhibits superior performance compared to all ablation models, demonstrating the positive outcomes of integrating both path and farsight descriptions to enhance the performance of LLM's reasoning"

## [POSITIVE] Hierarchical Reward Mechanism
Combines exploration reward, efficiency reward, and semantic (LLM) reward in a hierarchical priority structure (1st: Exploration, 2nd: Efficiency, 3rd: Semantic) to select the next navigation waypoint among candidate neighbor nodes.

**Delta**: +3.3% Success, +2.7% SPL on HM3D; +0.7% Success, +1.0% SPL on HSSD over Voronoi (no semantic reward)
**Condition**: Global Decision Module in VoroNav on HM3D and HSSD

**Evidence**: "The neighbor node that offers the highest cumulative reward is selected as the next target waypoint for navigation... balancing the priority among these factors becomes challenging. To mitigate potential conflicts, we have implemented a hierarchical structure within the reward system."

## [POSITIVE] LLM-based Semantic Reward (GPT-3.5)
Uses GPT-3.5 to estimate the probability of the target object appearing at each candidate neighbor node based on fused scene descriptions, providing a semantic reward vector for waypoint selection.

**Delta**: +2.8% Success, +2.7% SPL on HM3D over Voronoi without semantic reward
**Condition**: Comparison of VoroNav vs. Voronoi (no LLM) on HM3D

**Evidence**: "The Global Decision Module utilizes the commonsense reasoning capabilities of the large language model, GPT-3.5, to select the most promising goal node for finding or approaching the target object among all neighbor nodes."

## [POSITIVE] Stronger LLM (GPT-4 vs. GPT-3.5)
Replacing GPT-3.5 with GPT-4 as the reasoning engine in the VoroNav framework for semantic waypoint selection.

**Delta**: +0.1% Success, +1.9% SPL, +2.0% SCA, +4.3% SEA over GPT-3.5 on HM3D sample
**Condition**: 100-episode sample from HM3D; GPT-4 vs. GPT-3.5 comparison

**Evidence**: "The VoroNav framework with a stronger LLM performs better in navigation performance."

## [NEGATIVE] Gemini-pro as LLM backbone
Using Gemini-pro instead of GPT-3.5 or GPT-4 as the reasoning engine in VoroNav.

**Delta**: -5.0% Success, -1.9% SPL vs. GPT-3.5; -5.1% Success, -1.4% SPL vs. GPT-4 on HM3D sample
**Condition**: 100-episode sample from HM3D; Gemini-pro vs. GPT-3.5/GPT-4 comparison

**Evidence**: "VoroNav with Gemini-pro achieves 41.4 Success and 24.3 SPL, compared to 46.4/23.8 for GPT-3.5 and 46.5/25.7 for GPT-4"

## [POSITIVE] Voronoi-based Navigation (without semantics) vs. Frontier-based
Using Voronoi graph nodes as waypoints (without any semantic/LLM guidance) compared to frontier-based exploration that selects nearest unexplored boundary points.

**Delta**: +5.0% Success, +8.0% SPL on HM3D; +4.3% Success, +4.5% SPL on HSSD over Frontier
**Condition**: Comparison of Voronoi vs. Frontier baseline on HM3D and HSSD

**Evidence**: "Voronoi enhances the navigation process by proceeding to informative neighbor nodes along the RVG paths, thereby pursuing to uncover larger areas with very few steps."

## [POSITIVE] Voronoi-based Obstacle Avoidance (SCA metric)
Voronoi-based waypoints are placed at intersections in unoccupied regions away from obstacles, reducing collision incidence compared to frontier-based methods.

**Delta**: SCA: 29.4 (Voronoi) vs. 24.2 (Frontier) on HM3D; 40.2 vs. 35.5 on HSSD
**Condition**: Planning study on HM3D and HSSD; SCA metric

**Evidence**: "The higher SCA score suggests that, throughout the exploration process, the mid-term goals of the Voronoi-based methods are typically chosen at intersections within unoccupied regions, which are less likely to be in proximity to obstacles, thereby reducing the incidence of collisions compared to the frontier-based methods."

## [POSITIVE] Voronoi-based Perceptual Efficiency (SEA metric)
Voronoi intersections enable broader areas to be observed with minimal movement, increasing the ratio of explored area to path length.

**Delta**: SEA: 17.9 (Voronoi) vs. 17.4 (Frontier) on HM3D; 18.6 vs. 16.5 on HSSD
**Condition**: Planning study on HM3D and HSSD; SEA metric

**Evidence**: "a higher SEA score indicates that the Voronoi-based methods favor intersections rich in information, enabling broader areas to be observed with minimal movement."

## [NEUTRAL] Grounded-SAM for Open-Set Object Detection
Uses Grounded-SAM (combining Grounding DINO and Segment Anything) to predict category masks of RGB images for semantic mapping, enabling zero-shot object detection.

**Delta**: Used as standardized vision module across compared methods for fair evaluation
**Condition**: Applied uniformly to Random Exploration, Frontier, Voronoi, and L3MVN baselines for fair comparison

**Evidence**: "To guarantee the zero-shot navigation capability of each method, we use Grounded-SAM to replace the vision modules of methods marked by an asteroid (*), which aligns with our model."

## [POSITIVE] Decision-making at Sparse Voronoi Waypoints (LLM call frequency)
LLM (GPT) is only queried at sparse RVG nodes rather than at every step, minimizing latency impact on real-time robot operation.

**Delta**: Global step time: 10.2s; Local step time: 0.75s (local step is the critical real-time bottleneck)
**Condition**: Real-time navigation deployment; time consumption analysis

**Evidence**: "we use GPT solely for decision-making at sparse waypoints (RVG nodes) during navigation, ensuring minimal impact of GPT's latency on the robot's real-time operation. The critical factor influencing real-time performance most is the time consumption of the Local step."

## [NEGATIVE] Fixed-interval Decision-making (baseline approach)
Making navigation decisions at predetermined fixed intervals or step counts, as used by L3MVN, ESC, and Pixel-Nav, rather than at topologically informative positions.

**Delta**: ESC achieves 39.2% Success / 22.3% SPL vs. VoroNav's 42.0% / 26.0% on HM3D
**Condition**: Comparison of fixed-interval methods (L3MVN, ESC, Pixel-Nav) vs. VoroNav on HM3D

**Evidence**: "These three semantic planning methods uniformly make decisions at predetermined intervals, which can lead to agents determining the mid-term goal in suboptimal positions with insufficient observations, thereby failing to fully unleash the reasoning power of LLM."

## [POSITIVE] Human-cognition-aligned Prompt Design
Designing prompts that mirror human exploratory behavior (egocentric view + scenes along paths) to align with LLM training corpora, improving LLM comprehension and reasoning quality.

**Delta**: outperforms baseline LLM-guided methods (ESC, L3MVN)
**Condition**: LLM-guided navigation; prompt engineering for GPT-3.5

**Evidence**: "Descriptions that align analogously with human cognition ensure that the resulting prompts are closer to human corpora... previous works show that LLM typically exhibits enhanced performance when dealing with natural language problems similar to the corpora."

## [NEUTRAL] Fast Marching Method for Local Path Planning
Uses the Fast Marching Method to find the shortest path from the current position to the target waypoint on the obstacle map, selecting the nearest coordinate as the immediate navigation objective.

**Delta**: Local step time: 0.75s average
**Condition**: Local Policy Module; all navigation episodes

**Evidence**: "we use the Fast Marching Method (Sethian, 1996) to find the shortest path from the current position to the target, which is composed of a sequence of discrete points in the map."

## [NEUTRAL] Wavefront Propagation for Exploratory Path Search
Uses Wavefront Propagation to obtain the shortest path from the agent node to each exploratory node on the GVD for generating path descriptions.

**Delta**: Component of the path description pipeline; no isolated delta reported
**Condition**: Path Description generation in Global Decision Module

**Evidence**: "we leverage the Wavefront Propagation method to obtain the shortest path Pj from the agent node to the jth exploratory node on the GVD"
