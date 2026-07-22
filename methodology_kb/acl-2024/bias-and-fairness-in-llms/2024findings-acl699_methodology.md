# ScaLearn: Simple and Highly Parameter-Efficient Task Transfer by Learning to Scale

**Source**: https://aclanthology.org/2024.findings-acl.699/

## [POSITIVE] SCALEARN (non-uniform scaling)
Two-stage MTL transfer layer that learns element-wise scaling vectors applied to source adapter output representations, combined via element-wise sum

**Delta**: +0.35 avg on GLUE, +2pp avg on SuperGLUE vs AdapterFusion
**Condition**: GLUE, SuperGLUE, HumSet benchmarks with RoBERTa and XLM-R encoder LMs

**Evidence**: "SCALEARN and SCALEARN++ improve upon ADAPTERFUSION by 2 percentage points of the average results [on SuperGLUE]"

## [POSITIVE] SCALEARNUNIFORM (uniform scaling)
More parameter-efficient variant where each source adapter output is scaled by a single scalar parameter instead of a vector

**Delta**: competitive with SCALEARN, outperforms AdapterFusion
**Condition**: GLUE, SuperGLUE, HumSet benchmarks

**Evidence**: "all variants of SCALEARN, including the highly parameter-efficient SCALEARNUNIFORM++ achieve similarly good results with only a fraction of the parameters of ADAPTERFUSION"

## [POSITIVE] SCALEARN++ (layer-shared non-uniform scaling)
Variant of SCALEARN that shares scaling vector parameters across all transformer layers, reducing parameters by eliminating the L (layers) factor

**Delta**: best results on SuperGLUE avg (75.74) and HumSet avg (54.48)
**Condition**: SuperGLUE and HumSet benchmarks

**Evidence**: "SCALEARN++ improve upon ADAPTERFUSION by 2 percentage points of the average results"

## [POSITIVE] SCALEARNUNIFORM++ (layer-shared uniform scaling)
Most parameter-efficient variant with only |S|×|T| total transfer parameters (64 parameters for 8 tasks), sharing scalar parameters across all layers

**Delta**: only 64 transfer parameters, competitive results vs AdapterFusion
**Condition**: GLUE, SuperGLUE benchmarks with 8 tasks using RoBERTaBASE

**Evidence**: "SCALEARNUNIFORM++ only requires 64 parameters... all variants of SCALEARN, including the highly parameter-efficient SCALEARNUNIFORM++ achieve similarly good results"

## [POSITIVE] Two-stage MTL paradigm
Separating task learning (source adapters) from transfer learning (transfer layer), allowing independent optimization per target task

**Delta**: avoids destructive transfer, less sensitive to task selection vs joint MTL
**Condition**: GLUE, SuperGLUE, HumSet benchmarks

**Evidence**: "two-stage models generally outperform other baselines... our results also show the advantage of two-stage models in avoiding destructive effects during transfer learning"

## [POSITIVE] No distributional constraint on scaling weights
SCALEARN does not force scaling coefficients to sum to 1 (no softmax), unlike AdapterFusion

**Delta**: outperforms baseline
**Condition**: contrasted with AdapterFusion's attention-based weighted sum

**Evidence**: "SCALEARN models do not force any distributional properties on the ω values, as commonly imposed in previous work (Pfeiffer et al., 2021; Chronopoulou et al., 2023; Xin et al., 2022) through functions such as softmax and average"

## [NEGATIVE] AdapterFusion attention mechanism
Two-stage MTL transfer layer using attention (query/key/value matrices) to weight source adapter outputs, introducing 3×d²×L×|T| parameters

**Delta**: ~134% new parameters (170M for 8 tasks), underperforms SCALEARN
**Condition**: RoBERTaBASE with 8 tasks on GLUE/SuperGLUE

**Evidence**: "ADAPTERFUSION introduces ~134% new parameters for transfer learning... SCALEARN and SCALEARN++ improve upon ADAPTERFUSION by 2 percentage points"

