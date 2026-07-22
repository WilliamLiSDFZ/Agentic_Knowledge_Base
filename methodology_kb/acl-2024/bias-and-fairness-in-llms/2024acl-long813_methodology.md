# Can Large Language Models be Good Emotional Supporter? Mitigating Preference Bias on Emotional Support Conversation

**Source**: https://aclanthology.org/2024.acl-long.813/

## [POSITIVE] Strategy-Constrained Response Generation
Generating responses conditioned on a predicted or ground-truth support strategy rather than generating freely

**Delta**: outperforms baseline
**Condition**: When ground-truth strategy is provided to ChatGPT and LLaMA2-70B on ESConv

**Evidence**: "if the model can predict strategies correctly, there is significant room for improvement in the quality of emotional support response"

## [POSITIVE] Ground-Truth Strategy Conditioning
Using the correct ground-truth strategy to condition response generation instead of predicted or no strategy

**Delta**: ROUGE-L 17.16 vs 15.25 (no strategy) for ChatGPT; Satisfaction 4.06 vs 3.94
**Condition**: ChatGPT and LLaMA2-70B on ESConv response generation

**Evidence**: "The responses based on correct strategy (ground-truth strategy) outperforms those generated without strategy"

## [NEGATIVE] Self-Contact: Direct-Refine
Refining the initially generated response by instructing the model to revise its own output to incorporate emotional support elements

**Delta**: Q drops from 13.50 to 13.40, B increases from 1.38 to 1.60 for ChatGPT
**Condition**: Applied to ChatGPT and LLaMA2-70B on ESConv strategy prediction

**Evidence**: "the results of self-contact methods present a noticeable pattern in which proficiency declines and preference bias becomes more pronounced"

## [NEGATIVE] Self-Contact: Self-Refine
Generating self-feedback on the initial response emphasizing emotional support, then refining the response based on that feedback

**Delta**: Q drops from 13.50 to 12.37, B increases from 1.38 to 1.53 for ChatGPT; poor-quality responses increase from 16.7% to 17.4%
**Condition**: Applied to ChatGPT and LLaMA2-70B on ESConv strategy prediction

**Evidence**: "when LLMs have bias, thinking alone can deepen those bias, indicating that self-contact methods do not contribute to enhancing their capabilities to become better emotional supporters"

## [NEGATIVE] Self-Contact: Emotional-CoT
Chain-of-thought prompting that first generates user states as a reasoning path before generating strategy and response

**Delta**: Q drops from 13.50 to 9.55, B increases from 1.38 to 1.56 for ChatGPT
**Condition**: Applied to ChatGPT and LLaMA2-70B on ESConv strategy prediction

**Evidence**: "the results of self-contact methods present a noticeable pattern in which proficiency declines and preference bias becomes more pronounced"

## [NEGATIVE] Iterative Self-Refinement
Applying Direct-Refine or Self-Refine iteratively over multiple rounds

**Delta**: preference for initially preferred strategies grows with each iteration while dispreferred strategies become further dispreferred
**Condition**: Iterative Direct-Refine and Self-Refine applied to ChatGPT

**Evidence**: "we observe a trend where, as the iterations continue, there is a growing preference for strategy that is initially preferred (i.e., pi > 1). In contrast, the preference for strategies that are initially dispreferred (i.e., pi < 1) tends to diminish over successive iterations"

## [POSITIVE] External-Contact: COMET Commonsense Knowledge
Augmenting LLM prompts with filtered commonsense knowledge from COMET-BART using five relation types (xReact, xIntent, xNeed, xEffect, xWant)

**Delta**: B reduces from 1.38 to 0.95 for ChatGPT; Satisfaction win rate 52.1% vs vanilla ChatGPT
**Condition**: Applied to ChatGPT and LLaMA2-70B on ESConv

**Evidence**: "the application of external-contact methods mostly results in a reduction of preference bias on both closed- and open-source LLMs"

## [POSITIVE] External-Contact: Example Expansion (n-shot)
Increasing the number of randomly selected few-shot examples in the prompt beyond the baseline 2-shot setting

**Delta**: Q improves from 13.50 to 16.91, B reduces from 1.38 to 0.82 for ChatGPT; BLEU-2 improves to 7.45
**Condition**: Applied to ChatGPT and LLaMA2-70B; optimal at moderate n, degrades for n > 8

**Evidence**: "receiving assistance from a fine-tuned strategy planner (w/ Strategy Planner) or having more examples (w/ Example Expansion) seems to be more helpful than relying on commonsense knowledge"

## [NEGATIVE] Too Many Few-Shot Examples (n > 8)
Using a very large number of in-context examples (more than 8) in the prompt

**Delta**: preference bias B worsens significantly with n > 8
**Condition**: ChatGPT with example expansion on ESConv

