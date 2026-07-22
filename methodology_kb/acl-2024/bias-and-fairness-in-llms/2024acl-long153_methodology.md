# On Context Utilization in Summarization with Large Language Models

**Source**: https://aclanthology.org/2024.acl-long.153/

## [NEGATIVE] Lead Bias in LLM Summarization
LLMs disproportionately focus on content at the beginning of source documents when generating summaries, showing stronger lead bias than even reference summaries

**Delta**: statistically significant difference (p-value < 0.001) in bigram distribution between LLMs and references in 51 out of 55 (dataset, LLM) setups
**Condition**: Across 6 LLMs and 10 summarization datasets, especially on XSum, Reddit-TIFU, Arxiv, PubMed and GovReport

**Evidence**: "all summarization datasets except XSum, and Reddit-TIFU show some lead bias: salient bigrams from the reference are more likely to be found at the beginning of the source. However, LLMs show a significantly stronger lead bias on all datasets: bigrams from LLMs summaries are much more likely to be found in the first 20% words of the source."

## [NEGATIVE] Middle Curse / U-Shape Context Utilization
LLMs exhibit a U-shaped performance pattern where they focus on the beginning and end of their context window, largely ignoring the middle, leading to degraded summarization when salient information is in the middle

**Delta**: Performance can fall below random chance range, especially for reference-free metrics
**Condition**: Multi-document summarization on Multi-XScience and Multi-News; also observed on PubMed and SummScreenFD for all LLMs

**Evidence**: "LLMs can focus on the beginning and/or the end of their input, but largely ignore the middle. The U-shape or middle curse from Liu et al. (2023a) also applies to abstractive summarization."

## [POSITIVE] Hierarchical Summarization Inference
Divides input into k consecutive blocks, summarizes each block independently, then summarizes the concatenation of those summaries to alleviate the middle curse

**Delta**: Improves performance significantly on Mistral-7B on MiddleSum; very effective on scientific publications domain
**Condition**: Effective on scientific paper datasets (Arxiv, PubMed); less effective or harmful on other domains; lags behind Focus Prompt with GPT-3.5

**Evidence**: "Both alternative methods show promising results on open-source LLMs, notably on Mistral-7B for which they improve performance significantly. Across domains, hierarchical and incremental inference are very effective on scientific publications."

## [POSITIVE] Incremental Summarization Inference
Iteratively updates a running summary by processing consecutive blocks of the input, incorporating new content from each block into the existing summary

**Delta**: Improves performance significantly on Mistral-7B on MiddleSum; very effective on scientific publications domain
**Condition**: Effective on scientific paper datasets; less effective or harmful on other domains; lags behind Focus Prompt with GPT-3.5

**Evidence**: "Both alternative methods show promising results on open-source LLMs, notably on Mistral-7B for which they improve performance significantly. Across domains, hierarchical and incremental inference are very effective on scientific publications."

## [POSITIVE] Focus Prompt
Adding the instruction 'Please also pay attention to the middle section of the input when constructing the summary' to the prompt to alleviate the middle curse

**Delta**: Outperforms hierarchical and incremental summarization with GPT-3.5 on MiddleSum
**Condition**: Applied to GPT-3.5 on MiddleSum benchmark; comparison against hierarchical and incremental methods

**Evidence**: "they are not successful and lag behind Focus Prompt with GPT-3.5"

## [NEGATIVE] Scaling Context Window Beyond 4k Tokens
Extending the LLM context window beyond 4k tokens for long-input summarization, using methods like position interpolation or models with larger native context windows

**Delta**: All metrics plateau or even decrease (see Mistral-7B) from 4k context window upwards
**Condition**: Long-input summarization on Arxiv and GovReport with Xgen-7B, Mistral-7B, GPT-3.5, Vicuna-7B-1.5-16k, and Llama-2-7B-32k

**Evidence**: "Results on Arxiv and GovReport confirm our intuition: all metrics plateau or even decrease (see Mistral-7B) from 4k context window upwards... Our results suggest that in the current LLMs inference and evaluation framework, there is no need to exceed 4k tokens in the context window for open-source model."

## [POSITIVE] Position Interpolation for Context Extension
Using position interpolation (e.g., Vicuna-7B-1.5-16k and Llama-2-7B-32k) to extend the context window of Llama-2-7B to 16k and 32k tokens respectively

**Delta**: Both position interpolated models show more robustness compared to base models when scaling context length
**Condition**: Long-input summarization on Arxiv and GovReport when varying truncated maximum source length from 2k to 12k tokens

**Evidence**: "Both position interpolated models show more robustness; while GPT-3.5 seems to plateau at 8k tokens."

## [NEUTRAL] Decoding Method Variation (Greedy, Top-k, Top-p)
Comparing different decoding strategies: greedy decoding, top-k sampling (k=50, T=0.3), and top-p sampling (p=0.95, T=1.0) to assess their impact on position bias