## [NEGATIVE] AdapterSoup weight averaging
Merges weights of top-5 most similar source adapters based on sentence similarity, without learning a transfer layer

**Delta**: 71.52 avg on GLUE vs 85.36 for SCALEARN; 58.73 on SuperGLUE vs 75.55 for SCALEARN
**Condition**: GLUE and SuperGLUE benchmarks

**Evidence**: "the subpar performance of AdapterSoup suggests that calculating weights using sentence similarity is not appropriate for our specific problem setup"

## [NEGATIVE] Joint MTL with HyperFormer/HyperFormer++
Joint MTL using hypernetwork to generate task-specific adapter parameters shared across tasks

**Delta**: up to -27% vs STL on SuperGLUE (HyperFormer++ vs ADAPTER)
**Condition**: SuperGLUE benchmark with RoBERTaBASE

**Evidence**: "we observe performance drops for various joint MTL models in comparison to other models (up to −27% when comparing HYPERFORMER++ and ADAPTER). This may be a signal of the sensitivity of these models to the selection of tasks"

## [NEGATIVE] Joint MTL on HumSet
All joint MTL methods applied to the multilingual HumSet benchmark

**Delta**: up to -27% for STL and MTL versions of FINETUNE
**Condition**: HumSet benchmark with XLM-RBASE

**Evidence**: "all joint MTL methods show poor performance, highlighting the sensitivity of these methods to task selection (up to −27% for STL and MTL versions of FINETUNE)"

## [POSITIVE] Few-shot transfer learning with SCALEARN
Applying SCALEARN in low-data settings with k={4,16,32,100} training samples per target task

**Delta**: consistently outperforms ADAPTER and AdapterFusion across all k values (except k=4 on HumSet)
**Condition**: GLUE, SuperGLUE, HumSet few-shot settings

**Evidence**: "SCALEARN consistently outperforms ADAPTER and ADAPTERFUSION in all benchmarks and values of k (except for k=4 on HumSet) pointing to the strength of our method for data-lean settings"

## [NEUTRAL] Adapter reduction factor of 16
Using a bottleneck reduction factor of 16 in all adapter-based models for parameter efficiency

**Delta**: not separately quantified
**Condition**: all adapter-based models across all benchmarks

**Evidence**: "In all adapter-based models, we use a reduction factor of 16, and, following Pfeiffer et al. (2021), insert the modules after the feed-forward layer of the LM"

## [NEUTRAL] Adapter insertion after feed-forward layer
Inserting adapter modules only after each feed-forward block (Pfeiffer adapter style) for all models including adapted baselines

**Delta**: not separately quantified
**Condition**: all adapter-based models; standardized for fair comparison

**Evidence**: "we adapt PROPETL-M, HYPERFORMER, and HYPERFORMER++ to this setting by inserting the adapters only after each feed-forward block"

## [POSITIVE] Element-wise sum combination of scaled representations
Combining scaled source adapter outputs via simple element-wise sum rather than weighted average or attention

**Delta**: outperforms baseline
**Condition**: all SCALEARN variants across all benchmarks

**Evidence**: "Our core contribution regards the transfer layer... SCALEARN linearly scales and combines the output representations of source adapters... to achieve the objective of target task t"

## [NEUTRAL] COMPACTER++ parameter-efficient adapter
Highly parameter-efficient STL adapter using parameter-sharing between layers via hypercomplex multiplication

**Delta**: 0.02% parameters (29K), avg 83.40 on GLUE
**Condition**: STL setting on GLUE/SuperGLUE

**Evidence**: "COMPACTER++ (Mahabadi et al., 2021a) a highly parameter-efficient variation using parameter-sharing between layers"

## [NEUTRAL] (IA)^3 scaling vectors
STL method learning scaling vectors applied to key/value matrices and feed-forward intermediate activations

**Delta**: 0.05% parameters (57K), avg 82.78 on GLUE
**Condition**: STL setting on GLUE/SuperGLUE

**Evidence**: "(_IA_)3 (Liu et al., 2022), learning scaling vectors applied to the key and value matrices and intermediate activations in the LM's feed-forward layer"