**Evidence**: "while proficiency Q converges as n increases, preference bias B worsens significantly with larger values of n (n > 8), indicating that too many examples may be detrimental"

## [POSITIVE] External-Contact: Fine-Tuned Strategy Planner
A separately fine-tuned LLaMA2-7B classification model that predicts the next support strategy, whose output is then used to condition the LLM response generation

**Delta**: Q improves from 13.50 to 21.09, B reduces from 1.38 to 0.36 for ChatGPT; Satisfaction win rate 61.1%; poor-quality responses reduce from 16.7% to 8.0%
**Condition**: Applied to ChatGPT and LLaMA2-70B on ESConv; single planner used for both models

**Evidence**: "responses generated through the strategy planner, which exhibits the most significant improvements in preference bias, are the most helpful in reducing the seeker's emotional intensity"

## [POSITIVE] LLM-Based Strategy Planner Backbone
Using a generative LLM (e.g., LLaMA2-7B, Mistral) as the backbone for the strategy planner rather than an encoder-only model

**Delta**: LLaMA2-7B planner: Q=21.10, B=0.36; vs BERT: Q=18.02, B=0.50; vs RoBERTa: Q=21.01, B=0.60
**Condition**: Comparison of strategy planner backbones on ESConv test sets

**Evidence**: "using LLMs as the backbone model for the strategy planner leads to notable enhancements in proficiency and preference bias"

## [NEUTRAL] Encoder-Based Strategy Planner (BERT/RoBERTa)
Using encoder-only models (BERT or RoBERTa) fine-tuned as strategy planners

**Delta**: BERT: Q=18.02, B=0.50; RoBERTa: Q=21.01, B=0.60; comparable proficiency but higher preference bias than LLM-based planners
**Condition**: Used as strategy planner backbone on ESConv

**Evidence**: "while encoder-based models achieve performance comparable to LLMs, they exhibit relatively higher preference bias, indicating weaker robustness and potentially providing poor-quality emotional support"

## [POSITIVE] Strategy Description in Prompt
Including natural language descriptions of each support strategy in the prompt to enhance the model's understanding

**Delta**: outperforms baseline
**Condition**: Applied to all LLMs evaluated on ESConv

**Evidence**: "In the prompt, we include strategy descriptions to enhance the understanding of each strategy"

## [NEUTRAL] Random Few-Shot Example Selection
Randomly selecting few-shot examples with non-overlapping strategies to prevent strategy bias from example selection

**Delta**: strategy type in examples does not significantly impact results
**Condition**: 2-shot prompting for ChatGPT on ESConv

**Evidence**: "Figure 6b reveals consistent results across the diverse combinations. In summary, providing the appropriate number of examples may enhance preference bias, whereas the type of strategies within each example does not matter"

## [NEGATIVE] High Preference Bias in LLMs
LLMs exhibiting strong preference for specific strategies (e.g., Affirmation and Reassurance) over others, measured as standard deviation of Bradley-Terry preference scores

**Delta**: GPT-4 and ChatGPT show B~1.38-1.60; poor-quality responses at 16.7-21.2%
**Condition**: Observed across all evaluated LLMs on ESConv

**Evidence**: "exhibiting high preference for specific strategies hinders effective emotional support, aggravating its robustness in predicting the appropriate strategy"

## [POSITIVE] Low Preference Bias
Models exhibiting relatively uniform preference across strategies, leading to more robust performance across all conversation stages

**Delta**: LLaMA2-70B with B=0.47 shows more robust performance across D1/D2/D3 than GPT-4
**Condition**: Observed in LLaMA2-70B compared to GPT-4 on ESConv stage-specific test sets

**Evidence**: "LLaMA2-70B demonstrates relatively uniform preferences for strategies, leading to robust performance across Dt"

## [POSITIVE] 2-Shot Prompting for Open-Source LLMs
Providing 2 in-context examples to open-source LLMs to help them adhere to the desired output format

**Delta**: actual proficiency of open-source LLMs without examples may be worse than reported scores
**Condition**: Applied to LLaMA2-7B/70B, Vicuna, Solar, Mistral, Tulu on ESConv

**Evidence**: "We include 2-shot examples for open-source LLMs as they often struggle to adhere to the desired output format (e.g., wrong strategy that is not among the eight provided)"

## [POSITIVE] Oracle Strategy with LLM Response Generation
Providing the perfect ground-truth strategy to LLMs for response generation, representing an upper bound

**Delta**: poor-quality responses reduce to 3.8%; Satisfaction score 4.06 vs 3.94 (no strategy) for ChatGPT
**Condition**: ChatGPT and LLaMA2-70B on ESConv; residual failures indicate response generation is also a bottleneck

**Evidence**: "even when using an oracle strategy in LLMs (Table 8), responses that increase emotional intensity still exist (3.8%). This indicates a lack of ability to generate appropriate responses for emotional support, even when the strategy is perfectly selected"