**Delta**: No measurable difference in position bias across decoding methods
**Condition**: Tested on Llama-2-7B and XGen-7B on Arxiv and GovReport datasets

**Evidence**: "the decoding method does not affect position bias: for all setups, the LLMs show similar patterns as with our previous default decoding method. We conclude that the middle curse is independent from the decoding method."

## [POSITIVE] Instruction Tuning (Flan-T5 style)
Fine-tuning LLMs on instruction-following datasets (e.g., Flan) to improve alignment with task prompts; Flan-UL2 uses Flan-T5 instruction fine-tuning on top of UL2

**Delta**: Flan-UL2 closely matches the reference bigram distribution on XSum; dominates on standard-length datasets
**Condition**: Standard-length summarization datasets; Flan-UL2 is excluded from long-input datasets due to very poor performance caused by its 2k token context window limit

**Evidence**: "On XSum, Flan-UL2 closely matches the reference distribution, which we attribute to its better instruction tuning... Flan-UL2 dominates on standard-length datasets."

## [NEUTRAL] Filling Middle Context with Random/Irrelevant Documents
In multi-document summarization, replacing middle documents with random irrelevant documents while keeping the first and last documents salient, to test LLM robustness to middle content

**Delta**: Llama-2-13B maintains 98% of its performance with 5 random documents between first and last; GPT-3.5 score of 4.31 vs 4.35 with all documents on Multi-XScience
**Condition**: Multi-document summarization on Multi-XScience (7 docs) and Multi-News (5 docs)

**Evidence**: "filling with random noise between the first and last document (which amounts to a prompt mostly irrelevant to the reference) leads to a moderate drop in performance. For instance, on Multi-XScience, with 5 random documents between the first and last, Llama-2-13B maintains 98% of its performance."

## [NEGATIVE] GPT-3.5 as Summarization Evaluator
Using GPT-3.5 as a reference-free evaluation metric by prompting it to score summaries on a Likert scale from 1 to 5

**Delta**: GPT-3.5 evaluator shows strong negative Spearman correlation (-0.342 average) for Xgen-7B on long-input datasets, suggesting it is itself affected by the middle curse
**Condition**: Evaluation of long-input summarization; particularly unreliable when salient content is in the middle of the context

**Evidence**: "since GPT-3.5 itself is affected by the middle-curse from Liu et al. (2023a), it may not accurately evaluate summarization when salient content lays in the middle of the context."

## [NEGATIVE] Reference-Based Metrics (ROUGE-2, BERTScore, A3CU)
Using reference-based automatic metrics to evaluate summarization quality; these metrics show consistent negative correlation with position of salient information

**Delta**: Negative Spearman correlations consistently across datasets and models (e.g., Flan-UL2 ROUGE-2 average -0.128 on standard, -0.098 on long; BERTScore -0.187 and -0.132 respectively)
**Condition**: Across all 6 LLMs and both standard-length and long-input datasets

**Evidence**: "on standard-length datasets, reference-based evaluation metrics are negatively correlated to position of salient information. The correlation is only moderate, yet remarkably consistent across datasets (except Reddit-TIFU) and models."

## [NEUTRAL] Reference-Free Metrics (SummaC)
Using SummaC factual consistency metric as a reference-free evaluation; shows positive or no significant correlation with salient information position on standard datasets but switches to negative on long-input datasets for some models

**Delta**: Positive average Spearman correlation on standard datasets (e.g., Llama-2-7B: 0.293) but negative on long-input for Xgen-7B (-0.125) and Mistral-7B (-0.141)
**Condition**: Standard-length vs. long-input summarization datasets; behavior differs by model and dataset length

**Evidence**: "reference-free metrics show either no significant or positive correlation to information position. For long-input datasets... SummaC and GPT-3.5 tend to switch from positive to negative correlation, especially for Xgen-7B and Mistral-7B."

## [NEGATIVE] Base vs. Instruction-Tuned Models
Comparing base (non-instruction-tuned) LLMs against instruction-tuned chat variants for position bias analysis

**Delta**: Even stronger position bias with base models
**Condition**: Position bias analysis across summarization datasets

**Evidence**: "Results in Appendix E confirm an even stronger position bias with base models."

## [NEGATIVE] MiddleSum Evaluation Benchmark
A curated evaluation dataset of 225 samples from 5 long-input summarization datasets where salient information is concentrated in the middle of the context (earliest aligned source sentence starts at least 1,200 words in)

**Delta**: LLMs perform noticeably worse on MiddleSum compared to the full dataset sets
**Condition**: Evaluation benchmark specifically designed to expose the middle curse in long-input summarization

**Evidence**: "we see that LLMs perform noticeably worse on MiddleSum (green bars) as compared to the full set (gray bars), confirming that MiddleSum is a more challenging task."
