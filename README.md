# AI Research Papers by Topic

> A curated directory of notable AI research papers, organized by research topic. Conference and year are shown on each paper entry.
> The list structure is inspired by [papers_for_protein_design_using_DL](https://github.com/Peldom/papers_for_protein_design_using_DL).

**Last updated:** 2026-11-14T22:11:02+08:00  
**Coverage:** major AI conferences from 2024 onward · 494 selected papers  
**Entry format:** paper · conference and year · topic · short summary

## Contents

- [Language Models and NLP](#language-models-and-nlp)
- [AI Agents and Tools](#ai-agents-and-tools)
- [AI for Science and Biology](#ai-for-science-and-biology)
- [Computer Vision and Graphics](#computer-vision-and-graphics)
- [Speech and Audio](#speech-and-audio)
- [Multimodal Learning](#multimodal-learning)
- [Robotics and Embodied AI](#robotics-and-embodied-ai)
- [Reinforcement Learning and Decision-Making](#reinforcement-learning-and-decision-making)
- [Generative Models and World Models](#generative-models-and-world-models)
- [Representation Learning and Clustering](#representation-learning-and-clustering)
- [Theory and Optimization](#theory-and-optimization)
- [Trustworthy AI and Safety](#trustworthy-ai-and-safety)
- [AI Systems and Efficiency](#ai-systems-and-efficiency)
- [Datasets and Evaluation](#datasets-and-evaluation)
- [Graph Learning](#graph-learning)
- [Other AI Research](#other-ai-research)

---

> This is a curated selection, not a complete proceedings dump. It combines papers selected through public review records, notable conference presentations, awards, and citation signals when other signals are available. Coverage depends on the fields exposed by each venue-year source; an empty venue-year does not mean that no notable papers were published there. Numeric review ratings and their pre- or post-rebuttal snapshots are retained in the data files and are not displayed here.

## Language Models and NLP

- **[Books, Copyright, and the Future of Foundation Models: An Empirical Study of Fiction in Pretraining](https://openreview.net/forum?id=NpBFkL2BTm)** — *ICLR 2027 · Under review*
  - **Topic:** Pretraining data and copyright
  - **Summary:** Trains controlled 1B-parameter models to compare web text, public-domain books, and contemporary fiction as pretraining data, including their effects on creative-writing performance.

- **[Context Language Models](https://openreview.net/forum?id=U1ObEVC4A7)** — *ICLR 2027 · Under review*
  - **Topic:** Context management and agent memory
  - **Summary:** Treats context as an editable file managed by the language model, extending the approach to multi-agent contexts. The authors report better accuracy with lower compute on long-context and long-horizon tasks.

- **[Latent Taxonomies: How Property Induction Develops in Language Model Pre-training](https://openreview.net/forum?id=m5TLPK0U7O)** — *ICLR 2027 · Under review*
  - **Topic:** Category induction in language models
  - **Summary:** Continues pretraining models of different sizes on synthetic hierarchical facts. Properties transfer more readily within latent categories, and corresponding hierarchical structures emerge in model representations.

- **[Matryoshka Language Model Suites](https://openreview.net/forum?id=IgVNSa3MMg)** — *ICLR 2027 · Under review*
  - **Topic:** Efficient language-model training and inference
  - **Summary:** Nests language models of different sizes in one jointly trained architecture to reduce training costs and uses the embedded smaller model to improve speculative-decoding throughput.

- **[Periodic Weak Spots: Phase Sensitivity from Chunked KV-Cache Compression](https://openreview.net/forum?id=2dhoYgHiC2)** — *ICLR 2027 · Under review*
  - **Topic:** Long-context inference and KV-cache compression
  - **Summary:** Finds that retrieval under chunked KV-cache compression depends on a token's position relative to compression boundaries. Different phases can produce substantial accuracy differences.

- **[EDIT-Bench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits](https://openreview.net/forum?id=FtL9eEmU6v)** — *ICLR 2026 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We propose a new benchmark for evaluating an LLM's ability to perform code edits. Our data is gathered from in-the-wild code edits, leading to more realistic problems.

- **[From Markov to Laplace: How Mamba In-Context Learns Markov Chains](https://openreview.net/forum?id=kmK3WSCOCT)** — *ICLR 2026 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We uncover an interesting phenomenon where a single-layer Mamba represents the Bayes optimal Laplacian smoothing estimator when trained on Markov chains and we demonstrate it theoretically and empirically.

- **[Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments](https://openreview.net/forum?id=9gw03JpKK4)** — *ICLR 2026 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Gaia2 evaluates LLM agents in asynchronous, dynamic environments with action-level verification, revealing fundamental trade-offs between reasoning, speed, and robustness.

- **[GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training](https://openreview.net/forum?id=N9qIqvanBj)** — *ICLR 2026*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This paper presents GeoPT as a unified model pre-trained from large-scale geometries for general physics simulation.

- **[Hubble: a Model Suite to Advance the Study of LLM Memorization](https://openreview.net/forum?id=ZfdnZhOP0k)** — *ICLR 2026 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Hubble is a suite of paired LLMs (largest 8B), where the perturbed models are trained in the same way as standard models but with text (e.g. book passages, biographies, and test sets) inserted and designed to emulate key memorization risks.

- **[LLMs Get Lost In Multi-Turn Conversation](https://openreview.net/forum?id=VKGTGGcwl6)** — *ICLR 2026 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We discover that when LLMs take a wrong turn in a conversation, they get lost and do not recover.

- **[Transducing Language Models](https://openreview.net/forum?id=qOyF214xmg)** — *ICLR 2026 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We present a method for converting a language model over one set of tokens into a language model over another set of tokens

- **[3ViewSense: Spatial and Mental Perspective Reasoning from Orthographic Views in Vision-Language Models](https://openreview.net/forum?id=Hm8OEDKpiO)** — *ICML 2026 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Current Large Language Models have achieved Olympiad-level logic, yet Vision-Language Models paradoxically falter on elementary spatial tasks like block counting. This capability mismatch reveals a critical "spatial intelligence gap," where models fail to construct coherent 3D mental representations from 2D observations.

- **[A Constrained Optimization Perspective of Unrolled Transformers](https://openreview.net/forum?id=aYe8j2jOmK)** — *ICML 2026 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce a constrained optimization framework for training transformers that behave like optimization descent algorithms. Specifically, we enforce layerwise descent constraints on the objective function and replace standard empirical risk minimization (ERM) with a primal-dual training scheme.

- **[A Mechanistic Investigation of Theory of Mind in a Large Language Model](https://openreview.net/forum?id=z3sn6b2Hk3)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models successfully solve classic theory-of-mind tasks adapted from cognitive science, but the mechanisms underlying this ability remain unclear. Do they deploy circuitry specialized for reasoning about other minds, memorize common false-belief vignette structures and outputs, or rely on more domain-general computations?

- **[A Solvable Model of Chain-of-Thought in In-Context Learning](https://openreview.net/forum?id=B3HqjP2biY)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Chain-of-thought (CoT) reasoning has become a widely used mechanism for eliciting multi-step reasoning in large language models by generating intermediate reasoning steps at inference time. Yet the scaling behavior of generalization with CoT depth remains poorly understood.

- **[Cobra: Extending Mamba to Multi-Modal Large Language Model for Efficient Inference](https://ojs.aaai.org/index.php/AAAI/article/view/33131)** — *AAAI 2025*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In recent years, applying multi-modal large language models (MLLMs) in various fields has achieved remarkable success. However, as the foundation model for many downstream tasks, MLLMs comprise the well-known Transformer network, which has a less efficient quadratic computation complexity.

- **[FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts](https://ojs.aaai.org/index.php/AAAI/article/view/34568)** — *AAAI 2025*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Vision-Language Models (LVLMs) signify a groundbreaking paradigm shift within the Artificial Intelligence (AI) community, extending beyond the capabilities of Large Language Models (LLMs) by assimilating additional modalities (e.g., images). Despite this advancement, the safety of LVLMs remains adequately underexplored, with a potential overreliance on the safety assurances purported by their underlying LLMs.

- **[LiDAR-LLM: Exploring the Potential of Large Language Models for 3D LiDAR Understanding](https://ojs.aaai.org/index.php/AAAI/article/view/33001)** — *AAAI 2025*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recently, Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) have shown promise in instruction following and image understanding. While these models are powerful, they have not yet been developed to comprehend the more challenging 3D geometric and physical scenes, especially when it comes to the sparse outdoor LiDAR data.

- **[A New Formulation of Zipf’s Meaning-Frequency Law through Contextual Diversity](https://aclanthology.org/2025.acl-long.744/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This paper proposes formulating Zipf’s meaning-frequency law, the power law between word frequency and the number of meanings, as a relationship between word frequency and contextual diversity. The proposed formulation quantifies meaning counts as contextual diversity, which is based on the directions of contextualized word vectors obtained from a Language Model (LM).

- **[A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive](https://aclanthology.org/2025.acl-long.1454/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are increasingly utilized in autonomous decision-making, where they sample options from vast action spaces. However, the heuristics that guide this sampling process remain under-explored.

- **[All That Glitters is Not Novel: Plagiarism in AI Generated Research](https://aclanthology.org/2025.acl-long.1249/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Automating scientific research is considered the final frontier of science. Recently, several papers claim autonomous research agents can generate novel research ideas.

- **[Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral](https://aclanthology.org/2025.acl-long.294/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Moral reasoning is a complex cognitive process shaped by individual experiences and cultural contexts and presents unique challenges for computational analysis. While natural language processing (NLP) offers promising tools for studying this phenomenon, current research lacks cohesion, employing discordant datasets and tasks that examine isolated aspects of moral reasoning.

- **[Between Circuits and Chomsky: Pre-pretraining on Formal Languages Imparts Linguistic Biases](https://aclanthology.org/2025.acl-long.478/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Pretraining language models on formal language can improve their acquisition of natural language. Which features of the formal language impart an inductive bias that leads to effective transfer?

- **[Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention](https://aclanthology.org/2025.acl-long.270/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have shown remarkable capabilities in natural language processing but exhibit significant performance gaps among different languages. Most existing approaches to address these disparities rely on pretraining or fine-tuning, which are resource-intensive.

- **[Byte Latent Transformer: Patches Scale Better Than Tokens](https://aclanthology.org/2025.acl-long.453/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce the Byte Latent Transformer (BLT), a new byte-level LLM architecture that, for the first time, matches tokenization-based LLM performance at scale with significant improvements in inference efficiency and robustness. BLT encodes bytes into dynamically sized patches, which serve as the primary units of computation.

- **[HALoGEN: Fantastic LLM Hallucinations and Where to Find Them](https://aclanthology.org/2025.acl-long.71/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Despite their impressive ability to generate high-quality and fluent text, generative large language models (LLMs) also produce hallucinations: statements that are misaligned with established world knowledge or provided input context. However, measuring hallucination can be challenging, as having humans verify model generations on-the-fly is both expensive and time-consuming.

- **[Language Models Resist Alignment: Evidence From Data Compression](https://aclanthology.org/2025.acl-long.1141/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) may exhibit unintended or undesirable behaviors. Recent works have concentrated on aligning LLMs to mitigate harmful outputs.

- **[Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs](https://aclanthology.org/2025.acl-long.791/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We observe a novel phenomenon, *contextual entrainment*, across a wide range of language models (LMs) and prompt settings, providing a new mechanistic perspective on how LMs become distracted by “irrelevant” contextual information in the input prompt. Specifically, LMs assign significantly higher logits (or probabilities) to any tokens that have previously appeared in the context prompt, even for random tokens.

- **[LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts](https://aclanthology.org/2025.acl-long.1207/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Safety concerns in large language models (LLMs) have gained significant attention due to their exposure to potentially harmful data during pre-training. In this paper, we identify a new safety vulnerability in LLMs: their susceptibility to natural distribution shifts between attack prompts and original toxic prompts, where seemingly benign prompts, semantically related to harmful content, can bypass safety mechanisms.

- **[MaCP: Minimal yet Mighty Adaptation via Hierarchical Cosine Projection](https://aclanthology.org/2025.acl-long.1006/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We present a new adaptation method MaCP, Minimal yet Mighty adaptive Cosine Projection, that achieves exceptional performance while requiring minimal parameters and memory for fine-tuning large foundation models.Its general idea is to exploit the superior energy compaction and decorrelation properties of cosine projection to improve both model efficiency and accuracy.Specifically, it projects the weight change from the low-rank...

- **[Mapping 1,000+ Language Models via the Log-Likelihood Vector](https://aclanthology.org/2025.acl-long.1584/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** To compare autoregressive language models at scale, we propose using log-likelihood vectors computed on a predefined text set as model features. This approach has a solid theoretical basis: when treated as model coordinates, their squared Euclidean distance approximates the Kullback-Leibler divergence of text-generation probabilities.

- **[Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models](https://aclanthology.org/2025.acl-long.533/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The composition of pre-training datasets for large language models (LLMs) remains largely undisclosed, hindering transparency and efforts to optimize data quality—a critical driver of model performance. Current data selection methods, such as natural language quality assessments, diversity-based filters, and classifier-based approaches, are limited by single-dimensional evaluation or redundancy-focused strategies.

- **[MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Long Context Understanding (LCU) is a critical area for exploration in current large language models (LLMs). However, due to the inherently lengthy nature of long-text data, existing LCU benchmarks for LLMs often result in prohibitively high evaluation costs, like testing time and inference expenses.

- **[Palm: A Culturally Inclusive and Linguistically Diverse Dataset for Arabic LLMs](https://aclanthology.org/2025.acl-long.1579/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** As large language models (LLMs) become increasingly integrated into daily life, ensuring their cultural sensitivity and inclusivity is paramount. We introduce PALM, a year-long community-driven project covering all 22 Arab countries.

- **[Past Meets Present: Creating Historical Analogy with Large Language Models](https://aclanthology.org/2025.acl-long.200/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Historical analogies, which compare known past events with contemporary but unfamiliar events, are important abilities that help people make decisions and understand the world. However, research in applied history suggests that people have difficulty finding appropriate analogies.

- **[Pre3: Enabling Deterministic Pushdown Automata for Faster Structured LLM Generation](https://aclanthology.org/2025.acl-long.551/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Extensive LLM applications demand efficient structured generations, particularly for LR(1) grammars, to produce outputs in specified formats (e.g., JSON). Existing methods primarily parse LR(1) grammars into a pushdown automaton (PDA), leading to runtime execution overhead for context-dependent token processing, especially inefficient under large inference batches.To address these issues, we propose Pre3 that exploits deterministic...

- **[Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](https://aclanthology.org/2025.acl-long.1356/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recently, scaling test-time compute on Large Language Models (LLM) has garnered wide attention. However, there has been limited investigation of how various reasoning prompting strategies perform as scaling.

- **[Revisiting Compositional Generalization Capability of Large Language Models Considering Instruction Following Ability](https://aclanthology.org/2025.acl-long.1508/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In generative commonsense reasoning tasks such as CommonGen, generative large language models (LLMs) compose sentences that include all given concepts. However, when focusing on instruction-following capabilities, if a prompt specifies a concept order, LLMs must generate sentences that adhere to the specified order.

- **[SubLIME: Subset Selection via Rank Correlation Prediction for Data-Efficient LLM Evaluation](https://aclanthology.org/2025.acl-long.1477/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The rapid expansion of Large Language Models (LLMs) and natural language processing datasets has made exhaustive benchmark evaluations computationally prohibitive. Inspired by high-stakes competitions like the International Mathematical Olympiad-where a few well-chosen problems suffice to differentiate top performers—we present SubLIME, which reduces evaluation costs by 80% to 99% while preserving ranking fidelity.

- **[The AI Gap: How Socioeconomic Status Affects Language Technology Interactions](https://aclanthology.org/2025.acl-long.914/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Socioeconomic status (SES) fundamentally influences how people interact with each other and, more recently, with digital technologies like large language models (LLMs). While previous research has highlighted the interaction between SES and language technology, it was limited by reliance on proxy metrics and synthetic data.

- **[Towards the Law of Capacity Gap in Distilling Language Models](https://aclanthology.org/2025.acl-long.1097/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language model (LM) distillation aims at distilling the knowledge in a large teacher LM to a small student one. As a critical issue facing LM distillation, a superior student often arises from a teacher of a relatively small scale instead of a larger one, especially in the presence of substantial capacity gap between the teacher and student.

- **[Turning Trash into Treasure: Accelerating Inference of Large Language Models with Token Recycling](https://aclanthology.org/2025.acl-long.338/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The rapid growth in the parameters of LLMs has made inference latency a fundamental bottleneck. Speculative decoding represents a lossless approach to accelerate inference through a guess-and-verify paradigm.

- **[Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning](https://openreview.net/forum?id=dNW3RGW0gi)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Discovering efficient algorithms for solving complex problems has been an outstanding challenge in mathematics and computer science, requiring substantial human expertise over the years. Recent advancements in evolutionary search with large language models (LLMs) have shown promise in accelerating the discovery of algorithms across various domains, particularly in mathematics and optimization.

- **[Can LLM "Self-report"?: Evaluating the Validity of Self-report Scales in Measuring Personality Design in LLM-based Chatbots](https://openreview.net/forum?id=xqIwK9mNkj)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** A chatbot’s personality design is key to interaction quality. As chatbots evolved from rule-based systems to those powered by large language models (LLMs), evaluating the effectiveness of their personality design has become increasingly complex, particularly due to the open-ended nature of interactions.

- **[Can Performant LLMs Be Ethical? Quantifying the Impact of Web Crawling Opt-Outs](https://openreview.net/forum?id=a6QsOjr3wo)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The increasing adoption of web crawling opt-outs by copyright holders of online content raises critical questions about the impact of data compliance on large language model (LLM) performance. However, little is known about how these restrictions (and the resultant filtering of pretraining datasets) affect the capabilities of models trained using these corpora.

- **[EvalTree: Profiling Language Model Weaknesses via Hierarchical Capability Trees](https://openreview.net/forum?id=aV2hQN9vkp)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** An ideal model evaluation should achieve two goals: identifying where the model fails and providing actionable improvement guidance. Toward these goals for language model (LM) evaluations, we formulate the problem of generating a weakness profile, a set of weaknesses expressed in natural language, given an LM's performance on every individual instance in a benchmark.

- **[Fast Controlled Generation from Language Models with Adaptive Weighted Rejection Sampling](https://openreview.net/forum?id=3BmPSFAdq3)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The dominant approach to generating from language models subject to some constraint is locally constrained decoding (LCD), incrementally sampling tokens at each time step such that the constraint is never violated. Typically, this is achieved through token masking: looping over the vocabulary and excluding non-conforming tokens.

- **[FineWeb2: One Pipeline to Scale Them All — Adapting Pre-Training Data Processing to Every Language](https://openreview.net/forum?id=jnRBe6zatP)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Pre-training state-of-the-art large language models (LLMs) requires vast amounts of clean and diverse text data. While the open development of large high-quality English pre-training datasets has seen substantial recent progress, training performant multilingual LLMs remains a challenge, in large part due to the inherent difficulty of tailoring filtering and deduplication pipelines to a large number of languages.

- **[Fluid Language Model Benchmarking](https://openreview.net/forum?id=mxcCg9YRqj)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language model (LM) benchmarking faces several challenges: comprehensive evaluations are costly, benchmarks often fail to measure the intended capabilities, and evaluation quality can degrade due to labeling errors and benchmark saturation. Although various strategies have been proposed to mitigate these issues, they tend to address individual aspects in isolation, neglecting broader questions about overall evaluation quality.

- **[Resona: Improving Context Copying in Linear Recurrence Models with Retrieval](https://openreview.net/forum?id=4mxQmpnawk)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recent shifts in the space of large language model (LLM) research have shown an increasing focus on novel architectures to compete with prototypical Transformer-based models that have long dominated this space. Linear recurrent models have proven to be a viable competitor due to their computational efficiency.

- **[SuperBPE: Space Travel for Language Models](https://openreview.net/forum?id=lcDRvffeNP)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The assumption across nearly all language model (LM) tokenization schemes is that tokens should be subwords, i.e., contained within word boundaries. While providing a seemingly reasonable inductive bias, is this common practice limiting the potential of modern LMs?

- **[Tulu 3: Pushing Frontiers in Open Language Model Post-Training](https://openreview.net/forum?id=i1uGbfHHpH)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language model post-training is applied to refine behaviors and unlock new skills across a wide range of language models, but open recipes for applying these techniques lag behind proprietary ones. The underlying training data and recipes for post-training are simultaneously the most im- portant pieces of the puzzle and the portion with the least transparency.

- **[Understanding R1-Zero-Like Training: A Critical Perspective](https://openreview.net/forum?id=5PAF7PAY2Y)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** DeepSeek-R1-Zero has shown that reinforcement learning (RL) at scale can directly enhance the reasoning capabilities of LLMs without supervised fine-tuning. In this work, we critically examine R1-Zero-like training by analyzing its two core components: base models and RL.

- **[Insight-V: Exploring Long-Chain Visual Reasoning with Multimodal Large Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Dong_Insight-V_Exploring_Long-Chain_Visual_Reasoning_with_Multimodal_Large_Language_Models_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) demonstrate enhanced capabilities and reliability by reasoning more, evolving from Chain-of-Thought prompting to product-level solutions like OpenAI o1. Despite various efforts to improve LLM reasoning, high-quality long-chain reasoning data and optimized training pipelines still remain inadequately explored in vision-language tasks.

- **[3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding](https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** A 3D scene graph represents a compact scene model by capturing both the objects present and the semantic relationships between them, making it a promising structure for robotic applications. To effectively interact with users, an embodied intelligent agent should be able to answer a wide range of natural language queries about the surrounding 3D environment.

- **[Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models](https://openreview.net/forum?id=tc90LV0yRL)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language Model (LM) agents for cybersecurity that are capable of autonomously identifying vulnerabilities and executing exploits have potential to cause real-world impact. Policymakers, model providers, and researchers in the AI and cybersecurity communities are interested in quantifying the capabilities of such agents to help mitigate cyberrisk and investigate opportunities for penetration testing.

- **[Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://openreview.net/forum?id=WCRQFlji2q)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Hallucinations in large language models are a widespread problem, yet the mechanisms behind whether models will hallucinate are poorly understood, limiting our ability to solve this problem. Using sparse autoencoders as an interpretability tool, we discover that a key part of these mechanisms is entity recognition, where the model detects if an entity is one it can recall facts about.

- **[OLMoE: Open Mixture-of-Experts Language Models](https://openreview.net/forum?id=xXTkbTBmqq)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce OLMoE, a fully open, state-of-the-art language model leveraging sparse Mixture-of-Experts (MoE). OLMoE-1B-7B has 7 billion (B) parameters but uses only 1B per input token.

- **[Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://openreview.net/forum?id=BPgK5XW1Nb)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Aligning large language models (LLMs) with human preferences becomes a key component to obtaining state-of-the-art performance, but it yields a huge cost to construct a large human-annotated preference dataset. To tackle this problem, we propose a new framework, Spread Preference Annotation with direct preference judgment (SPA), that boosts the alignment of LLMs using only a very small amount of human-annotated preference data.

- **[Test of Time: A Benchmark for Evaluating LLMs on Temporal Reasoning](https://openreview.net/forum?id=44CoQe6VCq)** — *ICLR 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) have showcased remarkable reasoning capabilities, yet they remain susceptible to errors, particularly in temporal reasoning tasks involving complex temporal logic. Existing research has explored LLM performance on temporal reasoning using diverse datasets and benchmarks.

- **[Transformers Provably Solve Parity Efficiently with Chain of Thought](https://openreview.net/forum?id=n2NidsYDop)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This work provides the first theoretical analysis of training transformers to solve complex problems by recursively generating intermediate states, analogous to fine-tuning for chain-of-thought (CoT) reasoning. We consider training a one-layer transformer to solve the fundamental $k$-parity problem, extending the work on RNNs by \citet{Wies23}.

- **[Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://openreview.net/forum?id=gc8QAQfXv6)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Catastrophic forgetting (CF) poses a significant challenge in machine learning, where a model forgets previously learned information upon learning new tasks. Despite the advanced capabilities of Large Language Models (LLMs), they continue to face challenges with CF during continual learning.

- **[Position: Formal Mathematical Reasoning—A New Frontier in AI](https://openreview.net/forum?id=HuvAM5x2xG)** — *ICML 2025 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** AI for Mathematics (AI4Math) is intellectually intriguing and is crucial for AI-driven system design and verification. Extensive efforts on AI4Math have mirrored techniques in NLP, in particular, training large language models on carefully curated math datasets in text form.

- **[Position: General Intelligence Requires Reward-based Pretraining](https://openreview.net/forum?id=QMgCDPWL9Y)** — *ICML 2025 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have demonstrated impressive real-world utility, exemplifying artificial useful intelligence (AUI). However, their ability to reason adaptively and robustly -- the hallmarks of artificial general intelligence (AGI) -- remains fragile.

- **[Position: Language model developers should report train-test overlap](https://openreview.net/forum?id=J5MmGPWKfb)** — *ICML 2025 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language models are extensively evaluated, but correctly interpreting evaluation results requires knowledge of train-test overlap, which refers to the extent to which the language model is trained on the very data it is being tested on. The public currently lacks adequate information about train-test overlap: most models have no public train-test overlap statistics, and third parties cannot directly measure train-test overlap since...

- **[Position: Principles of Animal Cognition to Improve LLM Evaluations](https://openreview.net/forum?id=gCPJFcHskT)** — *ICML 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** It has become increasingly challenging to understand and evaluate LLM capabilities as these models exhibit a broader range of behaviors. In this position paper, we argue that LLM researchers should draw on the lessons from another field which has developed a rich set of experimental paradigms and design practices for probing the behavior of complex intelligent systems: animal cognition.

- **[Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://openreview.net/forum?id=tctWi7I5wd)** — *ICML 2025 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The proliferation of LLM bias probes introduces three challenges: we lack (1) principled criteria for selecting appropriate probes, (2) a system for reconciling conflicting results across probes, and (3) formal frameworks for reasoning about when and why experimental findings will generalize to real user behavior. In response, we propose a systematic approach to LLM social bias probing, drawing on insights from the social sciences.

- **[GPT-NER: Named Entity Recognition via Large Language Models](https://aclanthology.org/2025.findings-naacl.239/)** — *NAACL 2025 · Findings*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Despite the fact that large-scale Language Models (LLM) have achieved SOTA performances on a variety of NLP tasks, its performance on NER is still significantly below supervised baselines. This is due to the gap between the two tasks the NER and LLMs: the former is a sequence labeling task in nature while the latter is a text-generation model.In this paper, we propose GPT-NER to resolve this issue.

- **[GRAG: Graph Retrieval-Augmented Generation](https://aclanthology.org/2025.findings-naacl.232/)** — *NAACL 2025 · Findings*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Naive Retrieval-Augmented Generation (RAG) focuses on individual documents during retrieval and, as a result, falls short in handling networked documents which are very popular in many applications such as citation graphs, social media, and knowledge graphs. To overcome this limitation, we introduce Graph Retrieval-Augmented Generation (GRAG), which tackles the fundamental challenges in retrieving textual subgraphs and integrating...

- **[ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](https://aclanthology.org/2025.naacl-long.342/)** — *NAACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The pace of scientific research, vital for improving human life, is complex, slow, and needs specialized expertise. Meanwhile, novel, impactful research often stems from both a deep understanding of prior work, and a cross-pollination of ideas across domains and fields.

- **[Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://openreview.net/forum?id=4OsgYD7em5)** — *NeurIPS 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) has recently demonstrated notable success in enhancing the reasoning performance of large language models (LLMs), particularly in mathematics and programming tasks. It is widely believed that, similar to how traditional RL helps agents to explore and learn new strategies, RLVR enables LLMs to continuously self-improve, thus acquiring novel reasoning abilities that exceed the...

- **[Learning Linear Attention in Polynomial Time](https://openreview.net/forum?id=QN0E0KX2LM)** — *NeurIPS 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Previous research has explored the expressivity of Transformer models in simulating Boolean circuits or Turing machines. However, the efficient learnability of Transformers from data has remained an open question.

- **[Neither Valid nor Reliable? Investigating the Use of LLMs as Judges](https://openreview.net/forum?id=yqKfMr0yvY)** — *NeurIPS 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Evaluating natural language generation (NLG) systems remains a core challenge, further complicated by the rise of general-purpose large language models (LLMs). Recently, large language models as judges (LLJs) have emerged as a scalable, cost-effective alternative to traditional metrics, but their validity remains underexplored.

- **[Prompting as Scientific Inquiry](https://openreview.net/forum?id=yZU8kdwafM)** — *NeurIPS 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Prompting is the primary method by which we study and control large language models. It is also one of the most powerful: nearly every major capability attributed to LLMs—few-shot learning, chain-of-thought, constitutional AI—was first unlocked through prompting.

- **[Stop DDoS Attacking the Research Community with AI-Generated Survey Papers](https://openreview.net/forum?id=R5uuqCAPf8)** — *NeurIPS 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Survey papers are foundational to the scholarly progress of research communities, offering structured overviews that guide both novices and experts across disciplines. However, the recent surge of AI-generated surveys, especially enabled by large language models (LLMs), has transformed this traditionally labor-intensive genre into a low-effort, high-volume output.

- **[Benchmarking Large Language Models in Retrieval-Augmented Generation](https://ojs.aaai.org/index.php/AAAI/article/view/29728)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Retrieval-Augmented Generation (RAG) is a promising approach for mitigating the hallucination of large language models (LLMs). However, existing research lacks rigorous evaluation of the impact of retrieval-augmented generation on different large language models, which make it challenging to identify the potential bottlenecks in the capabilities of RAG for different LLMs.

- **[From Statistical Relational to Neuro-Symbolic Artificial Intelligence](https://ojs.aaai.org/index.php/AAAI/article/view/30294)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The integration of learning and reasoning is one of the key challenges in artificial intelligence and machine learning today. The area of Neuro-Symbolic AI (NeSy) tackles this challenge by integrating symbolic reasoning with neural networks.

- **[Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/29720)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce Graph of Thoughts (GoT): a framework that advances prompting capabilities in large language models (LLMs) beyond those offered by paradigms such as Chain-of-Thought or Tree of Thoughts (ToT). The key idea and primary advantage of GoT is the ability to model the information generated by an LLM as an arbitrary graph, where units of information ("LLM thoughts") are vertices, and edges correspond to dependencies between...

- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have drastically reshaped our interactions with artificial intelligence (AI) systems, showcasing impressive performance across an extensive array of tasks. Despite this, a notable hindrance remains—the deficiency of a long-term memory mechanism within these models.

- **[Visual Adversarial Examples Jailbreak Aligned Large Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/30150)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Warning: this paper contains data, prompts, and model outputs that are offensive in nature. Recently, there has been a surge of interest in integrating vision into Large Language Models (LLMs), exemplified by Visual Language Models (VLMs) such as Flamingo and GPT-4.

- **[AI ‘News’ Content Farms Are Easy to Make and Hard to Detect: A Case Study in Italian](https://aclanthology.org/2024.acl-long.817/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are increasingly used as ‘content farm’ models (CFMs), to generate synthetic text that could pass for real news articles. This is already happening even for languages that do not have high-quality monolingual LLMs.

- **[Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model](https://aclanthology.org/2024.acl-long.845/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recent breakthroughs in large language models (LLMs) have centered around a handful of data-rich languages. What does it take to broaden access to breakthroughs beyond first-class citizen languages?

- **[Can Large Language Models be Good Emotional Supporter? Mitigating Preference Bias on Emotional Support Conversation](https://aclanthology.org/2024.acl-long.813/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Emotional Support Conversation (ESC) is a task aimed at alleviating individuals’ emotional distress through daily conversation. Given its inherent complexity and non-intuitive nature, ESConv dataset incorporates support strategies to facilitate the generation of appropriate responses.

- **[Causal Estimation of Memorisation Profiles](https://aclanthology.org/2024.acl-long.834/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Understanding memorisation in language models has practical and societal implications, e.g., studying models’ training dynamics or preventing copyright infringements.Prior work defines memorisation as the causal effect of training with an instance on the model’s ability to predict that instance. This definition relies on a counterfactual: the ability to observe what would have happened had the model not seen that instance.Existing...

- **[Causal-Guided Active Learning for Debiasing Large Language Models](https://aclanthology.org/2024.acl-long.778/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Although achieving promising performance, recent analyses show that current generative large language models (LLMs) may still capture dataset biases and utilize them for generation, leading to poor generalizability and harmfulness of LLMs. However, due to the diversity of dataset biases and the over-optimization problem, previous prior-knowledge-based debiasing methods and fine-tuning-based debiasing methods may not be suitable for...

- **[CHECKWHY: Causal Fact Verification via Argument Structure](https://aclanthology.org/2024.acl-long.835/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** With the growing complexity of fact verification tasks, the concern with “thoughtful” reasoning capabilities is increasing. However, recent fact verification benchmarks mainly focus on checking a narrow scope of semantic factoids within claims and lack an explicit logical reasoning process.

- **[DIALECTBENCH: An NLP Benchmark for Dialects, Varieties, and Closely-Related Languages](https://aclanthology.org/2024.acl-long.777/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language technologies should be judged on their usefulness in real-world use cases. An often overlooked aspect in natural language processing (NLP) research and evaluation is language variation in the form of non-standard dialects or language varieties (hereafter, varieties).

- **[Discursive Socratic Questioning: Evaluating the Faithfulness of Language Models’ Understanding of Discourse Relations](https://aclanthology.org/2024.acl-long.341/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** While large language models have significantly enhanced the effectiveness of discourse relation classifications, it remains unclear whether their comprehension is faithful and reliable. We provide DiSQ, a new method for evaluating the faithfulness of understanding discourse based on question answering.

- **[Do Llamas Work in English? On the Latent Language of Multilingual Transformers](https://aclanthology.org/2024.acl-long.820/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We ask whether multilingual language models trained on unbalanced, English-dominated corpora use English as an internal pivot language—-a question of key importance for understanding how language models function and the origins of linguistic bias. Focusing on the Llama-2 family of transformer models, our study is based on carefully constructed non-English prompts with a unique correct single-token continuation.

- **[Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research](https://aclanthology.org/2024.acl-long.840/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Information about pretraining corpora used to train the current best-performing language models is seldom discussed: commercial models rarely detail their data, and even open models are often released without accompanying training data or recipes to reproduce them. As a result, it is challenging to conduct and advance scientific research on language modeling, such as understanding how training data impacts model capabilities and...

- **[Don’t Hallucinate, Abstain: Identifying LLM Knowledge Gaps via Multi-LLM Collaboration](https://aclanthology.org/2024.acl-long.786/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Despite efforts to expand the knowledge of large language models (LLMs), knowledge gaps—missing or outdated information in LLMs—might always persist given the evolving nature of knowledge. In this work, we study approaches to identify LLM knowledge gaps and abstain from answering questions when knowledge gaps are present.

- **[G-DIG: Towards Gradient-based DIverse and hiGh-quality Instruction Data Selection for Machine Translation](https://aclanthology.org/2024.acl-long.821/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have demonstrated remarkable abilities in general scenarios. Instruction finetuning empowers them to align with humans in various tasks.

- **[Getting Serious about Humor: Crafting Humor Datasets with Unfunny Large Language Models](https://aclanthology.org/2024.acl-short.76/)** — *ACL 2024 · Short*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Humor is a fundamental facet of human cognition and interaction. Yet, despite recent advances in natural language processing, humor detection remains a challenging task that is complicated by the scarcity of datasets that pair humorous texts with similar non-humorous counterparts.

- **[Greed is All You Need: An Evaluation of Tokenizer Inference Methods](https://aclanthology.org/2024.acl-short.73/)** — *ACL 2024 · Short*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** While subword tokenizers such as BPE and WordPiece are typically used to build vocabularies for NLP models, the method of decoding text into a sequence of tokens from these vocabularies is often left unspecified, or ill-suited to the method in which they were constructed. We provide a controlled analysis of seven tokenizer inference methods across four different algorithms and three vocabulary sizes, performed on a novel intrinsic...

- **[Having Beer after Prayer? Measuring Cultural Bias in Large Language Models](https://aclanthology.org/2024.acl-long.862/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** As the reach of large language models (LMs) expands globally, their ability to cater to diverse cultural contexts becomes crucial. Despite advancements in multilingual capabilities, models are not designed with appropriate cultural nuances.

- **[How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs](https://aclanthology.org/2024.acl-long.773/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Most traditional AI safety research views models as machines and centers on algorithm-focused attacks developed by security experts. As large language models (LLMs) become increasingly common and competent, non-expert users can also impose risks during daily interactions.

- **[IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages](https://aclanthology.org/2024.acl-long.843/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Despite the considerable advancements in English LLMs, the progress in building comparable models for other languages has been hindered due to the scarcity of tailored resources. Our work aims to bridge this divide by introducing an expansive suite of resources specifically designed for the development of Indic LLMs, covering 22 languages, containing a total of 251B tokens and 74.8M instruction-response pairs.

- **[IRCoder: Intermediate Representations Make Language Models Robust Multilingual Code Generators](https://aclanthology.org/2024.acl-long.802/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Code generation has fast become one of the most popular applications of language models (LMs). Nonetheless, research on multilingual aspects of Code-LMs, such as cross-lingual transfer between different programming languages, language-specific data augmentation, and post-hoc LM adaptation, alongside the exploitation of data sources other than the original textual content, has been much sparser than for their natural language...

- **[L-Eval: Instituting Standardized Evaluation for Long Context Language Models](https://aclanthology.org/2024.acl-long.776/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recently, there has been growing interest in long-context scaling of large language models (LLMs). To facilitate research in this field, we propose L-Eval to institute a more standardized evaluation for Long-Context Language Models (LCLMs) addressing two key aspects: dataset construction and evaluation metrics.

- **[MAP’s not dead yet: Uncovering true language model modes by conditioning away degeneracy](https://aclanthology.org/2024.acl-long.855/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** It has been widely observed that exact or approximate MAP (mode-seeking) decoding from natural language generation (NLG) models consistently leads to degenerate outputs (Holtzman et al., 2019; Stahlberg and Byrne, 2019). Prior work has attributed this behavior to either a fundamental and unavoidable inadequacy of modes in probabilistic models or weaknesses in language modeling.

- **[Media Framing: A typology and Survey of Computational Approaches Across Disciplines](https://aclanthology.org/2024.acl-long.822/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Framing studies how individuals and societies make sense of the world, by communicating or representing complex issues through schema of interpretation. The framing of information in the mass media influences our interpretation of facts and corresponding decisions, so detecting and analysing it is essential to understand biases in the information we consume.

- **[MIDGARD: Self-Consistency Using Minimum Description Length for Structured Commonsense Reasoning](https://aclanthology.org/2024.acl-long.380/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We study the task of conducting structured reasoning as generating a reasoning graph from natural language input using large language models (LLMs). Previous approaches have explored various prompting schemes, yet they suffer from error propagation due to the autoregressive nature and single-pass-based decoding, which lack error correction capability.

- **[Mission: Impossible Language Models](https://aclanthology.org/2024.acl-long.787/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Chomsky and others have very directly claimed that large language models (LLMs) are equally capable of learning languages that are possible and impossible for humans to learn. However, there is very little published experimental evidence to support such a claim.

- **[MultiPICo: Multilingual Perspectivist Irony Corpus](https://aclanthology.org/2024.acl-long.849/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recently, several scholars have contributed to the growth of a new theoretical framework in NLP called perspectivism. This approach aimsto leverage data annotated by different individuals to model diverse perspectives that affect their opinions on subjective phenomena such as irony.

- **[Must NLP be Extractive?](https://aclanthology.org/2024.acl-long.797/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** How do we roll out language technologies across a world with 7,000 languages? In one story, we scale the successes of NLP further into ‘low-resource’ languages, doing ever more with less.

- **[Natural Language Satisfiability: Exploring the Problem Distribution and Evaluating Transformer-based Language Models](https://aclanthology.org/2024.acl-long.815/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Efforts to apply transformer-based language models (TLMs) to the problem of reasoning in natural language have enjoyed ever-increasing success in recent years. The most fundamental task in this area to which nearly all others can be reduced is that of determining satisfiability.

- **[OLMo: Accelerating the Science of Language Models](https://aclanthology.org/2024.acl-long.841/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language models (LMs) have become ubiquitous in both NLP research and in commercial product offerings. As their commercial importance has surged, the most powerful models have become closed off, gated behind proprietary interfaces, with important details of their training data, architectures, and development undisclosed.

- **[Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models](https://aclanthology.org/2024.acl-long.816/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Much recent work seeks to evaluate values and opinions in large language models (LLMs) using multiple-choice surveys and questionnaires. Most of this work is motivated by concerns around real-world LLM applications.

- **[Quantized Side Tuning: Fast and Memory-Efficient Tuning of Quantized Large Language Models](https://aclanthology.org/2024.acl-long.1/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Finetuning large language models (LLMs) has been empirically effective on a variety of downstream tasks. Existing approaches to finetuning an LLM either focus on parameter-efficient finetuning, which only updates a small number of trainable parameters, or attempt to reduce the memory footprint during the training phase of the finetuning.

- **[RomanSetu: Efficiently unlocking multilingual capabilities of Large Language Models via Romanization](https://aclanthology.org/2024.acl-long.833/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This study addresses the challenge of extending Large Language Models (LLMs) to non-English languages, specifically those using non-Roman scripts. We propose an approach that utilizes the romanized form of text as an interface for LLMs, hypothesizing that its frequent informal use and shared tokens with English enhance cross-lingual alignment.

- **[Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models](https://aclanthology.org/2024.acl-long.818/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This paper explores the impact of extending input lengths on the capabilities of Large Language Models (LLMs). Despite LLMs advancements in recent times, their performance consistency across different input lengths is not well understood.

- **[Spiral of Silence: How is Large Language Model Killing Information Retrieval?—A Case Study on Open Domain Question Answering](https://aclanthology.org/2024.acl-long.798/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The practice of Retrieval-Augmented Generation (RAG), which integrates Large Language Models (LLMs) with retrieval systems, has become increasingly prevalent. However, the repercussions of LLM-derived content infiltrating the web and influencing the retrieval-generation feedback loop are largely uncharted territories.

- **[Steering Llama 2 via Contrastive Activation Addition](https://aclanthology.org/2024.acl-long.828/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce Contrastive Activation Addition (CAA), a method for steering language models by modifying their activations during forward passes. CAA computes “steering vectors” by averaging the difference in residual stream activations between pairs of positive and negative examples of a particular behavior, such as factual versus hallucinatory responses.

- **[The Earth is Flat because...: Investigating LLMs’ Belief towards Misinformation via Persuasive Conversation](https://aclanthology.org/2024.acl-long.858/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) encapsulate vast amounts of knowledge but still remain vulnerable to external misinformation. Existing research mainly studied this susceptibility behavior in a single-turn setting.

- **[VariErr NLI: Separating Annotation Error from Human Label Variation](https://aclanthology.org/2024.acl-long.123/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Human label variation arises when annotators assign different labels to the same item for valid reasons, while annotation errors occur when labels are assigned for invalid reasons. These two issues are prevalent in NLP benchmarks, yet existing research has studied them in isolation.

- **[Why are Sensitive Functions Hard for Transformers?](https://aclanthology.org/2024.acl-long.800/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Empirical studies have identified a range of learnability biases and limitations of transformers, such as a persistent difficulty in learning to compute simple formal languages such as PARITY, and a bias towards low-degree functions. However, theoretical understanding remains limited, with existing expressiveness theory either overpredicting or underpredicting realistic learning abilities.

- **[Word Embeddings Are Steers for Language Models](https://aclanthology.org/2024.acl-long.864/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language models (LMs) automatically learn word embeddings during pre-training on language corpora. Although word embeddings are usually interpreted as feature vectors for individual words, their roles in language model generation remain underexplored.

- **[Mechanics of Next Token Prediction with Self-Attention](https://proceedings.mlr.press/v238/li24f.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Transformer-based language models are trained on large datasets to predict the next token given an input sequence. Despite this simple training objective, they have led to revolutionary advances in natural language processing.

- **[Multi-resolution Time-Series Transformer for Long-term Forecasting](https://proceedings.mlr.press/v238/zhang24l.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The performance of transformers for time-series forecasting has improved significantly. Recent architectures learn complex temporal patterns by segmenting a time-series into patches and using the patches as tokens.

- **[Quantifying Uncertainty in Natural Language Explanations of Large Language Models](https://proceedings.mlr.press/v238/harsha-tanneru24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are increasingly used as powerful tools for several high-stakes natural language processing (NLP) applications. Recent prompting works claim to elicit intermediate reasoning steps and key tokens that serve as proxy explanations for LLM predictions.

- **[AI-generated text boundary detection with RoFT](https://openreview.net/forum?id=kzzwTrt04Z)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Due to the rapid development of large language models, people increasingly often encounter texts that may start as written by a human but continue as machine-generated. Detecting the boundary between human-written and machine-generated parts of such texts is a challenging problem that has not received much attention in literature.

- **[Can Language Models Solve Olympiad Programming?](https://openreview.net/forum?id=kGa4fMtP9l)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Olympiad programming is one of the hardest reasoning challenges for humans, yet it has been understudied as a domain to benchmark language models (LMs). In this paper, we introduce the USACO benchmark with 307 problems from USA Computing Olympiad contests, along with high-quality unit tests, reference code, and official analysis for each problem.

- **[Dated Data: Tracing Knowledge Cutoffs in Large Language Models](https://openreview.net/forum?id=wS7PxDjy6m)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are often paired with a reported cutoff date, the time at which training data was gathered. Such information is crucial for applications where the LLM must provide up-to-date information.

- **[Evaluating Cultural Adaptability of a Large Language Model via Simulation of Synthetic Personas](https://openreview.net/forum?id=S4ZOkV1AHl)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The success of Large Language Models (LLMs) in multicultural environments hinges on their ability to understand users' diverse cultural backgrounds. We measure this capability by having an LLM simulate human profiles representing various nationalities within the scope of a questionnaire-style psychological experiment.

- **[Information-Theoretic Distillation for Reference-less Summarization](https://openreview.net/forum?id=JXcXnJJSuL)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The current winning recipe for automatic summarization is using proprietary large-scale language models (LLMs) such as ChatGPT as is, or imitation learning from them as teacher models. While increasingly ubiquitous dependence on such large-scale language models is convenient, there remains an important question of whether small-scale models could have achieved competitive results, if we were to seek an alternative learning...

- **[Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://openreview.net/forum?id=tEYskw1VY2)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers' computational inefficiency on long sequences, but they have not...

- **[Measuring and Controlling Instruction (In)Stability in Language Model Dialogs](https://openreview.net/forum?id=60a1SAtH4e)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** System-prompting is a standard tool for customizing language-model chatbots, enabling them to follow a specific instruction. An implicit assumption in the use of system prompts is that they will be _stable_, so the chatbot will continue to generate text according to the stipulated instructions for the duration of a conversation.

- **[PolygloToxicityPrompts: Multilingual Evaluation of Neural Toxic Degeneration in Large Language Models](https://openreview.net/forum?id=ootI3ZO6TJ)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recent advances in large language models (LLMs) have led to their extensive global deployment, and ensuring their safety calls for comprehensive and multilingual toxicity evaluations. However, existing toxicity benchmarks are overwhelmingly focused on English, posing serious risks to deploying LLMs in other languages.

- **[Will the Real Linda Please Stand up...to Large Language Models? Examining the Representativeness Heuristic in LLMs](https://openreview.net/forum?id=3GhOWfSLrD)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Although large language models (LLMs) have demonstrated remarkable proficiency in modeling text and generating human-like text, they may exhibit biases acquired from training data in doing so. Specifically, LLMs may be susceptible to a common cognitive trap in human decision-making called the representativeness heuristic.

- **[Environment Curriculum Generation via Large Language Models](https://openreview.net/forum?id=F0rWEID2gb)** — *CoRL 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recent work has demonstrated that a promising strategy for teaching robots a wide range of complex skills is by training them on a curriculum of progressively more challenging environments. However, developing an effective curriculum of environment distributions currently requires significant expertise, which must be repeated for every new domain.

- **[PoliFormer: Scaling On-Policy RL with Transformers Results in Masterful Navigators](https://openreview.net/forum?id=KdVLK0Wo5z)** — *CoRL 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We present PoliFormer (Policy Transformer), an RGB-only indoor navigation agent trained end-to-end with reinforcement learning at scale that generalizes to the real-world without adaptation despite being trained purely in simulation. PoliFormer uses a foundational vision transformer encoder with a causal transformer decoder enabling long-term memory and reasoning.

- **[CogAgent: A Visual Language Model for GUI Agents](https://openreview.net/forum?id=d3199X5spZ)** — *CVPR 2024 · Highlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** People are spending an enormous amount of time on digital devices through graphical user interfaces (GUIs) e.g. computer or smartphone screens. Large language models (LLMs) such as ChatGPT can assist people in tasks like writing emails but struggle to understand and interact with GUIs thus limiting their potential to increase automation levels.

- **[Improved Baselines with Visual Instruction Tuning](https://openreview.net/forum?id=qiYIqH8HuZ)** — *CVPR 2024 · Highlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large multimodal models (LMM) have recently shown encouraging progress with visual instruction tuning. In this paper we present the first systematic study to investigate the design choices of LMMs in a controlled setting under the LLaVA framework.

- **[PointLLM: Empowering Large Language Models to Understand Point Clouds](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3601_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** "The unprecedented advancements in Large Language Models (LLMs) have shown a profound impact on natural language processing but are yet to fully embrace the realm of 3D understanding. This paper introduces PointLLM, a preliminary effort to fill this gap, empowering LLMs to understand point clouds and offering a new avenue beyond 2D data.

- **[A User-Centric Multi-Intent Benchmark for Evaluating Large Language Models](https://aclanthology.org/2024.emnlp-main.210/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) are essential tools that users employ across various scenarios, so evaluating their performance and guiding users in selecting the suitable service is important. Although many benchmarks exist, they mainly focus on specific predefined model abilities, such as world knowledge, reasoning, etc.

- **[Are Large Language Models Capable of Generating Human-Level Narratives?](https://aclanthology.org/2024.emnlp-main.978/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** As daily reliance on large language models (LLMs) grows, assessing their generation quality is crucial to understanding how they might impact on our communications. This paper investigates the capability of LLMs in storytelling, focusing on narrative development and plot progression.

- **[Backward Lens: Projecting Language Model Gradients into the Vocabulary Space](https://aclanthology.org/2024.emnlp-main.142/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Understanding how Transformer-based Language Models (LMs) learn and recall information is a key goal of the deep learning community. Recent interpretability methods project weights and hidden states obtained from the forward pass to the models’ vocabularies, helping to uncover how information flows within LMs.

- **[Do LLMs Plan Like Human Writers? Comparing Journalist Coverage of Press Releases with LLMs](https://aclanthology.org/2024.emnlp-main.1216/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Journalists engage in multiple steps in the news writing process that depend on human creativity, like exploring different “angles” (i.e. the specific perspectives a reporter takes). These can potentially be aided by large language models (LLMs).

- **[Finding Blind Spots in Evaluator LLMs with Interpretable Checklists](https://aclanthology.org/2024.emnlp-main.911/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are increasingly relied upon to evaluate text outputs of other LLMs, thereby influencing leaderboards and development decisions. However, concerns persist over the accuracy of these assessments and the potential for misleading conclusions.

- **[Fishing for Magikarp: Automatically Detecting Under-trained Tokens in Large Language Models](https://aclanthology.org/2024.emnlp-main.649/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The disconnect between tokenizer creation and model training in language models allows for specific inputs, such as the infamous SolidGoldMagikarp token, to induce unwanted model behaviour. Although such ‘glitch tokens’, tokens present in the tokenizer vocabulary but that are nearly or entirely absent during model training, have been observed across various models, a reliable method to identify and address them has been missing.

- **[Formality is Favored: Unraveling the Learning Preferences of Large Language Models on Data with Conflicting Knowledge](https://aclanthology.org/2024.emnlp-main.304/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Having been trained on massive pretraining data, large language models have shown excellent performance on many knowledge-intensive tasks. However, pretraining data tends to contain misleading and even conflicting information, and it is intriguing to understand how LLMs handle these noisy data during training.

- **[GoldCoin: Grounding Large Language Models in Privacy Laws via Contextual Integrity Theory](https://aclanthology.org/2024.emnlp-main.195/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Privacy issues arise prominently during the inappropriate transmission of information between entities. Existing research primarily studies privacy by exploring various privacy attacks, defenses, and evaluations within narrowly predefined patterns, while neglecting that privacy is not an isolated, context-free concept limited to traditionally sensitive data (e.g., social security numbers), but intertwined with intricate social...

- **[KidLM: Advancing Language Models for Children – Early Insights and Future Directions](https://aclanthology.org/2024.emnlp-main.277/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recent studies highlight the potential of large language models in creating educational tools for children, yet significant challenges remain in maintaining key child-specific properties such as linguistic nuances, cognitive needs, and safety standards. In this paper, we explore foundational steps toward the development of child-specific language models, emphasizing the necessity of high-quality pre-training data.

- **[Language Models Learn Rare Phenomena from Less Rare Phenomena: The Case of the Missing AANNs](https://aclanthology.org/2024.emnlp-main.53/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language models learn rare syntactic phenomena, but the extent to which this is attributable to generalization vs. memorization is a major open question. To that end, we iteratively trained transformer language models on systematically manipulated corpora which were human-scale in size, and then evaluated their learning of a rare grammatical phenomenon: the English Article+Adjective+Numeral+Noun (AANN) construction (“a beautiful...

- **[Learning Planning-based Reasoning by Trajectories Collection and Process Reward Synthesizing](https://aclanthology.org/2024.emnlp-main.20/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have demonstrated significant potential in handling complex reasoning tasks through step-by-step rationale generation. However, recent studies have raised concerns regarding the hallucination and flaws in their reasoning process.

- **[Learning to Retrieve Iteratively for In-Context Learning](https://aclanthology.org/2024.emnlp-main.406/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce iterative retrieval, a novel framework that empowers retrievers to make iterative decisions through policy optimization. Finding an optimal portfolio of retrieved items is a combinatorial optimization problem, generally considered NP-hard.

- **[Measuring Psychological Depth in Language Models](https://aclanthology.org/2024.emnlp-main.953/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Evaluations of creative stories generated by large language models (LLMs) often focus on objective properties of the text, such as its style, coherence, and diversity. While these metrics are indispensable, they do not speak to a story’s subjective, psychological impact from a reader’s perspective.

- **[OATH-Frames: Characterizing Online Attitudes Towards Homelessness with LLM Assistants](https://aclanthology.org/2024.emnlp-main.724/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Warning: Contents of this paper may be upsetting.Public attitudes towards key societal issues, expressed on online media, are of immense value in policy and reform efforts, yet challenging to understand at scale. We study one such social issue: homelessness in the U.S., by leveraging the remarkable capabilities of large language models to assist social work experts in analyzing millions of posts from Twitter.

- **[Pretraining Data Detection for Large Language Models: A Divergence-based Calibration Method](https://aclanthology.org/2024.emnlp-main.300/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** As the scale of training corpora for large language models (LLMs) grows, model developers become increasingly reluctant to disclose details on their data. This lack of transparency poses challenges to scientific evaluation and ethical deployment.

- **[sign.mt: Real-Time Multilingual Sign Language Translation Application](https://aclanthology.org/2024.emnlp-demo.19/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This paper presents sign.mt, an open-source application for real-time multilingual bi-directional translation between spoken and signed languages. Harnessing state-of-the-art open-source models, this tool aims to address the communication divide between the hearing and the deaf, facilitating seamless translation in both spoken-to-signed and signed-to-spoken translation directions.

- **[STOP! Benchmarking Large Language Models with Sensitivity Testing on Offensive Progressions](https://aclanthology.org/2024.emnlp-main.243/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Mitigating explicit and implicit biases in Large Language Models (LLMs) has become a critical focus in the field of natural language processing. However, many current methodologies evaluate scenarios in isolation, without considering the broader context or the spectrum of potential biases within each situation.

- **[The Zeno’s Paradox of ‘Low-Resource’ Languages](https://aclanthology.org/2024.emnlp-main.983/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The disparity in the languages commonly studied in Natural Language Processing (NLP) is typically reflected by referring to languages as low vs high-resourced. However, there is limited consensus on what exactly qualifies as a ‘low-resource language.’ To understand how NLP papers define and study ‘low resource’ languages, we qualitatively analyzed 150 papers from the ACL Anthology and popular speech-processing conferences that...

- **[Towards Cross-Cultural Machine Translation with Retrieval-Augmented Generation from Multilingual Knowledge Graphs](https://aclanthology.org/2024.emnlp-main.914/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Translating text that contains entity names is a challenging task, as cultural-related references can vary significantly across languages. These variations may also be caused by transcreation, an adaptation process that entails more than transliteration and word-for-word translation.

- **[Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving](https://aclanthology.org/2024.emnlp-main.172/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Natural language explanations represent a proxy for evaluating explanation-based and multi-step Natural Language Inference (NLI) models. However, assessing the validity of explanations for NLI is challenging as it typically involves the crowd-sourcing of apposite datasets, a process that is time-consuming and prone to logical errors.

- **[When Is Multilinguality a Curse? Language Modeling for 250 High- and Low-Resource Languages](https://aclanthology.org/2024.emnlp-main.236/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Multilingual language models are widely used to extend NLP systems to low-resource languages. However, concrete evidence for the effects of multilinguality on language modeling performance in individual languages remains scarce.

- **[Which questions should I answer? Salience Prediction of Inquisitive Questions](https://aclanthology.org/2024.emnlp-main.1114/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Inquisitive questions — open-ended, curiosity-driven questions people ask as they read — are an integral part of discourse processing and comprehension. Recent work in NLP has taken advantage of question generation capabilities of LLMs to enhance a wide range of applications.

- **[BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://openreview.net/forum?id=7Ttk3RzDeu)** — *ICLR 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Summarizing book-length documents ($>$100K tokens) that exceed the context window size of large language models (LLMs) requires first breaking the input document into smaller chunks and then prompting an LLM to merge, update, and compress chunk-level summaries. Despite the complexity and importance of this task, it has yet to be meaningfully studied due to the challenges of evaluation: existing book-length summarization datasets...

- **[The mechanistic basis of data dependence and abrupt learning in an in-context classification task](https://openreview.net/forum?id=aN4Jf6Cx69)** — *ICLR 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Transformer models exhibit in-context learning: the ability to accurately predict the response to a novel query based on illustrative examples in the input sequence, which contrasts with traditional in-weights learning of query-output relationships. What aspects of the training data distribution and architecture favor in-context vs in-weights learning?

- **[Understanding and Mitigating the Label Noise in Pre-training on Downstream Tasks](https://openreview.net/forum?id=TjhUtloBZU)** — *ICLR 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Pre-training on large-scale datasets and then fine-tuning on downstream tasks have become a standard practice in deep learning. However, pre-training data often contain label noise that may adversely affect the generalization of the model.

- **[GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection](https://openreview.net/forum?id=hYHsrKDiX7)** — *ICML 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Training Large Language Models (LLMs) presents significant memory challenges, predominantly due to the growing size of weights and optimizer states. Common memory-reduction approaches, such as low-rank adaptation (LoRA), add a trainable low-rank matrix to the frozen pre-trained weight in each layer, reducing trainable parameters and optimizer states.

- **[Nash Learning from Human Feedback](https://openreview.net/forum?id=Y5AmNYiyCQ)** — *ICML 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Reinforcement learning from human feedback (RLHF) has emerged as the main paradigm for aligning large language models (LLMs) with human preferences. Traditionally, RLHF involves the initial step of learning a reward model from pairwise human feedback, i.e., expressed as preferences between pairs of text generations.

- **[NExT-GPT: Any-to-Any Multimodal LLM](https://openreview.net/forum?id=NZQkumsNlf)** — *ICML 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** While recently Multimodal Large Language Models (MM-LLMs) have made exciting strides, they mostly fall prey to the limitation of only input-side multimodal understanding, without the ability to produce content in multiple modalities. As we humans always perceive the world and communicate with people through various modalities, developing any-to-any MM-LLMs capable of accepting and delivering content in any modality becomes essential...

- **[Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modulo Frameworks](https://openreview.net/forum?id=Th8JPEmH4z)** — *ICML 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We argue that auto-regressive LLMs cannot, by themselves, do planning or self-verification (which is after all a form of reasoning), and shed some light on the reasons for misunderstandings in the literature. We will also argue that LLMs should be viewed as universal approximate knowledge sources that have much more meaningful roles to play in planning/reasoning tasks beyond simple front-end/back-end format translators.

- **[Unified Training of Universal Time Series Forecasting Transformers](https://openreview.net/forum?id=Yd8eHMY1wz)** — *ICML 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Deep learning for time series forecasting has traditionally operated within a one-model-per-dataset framework, limiting its potential to leverage the game-changing impact of large pre-trained models. The concept of *universal forecasting*, emerging from pre-training on a vast collection of time series datasets, envisions a single Large Time Series Model capable of addressing diverse downstream forecasting tasks.

- **[VideoPoet: A Large Language Model for Zero-Shot Video Generation](https://openreview.net/forum?id=LRkJwPIDuE)** — *ICML 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We present VideoPoet, a language model capable of synthesizing high-quality video from a large variety of conditioning signals. VideoPoet employs a decoder-only transformer architecture that processes multimodal inputs -- including images, videos, text, and audio.

- **[Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision](https://openreview.net/forum?id=ghNRg2mEgN)** — *ICML 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Widely used alignment techniques, such as reinforcement learning from human feedback (RLHF), rely on the ability of humans to supervise model behavior---for example, to evaluate whether a model faithfully followed instructions or generated safe outputs. However, future superhuman models will behave in complex ways too difficult for humans to reliably evaluate; humans will only be able to *weakly supervise* superhuman models.

- **[AutoTAMP: Autoregressive Task and Motion Planning with LLMs as Translators and Checkers](https://ieeexplore.ieee.org/document/10611163/)** — *ICRA 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** For effective human-robot interaction, robots need to understand, plan, and execute complex, long-horizon tasks described by natural language. Recent advances in large language models (LLMs) have shown promise for translating natural language into robot action sequences for complex tasks.

- **[Driving with LLMs: Fusing Object-Level Vector Modality for Explainable Autonomous Driving](https://ieeexplore.ieee.org/document/10611018/)** — *ICRA 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have shown promise in the autonomous driving sector, particularly in generalization and interpretability. We introduce a unique objectlevel multimodal LLM architecture that merges vectorized numeric modalities with a pre-trained LLM to improve context understanding in driving situations.

- **[LLM-Grounder: Open-Vocabulary 3D Visual Grounding with Large Language Model as an Agent](https://ieeexplore.ieee.org/document/10610443/)** — *ICRA 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** 3D visual grounding is a critical skill for household robots, enabling them to navigate, manipulate objects, and answer questions based on their environment. While existing approaches often rely on extensive labeled data or exhibit limitations in handling complex language queries, we propose LLM-Grounder, a novel zero-shot, open-vocabulary, Large Language Model (LLM)-based 3D visual grounding pipeline.

- **[RoCo: Dialectic Multi-Robot Collaboration with Large Language Models](https://ieeexplore.ieee.org/document/10610855/)** — *ICRA 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We propose a novel approach to multi-robot collaboration that harnesses the power of pre-trained large language models (LLMs) for both high-level communication and low-level path planning. Robots are equipped with LLMs to discuss and collectively reason task strategies.

- **[A Survey of Graph Meets Large Language Model: Progress and Future Directions](https://www.ijcai.org/proceedings/2024/898)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Graph plays a significant role in representing and analyzing complex relationships in real-world applications such as citation networks, social networks, and biological data. Recently, Large Language Models (LLMs), which have achieved tremendous success in various domains, have also been leveraged in graph-related tasks to surpass traditional Graph Neural Networks (GNNs) based methods and yield state-of-the-art performance.

- **[Beyond the Limits: A Survey of Techniques to Extend the Context Length in Large Language Models](https://www.ijcai.org/proceedings/2024/917)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recently, large language models (LLMs) have shown remarkable capabilities including understanding context, engaging in logical reasoning, and generating responses. However, this is achieved at the expense of stringent computational and memory requirements, hindering their ability to effectively support long input sequences.

- **[Large Language Models Are Not Strong Abstract Reasoners](https://www.ijcai.org/proceedings/2024/693)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models have shown tremendous performance on a large variety of natural language processing tasks, ranging from text comprehension to common sense reasoning. However, the mechanisms responsible for this success remain opaque, and it is unclear whether LLMs can achieve human-like cognitive capabilities or whether these models are still fundamentally circumscribed.

- **[Large Language Models for Time Series: A Survey](https://www.ijcai.org/proceedings/2024/921)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have seen significant use in domains such as natural language processing and computer vision. Going beyond text, image and graphics, LLMs present a significant potential for analysis of time series data, benefiting domains such as climate, IoT, healthcare, traffic, audio and finance.

- **[ProtoPFormer: Concentrating on Prototypical Parts in Vision Transformers for Interpretable Image Recognition](https://www.ijcai.org/proceedings/2024/168)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Prototypical part network (ProtoPNet) and its variants have drawn wide attention and been applied to various tasks due to their inherent self-explanatory property. Previous ProtoPNets are primarily built upon convolutional neural networks (CNNs).

- **[ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://www.ijcai.org/proceedings/2024/339)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Screen user interfaces (UIs) and infographics, sharing similar visual language and design principles, play important roles in human communication and human-machine interaction. We introduce ScreenAI, a vision-language model that specializes in UI and infographics understanding.

- **[DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment](https://ieeexplore.ieee.org/document/10802284/)** — *IROS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) encode a vast amount of semantic knowledge and possess remarkable understanding and reasoning capabilities. Previous work has explored how to ground LLMs in robotic tasks to generate feasible and executable textual plans.

- **[LLM3: Large Language Model-based Task and Motion Planning with Motion Failure Reasoning](https://ieeexplore.ieee.org/document/10801328/)** — *IROS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Conventional Task and Motion Planning (TAMP) approaches rely on manually designed interfaces connecting symbolic task planning with continuous motion generation. These domain-specific and labor-intensive modules are limited in addressing emerging tasks in real-world settings.

- **[SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models](https://ieeexplore.ieee.org/document/10802322/)** — *IROS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In this work, we introduce SMART-LLM, an innovative framework designed for embodied multi-robot task planning. SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (LLMs), harnesses the power of LLMs to convert high-level task instructions provided as input into a multi-robot task plan.

- **[AnnoLLM: Making Large Language Models to Be Better Crowdsourced Annotators](https://aclanthology.org/2024.naacl-industry.15/)** — *NAACL 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Many natural language processing (NLP) tasks rely on labeled data to train machine learning models with high performance. However, data annotation is time-consuming and expensive, especially when the task involves a large amount of data or requires specialized domains.

- **[Large Language Models are Effective Text Rankers with Pairwise Ranking Prompting](https://aclanthology.org/2024.findings-naacl.97/)** — *NAACL 2024 · Findings*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Ranking documents using Large Language Models (LLMs) by directly feeding the query and candidate documents into the prompt is an interesting and practical problem. However, researchers have found it difficult to outperform fine-tuned baseline rankers on benchmark datasets.We analyze pointwise and listwise ranking prompts used by existing methods and argue that off-the-shelf LLMs do not fully understand these challenging ranking...

- **[Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions](https://aclanthology.org/2024.findings-naacl.130/)** — *NAACL 2024 · Findings*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have demonstrated remarkable capabilities in various NLP tasks. However, previous works have shown these models are sensitive towards prompt wording, and few-shot demonstrations and their order, posing challenges to fair assessment of these models.

- **[Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks](https://aclanthology.org/2024.naacl-long.102/)** — *NAACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The impressive performance of recent language models across a wide range of tasks suggests that they possess a degree of abstract reasoning skills. Are these skills general and transferable, or specialized to specific tasks seen during pretraining?

- **[Sentiment Analysis in the Era of Large Language Models: A Reality Check](https://aclanthology.org/2024.findings-naacl.246/)** — *NAACL 2024 · Findings*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Sentiment analysis (SA) has been a long-standing research area in natural language processing. With the recent advent of large language models (LLMs), there is great potential for their employment on SA problems.

- **[Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration](https://aclanthology.org/2024.naacl-long.15/)** — *NAACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Human intelligence thrives on cognitive synergy, where collaboration among different minds yield superior outcomes compared to isolated individuals. In this work, we propose Solo Performance Prompting (SPP), which transforms a single LLM into a cognitive synergist by engaging in multi-turn self-collaboration with multiple personas.

- **[XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models](https://aclanthology.org/2024.naacl-long.301/)** — *NAACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Without proper safeguards, large language models will readily follow malicious instructions and generate toxic content. This risk motivates safety efforts such as red-teaming and large-scale feedback learning, which aim to make models both helpful and harmless.

- **[A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://openreview.net/forum?id=RJZRhMzZzH)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) have achieved impressive success on many benchmarks for mathematical reasoning. However, there is growing concern that some of this performance actually reflects dataset contamination, where data closely resembling benchmark questions leaks into the training data, instead of true reasoning ability.

- **[BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://openreview.net/forum?id=u7m2CG84BQ)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In recent years, the input context sizes of large language models (LLMs) have increased dramatically. However, existing evaluation methods have not kept pace, failing to comprehensively assess the efficiency of models in handling long contexts.

- **[Dataset and Lessons Learned from the 2024 SaTML LLM Capture-the-Flag Competition](https://openreview.net/forum?id=WUWHVN4gxk)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language model systems face significant security risks from maliciously crafted messages that aim to overwrite the system's original instructions or leak private data. To study this problem, we organized a capture-the-flag competition at IEEE SaTML 2024, where the flag is a secret string in the LLM system prompt.

- **[Instruction Tuning Large Language Models to Understand Electronic Health Records](https://openreview.net/forum?id=Dgy5WVgPd2)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) have shown impressive capabilities in solving a wide range of tasks based on human instructions. However, developing a conversational AI assistant for electronic health record (EHR) data remains challenging due to (1) the lack of large-scale instruction-following datasets and (2) the limitations of existing model architectures in handling complex and heterogeneous EHR data.

- **[LINGOLY: A Benchmark of Olympiad-Level Linguistic Reasoning Puzzles in Low Resource and Extinct Languages](https://openreview.net/forum?id=cLga8GStdk)** — *NeurIPS 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In this paper, we present the LingOly benchmark, a novel benchmark for advanced reasoning abilities in large language models. Using challenging Linguistic Olympiad puzzles, we evaluate (i) capabilities for in-context identification and generalisation of linguistic patterns in very low-resource or extinct languages, and (ii) abilities to follow complex task instructions.

- **[PrivAuditor: Benchmarking Data Protection Vulnerabilities in LLM Adaptation Techniques](https://openreview.net/forum?id=VpkfxuVXwx)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are recognized for their potential to be an important building block toward achieving artificial general intelligence due to their unprecedented capability for solving diverse tasks. Despite these achievements, LLMs often underperform in domain-specific tasks without training on relevant domain data.

- **[xLSTM: Extended Long Short-Term Memory](https://openreview.net/forum?id=ARAxPPIAhq)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In the 1990s, the constant error carousel and gating were introduced as the central ideas of the Long Short-Term Memory (LSTM). Since then, LSTMs have stood the test of time and contributed to numerous deep learning success stories, in particular they constituted the first Large Language Models (LLMs).

## AI Agents and Tools

- **[DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents](https://openreview.net/forum?id=q1jd5DsPfx)** — *ICLR 2027 · Under review*
  - **Topic:** Agent red-teaming and safety
  - **Summary:** Introduces a red-teaming platform and automated attack agents for evaluating tool use, prompt injection, and other safety risks across reproducible agent environments.

- **[OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://openreview.net/forum?id=ddJW429f5j)** — *ICLR 2027 · Under review*
  - **Topic:** Long-horizon computer-use agents
  - **Summary:** Introduces 108 long-horizon computer-use workflows covering cross-source reasoning, dynamic interfaces, and hidden-state inference for evaluating real-world computer-use agents.

- **[$\\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://openreview.net/forum?id=OC2z7iSQKa)** — *ICML 2026 · Spotlight*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Existing benchmarks for conversational AI agents simulate _single-control_ environments, where only the AI agent can use tools to interact with the world, while the user remains a passive information provider. This differs from real-world scenarios like technical support, where users need to actively participate in modifying the state of the (shared) world.

- **[R2E-Gym: Procedural Environment Generation and Hybrid Verifiers for Scaling Open-Weights SWE Agents](https://openreview.net/forum?id=7evvwwdo3z)** — *COLM 2025 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Improving open-source models on real-world SWE tasks (solving GITHUB issues) faces two key challenges: 1) scalable curation of execution environments to train these models, and, 2) optimal scaling of test-time compute. We introduce R2EGym, the largest procedurally-curated executable gym environment for training real-world SWE-agents, consisting of more than 8.1K tasks.

- **[Position: AI Agents Need Authenticated Delegation](https://openreview.net/forum?id=9skHxuHyM4)** — *ICML 2025 · Oral*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** The rapid deployment of autonomous AI agents creates urgent challenges in the areas of authorization, accountability, and access control in task delegation. This position paper argues that authenticated and auditable delegation of authority to AI agents is a critical component of mitigating practical risks and unlocking the value of agents.

- **[Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://openreview.net/forum?id=4KhDd0Ozqe)** — *ICML 2025 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Self-improving agents aim to continuously acquire new capabilities with minimal supervision. However, current approaches face two key limitations: their self-improvement processes are often rigid, fail to generalize across tasks domains, and struggle to scale with increasing agent capabilities.

- **[EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](https://aclanthology.org/2025.naacl-long.44/)** — *NAACL 2025 · Long*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** There has been a rising interest in utilizing tools in applications of autonomous agents based on large language models (LLMs) to address intricate real-world tasks. To develop LLMbased agents, it usually requires LLMs to understand many tool functions from different tool documentations.

- **[Simulating Classroom Education with LLM-Empowered Agents](https://aclanthology.org/2025.naacl-long.520/)** — *NAACL 2025 · Long*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Large language models (LLMs) have been applied across various intelligent educational tasks to assist teaching. While preliminary studies have focused on task-specific, independent LLM-empowered agents, the potential of LLMs within a multi-agent collaborative framework for classroom simulation with real user participation remains unexplored.

- **[UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26/)** — *NAACL 2025 · Long*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** We introduce UFO, a UI-Fcused agent designed to fulfill user requests tailored to Windows OS applications by observing and analyzing the GUI and control information of these applications. UFO utilizes a hierarchical dual-agent framework that decomposes user requests using a divide-and-conquer approach, enabling seamless navigation and addressing sub-tasks across multiple applications.

- **[Embracing Trustworthy Brain-Agent Collaboration as Paradigm Extension for Intelligent Assistive Technologies](https://openreview.net/forum?id=VZnOKzQ5qW)** — *NeurIPS 2025 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Brain-Computer Interfaces (BCIs) offer a direct communication pathway between the human brain and external devices, holding significant promise for individuals with severe neurological impairments. However, their widespread adoption is hindered by critical limitations, such as low information transfer rates and extensive user-specific calibration.

- **[Simulating Society Requires Simulating Thought](https://openreview.net/forum?id=EvXWexakZX)** — *NeurIPS 2025 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Simulating society with large language models (LLMs), we argue, requires more than generating plausible behavior; it demands cognitively grounded reasoning that is structured, revisable, and traceable. LLM-based agents are increasingly used to emulate individual and group behavior, primarily through prompting and supervised fine-tuning.

- **[ExpeL: LLM Agents Are Experiential Learners](https://ojs.aaai.org/index.php/AAAI/article/view/29936)** — *AAAI 2024*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** The recent surge in research interest in applying large language models (LLMs) to decision-making tasks has flourished by leveraging the extensive world knowledge embedded in LLMs. While there is a growing demand to tailor LLMs for custom decision-making tasks, finetuning them for specific tasks is resource-intensive and may diminish the model's generalization capabilities.

- **[AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://aclanthology.org/2024.acl-long.850/)** — *ACL 2024 · Long*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Autonomous agents that address day-to-day digital tasks (e.g., ordering groceries for a household), must not only operate multiple apps (e.g., notes, messaging, shopping app) via APIs, but also generate rich code with complex control flow in an iterative manner based on their interaction with the environment. However, existing benchmarks for tool use are inadequate, as they only cover tasks that require a simple sequence of API calls.

- **[EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities](https://aclanthology.org/2024.acl-long.829/)** — *ACL 2024 · Long*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** The advent of artificial intelligence has led to a growing emphasis on data-driven modeling in macroeconomics, with agent-based modeling (ABM) emerging as a prominent bottom-up simulation paradigm. In ABM, agents (*e.g.*, households, firms) interact within a macroeconomic environment, collectively generating market dynamics.

- **[OpenOmni: A Collaborative Open Source Tool for Building Future-Ready Multimodal Conversational Agents](https://aclanthology.org/2024.emnlp-demo.5/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Multimodal conversational agents are highly desirable because they offer natural and human-like interaction.However, there is a lack of comprehensive end-to-end solutions to support collaborative development and benchmarking.While proprietary systems like GPT-4o and Gemini demonstrating impressive integration of audio, video, and text with response times of 200-250ms, challenges remain in balancing latency, accuracy, cost, and data...

- **[SUPER: Evaluating Agents on Setting Up and Executing Tasks from Research Repositories](https://aclanthology.org/2024.emnlp-main.702/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Given that Large Language Models (LLMs) have made significant progress in writing code, can they now be used to autonomously reproduce results from research repositories? Such a capability would be a boon to the research community, helping researchers validate, understand, and extend prior work.

- **[TravelPlanner: A Benchmark for Real-World Planning with Language Agents](https://openreview.net/forum?id=l5XQzNkAOe)** — *ICML 2024 · Spotlight*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Planning has been part of the core pursuit for artificial intelligence since its conception, but earlier AI agents mostly focused on constrained settings because many of the cognitive substrates necessary for human-level planning have been lacking. Recently, language agents powered by large language models (LLMs) have shown interesting capabilities such as tool use and reasoning.

- **[AutoAgents: A Framework for Automatic Agent Generation](https://www.ijcai.org/proceedings/2024/3)** — *IJCAI 2024 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Large language models (LLMs) have enabled remarkable advances in automated task-solving with multi-agent systems. However, most existing LLM-based multi-agent approaches rely on predefined agents to handle simple tasks, limiting the adaptability of multi-agent collaboration to different scenarios.

- **[Large Language Model Based Multi-agents: A Survey of Progress and Challenges](https://www.ijcai.org/proceedings/2024/890)** — *IJCAI 2024 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Large Language Models (LLMs) have achieved remarkable success across a wide array of tasks. Due to their notable capabilities in planning and reasoning, LLMs have been utilized as autonomous agents for the automatic execution of various tasks.

- **[Scalable Multi-Agent Reinforcement Learning for Warehouse Logistics with Robotic and Human Co-Workers](https://ieeexplore.ieee.org/document/10802813/)** — *IROS 2024 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** We consider a warehouse in which dozens of mobile robots and human pickers work together to collect and deliver items within the warehouse. The fundamental problem we tackle, called the order-picking problem, is how these worker agents must coordinate their movement and actions in the warehouse to maximise performance in this task.

## AI for Science and Biology

- **[Co-folding with a Soup of Representations](https://openreview.net/forum?id=Jn7WiQ9LtS)** — *ICLR 2027 · Under review*
  - **Topic:** Protein and biomolecular structure prediction
  - **Summary:** Combines pair representations from multiple co-folding models to predict protein and other biomolecular complex structures without retraining the underlying models.

- **[Language-Enhanced Representation Learning for Single-Cell Transcriptomics](https://openreview.net/forum?id=A3QZpECGSw)** — *ICLR 2026*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** Single-cell RNA sequencing (scRNA-seq) offers detailed insights into cellular heterogeneity. Recent advancements leverage single-cell large language models (scLLMs) for effective representation learning.

- **[A Call to Lagrangian Action: Learning Population Mechanics from Temporal Snapshots](https://openreview.net/forum?id=MjPv4kRu3H)** — *ICML 2026 · Spotlight*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** The population dynamics of molecules, cells, and organisms are governed by a number of unknown internal and external forces. In the last decade, population dynamics have predominately been modeled with Wasserstein gradient flows.

- **[Learning stochastic dynamics from snapshots through regularized unbalanced optimal transport](https://openreview.net/forum?id=gQlxd3Mtru)** — *ICLR 2025 · Oral*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** Reconstructing dynamics using samples from sparsely time-resolved snapshots is an important problem in both natural sciences and machine learning. Here, we introduce a new deep learning approach for solving regularized unbalanced optimal transport (RUOT) and inferring continuous unbalanced stochastic dynamics from observed snapshots.

- **[Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://openreview.net/forum?id=YuMEUNNpeb)** — *ICML 2025 · Oral*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** Medical large language models (LLMs) research often makes bold claims, from encoding clinical knowledge to reasoning like a physician. These claims are usually backed by evaluation on competitive benchmarks—a tradition inherited from mainstream machine learning.

- **[Huatuo-26M, a Large-scale Chinese Medical QA Dataset](https://aclanthology.org/2025.findings-naacl.211/)** — *NAACL 2025 · Findings*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** Large Language Models infuse newfound vigor into the advancement of the medical domain, yet the scarcity of data poses a significant bottleneck hindering community progress. In this paper, we release the largest ever medical Question Answering (QA) dataset with 26 Million QA pairs named Huatuo-26M.

- **[Fool Me Once? Contrasting Textual and Visual Explanations in a Clinical Decision-Support Setting](https://aclanthology.org/2024.emnlp-main.1051/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** The growing capabilities of AI models are leading to their wider use, including in safety-critical domains. Explainable AI (XAI) aims to make these models safer to use by making their inference process more transparent.

## Computer Vision and Graphics

- **[OSFAL: Orthogonal Cross-Spectral Feature Alignment and Layer-Localized Cross-View Learning for Any-Scenario Person Re-Identification](https://openreview.net/forum?id=3WJt45k8b3)** — *ICLR 2027 · Under review*
  - **Topic:** Cross-spectral person re-identification
  - **Summary:** Addresses cross-spectral and aerial-ground person re-identification by aligning spectral features and learning hierarchical cross-view features in one model.

- **[VolS-GS: Relightable Gaussian Splatting With Volumetric Subsurface Scattering](https://openreview.net/forum?id=RWcRiQ45vV)** — *ICLR 2027 · Under review*
  - **Topic:** Gaussian Splatting and light transport
  - **Summary:** Applies differentiable volumetric light transport to Gaussian Splatting to model subsurface scattering. The method reconstructs relightable objects from captures under a single light source.

- **[$\\pi^3$: Permutation-Equivariant Visual Geometry Learning](https://openreview.net/forum?id=DTQIjngDta)** — *ICLR 2026 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** $\pi^3$ is a feed-forward model that reconstructs 3D geometry without a fixed reference view, making it more robust and accurate for tasks like camera pose and depth estimation.

- **[Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator](https://openreview.net/forum?id=kI27Niy4xY)** — *ICLR 2026 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Text-to-3D scene generative modelling by unifying a video generative model with a foundational 3D model via model stitching and alignment.

- **[A Distributional View for Visual Mechanistic Interpretability: KL-Minimal Soft-Constraint Principle](https://openreview.net/forum?id=TZvHUmClPP)** — *ICML 2026 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Most current paradigms in visual mechanistic interpretability (MI) remain confined to interpreting internal units of the vision model via heuristic methods (e.g., top-$K$ activation retrieval or optimization with regularization). In this work, we establish a theoretical distributional view for visual MI, which models the influence of a feature activation on the natural image distribution, thereby formulating a Kullback-Leibler...

- **[3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model](https://openreview.net/forum?id=1PQ7pf3kVm)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Feed-forward 3D reconstruction models have demonstrated strong generalization under large-scale pre-training, yet they struggle in long-tail scenarios such as low-light reconstruction, joint human-scene reconstruction, and test-time adaptation. We observe relational attention structure collapse, manifested as the failure of cross-view correspondences, as a primary cause of these limitations.

- **[A multi-scale information geometry reveals the structure of mutual information in neural populations](https://openreview.net/forum?id=B1fQuBGYFx)** — *NeurIPS 2026 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Understanding how neural population responses represent sensory information is a central problem in systems neuroscience. One approach is to define a representational geometry on stimulus space in which distances reflect how reliably stimuli can be distinguished from neural activity.

- **[AdaCodec: A Predictive Visual Code for Video MLLMs](https://openreview.net/forum?id=utdVAXHnlv)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Video is temporally redundant: adjacent frames usually share most objects, background, and layout. Yet existing video multimodal large language models (video MLLMs) usually encode each sampled frame as an independent RGB image, causing visual tokens to repeat content already present in earlier frames.

- **[AdapToPASS: Ambiguity-aware Adaptive Spherical Transformer for Panoramic Semantic Segmentation](https://openreview.net/forum?id=WWQOepiVLd)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Spherical Transformers have emerged as a promising framework for panoramic semantic segmentation (PASS) by operating directly on spherical geometry and alleviating projection-induced distortions. However, existing architectures rely on assumptions of canonical spherical structure and stable viewpoints, which are frequently violated in real-world $360^\circ$ imagery due to unconstrained camera motion, introducing significant...

- **[EfficientVMamba: Atrous Selective Scan for Light Weight Visual Mamba](https://ojs.aaai.org/index.php/AAAI/article/view/32690)** — *AAAI 2025*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Prior efforts in light-weight model development mainly centered on CNN and Transformer-based designs yet faced persistent challenges. CNNs adept at local feature extraction compromise resolution while Transformers offer global reach but escalate computational demands O(N^2).

- **[IMAGDressing-v1: Customizable Virtual Dressing](https://ojs.aaai.org/index.php/AAAI/article/view/32729)** — *AAAI 2025*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Existing virtual try-on (VTON) methods provide only limited user control over garment attributes and generally overlook essential factors such as face, pose, and scene context. To address these limitations, we introduce the virtual dressing (VD) task, which aims to synthesize freely editable human images conditioned on fixed garments and optional user-defined inputs.

- **[Point Cloud Mamba: Point Cloud Learning via State Space Model](https://ojs.aaai.org/index.php/AAAI/article/view/33098)** — *AAAI 2025*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Recently, state space models have exhibited strong global modeling capabilities and linear computational complexity in contrast to transformers. This research focuses on applying such architecture to more efficiently and effectively model point cloud data globally with linear computational complexity.

- **[Segment Any 3D Gaussians](https://ojs.aaai.org/index.php/AAAI/article/view/32193)** — *AAAI 2025*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** This paper presents SAGA (Segment Any 3D GAussians), a highly efficient 3D promptable segmentation method based on 3D Gaussian Splatting (3D-GS). Given 2D visual prompts as input, SAGA can segment the corresponding 3D target represented by 3D Gaussians within 4 ms.

- **[U-KAN Makes Strong Backbone for Medical Image Segmentation and Generation](https://ojs.aaai.org/index.php/AAAI/article/view/32491)** — *AAAI 2025*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** U-Net has become a cornerstone in various visual applications such as image segmentation and diffusion probability models. While numerous innovative designs and improvements have been introduced by incorporating transformers or MLPs, the networks are still limited to linearly modeling patterns as well as the deficient interpretability.

- **[DepthCrafter: Generating Consistent Long Depth Sequences for Open-world Videos](https://openaccess.thecvf.com/content/CVPR2025/html/Hu_DepthCrafter_Generating_Consistent_Long_Depth_Sequences_for_Open-world_Videos_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Estimating video depth in open-world scenarios is challenging due to the diversity of videos in appearance, content motion, camera movement, and length. We present DepthCrafter, an innovative method for generating temporally consistent long depth sequences with intricate details for open-world videos, without requiring any supplementary information such as camera poses or optical flow.

- **[Identity-Preserving Text-to-Video Generation by Frequency Decomposition](https://openaccess.thecvf.com/content/CVPR2025/html/Yuan_Identity-Preserving_Text-to-Video_Generation_by_Frequency_Decomposition_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Identity-preserving text-to-video (IPT2V) generation aims to create high-fidelity videos with consistent human identity. It is an important task in video generation but remains an open problem for generative models.

- **[MoSca: Dynamic Gaussian Fusion from Casual Videos via 4D Motion Scaffolds](https://openaccess.thecvf.com/content/CVPR2025/html/Lei_MoSca_Dynamic_Gaussian_Fusion_from_Casual_Videos_via_4D_Motion_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We introduce 4D Motion Scaffolds (MoSca), a modern 4D reconstruction system designed to reconstruct and synthesize novel views of dynamic scenes from monocular videos captured casually in the wild. To address such a challenging and ill-posed inverse problem, we leverage prior knowledge from foundational vision models and lift the video data to a novel Motion Scaffold (MoSca) representation, which compactly and smoothly encodes the...

- **[Structured 3D Latents for Scalable and Versatile 3D Generation](https://openaccess.thecvf.com/content/CVPR2025/html/Xiang_Structured_3D_Latents_for_Scalable_and_Versatile_3D_Generation_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We introduce a novel 3D generation method for versatile and high-quality 3D asset creation.The cornerstone is a unified Structured LATent (SLAT) representation which allows decoding to different output formats, such as Radiance Fields, 3D Gaussians, and meshes. This is achieved by integrating a sparsely-populated 3D grid with dense multiview visual features extracted from a powerful vision foundation model, comprehensively capturing...

- **[UniReal: Universal Image Generation and Editing via Learning Real-world Dynamics](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_UniReal_Universal_Image_Generation_and_Editing_via_Learning_Real-world_Dynamics_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We introduce UniReal, a unified framework designed to address various image generation and editing tasks. Existing solutions often vary by tasks, yet share fundamental principles: preserving consistency between inputs and outputs while capturing visual variations.

- **[Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis](https://openaccess.thecvf.com/content/CVPR2025/html/Fu_Video-MME_The_First-Ever_Comprehensive_Evaluation_Benchmark_of_Multi-modal_LLMs_in_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** In the quest for artificial general intelligence, Multi-modal Large Language Models (MLLMs) have emerged as a focal point in recent advancements. However, the predominant focus remains on developing their capabilities in static image understanding.

- **[WonderWorld: Interactive 3D Scene Generation from a Single Image](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_WonderWorld_Interactive_3D_Scene_Generation_from_a_Single_Image_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We present WonderWorld, a novel framework for interactive 3D scene generation that enables users to interactively specify scene contents and layout and see the created scenes in low latency. The major challenge lies in achieving fast generation of 3D scenes.

- **["Principal Components" Enable A New Language of Images](https://openaccess.thecvf.com/content/ICCV2025/html/Wen_Principal_Components_Enable_A_New_Language_of_Images_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We introduce a novel visual tokenization framework that embeds a provable PCA-like structure into the latent token space. While existing visual tokenizers primarily optimize for reconstruction fidelity, they often neglect the structural properties of the latent space--a critical factor for both interpretability and downstream tasks.

- **[2D Gaussian Splatting-based Sparse-view Transparent Object Depth Reconstruction via Physics Simulation for Scene Update](https://openaccess.thecvf.com/content/ICCV2025/html/Kim_2D_Gaussian_Splatting-based_Sparse-view_Transparent_Object_Depth_Reconstruction_via_Physics_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Understanding the 3D geometry of transparent objects from RGB images is challenging due to their inherent physical properties, such as reflection and refraction. To address these difficulties, especially in scenarios with sparse views and dynamic environments, we introduce TRAN-D, a novel 2D Gaussian Splatting-based depth reconstruction method for transparent objects.

- **[2HandedAfforder: Learning Precise Actionable Bimanual Affordances from Human Videos](https://openaccess.thecvf.com/content/ICCV2025/html/Heidinger_2HandedAfforder_Learning_Precise_Actionable_Bimanual_Affordances_from_Human_Videos_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** When interacting with objects, humans effectively reason about which regions of objects are viable for an intended action, i.e., the affordance regions of the object. They can also account for subtle differences in object regions based on the task to be performed and whether one or two hands need to be used.

- **[3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Vision-language navigation (VLN) requires an agent to traverse complex 3D environments based on natural language instructions, necessitating a thorough scene understanding. While existing works equip agents with various scene representations to enhance spatial awareness, they often neglect the complex 3D geometry and rich semantics in VLN scenarios, limiting the ability to generalize across diverse and unseen environments.

- **[3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial Camouflage Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Lou_3D_Gaussian_Splatting_Driven_Multi-View_Robust_Physical_Adversarial_Camouflage_Generation_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Physical adversarial attack methods expose the vulnerabilities of deep neural networks and pose a significant threat to safety-critical scenarios such as autonomous driving. Camouflage-based physical attack is a more promising approach compared to the patch-based attack, offering stronger adversarial effectiveness in complex physical environments.

- **[3D Mesh Editing using Masked LRMs](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_3D_Mesh_Editing_using_Masked_LRMs_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We present a novel approach to mesh shape editing, building on recent progress in 3D reconstruction from multi-view images. We formulate shape editing as a conditional reconstruction problem, where the model must reconstruct the input shape with the exception of a specified 3D region, in which the geometry should be generated from the conditional signal.

- **[3D Test-time Adaptation via Graph Spectral Driven Point Shift](https://openaccess.thecvf.com/content/ICCV2025/html/Wei_3D_Test-time_Adaptation_via_Graph_Spectral_Driven_Point_Shift_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** While test-time adaptation (TTA) methods effectively address domain shifts by dynamically adapting pre-trained models to target domain data during online inference, their application to 3D point clouds is hindered by their irregular and unordered structure. Current 3D TTA methods often rely on computationally expensive spatial-domain optimizations and may require additional training data.

- **[3D-MOOD: Lifting 2D to 3D for Monocular Open-Set Object Detection](https://openaccess.thecvf.com/content/ICCV2025/html/Yang_3D-MOOD_Lifting_2D_to_3D_for_Monocular_Open-Set_Object_Detection_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Monocular 3D object detection is valuable for various applications such as robotics and AR/VR. Existing methods are confined to closed-set settings, where the training and testing sets consist of the same scenes and/or object categories.

- **[SAM 2: Segment Anything in Images and Videos](https://openreview.net/forum?id=Ha6RTeWMd0)** — *ICLR 2025 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We present Segment Anything Model 2 (SAM 2), a foundation model towards solving promptable visual segmentation in images and videos. We build a data engine, which improves model and data via user interaction, to collect the largest video segmentation dataset to date.

- **[Stop the Nonconsensual Use of Nude Images in Research](https://openreview.net/forum?id=Ev5xwr3vWh)** — *NeurIPS 2025 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** In order to train, test, and evaluate nudity detection models, machine learning researchers typically rely on nude images scraped from the Internet. Our research finds that this content is collected and, in some cases, subsequently \emph{distributed} by researchers without consent, leading to potential misuse and exacerbating harm against the subjects depicted. \textbf{This position paper argues that the distribution of...

- **[Learning to Manipulate Anywhere: A Visual Generalizable Framework For Reinforcement Learning](https://openreview.net/forum?id=jart4nhCQr)** — *CoRL 2024 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Can we endow visuomotor robots with generalization capabilities to operate in diverse open-world scenarios? In this paper, we propose Maniwhere, a generalizable framework tailored for visual reinforcement learning, enabling the trained robot policies to generalize across a combination of multiple visual disturbance types.

- **[Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding](https://openreview.net/forum?id=4Gr7XY897V)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Large language models have demonstrated impressive universal capabilities across a wide range of open-ended tasks and have extended their utility to encompass multimodal conversations. However existing methods encounter challenges in effectively handling both image and video understanding particularly with limited visual tokens.

- **[Gaussian Splatting SLAM](https://openreview.net/forum?id=JG1QNqyYAx)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We present the first application of 3D Gaussian Splatting in monocular SLAM the most fundamental but the hardest setup for Visual SLAM. Our method which runs live at 3fps utilises Gaussians as the only 3D representation unifying the required representation for accurate efficient tracking mapping and high-quality rendering.

- **[GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting](https://openreview.net/forum?id=vcOqRbHk4S)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** In this paper we introduce GS-SLAM that first utilizes 3D Gaussian representation in the Simultaneous Localization and Mapping (SLAM) system. It facilitates a better balance between efficiency and accuracy.

- **[Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding](https://openreview.net/forum?id=zV2ChTopvn)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Large Vision-Language Models (LVLMs) have advanced considerably intertwining visual recognition and language understanding to generate content that is not only coherent but also contextually attuned. Despite their success LVLMs still suffer from the issue of object hallucinations where models generate plausible yet incorrect outputs that include objects that do not exist in the images.

- **[Monkey: Image Resolution and Text Label Are Important Things for Large Multi-modal Models](https://openreview.net/forum?id=NZitcrCWos)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Large Multimodal Models (LMMs) have shown promise in vision-language tasks but struggle with high-resolution input and detailed scene understanding. Addressing these challenges we introduce Monkey to enhance LMM capabilities.

- **[MVBench: A Comprehensive Multi-modal Video Understanding Benchmark](https://openreview.net/forum?id=5XAIjTAiVE)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** With the rapid development of Multi-modal Large Language Models (MLLMs) a number of diagnostic benchmarks have recently emerged to evaluate the comprehension capabilities of these models. However most benchmarks predominantly assess spatial understanding in the static image tasks while overlooking temporal understanding in the dynamic video tasks.

- **[Scaffold-GS: Structured 3D Gaussians for View-Adaptive Rendering](https://openreview.net/forum?id=GKA4hmpBHa)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Summary unavailable in the public source record.

- **[VBench: Comprehensive Benchmark Suite for Video Generative Models](https://openreview.net/forum?id=botzvmshkA)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Video generation has witnessed significant advancements yet evaluating these models remains a challenge. A comprehensive evaluation benchmark for video generation is indispensable for two reasons: 1) Existing metrics do not fully align with human perceptions; 2) An ideal evaluation system should provide insights to inform future developments of video generation.

- **[Wonder3D: Single Image to 3D using Cross-Domain Diffusion](https://openreview.net/forum?id=ozhMlCjv24)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** In this work we introduce Wonder3D a novel method for generating high-fidelity textured meshes from single-view images with remarkable efficiency. Recent methods based on the Score Distillation Sampling (SDS) loss methods have shown the potential to recover 3D geometry from 2D diffusion priors but they typically suffer from time-consuming per-shape optimization and inconsistent geometry.

- **[An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10478_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "In this study, we identify the inefficient attention phenomena in Large Vision-Language Models (LVLMs), notably within prominent models like LLaVA-1.5, QwenVL-Chat, and Video-LLaVA. We find that the attention computation over visual tokens is extremely inefficient in the deep layers of popular LVLMs, suggesting a need for a sparser approach compared to textual data handling.

- **[DriveLM: Driving with Graph Visual Question Answering](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6870_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "We study how vision-language models (VLMs) trained on web-scale data can be integrated into end-to-end driving systems to boost generalization and enable interactivity with human users. While recent approaches adapt VLMs to driving via single-round visual question answering (VQA), human drivers reason about decisions in multiple steps.

- **[DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6298_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "Animating a still image offers an engaging visual experience. Traditional image animation techniques mainly focus on animating natural scenes with stochastic dynamics (e.g. clouds and fluid) or domain-specific motions (e.g. human hair or body motions), and thus limits their applicability to more general visual content.

- **[Grounding Image Matching in 3D with MASt3R](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9080_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "Image Matching is a core component of all best-performing algorithms and pipelines in 3D vision. Yet despite matching being fundamentally a 3D problem, intrinsically linked to camera pose and scene geometry, it is typically treated as a 2D problem.

- **[LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/465_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "3D content creation has achieved significant progress in terms of both quality and speed. Although current feed-forward models can produce 3D objects in seconds, their resolution is constrained by the intensive computation required during training.

- **[MotionDirector: Motion Customization of Text-to-Video Diffusion Models](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7327_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "Large-scale pre-trained diffusion models have exhibited remarkable capabilities in diverse video generations. Given a set of video clips of the same motion concept, the task of Motion Customization is to adapt existing text-to-video diffusion models to generate videos with this motion.

- **[MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3187_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "We introduce , an efficient model that, given sparse multi-view images as input, predicts clean feed-forward 3D Gaussians. To accurately localize the Gaussian centers, we build a cost volume representation via plane sweeping, where the cross-view feature similarities stored in the cost volume can provide valuable geometry cues to the estimation of depth.

- **[SV3D: Novel Multi-view Synthesis and 3D Generation from a Single Image using Latent Video Diffusion](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/150_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "We present Stable Video 3D (SV3D) — a latent video diffusion model for high-resolution, image-to-multi-view generation of orbital videos around a 3D object. Recent works propose to adapt 2D generative models for novel view synthesis (NVS) and 3D optimization.

- **[An image speaks a thousand words, but can everyone listen? On image transcreation for cultural relevance](https://aclanthology.org/2024.emnlp-main.573/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Given the rise of multimedia content, human translators increasingly focus on culturally adapting not only words but also other modalities such as images to convey the same meaning. While several applications stand to benefit from this, machine translation systems remain confined to dealing with language in speech and text.

- **[Threshold-driven Pruning with Segmented Maximum Term Weights for Approximate Cluster-based Sparse Retrieval](https://aclanthology.org/2024.emnlp-main.1101/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** This paper revisits dynamic pruning through rank score thresholding in cluster-based sparse retrieval to skip the index partially at cluster and document levels during inference. It proposes a two-parameter pruning control scheme called ASC with a probabilistic guarantee on rank-safeness competitiveness.

- **[Words Worth a Thousand Pictures: Measuring and Understanding Perceptual Variability in Text-to-Image Generation](https://aclanthology.org/2024.emnlp-main.311/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Diffusion models are the state of the art in text-to-image generation, but their perceptual variability remains understudied. In this paper, we examine how prompts affect image variability in black-box diffusion-based models.

- **[DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation](https://openreview.net/forum?id=UyNXMqnN3c)** — *ICLR 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Recent advances in 3D content creation mostly leverage optimization-based 3D generation via score distillation sampling (SDS). Though promising results have been exhibited, these methods often suffer from slow per-sample optimization, limiting their practical usage.

- **[LRM: Large Reconstruction Model for Single Image to 3D](https://openreview.net/forum?id=sllU8vvsFF)** — *ICLR 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We propose the first Large Reconstruction Model (LRM) that predicts the 3D model of an object from a single input image within just 5 seconds. In contrast to many previous methods that are trained on small-scale datasets such as ShapeNet in a category-specific fashion, LRM adopts a highly scalable transformer-based architecture with 500 million learnable parameters to directly predict a neural radiance field (NeRF) from the input image.

- **[Real3D-Portrait: One-shot Realistic 3D Talking Portrait Synthesis](https://openreview.net/forum?id=7ERQPyR2eb)** — *ICLR 2024 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** One-shot 3D talking portrait generation aims to reconstruct a 3D avatar from an unseen image, and then animate it with a reference video or audio to generate a talking portrait video. The existing methods fail to simultaneously achieve the goals of accurate 3D avatar reconstruction and stable talking face animation.

- **[SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis](https://openreview.net/forum?id=di52zR8xgf)** — *ICLR 2024 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We present Stable Diffusion XL (SDXL), a latent diffusion model for text-to-image synthesis. Compared to previous versions of Stable Diffusion, SDXL leverages a three times larger UNet backbone, achieved by significantly increasing the number of attention blocks and including a second text encoder.

- **[SyncDreamer: Generating Multiview-consistent Images from a Single-view Image](https://openreview.net/forum?id=MN3yH2ovHb)** — *ICLR 2024 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** In this paper, we present a novel diffusion model called SyncDreamer that generates multiview-consistent images from a single-view image. Using pretrained large-scale 2D diffusion models, recent work Zero123 demonstrates the ability to generate plausible novel views from a single-view image of an object.

- **[DoRA: Weight-Decomposed Low-Rank Adaptation](https://openreview.net/forum?id=3d5CIRG1n2)** — *ICML 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Among the widely used parameter-efficient fine-tuning (PEFT) methods, LoRA and its variants have gained considerable popularity because of avoiding additional inference costs. However, there still often exists an accuracy gap between these methods and full fine-tuning (FT).

- **[Genie: Generative Interactive Environments](https://openreview.net/forum?id=bJbSbJskOS)** — *ICML 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We introduce Genie, the first *generative interactive environment* trained in an unsupervised manner from unlabelled Internet videos. The model can be prompted to generate an endless variety of action-controllable virtual worlds described through text, synthetic images, photographs, and even sketches.

- **[Scaling Rectified Flow Transformers for High-Resolution Image Synthesis](https://openreview.net/forum?id=FPnUhsQJ5B)** — *ICML 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Diffusion models create data from noise by inverting the forward paths of data towards noise and have emerged as a powerful generative modeling technique for high-dimensional, perceptual data such as images and videos. Rectified flow is a recent generative model formulation that connects data and noise in a straight line.

- **[ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://ieeexplore.ieee.org/document/10610243/)** — *ICRA 2024 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** For robots to perform a wide variety of tasks, they require a 3D representation of the world that is semantically rich, yet compact and efficient for task-driven perception and planning. Recent approaches have attempted to leverage features from large vision-language models to encode semantics in 3D representations.

- **[CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://openreview.net/forum?id=E18kRXTGmV)** — *NeurIPS 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Visual Question Answering~(VQA) is an important task in multimodal AI, which requires models to understand and reason on knowledge present in visual and textual data. However, most of the current VQA datasets and models are primarily focused on English and a few major world languages, with images that are Western-centric.

- **[GAIA: Rethinking Action Quality Assessment for AI-Generated Videos](https://openreview.net/forum?id=BZe6dmDk5K)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Assessing action quality is both imperative and challenging due to its significant impact on the quality of AI-generated videos, further complicated by the inherently ambiguous nature of actions within AI-generated video (AIGV). Current action quality assessment (AQA) algorithms predominantly focus on actions from real specific scenarios and are pre-trained with normative action features, thus rendering them inapplicable in AIGVs.

## Speech and Audio

- **[Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition](https://openreview.net/forum?id=sSbEEHNEsL)** — *ICLR 2026 · Poster*
  - **Topic:** Speech, audio, and music
  - **Summary:** Unified Speech Recognition (USR) has emerged as a semi-supervised framework for training a single model for audio, visual, and audiovisual speech recognition, achieving state-of-the-art results on in-distribution benchmarks. However, its reliance on autoregressive pseudo-labelling makes training expensive, while its decoupled supervision of CTC and attention branches increases susceptibility to self-reinforcing errors, particularly...

- **[HateDay: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter](https://aclanthology.org/2025.acl-long.115/)** — *ACL 2025 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** To address the global challenge of online hate speech, prior research has developed detection models to flag such content on social media. However, due to systematic biases in evaluation datasets, the real-world effectiveness of these models remains unclear, particularly across geographies.

- **[IndicSynth: A Large-Scale Multilingual Synthetic Speech Dataset for Low-Resource Indian Languages](https://aclanthology.org/2025.acl-long.1070/)** — *ACL 2025 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** Recent advances in synthetic speech generation technology have facilitated the generation of high-quality synthetic (fake) speech that emulates human voices. These technologies pose a threat of misuse for identity theft and the spread of misinformation.

- **[Toward Automatic Discovery of a Canine Phonetic Alphabet](https://aclanthology.org/2025.acl-long.451/)** — *ACL 2025 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** Dogs communicate intelligently but little is known about the phonetic properties of their vocalization communication. For the first time, this paper presents an iterative algorithm inspired by human phonetic discovery, which is based on minimal pairs that determine phonemes by distinguishing different words in human language, and is able to produce a complete alphabet of distinct canine phoneme-like units.

- **[AudioGPT: Understanding and Generating Speech, Music, Sound, and Talking Head](https://ojs.aaai.org/index.php/AAAI/article/view/30570)** — *AAAI 2024*
  - **Topic:** Speech, audio, and music
  - **Summary:** Large language models (LLMs) have exhibited remarkable capabilities across a variety of domains and tasks, challenging our understanding of learning and cognition. Despite the recent success, current LLMs are not capable of processing complex audio information or conducting spoken conversations (like Siri or Alexa).

- **[Language Complexity and Speech Recognition Accuracy: Orthographic Complexity Hurts, Phonological Complexity Doesn’t](https://aclanthology.org/2024.acl-long.827/)** — *ACL 2024 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** We investigate what linguistic factors affect the performance of Automatic Speech Recognition (ASR) models. We hypothesize that orthographic and phonological complexities both degrade accuracy.

- **[Let’s Go Real Talk: Spoken Dialogue Model for Face-to-Face Conversation](https://aclanthology.org/2024.acl-long.860/)** — *ACL 2024 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** In this paper, we introduce a novel Face-to-Face spoken dialogue model. It processes audio-visual speech from user input and generates audio-visual speech as the response, marking the initial step towards creating an avatar chatbot system without relying on intermediate text.

- **[Speech Translation with Speech Foundation Models and Large Language Models: What is There and What is Missing?](https://aclanthology.org/2024.acl-long.789/)** — *ACL 2024 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** The field of natural language processing (NLP) has recently witnessed a transformative shift with the emergence of foundation models, particularly Large Language Models (LLMs) that have revolutionized text-based NLP. This paradigm has extended to other modalities, including speech, where researchers are actively exploring the combination of Speech Foundation Models (SFMs) and LLMs into single, unified models capable of addressing...

- **[Towards Robust Speech Representation Learning for Thousands of Languages](https://aclanthology.org/2024.emnlp-main.570/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Speech, audio, and music
  - **Summary:** Self-supervised learning (SSL) has helped extend speech technologies to more languages by reducing the need for labeled data. However, models are still far from supporting the world’s 7000+ languages.

- **[Twists, Humps, and Pebbles: Multilingual Speech Recognition Models Exhibit Gender Performance Gaps](https://aclanthology.org/2024.emnlp-main.1188/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Speech, audio, and music
  - **Summary:** Current automatic speech recognition (ASR) models are designed to be used across many languages and tasks without substantial changes. However, this broad language coverage hides performance gaps within languages, for example, across genders.

- **[NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models](https://openreview.net/forum?id=dVhrnjZJad)** — *ICML 2024 · Oral*
  - **Topic:** Speech, audio, and music
  - **Summary:** While recent large-scale text-to-speech (TTS) models have achieved significant progress, they still fall shorts in speech quality, similarity, and prosody. Considering that speech intricately encompasses various attributes (e.g., content, prosody, timbre, and acoustic details) that pose significant challenges for generation, a natural idea is to factorize speech into individual subspaces representing different attributes and...

- **[GTSinger: A Global Multi-Technique Singing Corpus with Realistic Music Scores for All Singing Tasks](https://openreview.net/forum?id=z64azPC6Nl)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Speech, audio, and music
  - **Summary:** The scarcity of high-quality and multi-task singing datasets significantly hinders the development of diverse controllable and personalized singing tasks, as existing singing datasets suffer from low quality, limited diversity of languages and singers, absence of multi-technique information and realistic music scores, and poor task suitability. To tackle these problems, we present GTSinger, a large Global, multi-Technique,...

## Multimodal Learning

- **[Generative Universal Verifier as Multimodal Meta-Reasoner](https://openreview.net/forum?id=DM0Y0oL33T)** — *ICLR 2026 · Oral*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** We introduce *Generative Universal Verifier*, a novel concept and plugin designed for next-generation multimodal reasoning in vision-language models and unified multimodal models, providing the fundamental capability of reflection and refinement on visual outcomes during the reasoning and generation process. This work makes three main contributions: (1) We build **ViVerBench**, a comprehensive benchmark spanning $16$ categories of...

- **[$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](https://openreview.net/forum?id=vlhoswksBO)** — *CoRL 2025 · Oral*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild.

- **[Multimodal Autoregressive Pre-training of Large Vision Encoders](https://openaccess.thecvf.com/content/CVPR2025/html/Fini_Multimodal_Autoregressive_Pre-training_of_Large_Vision_Encoders_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** We introduce a novel method for pre-training of large-scale vision encoders. Building on recent advancements in autoregressive pre-training of vision models, we extend this framework to a multimodal setting, i.e., images and text.

- **[2.5 Years in Class: A Multimodal Textbook for Vision-Language Pretraining](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_2.5_Years_in_Class_A_Multimodal_Textbook_for_Vision-Language_Pretraining_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** Compared to image-text pair data, interleaved corpora enable Vision-Language Models (VLMs) to understand the world more naturally like humans. However, such existing datasets are crawled from webpage, facing challenges like low knowledge density, loose image-text relations, and poor logical coherence between images.

- **[LMMs-Eval: Reality Check on the Evaluation of Large Multimodal Models](https://aclanthology.org/2025.findings-naacl.51/)** — *NAACL 2025 · Findings*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** The advances of large foundation models necessitate wide-coverage, low-cost, and zero-contamination benchmarks. Despite continuous exploration of language model evaluations, comprehensive studies on the evaluation of Large Multi-modal Models (LMMs) remain limited.

- **[Detecting and Preventing Hallucinations in Large Vision Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/29771)** — *AAAI 2024*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** Instruction tuned Large Vision Language Models (LVLMs) have significantly advanced in generalizing across a diverse set of multi-modal tasks, especially for Visual Question Answering (VQA). However, generating detailed responses that are visually grounded is still a challenging task for these models.

- **[CaMML: Context-Aware Multimodal Learner for Large Models](https://aclanthology.org/2024.acl-long.223/)** — *ACL 2024 · Long*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** In this work, we introduce Context-Aware MultiModal Learner (CaMML), for tuning large multimodal models (LMMs). CaMML, a lightweight module, is crafted to seamlessly integrate multimodal contextual samples into large models, thereby empowering the model to derive knowledge from analogous, domain-specific, up-to-date information and make grounded inferences.

- **[MMToM-QA: Multimodal Theory of Mind Question Answering](https://aclanthology.org/2024.acl-long.851/)** — *ACL 2024 · Long*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** Theory of Mind (ToM), the ability to understand people’s mental states, is an essential ingredient for developing machines with human-level social intelligence. Recent machine learning models, particularly large language models, seem to show some aspects of ToM understanding.

- **[OpenVLA: An Open-Source Vision-Language-Action Model](https://openreview.net/forum?id=ZMnD6QZAE6)** — *CoRL 2024 · Poster*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** Large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new behaviors from scratch, we can fine-tune such vision-language-action (VLA) models to obtain robust, generalizable policies for visuomotor control. Yet, widespread adoption of VLAs for robotics has been challenging as 1) existing VLAs...

- **[mPLUG-Owl2: Revolutionizing Multi-modal Large Language Model with Modality Collaboration](https://openreview.net/forum?id=3HLrlk9Vyj)** — *CVPR 2024 · Highlight*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** Multi-modal Large Language Models (MLLMs) have demonstrated impressive instruction abilities across various open-ended tasks. However previous methods have primarily focused on enhancing multi-modal capabilities.

- **[MMBENCH: Is Your Multi-Modal Model an All-around Player?](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/959_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** "Large vision-language models (VLMs) have recently achieved remarkable progress, exhibiting impressive multimodal perception and reasoning abilities. However, effectively evaluating these large VLMs remains a major challenge, hindering future development in this domain.

## Robotics and Embodied AI

- **[Embodied Navigation Foundation Model](https://openreview.net/forum?id=kkBOIsrCXh)** — *ICLR 2026 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We propose a cross-task and cross-embodiment navigation foundation model.

- **[Language Prompt for Autonomous Driving](https://ojs.aaai.org/index.php/AAAI/article/view/32902)** — *AAAI 2025*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** A new trend in the computer vision community is to capture objects of interest following flexible human command represented by a natural language prompt. However, the progress of using language prompts in driving scenarios is stuck in a bottleneck due to the scarcity of paired prompt-instance data.

- **[AirExo-2: Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons](https://openreview.net/forum?id=ksOrtEgIC0)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Scaling up robotic imitation learning for real-world applications requires efficient and scalable demonstration collection methods. While teleoperation is effective, it depends on costly and inflexible robot platforms.

- **[ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes](https://openreview.net/forum?id=4XKKUifQ9c)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions. Existing methods primarily focus on single-object grasping or grasp-pose prediction without interaction, which are insufficient for complex, cluttered scenes.

- **[DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration](https://openreview.net/forum?id=Tl7girqoLi)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Imitation learning has shown great promise in robotic manipulation, but the policy’s execution is often unsatisfactorily slow due to commonly tardy demonstrations collected by human operators. In this work, we present DemoSpeedup, a self-supervised method to accelerate visuomotor policy execution via entropy-guided demonstration acceleration.

- **[DexSkin: High-Coverage Conformable Robotic Skin for Learning Contact-Rich Manipulation](https://openreview.net/forum?id=CNPCSuwxJw)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Human skin provides a rich tactile sensing stream, localizing intentional and unintentional contact events over a large and contoured region. Replicating these tactile sensing capabilities for dexterous robotic manipulation systems remains a longstanding challenge.

- **[DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation](https://openreview.net/forum?id=XrgRvBklWu)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We present DexUMI - a data collection and policy learning framework that uses the human hand as the natural interface to transfer dexterous manipulation skills to various robot hands. DexUMI incorporates hardware and software adaptations to minimize the embodiment gap between the human hand and various robot hands.

- **[Fabrica: Dual-Arm Assembly of General Multi-Part Objects via Integrated Planning and Learning](https://openreview.net/forum?id=aSUNzvEJIf)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Multi-part assembly poses significant challenges for robotic systems to execute long-horizon, contact-rich manipulation with generalization across complex geometries. We present a dual-arm robotic system capable of end-to-end planning and control for autonomous assembly of general multi-part objects.

- **[FACET: Force-Adaptive Control via Impedance Reference Tracking for Legged Robots](https://openreview.net/forum?id=EcOGafgvuC)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Reinforcement learning (RL) has made significant strides in legged robot control, enabling locomotion across diverse terrains and complex loco-manipulation capabilities. However, the commonly used position or velocity tracking-based objectives are agnostic to forces experienced by the robot, leading to stiff and potentially dangerous behaviors and poor control during forceful interactions.

- **[Emerging Risks from Embodied AI Require Urgent Policy Action](https://openreview.net/forum?id=fXiPp3qvrW)** — *NeurIPS 2025 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** The field of embodied AI (EAI) is rapidly advancing. Unlike virtual AI, EAI systems can exist in, learn from, reason about, and act in the physical world.

- **[A Language Agent for Autonomous Driving](https://openreview.net/forum?id=UPE6WYE8vg)** — *COLM 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Human-level driving is an ultimate goal of autonomous driving. Conventional approaches formulate autonomous driving as a perception-prediction-planning framework, yet their systems do not capitalize on the inherent reasoning ability and experiential knowledge of humans.

- **[D$^3$RoMa: Disparity Diffusion-based Depth Sensing for Material-Agnostic Robotic Manipulation](https://openreview.net/forum?id=7E3JAys1xO)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Depth sensing is an important problem for 3D vision-based robotics. Yet, a real-world active stereo or ToF depth camera often produces noisy and incomplete depth which bottlenecks robot performances.

- **[HumanPlus: Humanoid Shadowing and Imitation from Humans](https://openreview.net/forum?id=WnSl42M9Z4)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** One of the key arguments for building robots that have similar form factors to human beings is that we can leverage the massive human data for training.Yet, doing so has remained challenging in practice due to the complexities in humanoid perception and control, lingering physical gaps between humanoids and humans in morphologies and actuation, and lack of a data pipeline for humanoids to learn autonomous skills from egocentric...

- **[Learning to Open and Traverse Doors with a Legged Manipulator](https://openreview.net/forum?id=VoC3wF6fbh)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Using doors is a longstanding challenge in robotics and is of significant practical interest in giving robots greater access to human-centric spaces. The task is challenging due to the need for online adaptation to varying door properties and precise control in manipulating the door panel and navigating through the confined doorway.

- **[Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild](https://openreview.net/forum?id=vBj5oC60Lk)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Recent works have proposed a number of general-purpose robotic foundation models that can control a variety of robotic platforms to perform a range of different tasks, including in the domains of navigation and manipulation. However, such models are typically trained via imitation learning, which precludes the ability to improve autonomously through experience that the robot gathers on the job.

- **[OCCAM: Online Continuous Controller Adaptation with Meta-Learned Models](https://openreview.net/forum?id=xeFKtSXPMd)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Control tuning and adaptation present a significant challenge to the usage of robots in diverse environments. It is often nontrivial to find a single set of control parameters by hand that work well across the broad array of environments and conditions that a robot might encounter.

- **[Play to the Score: Stage-Guided Dynamic Multi-Sensory Fusion for Robotic Manipulation](https://openreview.net/forum?id=N5IS6DzBmL)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Humans possess a remarkable talent for flexibly alternating to different senses when interacting with the environment. Picture a chef skillfully gauging the timing of ingredient additions and controlling the heat according to the colors, sounds, and aromas, seamlessly navigating through every stage of the complex cooking process.

- **[Reinforcement Learning with Foundation Priors: Let Embodied Agent Efficiently Learn on Its Own](https://openreview.net/forum?id=dsxmR6lYlg)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Reinforcement learning (RL) is a promising approach for solving robotic manipulation tasks. However, it is challenging to apply the RL algorithms directly in the real world.

- **[Robotic Control via Embodied Chain-of-Thought Reasoning](https://openreview.net/forum?id=S70MgnIA0v)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** A key limitation of learned robot control policies is their inability to generalize outside their training data. Recent works on vision-language-action models (VLAs) have shown that the use of large, internet pre-trained vision-language models as the backbone of learned robot policies can substantially improve their robustness and generalization ability.

- **[Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation](https://openreview.net/forum?id=AuJnXGq3AL)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Modern machine learning systems rely on large datasets to attain broad generalization, and this often poses a challenge in robotic learning, where each robotic platform and task might have only a small dataset. By training a single policy across many different kinds of robots, a robotic learning method can leverage much broader and more diverse datasets, which in turn can lead to better generalization and robustness.

- **[Visual Whole-Body Control for Legged Loco-Manipulation](https://openreview.net/forum?id=cT2N3p1AcE)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We study the problem of mobile manipulation using legged robots equipped with an arm, namely legged loco-manipulation. The robot legs, while usually utilized for mobility, offer an opportunity to amplify the manipulation capabilities by conducting whole-body control.

- **[Thin-Shell Object Manipulations With Differentiable Physics Simulations](https://openreview.net/forum?id=KsUh8MMFKQ)** — *ICLR 2024 · Spotlight*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** In this work, we aim to teach robots to manipulate various thin-shell materials. Prior works studying thin-shell object manipulation mostly rely on heuristic policies or learn policies from real-world video demonstrations, and only focus on limited material types and tasks (e.g., cloth unfolding).

- **[Extreme Parkour with Legged Robots](https://ieeexplore.ieee.org/document/10610200/)** — *ICRA 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Humans can perform parkour by traversing obstacles in a highly dynamic fashion requiring precise eye-muscle coordination and movement. Getting robots to do the same task requires overcoming similar challenges.

- **[NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://ieeexplore.ieee.org/document/10610665/)** — *ICRA 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Robotic learning for navigation in unfamiliar environments needs to provide policies for both task-oriented navigation (i.e., reaching a goal that the robot has located), and task-agnostic exploration (i.e., searching for a goal in a novel setting). Typically, these roles are handled by separate models, for example by using subgoal proposals, planning, or separate navigation strategies.

- **[Open X-Embodiment: Robotic Learning Datasets and RT-X Models : Open X-Embodiment Collaboration0](https://ieeexplore.ieee.org/document/10611477/)** — *ICRA 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Large, high-capacity models trained on diverse datasets have shown remarkable successes on efficiently tackling downstream applications. In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting point for many applications.

- **[Physically Grounded Vision-Language Models for Robotic Manipulation](https://ieeexplore.ieee.org/document/10610090/)** — *ICRA 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Recent advances in vision-language models (VLMs) have led to improved performance on tasks such as visual question answering and image captioning. Consequently, these models are now well-positioned to reason about the physical world, particularly within domains such as robotic manipulation.

- **[RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking](https://ieeexplore.ieee.org/document/10611293/)** — *ICRA 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** The grand aim of having a single robot that can manipulate arbitrary objects in diverse settings is at odds with the paucity of robotics datasets. Acquiring and growing such datasets is strenuous due to manual efforts, operational costs, and safety challenges.

- **[CoPa: General Robotic Manipulation through Spatial Constraints of Parts with Foundation Models](https://ieeexplore.ieee.org/document/10801352/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Foundation models pre-trained on web-scale data are shown to encapsulate extensive world knowledge beneficial for robotic manipulation in the form of task planning. However, the actual physical implementation of these plans often relies on task-specific learning methods, which require significant data collection and struggle with generalizability.

- **[Extended Tree Search for Robot Task and Motion Planning](https://ieeexplore.ieee.org/document/10802552/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Integrated Task and Motion Planning (TAMP) offers opportunities for achieving generalized autonomy in robots but also poses challenges. It involves searching in both symbolic task space and high-dimensional motion space, while also addressing geometrically infeasible actions within its hierarchical process.

- **[GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators](https://ieeexplore.ieee.org/document/10801581/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Humans can teleoperate robots to accomplish complex manipulation tasks. Imitation learning has emerged as a powerful framework that leverages human teleoperated demonstrations to teach robots new skills.

- **[Learning Agile Locomotion on Risky Terrains](https://ieeexplore.ieee.org/document/10801909/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Quadruped robots have shown remarkable mobility on various terrains through reinforcement learning. Yet, in the presence of sparse footholds and risky terrains such as stepping stones and balance beams, which require precise foot placement to avoid falls, model-based approaches are often used.

- **[Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](https://ieeexplore.ieee.org/document/10801984/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We present Human to Humanoid (H2O), a reinforcement learning (RL) based framework that enables real-time whole-body teleoperation of a full-sized humanoid robot with only an RGB camera. To create a large-scale retargeted motion dataset of human movements for humanoid robots, we propose a scalable "sim-to-data" process to filter and pick feasible motions using a privileged motion imitator.

- **[Whole-body Humanoid Robot Locomotion with Human Reference](https://ieeexplore.ieee.org/document/10801451/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Recently, humanoid robots have made significant advances in their ability to perform challenging tasks due to the deployment of Reinforcement Learning (RL), however, the inherent complexity of humanoid robots, including the difficulty of designing complicated reward functions and training entire sophisticated systems, still poses a notable challenge. To conquer these challenges, after many iterations and in-depth investigations, we...

- **[Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making](https://openreview.net/forum?id=iSwK1YqO7v)** — *NeurIPS 2024 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We aim to evaluate Large Language Models (LLMs) for embodied decision making. While a significant body of work has been leveraging LLMs for decision making in embodied environments, we still lack a systematic understanding of their performance because they are usually applied in different domains, for different purposes, and built based on different inputs and outputs.

- **[SpreadsheetBench: Towards Challenging Real World Spreadsheet Manipulation](https://openreview.net/forum?id=KYxzmRLF6i)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We introduce SpreadsheetBench, a challenging spreadsheet manipulation benchmark exclusively derived from real-world scenarios, designed to immerse current large language models (LLMs) in the actual workflow of spreadsheet users. Unlike existing benchmarks that rely on synthesized queries and simplified spreadsheet files, SpreadsheetBench is built from 912 real questions gathered from online Excel forums, which reflect the intricate...

## Reinforcement Learning and Decision-Making

- **[Learning While Scheduling Jobs under Context-Dependent Service Rates: An Anytime Rate-Optimal Algorithm](https://openreview.net/forum?id=ZZ2jyq4qFC)** — *ICLR 2027 · Under review*
  - **Topic:** Contextual bandits and job scheduling
  - **Summary:** Studies online learning and job scheduling when service rates are unknown. It proposes WISE, an anytime algorithm with queue-regret guarantees that does not require a known time horizon.

- **[Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data](https://openreview.net/forum?id=oBXfPyi47m)** — *ICLR 2026 · Poster*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** Leveraging offline data is a promising way to improve the sample efficiency of online reinforcement learning (RL). This paper expands the pool of usable data for offline-to-online RL by leveraging abundant non-curated data that is reward-free, of mixed quality, and collected across multiple embodiments.

- **[A Causal Decomposition Approach for Fair Contextual Multi-Armed Bandits](https://openreview.net/forum?id=kHEL0GD175)** — *ICML 2026 · Spotlight*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** Counterfactual reasoning is one of the fundamental facets of human cognition, involved in various tasks such as explanation, credit assignment, blame, and responsibility. It describes the queries what would have happened had some intervention been performed given that something else, corresponding to Layer 3 of the Pearl Causal Hierarchy.

- **[Adaptive Stepsizes for Eligibility Traces in Deep Reinforcement Learning](https://openreview.net/forum?id=LfxKFrgnlA)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** Modern deep reinforcement learning algorithms often store past sensory observations in a buffer for later replay and learning. However, this process is biologically implausible; animals do not store raw sensory observations.

- **[Corruption Robust Offline Reinforcement Learning with Human Feedback](https://openreview.net/forum?id=AM5VTtoexY)** — *AISTATS 2025 · Oral*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** We study data corruption robustness for reinforcement learning with human feedback (RLHF) in an offline setting. Given an offline dataset of pairs of trajectories along with feedback about human preferences, an $\varepsilon$-fraction of the pairs is corrupted (e.g., feedback flipped or trajectory features manipulated), capturing an adversarial attack or noisy human preferences.

- **[Distributional Counterfactual Explanations With Optimal Transport](https://openreview.net/forum?id=cGnnwEm2gu)** — *AISTATS 2025 · Oral*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** Counterfactual explanations (CE) are the de facto method for providing insights into black-box decision-making models by identifying alternative inputs that lead to different outcomes. However, existing CE approaches, including group and global methods, focus predominantly on specific input modifications, lacking the ability to capture nuanced distributional characteristics that influence model outcomes across the entire...

- **[Generative Flow Networks as Entropy-Regularized RL](https://proceedings.mlr.press/v238/tiapkin24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** The recently proposed generative flow networks (GFlowNets) are a method of training a policy to sample compositional discrete objects with probabilities proportional to a given reward via a sequence of actions. GFlowNets exploit the sequential nature of the problem, drawing parallels with reinforcement learning (RL).

- **[Privileged Sensing Scaffolds Reinforcement Learning](https://openreview.net/forum?id=EpVe8jAjdx)** — *ICLR 2024 · Spotlight*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** We need to look at our shoelaces as we first learn to tie them but having mastered this skill, can do it from touch alone. We call this phenomenon “sensory scaffolding”: observation streams that are not needed by a master might yet aid a novice learner.

## Generative Models and World Models

- **[WBench: A Comprehensive Multi-turn Benchmark for Interactive World Model Evaluation](https://openreview.net/forum?id=PQdqz0vaG5)** — *ICLR 2027 · Under review*
  - **Topic:** Interactive world-model evaluation
  - **Summary:** Introduces a benchmark with 289 cases and 1,058 interaction turns for evaluating video quality, instruction following, consistency, and physical plausibility in interactive world models.

- **[La-Proteina: Atomistic Protein Generation via Partially Latent Flow Matching](https://openreview.net/forum?id=RDerF20JYT)** — *ICLR 2026 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** We introduce a partially latent flow matching model for atomistic protein design.

- **[A Kinetic Energy Perspective of Flow Matching](https://openreview.net/forum?id=d6IyHrX48y)** — *ICML 2026 · Spotlight*
  - **Topic:** Generative modeling and world models
  - **Summary:** Flow-based generative models can be viewed through a physics lens: sampling transports a particle from noise to data by integrating a learned velocity field, and each sample corresponds to a trajectory with its own dynamical effort. Motivated by classical mechanics, we introduce Kinetic Path Energy (KPE), an action-like, per-sample diagnostic that measures the accumulated kinetic effort along an ordinary differential equation (ODE)...

- **[Belief-Conditioned One-Step Diffusion: Real-Time Trajectory Planning with Just-Enough Sensing](https://openreview.net/forum?id=t2asRJv2SD)** — *CoRL 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Robots equipped with rich sensor suites can localize reliably in partially-observable environments---but powering every sensor continuously is wasteful and often infeasible. Belief-space planners address this by propagating pose-belief covariance through analytic models and switching sensors heuristically--a brittle, runtime expensive approach.

- **[Cross-Sensor Touch Generation](https://openreview.net/forum?id=oGcC8nMOit)** — *CoRL 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Today's visuo-tactile sensors come in many shapes and sizes, making it challenging to develop general-purpose tactile representations. This is because most models are tied to a specific sensor design.

- **[3DTopia-XL: Scaling High-quality 3D Asset Generation via Primitive Diffusion](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_3DTopia-XL_Scaling_High-quality_3D_Asset_Generation_via_Primitive_Diffusion_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Generative modeling and world models
  - **Summary:** The increasing demand for high-quality 3D assets across various industries necessitates efficient and automated 3D content creation. Despite recent advancements in 3D generative models, existing methods still face challenges with optimization speed, geometric fidelity, and the lack of assets for physically based rendering (PBR).

- **[DiffusionDrive: Truncated Diffusion Model for End-to-End Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_DiffusionDrive_Truncated_Diffusion_Model_for_End-to-End_Autonomous_Driving_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Generative modeling and world models
  - **Summary:** Recently, the diffusion model has emerged as a powerful generative technique for robotic policy learning, capable of modeling multi-mode action distributions. Leveraging its capability for end-to-end autonomous driving is a promising direction.

- **[BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://openreview.net/forum?id=YrycTjllL0)** — *ICLR 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Task automation has been greatly empowered by the recent advances in Large Language Models (LLMs) via Python code, where the tasks range from software engineering development to general-purpose reasoning. While current benchmarks have shown that LLMs can solve tasks using programs like human developers, the majority of their evaluations are limited to short and self-contained algorithmic tasks or standalone function calls.

- **[Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think](https://openreview.net/forum?id=DJSZGGZYVi)** — *ICLR 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Recent studies have shown that the denoising process in (generative) diffusion models can induce meaningful (discriminative) representations inside the model, though the quality of these representations still lags behind those learned through recent self-supervised learning methods. We argue that one main bottleneck in training large-scale diffusion models for generation lies in effectively learning these representations.

- **[Scaling In-the-Wild Training for Diffusion-based Illumination Harmonization and Editing by Imposing Consistent Light Transport](https://openreview.net/forum?id=u1cQYxRI1H)** — *ICLR 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Diffusion-based image generators are becoming unique methods for illumination harmonization and editing. The current bottleneck in scaling up the training of diffusion-based illumination editing models is mainly in the difficulty of preserving the underlying image details and maintaining intrinsic properties, such as albedos, unchanged.

- **[Simplifying, Stabilizing and Scaling Continuous-time Consistency Models](https://openreview.net/forum?id=LyJi5ugyJx)** — *ICLR 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Consistency models (CMs) are a powerful class of diffusion-based generative models optimized for fast sampling. Most existing CMs are trained using discretized timesteps, which introduce additional hyperparameters and are prone to discretization errors.

- **[NeurIPS should lead scientific consensus on AI policy](https://openreview.net/forum?id=a4oXTW1PW2)** — *NeurIPS 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Designing wise AI policy is a grand challenge for society. To design such policy, policymakers should place a premium on rigorous evidence and scientific consensus.

- **[Real-Time Hyper-Personalized Generative AI Should Be Regulated to Prevent the Rise of "Digital Heroin"](https://openreview.net/forum?id=1IpHkK5Q8F)** — *NeurIPS 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** This position paper argues that real-time generative AI has the potential to become the next wave of addictive digital media, creating a new class of digital content akin to ``digital heroin'' with severe implications for mental health and youth development. By shortening the content-generation feedback loop to mere seconds, these advanced models will soon be able to hyper-personalize outputs on the fly.

- **[T2I-Adapter: Learning Adapters to Dig Out More Controllable Ability for Text-to-Image Diffusion Models](https://ojs.aaai.org/index.php/AAAI/article/view/28226)** — *AAAI 2024*
  - **Topic:** Generative modeling and world models
  - **Summary:** The incredible generative ability of large-scale text-to-image (T2I) models has demonstrated strong power of learning complex structures and meaningful semantics. However, relying solely on text prompts cannot fully take advantage of the knowledge learned by the model, especially when flexible and accurate controlling (e.g., structure and color) is needed.

- **[Deciphering Oracle Bone Language with Diffusion Models](https://aclanthology.org/2024.acl-long.831/)** — *ACL 2024 · Long*
  - **Topic:** Generative modeling and world models
  - **Summary:** Originating from China’s Shang Dynasty approximately 3,000 years ago, the Oracle Bone Script (OBS) is a cornerstone in the annals of linguistic history, predating many established writing systems. Despite the discovery of thousands of inscriptions, a vast expanse of OBS remains undeciphered, casting a veil of mystery over this ancient language.

- **[Adaptivity of Diffusion Models to Manifold Structures](https://proceedings.mlr.press/v238/tang24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** Empirical studies have demonstrated the effectiveness of (score-based) diffusion models in generating high-dimensional data, such as texts and images, which typically exhibit a low-dimensional manifold nature. These empirical successes raise the theoretical question of whether score-based diffusion models can optimally adapt to low-dimensional manifold structures.

- **[Generating and Imputing Tabular Data via Diffusion and Flow-based Gradient-Boosted Trees](https://proceedings.mlr.press/v238/jolicoeur-martineau24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** Tabular data is hard to acquire and is subject to missing values. This paper introduces a novel approach for generating and imputing mixed-type (continuous and categorical) tabular data utilizing score-based diffusion and conditional flow matching.

- **[Simulation-Free Schrödinger Bridges via Score and Flow Matching](https://proceedings.mlr.press/v238/tong24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** We present simulation-free score and flow matching ([SF]$^2$M), a simulation-free objective for inferring stochastic dynamics given unpaired samples drawn from arbitrary source and target distributions. Our method generalizes both the score-matching loss used in the training of diffusion models and the recently proposed flow matching loss used in the training of continuous normalizing flows. [SF]$^2$M interprets continuous-time...

- **[Theoretically Grounded Loss Functions and Algorithms for Score-Based Multi-Class Abstention](https://proceedings.mlr.press/v238/mao24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** Learning with abstention is a key scenario where the learner can abstain from making a prediction at some cost. In this paper, we analyze the score-based formulation of learning with abstention in the multi-class classification setting.

- **[Does Collaborative Human–LM Dialogue Generation Help Information Extraction from Human–Human Dialogues?](https://openreview.net/forum?id=uILyEJGKWw)** — *COLM 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** The capabilities of pretrained language models (LMs) have opened opportunities to explore new application areas, but applications involving human-human interaction are limited by the fact that most data is protected from public release for privacy reasons. Problem-solving human-human dialogues in real applications can be much more complex than existing Wizard-of-Oz collections, preventing successful domain transfer.

- **[EquiGraspFlow: SE(3)-Equivariant 6-DoF Grasp Pose Generative Flows](https://openreview.net/forum?id=5lSkn5v4LK)** — *CoRL 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** Traditional methods for synthesizing 6-DoF grasp poses from 3D observations often rely on geometric heuristics, resulting in poor generalizability, limited grasp options, and higher failure rates. Recently, data-driven methods have been proposed that use generative models to learn the distribution of grasp poses and generate diverse candidate poses.

- **[Adversarial Diffusion Distillation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/11557_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** "We introduce Adversarial Diffusion Distillation (ADD), a novel training approach that efficiently samples large-scale foundational image diffusion models in just 1–4 steps while maintaining high image quality. We use score distillation to leverage large-scale off-the-shelf image diffusion models as a teacher signal in combination with an adversarial loss to ensure high image fidelity even in the low-step regime of one or two...

- **[CoGen: Learning from Feedback with Coupled Comprehension and Generation](https://aclanthology.org/2024.emnlp-main.721/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Generative modeling and world models
  - **Summary:** Systems with both language comprehension and generation capabilities can benefit from the tight connection between the two. This work studies coupling comprehension and generation with focus on continually learning from interaction with users.

- **[Generalization in diffusion models arises from geometry-adaptive harmonic representations](https://openreview.net/forum?id=ANvmVS2Yr0)** — *ICLR 2024 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Deep neural networks (DNNs) trained for image denoising are able to generate high-quality samples with score-based reverse diffusion algorithms. These impressive capabilities seem to imply an escape from the curse of dimensionality, but recent reports of memorization of the training set raise the question of whether these networks are learning the "true" continuous density of the data.

- **[Monte Carlo guided Denoising Diffusion models for Bayesian linear inverse problems.](https://openreview.net/forum?id=nHESwXvxWK)** — *ICLR 2024 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Ill-posed linear inverse problems arise frequently in various applications, from computational photography to medical imaging. A recent line of research exploits Bayesian inference with informative priors to handle the ill-posedness of such problems.

- **[Probablistic Emulation of a Global Climate Model with Spherical DYffusion](https://openreview.net/forum?id=Ib2iHIJRTh)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Generative modeling and world models
  - **Summary:** Data-driven deep learning models are transforming global weather forecasting. It is an open question if this success can extend to climate modeling, where the complexity of the data and long inference rollouts pose significant challenges.

## Representation Learning and Clustering

- **[Reliable Correspondence Learning for Incomplete and Unaligned Multi-View Clustering](https://openreview.net/forum?id=Lkq8S9i7Qm)** — *ICLR 2027 · Under review*
  - **Topic:** Incomplete multi-view clustering
  - **Summary:** Learns reliable correspondences for incomplete, unaligned multi-view data using a shared coordinate system and local sparse transport, reducing the effect of incorrect matches on clustering.

- **[Rethinking Multi-View Clustering as Symmetric Incremental Reasoning](https://openreview.net/forum?id=5PWu6Ds1fO)** — *ICLR 2027 · Under review*
  - **Topic:** Multi-view clustering
  - **Summary:** Recasts multi-view clustering as symmetric incremental reasoning across views. Complementary view interaction, feature modulation, and semantic consistency are used to improve clustering.

- **[Uncertainty-Driven Trustworthy Multi-modal Information Bottleneck Clustering](https://openreview.net/forum?id=n9zG3wmMK9)** — *ICLR 2027 · Under review*
  - **Topic:** Uncertainty-aware multimodal clustering
  - **Summary:** Addresses uncertainty and modality conflicts in multimodal clustering by adapting information compression to uncertainty, then combining uncertainty-aware fusion with evidence-theoretic opinion aggregation.

- **[A Graph Foundation Model for Unified Clustering](https://openreview.net/forum?id=BuafzhL3jU)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Representation learning and clustering
  - **Summary:** Graph clustering is a fundamental task for understanding graph-structured data without labels, yet classical end-to-end methods require retraining on each dataset, limiting their generalization ability. Although Graph Foundation Models (GFMs) enable transferable learning across diverse graph tasks, they are not directly applicable to graph clustering.

- **[SatCLIP: Global, General-Purpose Location Embeddings with Satellite Imagery](https://ojs.aaai.org/index.php/AAAI/article/view/32457)** — *AAAI 2025*
  - **Topic:** Representation learning and clustering
  - **Summary:** Geographic information is essential for modeling tasks in fields ranging from ecology to epidemiology. However, extracting relevant location characteristics for a given task can be challenging, often requiring expensive data fusion or distillation from massive global imagery datasets.

- **[I0T: Embedding Standardization Method Towards Zero Modality Gap](https://aclanthology.org/2025.acl-long.1319/)** — *ACL 2025 · Long*
  - **Topic:** Representation learning and clustering
  - **Summary:** Contrastive Language-Image Pretraining (CLIP) enables zero-shot inference in downstream tasks such as image-text retrieval and classification. However, recent works extending CLIP suffer from the issue of *modality gap*, which arises when the image and text embeddings are projected to disparate manifolds, deviating from the intended objective of image-text contrastive learning.

- **[Position: Deep Learning is Not So Mysterious or Different](https://openreview.net/forum?id=42Au7FoD8F)** — *ICML 2025 · Spotlight*
  - **Topic:** Representation learning and clustering
  - **Summary:** Deep neural networks are often seen as different from other model classes by defying conventional notions of generalization. Popular examples of anomalous generalization behaviour include benign overfitting, double descent, and the success of overparametrization.

- **[Tree-Averaging Algorithms for Ensemble-Based Unsupervised Discontinuous Constituency Parsing](https://aclanthology.org/2024.acl-long.808/)** — *ACL 2024 · Long*
  - **Topic:** Representation learning and clustering
  - **Summary:** We address unsupervised discontinuous constituency parsing, where we observe a high variance in the performance of the only previous model in the literature. We propose to build an ensemble of different runs of the existing discontinuous parser by averaging the predicted trees, to stabilize and boost performance.

- **[Exploitation of a Latent Mechanism in Graph Contrastive Learning: Representation Scattering](https://openreview.net/forum?id=R8SolCx62K)** — *NeurIPS 2024 · Oral*
  - **Topic:** Representation learning and clustering
  - **Summary:** Graph Contrastive Learning (GCL) has emerged as a powerful approach for generating graph representations without the need for manual annotation. Most advanced GCL methods fall into three main frameworks: node discrimination, group discrimination, and bootstrapping schemes, all of which achieve comparable performance.

- **[WikiDBs: A Large-Scale Corpus Of Relational Databases From Wikidata](https://openreview.net/forum?id=abXaOcvujs)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Representation learning and clustering
  - **Summary:** Deep learning on tabular data, and particularly tabular representation learning, has recently gained growing interest. However, representation learning for relational databases with multiple tables is still an underexplored area, which may be attributed to the lack of openly available resources.

## Theory and Optimization

- **[Bridging the Gap Between Homogeneous and Heterogeneous Asynchronous Optimization Is Surprisingly Difficult](https://openreview.net/forum?id=XsOXBiKamY)** — *ICLR 2027 · Under review*
  - **Topic:** Asynchronous distributed optimization
  - **Summary:** Analyzes the gap between homogeneous and heterogeneous data in asynchronous distributed optimization. It shows that common similarity assumptions do not remove the complexity barrier in heterogeneous settings and studies improvements under interpolation conditions.

- **[Drift Is Not Enough: A Diffusive Floor for Gradient Propagation in Recurrent Networks](https://openreview.net/forum?id=X4lPQWX5Ds)** — *ICLR 2027 · Under review*
  - **Topic:** Gradient dynamics in recurrent networks
  - **Summary:** Shows that zero asymptotic drift in recurrent-network gradients does not guarantee finite-horizon stability, and characterizes diffusion-driven vanishing and exploding gradients.

- **[Optimal VC Dimension of Contrastive Learning With Margin](https://openreview.net/forum?id=cRvwvthrBO)** — *ICLR 2027 · Under review*
  - **Topic:** Generalization theory for contrastive learning
  - **Summary:** Studies the VC dimension and sample complexity of margin-based contrastive learning, deriving tighter upper and lower bounds for a previously unresolved margin setting.

- **[Characterizing the Discrete Geometry of ReLU Networks](https://openreview.net/forum?id=TgLW2DiRDG)** — *ICLR 2026 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** We describe the geometry of the polyhedral complexes defined by the linear regions of ReLU networks, both by theoretically bounding their connectivity and diameter and by empirically characterizing it using experiments on trained networks.

- **[Special Unitary Parameterized Estimators of Rotation](https://openreview.net/forum?id=VaS6xcDrTb)** — *ICLR 2026 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** Solving Wahba's problem with special unitary matrices, leading to new optimization formulations as well as representations for learning rotations in neural networks.

- **[The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm](https://openreview.net/forum?id=yRtgZ1K8hO)** — *ICLR 2026 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** We introduce a GPU-friendly algorithm for computing the polar decomposition of a matrix to low accuracy that is optimal in its class. This improves Muon.

- **[(Doubly) Exponential Lower Bounds for Follow the Regularized Leader in Potential Games](https://openreview.net/forum?id=l6KZJO7w48)** — *ICML 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** Follow the regularized leader (FTRL) is the premier algorithm for online optimization. However, despite decades of research on its convergence in constrained optimization---and potential games in particular---its behavior remained hitherto poorly understood.

- **[A Fully First-Order Layer for Differentiable Optimization](https://openreview.net/forum?id=jJur8Fq7IK)** — *ICML 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** Differentiable optimization studies how to embed a mathematical program as a differentiable layer in machine learning pipelines. However, existing approaches typically rely on implicit differentiation, involving expensive Hessian computation while differentiating through optimality conditions.

- **[(Strongly) Replicable Distribution Testers imply High Probability Distribution Testers](https://openreview.net/forum?id=eNNEiQ8BAO)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** We study connections between the sample cost of replicability, which requires an algorithm to produce consistent outputs in different runs, and the sample complexity in the high success probability regime for distribution testing algorithms. Specifically, we consider a stronger notion of replicability, which we term as strong replicability, and show that any $\rho$-strongly-replicable testing algorithm can be converted in a blackbox...

- **[A Near-optimal SQ Lower Bound for Smoothed Agnostic Learning of Boolean Halfspaces](https://openreview.net/forum?id=hf4WNJ6sRf)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** We study the complexity of smoothed agnostic learning of halfspaces on $\{\pm 1\}^n$ under uniform marginals in the model of \citet{KM25} where each input coordinate is independently flipped with probability $\sigma \in (0, {1}/{2})$. We show that $L^1$ polynomial regression achieves runtime and sample complexity $\tilde{O}(n^{O(\log(1/\varepsilon)/\sigma)})$, and prove a nearly matching Statistical Query complexity lower bound of...

- **[A Theoretical Analysis of Test-Driven Code Generation](https://openreview.net/forum?id=pnb7TQTzC2)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** Code assistants are increasingly utilized in test-driven software development, yet the theoretical mechanisms behind their environment-interaction strategies remain underexplored. We provide a probabilistic framework for two dominant paradigms: code selection after generation using the execution environment, and code generation conditioned on environment feedback.

- **[A Novel Convex Gaussian Min Max Theorem for Repeated Features](https://openreview.net/forum?id=T2FJaLgM4r)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** The Convex Gaussian Min-Max Theorem (CGMT) allows for the study of min-max optimization problems over bilinear Gaussian forms by instead considering an alternative optimization problem whose statistical properties are tied to that of the primary optimization. We prove a generalization of the CGMT to a family of problems in machine learning (ML) with correlated entries in the data matrix.

- **[A Random Matrix Theory Perspective on the Spectrum of Learned Features and Asymptotic Generalization Capabilities](https://openreview.net/forum?id=3K7rKkU7Ri)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** A key property of neural networks is their capacity of adapting to data during training. Yet, our current mathematical understanding of feature learning and its relationship to generalization remain limited.

- **[A Robust Kernel Statistical Test of Invariance: Detecting Subtle Asymmetries](https://openreview.net/forum?id=uPgGW67dSX)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** While invariances naturally arise in almost any type of real-world data, no efficient and robust test exists for detecting them in observational data under arbitrarily given group actions. We tackle this problem by studying measures of invariance that can capture even negligible underlying patterns.

- **[Additive Model Boosting: New Insights and Path(ologie)s](https://openreview.net/forum?id=p4CHBlYxYj)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** Additive models (AMs) have sparked a lot of interest in machine learning recently, allowing the incorporation of interpretable structures into a wide range of model classes. Many commonly used approaches to fit a wide variety of potentially complex additive models build on the idea of boosting additive models.

- **[Causal discovery in mixed additive noise models](https://openreview.net/forum?id=1YNxc4j8sd)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** Uncovering causal relationships in datasets that include both categorical and continuous variables is a challenging problem. The overwhelming majority of existing methods restrict their application to dealing with a single type of variable.

- **[Cubic regularized subspace Newton for non-convex optimization](https://openreview.net/forum?id=FI1Q9Bi4rH)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** This paper addresses the optimization problem of minimizing non-convex continuous functions, a problem highly relevant in high-dimensional machine learning scenarios, particularly those involving over-parameterization. We analyze a randomized coordinate second-order method named SSCN, which can be interpreted as applying the cubic regularization of Newton's method in random subspaces.

- **[LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://openreview.net/forum?id=VpWki1v2P8)** — *ICLR 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** Low-rank adaption (LoRA) is a widely used parameter-efficient finetuning method for LLM that reduces memory requirements. However, current LoRA optimizers lack transformation invariance, meaning the updates depending on how the two LoRA factors are scaled or rotated.

- **[Position: Algebra Unveils Deep Learning - An Invitation to Neuroalgebraic Geometry](https://openreview.net/forum?id=mzc1KPkIMJ)** — *ICML 2025 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** In this position paper, we promote the study of function spaces parameterized by machine learning models through the lens of algebraic geometry. To this end, we focus on algebraic models, such as neural networks with polynomial activations, whose associated function spaces are semi-algebraic varieties.

- **[Position: Constants are Critical in Regret Bounds for Reinforcement Learning](https://openreview.net/forum?id=3wEY0NB2pG)** — *ICML 2025 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** Mainstream research in theoretical RL is currently focused on designing online learning algorithms with regret bounds that match the corresponding regret lower bound up to multiplicative constants (and, sometimes, logarithmic terms). In this position paper, we constructively question this trend, arguing that algorithms should be designed to at least minimize the amount of unnecessary exploration, and we highlight the significant...

- **[Rigor in AI: Doing Rigorous AI Work Requires a Broader, Responsible AI-Informed Conception of Rigor](https://openreview.net/forum?id=USqNoPVhxx)** — *NeurIPS 2025 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** In AI research and practice, rigor remains largely understood in terms of methodological rigor---such as whether mathematical, statistical, or computational methods are correctly applied. We argue that this narrow conception of rigor has contributed to the concerns raised by the responsible AI community, including overblown claims about the capabilities of AI systems.

- **[COKE: A Cognitive Knowledge Graph for Machine Theory of Mind](https://aclanthology.org/2024.acl-long.848/)** — *ACL 2024 · Long*
  - **Topic:** Learning theory and optimization
  - **Summary:** Theory of mind (ToM) refers to humans’ ability to understand and infer the desires, beliefs, and intentions of others. The acquisition of ToM plays a key role in humans’ social cognition and interpersonal relations.

- **[A General Theoretical Paradigm to Understand Learning from Human Preferences](https://proceedings.mlr.press/v238/gheshlaghi-azar24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** The prevalent deployment of learning from human preferences through reinforcement learning (RLHF) relies on two important approximations: the first assumes that pairwise preferences can be substituted with pointwise rewards. The second assumes that a reward model trained on these pointwise rewards can generalize from collected data to out-of-distribution data sampled by the policy.

- **[Identifying Spurious Biases Early in Training through the Lens of Simplicity Bias](https://proceedings.mlr.press/v238/yang24c.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** Neural networks trained with (stochastic) gradient descent have an inductive bias towards learning simpler solutions. This makes them highly prone to learning spurious correlations in the training data, that may not hold at test time.

- **[A Survey on Deep Learning for Theorem Proving](https://openreview.net/forum?id=zlw6AHwukB)** — *COLM 2024 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** Theorem proving is a fundamental aspect of mathematics, spanning from informal reasoning in natural language to rigorous derivations in formal systems. In recent years, the advancement of deep learning, especially the emergence of large language models, has sparked a notable surge of research exploring these techniques to enhance the process of theorem proving.

- **[DEM: Distribution Edited Model for Training with Mixed Data Distributions](https://aclanthology.org/2024.emnlp-main.1074/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Learning theory and optimization
  - **Summary:** Training with mixed data distributions is a common and important part of creating multi-task and instruction-following models. The diversity of the data distributions and cost of joint training makes the optimization procedure extremely challenging.

## Trustworthy AI and Safety

- **[Allocation-Dependent Distortion for Fair Clustering Ensembles](https://openreview.net/forum?id=V84yBc0EgP)** — *ICLR 2027 · Under review*
  - **Topic:** Fair clustering
  - **Summary:** Studies how fair clustering ensembles should account for the allocation of protected groups across clusters. It introduces an allocation-dependent distortion objective and analyzes its relationship to group disparities.

- **[Training Honesty Adapters To Detect Deception In LLMs](https://openreview.net/forum?id=gpt1K3Ia4D)** — *ICLR 2027 · Under review*
  - **Topic:** Deception detection in language models
  - **Summary:** Trains LoRA honesty adapters on on-policy dialogue to detect deception, reporting improved detection of unseen models over several probing baselines.

- **[A Dirac-Frenkel-Onsager Principle: Instantaneous Residual Minimization with Gauge Momentum for Nonlinear Parametrizations of PDE Solutions](https://openreview.net/forum?id=aDPbUSUCwh)** — *ICML 2026 · Spotlight*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Dirac-Frenkel instantaneous residual minimization evolves nonlinear parametrizations of PDE solutions in time, but ill-conditioning can render the parameter dynamics non-unique. We interpret this non-uniqueness as a gauge freedom: nullspace directions that leave the time derivative unchanged can be used to select better-conditioned parameter velocities.

- **[A Factorized Low-Rank RNN Framework for Uncovering Independent Neural Latent Dynamics and Connectivity](https://openreview.net/forum?id=QvIbmX9jBr)** — *ICML 2026 · Spotlight*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Low-rank recurrent neural networks (lrRNNs) are a class of models that uncover low-dimensional latent dynamics underlying neural population activity. Although their functional connectivity is low-rank, it lacks independence interpretations, making it difficult to assign distinct computational roles to different latent dimensions.

- **[A Noise Sensitivity Exponent Controls Large Statistical-to-Computational Gaps in Single- and Multi-Index Models](https://openreview.net/forum?id=KHhO311xZ2)** — *ICML 2026 · Spotlight*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Understanding when learning is statistically possible yet computationally hard is a central challenge in high-dimensional statistics. In this work, we investigate this question in the context of single- and multi-index models, classes of functions widely studied as benchmarks to probe the ability of machine learning methods to discover features in high-dimensional data.

- **[Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities for Downstream Task Scaling Law](https://aclanthology.org/2025.acl-long.1157/)** — *ACL 2025 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Scaling law builds the relationship between training computation and validation loss, enabling researchers to effectively predict the loss trending of models across different levels of computation. However, a gap still remains between validation loss and the model’s downstream capabilities, making it untrivial to apply scaling law to direct performance prediction for downstream tasks.

- **[Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs](https://aclanthology.org/2025.acl-long.341/)** — *ACL 2025 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Algorithmic fairness has conventionally adopted the mathematically convenient perspective of racial color-blindness (i.e., difference unaware treatment). However, we contend that in a range of important settings, group difference awareness matters.

- **[LaTIM: Measuring Latent Token-to-Token Interactions in Mamba Models](https://aclanthology.org/2025.acl-long.1194/)** — *ACL 2025 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** State space models (SSMs), such as Mamba, have emerged as an efficient alternative to transformers for long-context sequence modeling. However, despite their growing adoption, SSMs lack the interpretability tools that have been crucial for understanding and improving attention-based architectures.

- **[Balls-and-Bins Sampling for DP-SGD](https://openreview.net/forum?id=RwJTeddgRD)** — *AISTATS 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** We introduce the _Balls-and-Bins_ sampling for differentially private (DP) optimization methods such as DP-SGD. While it has been common practice to use some form of shuffling in DP-SGD implementations, privacy accounting algorithms have typically assumed that Poisson subsampling is used instead.

- **[Divide, Discover, Deploy: Factorized Skill Learning with Symmetry and Style Priors](https://openreview.net/forum?id=Ddb8w8FVV9)** — *CoRL 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Unsupervised Skill Discovery (USD) allows agents to autonomously learn diverse behaviors without task-specific rewards. While recent USD methods have shown promise, their application to real-world robotics remains underexplored.

- **[Artificial Kuramoto Oscillatory Neurons](https://openreview.net/forum?id=nwDRD4AMoN)** — *ICLR 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** It has long been known in both neuroscience and AI that ``binding'' between neurons leads to a form of competitive learning where representations are compressed in order to represent more abstract concepts in deeper layers of the network. More recently, it was also hypothesized that dynamic (spatiotemporal) representations play an important role in both neuroscience and AI.

- **[Safety Alignment Should be Made More Than Just a Few Tokens Deep](https://openreview.net/forum?id=6Mxhg9PtDE)** — *ICLR 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** The safety alignment of current Large Language Models (LLMs) is vulnerable. Simple attacks, or even benign fine-tuning, can jailbreak aligned models.

- **[Position: AI Safety should prioritize the Future of Work](https://openreview.net/forum?id=CA9NxmmUG5)** — *ICML 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Current efforts in AI safety prioritize filtering harmful content, preventing manipulation of human behavior, and eliminating existential risks in cybersecurity or biosecurity. While pressing, this narrow focus overlooks critical human-centric considerations that shape the long-term trajectory of a society.

- **[Position: Generative AI Regulation Can Learn from Social Media Regulation](https://openreview.net/forum?id=fRk0nKLKrJ)** — *ICML 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** There is strong agreement that generative AI should be regulated, but strong disagreement on how to approach regulation. While some argue that AI regulation should mostly rely on extensions of existing laws, others argue that entirely new laws and regulations are needed to ensure that generative AI benefits society.

- **[Machine Unlearning Doesn't Do What You Think: Lessons for Generative AI Policy and Research](https://openreview.net/forum?id=mfd6GRW4Az)** — *NeurIPS 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** "Machine unlearning" is a popular proposed solution for mitigating the existence of content in an AI model that is problematic for legal or moral reasons, including privacy, copyright, safety, and more. For example, unlearning is often invoked as a solution for removing the effects of specific information from a generative-AI model's parameters, e.g., a particular individual's personal data or the inclusion of copyrighted content in...

- **[More effort is needed to protect pedestrian privacy in the era of AI](https://openreview.net/forum?id=rdeCalg68L)** — *NeurIPS 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** In the era of artificial intelligence (AI), pedestrian privacy is increasingly at risk. In research areas such as autonomous driving, computer vision, and surveillance, large datasets are often collected in public spaces, capturing pedestrians without consent or anonymization.

- **[Position: Bridge the Gaps between Machine Unlearning and AI Regulation](https://openreview.net/forum?id=0ngi2StMwC)** — *NeurIPS 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** The "right to be forgotten" and the data privacy laws that encode it have motivated machine unlearning since its earliest days. Now, some argue that an inbound wave of artificial intelligence regulations — like the European Union's Artificial Intelligence Act (AIA) — may offer important new use cases for machine unlearning.

- **[Position: Towards Bidirectional Human-AI Alignment](https://openreview.net/forum?id=PgA9rZoMY8)** — *NeurIPS 2025 · Poster*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Recent advances in general-purpose AI underscore the urgent need to align AI systems with human goals and values. Yet, the lack of a clear, shared understanding of what constitutes "alignment" limits meaningful progress and cross-disciplinary collaboration.

- **[Preference Ranking Optimization for Human Alignment](https://ojs.aaai.org/index.php/AAAI/article/view/29865)** — *AAAI 2024*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Large language models (LLMs) often contain misleading content, emphasizing the need to align them with human values to ensure secure AI systems. Reinforcement learning from human feedback (RLHF) has been employed to achieve this alignment.

- **[CausalGym: Benchmarking causal interpretability methods on linguistic tasks](https://aclanthology.org/2024.acl-long.785/)** — *ACL 2024 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Language models (LMs) have proven to be powerful tools for psycholinguistic research, but most prior work has focused on purely behavioural measures (e.g., surprisal comparisons). At the same time, research in model interpretability has begun to illuminate the abstract causal mechanisms shaping LM behavior.

- **[Emulated Disalignment: Safety Alignment for Large Language Models May Backfire!](https://aclanthology.org/2024.acl-long.842/)** — *ACL 2024 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Large language models (LLMs) undergo safety alignment to ensure safe conversations with humans. However, this paper introduces a training-free attack method capable of reversing safety alignment, converting the outcomes of stronger alignment into greater potential for harm by accessing only LLM output token distributions.

- **[PsySafe: A Comprehensive Framework for Psychological-based Attack, Defense, and Evaluation of Multi-agent System Safety](https://aclanthology.org/2024.acl-long.812/)** — *ACL 2024 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Multi-agent systems, when enhanced with Large Language Models (LLMs), exhibit profound capabilities in collective intelligence. However, the potential misuse of this intelligence for malicious purposes presents significant risks.

- **[Meta Continual Learning Revisited: Implicitly Enhancing Online Hessian Approximation via Variance Reduction](https://openreview.net/forum?id=TpD2aG1h0D)** — *ICLR 2024 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Regularization-based methods have so far been among the *de facto* choices for continual learning. Recent theoretical studies have revealed that these methods all boil down to relying on the Hessian matrix approximation of model weights.

- **[Continual Learning with Pre-Trained Models: A Survey](https://www.ijcai.org/proceedings/2024/924)** — *IJCAI 2024 · Poster*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Nowadays, real-world applications often face streaming data, which requires the learning system to absorb new knowledge as data evolves. Continual Learning (CL) aims to achieve this goal and meanwhile overcome the catastrophic forgetting of former knowledge when learning new ones.

- **[The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models](https://openreview.net/forum?id=DFr5hteojx)** — *NeurIPS 2024 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Human feedback is central to the alignment of Large Language Models (LLMs). However, open questions remain about the methods (how), domains (where), people (who) and objectives (to what end) of feedback processes.

## AI Systems and Efficiency

- **[Feedback-driven recurrent quantum neural network universality](https://openreview.net/forum?id=248ysaRatx)** — *ICLR 2026 · Poster*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** The paper proves quantitative universal approximation results for learning state-space systems using recurrent quantum neural networks.

- **[Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126/)** — *ACL 2025 · Long*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** Long-context modeling is crucial for next-generation language models, yet the high computational cost of standard attention mechanisms poses significant computational challenges. Sparse attention offers a promising direction for improving efficiency while maintaining model capabilities.

- **[Certifiably Quantisation-Robust training and inference of Neural Networks](https://openreview.net/forum?id=qtppWP3gXl)** — *AISTATS 2025 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** We tackle the problem of computing guarantees for the robustness of neural networks against quantisation of their inputs, parameters and activation values. In particular, we pose the problem of bounding the worst-case discrepancy between the original neural network and all possible quantised ones parametrised by a given maximum quantisation diameter $\epsilon > 0$ over a finite dataset.

- **[Entropic Matching for Expectation Propagation of Markov Jump Processes](https://openreview.net/forum?id=23yqeRmadg)** — *AISTATS 2025 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** We propose a novel, tractable latent state inference scheme for Markov jump processes, for which exact inference is often intractable. Our approach is based on an entropic matching framework that can be embedded into the well-known expectation propagation algorithm.

- **[PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling](https://openreview.net/forum?id=ayi7qezU87)** — *COLM 2025 · Poster*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** In this study, we investigate whether attention-based information flow inside large language models (LLMs) is aggregated through noticeable patterns for long context processing. Our observations reveal that LLMs aggregate information through Pyramidal Information Funneling where attention is scattering widely in lower layers, progressively consolidating within specific contexts, and ultimately focusing on critical tokens (a.k.a...

- **[Timestep Embedding Tells: It's Time to Cache for Video Diffusion Model](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Timestep_Embedding_Tells_Its_Time_to_Cache_for_Video_Diffusion_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** As a fundamental backbone for video generation, diffusion models are challenged by low inference speed due to the sequential nature of denoising.Previous methods speed up the models by caching and reusing model outputs at uniformly selected timesteps.However, such a strategy neglects the fact that differences among model outputs are not uniform across timesteps, which hinders selecting the appropriate model outputs to cache, leading...

- **[Position: Humanity Faces Existential Risk from Gradual Disempowerment](https://openreview.net/forum?id=mWlnrtOTtm)** — *ICML 2025 · Poster*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** This paper examines the systemic risks posed by incremental advancements in artificial intelligence, developing the concept of `gradual disempowerment', in contrast to the abrupt takeover scenarios commonly discussed in AI safety. We analyze how even incremental improvements in AI capabilities can undermine human influence over large-scale systems that society depends on, including the economy, culture, and nation-states.

- **[Military AI Needs Technically-Informed Regulation to Safeguard AI Research and its Applications](https://openreview.net/forum?id=gXTFLbGUQp)** — *NeurIPS 2025 · Poster*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** Military weapon systems and command-and-control infrastructure augmented by artificial intelligence (AI) have seen rapid development and deployment in recent years. However, the sociotechnical impacts of AI on combat systems, military decision-making, and the norms of warfare have been understudied.

- **[Position: If Innovation in AI systematically Violates Fundamental Rights, Is It Innovation at All?](https://openreview.net/forum?id=PFRandBfSz)** — *NeurIPS 2025 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** Artificial intelligence (AI) now permeates critical infrastructures and decisionmaking systems where failures produce social, economic, and democratic harm. This position paper challenges the entrenched belief that regulation and innovation are opposites.

- **[MobileNetV4: Universal Models for the Mobile Ecosystem](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5647_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** "We present the latest generation of MobileNets: MobileNetV4 (MNv4). They feature universally-efficient architecture designs for mobile devices.

- **[Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs](https://openreview.net/forum?id=uNrFpDPMyo)** — *ICLR 2024 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** In this study, we introduce adaptive KV cache compression, a plug-and-play method that reduces the memory footprint of generative inference for Large Language Models (LLMs). Different from the conventional KV cache that retains key and value vectors for all context tokens, we conduct targeted profiling to discern the intrinsic structure of attention modules.

- **[Convolutional Differentiable Logic Gate Networks](https://openreview.net/forum?id=4bKEFyUHT4)** — *NeurIPS 2024 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** With the increasing inference cost of machine learning models, there is a growing interest in models with fast and efficient inference. Recently, an approach for learning logic gate networks directly via a differentiable relaxation was proposed.

## Datasets and Evaluation

- **[BIRD-INTERACT: Re-imagining Text-to-SQL Evaluation via Lens of Dynamic Interactions](https://openreview.net/forum?id=nHrYBGujps)** — *ICLR 2026 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Large language models (LLMs) have demonstrated remarkable performance on single-turn text-to-SQL tasks, but real-world database applications predominantly require multi-turn interactions to handle ambiguous queries, execution errors, and evolving user requirements. Existing multi-turn benchmarks fall short of capturing this complexity, either by treating conversation histories as static context or by limiting evaluation to narrow,...

- **[AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset](https://aclanthology.org/2025.acl-long.96/)** — *ACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Recent advancements in large language model (LLM) performance on medical multiplechoice question (MCQ) benchmarks have stimulated interest from healthcare providers and patients globally. Particularly in low-andmiddle-income countries (LMICs) facing acute physician shortages and lack of specialists, LLMs offer a potentially scalable pathway to enhance healthcare access and reduce costs.

- **[Beyond N-Grams: Rethinking Evaluation Metrics and Strategies for Multilingual Abstractive Summarization](https://aclanthology.org/2025.acl-long.932/)** — *ACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Automatic N-gram based metrics such as ROUGE are widely used for evaluating generative tasks such as summarization. While these metrics are considered indicative (even if imperfect), of human evaluation for English, their suitability for other languages remains unclear.

- **[BRIGHTER: BRIdging the Gap in Human-Annotated Textual Emotion Recognition Datasets for 28 Languages](https://aclanthology.org/2025.acl-long.436/)** — *ACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** People worldwide use language in subtle and complex ways to express emotions. Although emotion recognition–an umbrella term for several NLP tasks–impacts various applications within NLP and beyond, most work in this area has focused on high-resource languages.

- **[From Real to Synthetic: Synthesizing Millions of Diversified and Complicated User Instructions with Attributed Grounding](https://aclanthology.org/2025.acl-long.517/)** — *ACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** The pursuit of diverse, complex, and large-scale instruction data is crucial for automatically aligning large language models (LLMs). While there are methods capable of generating synthetic instructions at scale, they either suffer from limited grounding sources, leading to a narrow distribution, or rely on trivial extensions that fail to produce meaningful trajectories in terms of complexity.

- **[PARME: Parallel Corpora for Low-Resourced Middle Eastern Languages](https://aclanthology.org/2025.acl-long.1451/)** — *ACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** The Middle East is characterized by remarkable linguistic diversity, with over 400 million inhabitants speaking more than 60 languages across multiple language families. This study presents a pioneering work in developing the first parallel corpora for eight severely under-resourced varieties in the region–PARME, addressing fundamental challenges in low-resource scenarios including non-standardized writing and dialectal complexity.

- **[Déjà Vu: Multilingual LLM Evaluation through the Lens of Machine Translation Evaluation](https://openreview.net/forum?id=yxzVanFoij)** — *COLM 2025 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Generation capabilities and language coverage of multilingual large language models (mLLMs) are advancing rapidly. However, evaluation practices for generative abilities of mLLMs are still lacking comprehensiveness, scientific rigor, and consistent adoption across research labs, which undermines their potential to meaningfully guide mLLM development.

- **[The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains](https://openreview.net/forum?id=9rwtezthwo)** — *COLM 2025 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Improvements in language models are often driven by increasing the quality of the data we train them on, which can be limiting when strong supervision is not readily available. In this work, we show that paired preference data consisting of individually weak data points can enable gains beyond the strength of each individual sample.

- **[Data Retrieval with Importance Weights for Few-Shot Imitation Learning](https://openreview.net/forum?id=wnWYoetLhC)** — *CoRL 2025 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** While large-scale robot datasets have propelled recent progress in imitation learning, learning from smaller task specific datasets remains critical for deployment in new environments and unseen tasks. One such approach to few-shot imitation learning is retrieval-based imitation learning, which extracts relevant samples from large, widely available prior datasets to augment a limited demonstration dataset.

- **[Position: AI Competitions Provide the Gold Standard for Empirical Rigor in GenAI Evaluation](https://openreview.net/forum?id=Rxd2TpV6Eg)** — *ICML 2025 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** In this position paper, we observe that empirical evaluation in Generative AI is at a crisis point since traditional ML evaluation and benchmarking strategies are insufficient to meet the needs of evaluating modern GenAI models and systems. There are many reasons for this, including the fact that these models typically have nearly unbounded input and output spaces, typically do not have a well defined ground truth target, and...

- **[Position: Human Baselines in Model Evaluations Need Rigor and Transparency (With Recommendations & Reporting Checklist)](https://openreview.net/forum?id=gwhPvu97Gm)** — *ICML 2025 · Spotlight*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** **In this position paper, we argue that human baselines in foundation model evaluations must be more rigorous and more transparent to enable meaningful comparisons of human vs. AI performance, and we provide recommendations and a reporting checklist towards this end.** Human performance baselines are vital for the machine learning community, downstream users, and policymakers to interpret AI evaluations.

- **[In-Context Learning with Long-Context Models: An In-Depth Exploration](https://aclanthology.org/2025.naacl-long.605/)** — *NAACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** As model context lengths continue to increase, the number of demonstrations that can be provided in-context approaches the size of entire training datasets. We study the behavior of in-context learning (ICL) at this extreme scale on multiple datasets and models.

- **[RewardBench: Evaluating Reward Models for Language Modeling](https://aclanthology.org/2025.findings-naacl.96/)** — *NAACL 2025 · Findings*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Reward models (RMs) are at the crux of successfully using RLHF to align pretrained models to human preferences, yet there has been relatively little study that focuses on evaluation of those models. Evaluating reward models presents an opportunity to understand the opaque technologies used for alignment of language models and which values are embedded in them.

- **[Fostering the Ecosystem of AI for Social Impact Requires Expanding and Strengthening Evaluation Standards](https://openreview.net/forum?id=dl5pvd5IgW)** — *NeurIPS 2025 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** There has been increasing research interest in AI/ML for social impact, and correspondingly more publication venues refining review criteria for practice-driven AI/ML research. However, these review guidelines tend to most concretely recognize projects that simultaneously achieve deployment and novel ML methodological innovation.

- **[Measuring Fingerprints of Web-filtered Text Datasets and Fingerprint Propagation Through Training](https://openreview.net/forum?id=iKwHwCaddB)** — *NeurIPS 2025 · Spotlight*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** We investigate fingerprints in pretraining datasets for large language models (LLMs) through dataset classification experiments. Building on prior work demonstrating the existence of fingerprints or biases in popular computer vision datasets, we analyze popular open-source pretraining datasets for LLMs derived from CommonCrawl including C4, RefinedWeb, DolmaCC, RedPajama-V2, FineWeb, and DCLM-Baseline.

- **[COSMIC: Mutual Information for Task-Agnostic Summarization Evaluation](https://aclanthology.org/2024.acl-long.686/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Assessing the quality of summarizers poses significant challenges—gold summaries are hard to obtain and their suitability depends on the use context of the summarization system. Who is the user of the system, and what do they intend to do with the summary?

- **[Distributional Inclusion Hypothesis and Quantifications: Probing for Hypernymy in Functional Distributional Semantics](https://aclanthology.org/2024.acl-long.784/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Functional Distributional Semantics (FDS) models the meaning of words by truth-conditional functions. This provides a natural representation for hypernymy but no guarantee that it can be learnt when FDS models are trained on a corpus.

- **[Estimating the Level of Dialectness Predicts Inter-annotator Agreement in Multi-dialect Arabic Datasets](https://aclanthology.org/2024.acl-short.70/)** — *ACL 2024 · Short*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** On annotating multi-dialect Arabic datasets, it is common to randomly assign the samples across a pool of native Arabic speakers. Recent analyses recommended routing dialectal samples to native speakers of their respective dialects to build higher-quality datasets.

- **[Latxa: An Open Language Model and Evaluation Suite for Basque](https://aclanthology.org/2024.acl-long.799/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** We introduce Latxa, a family of large language models for Basque ranging from 7 to 70 billion parameters. Latxa is based on Llama 2, which we continue pretraining on a new Basque corpus comprising 4.3M documents and 4.2B tokens.

- **[M4LE: A Multi-Ability Multi-Range Multi-Task Multi-Domain Long-Context Evaluation Benchmark for Large Language Models](https://aclanthology.org/2024.acl-long.832/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Managing long sequences has become an important and necessary feature for large language models (LLMs). However, assessing their ability to handle long contexts remains a challenge.

- **[MultiLegalPile: A 689GB Multilingual Legal Corpus](https://aclanthology.org/2024.acl-long.805/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Large, high-quality datasets are crucial for training Large Language Models (LLMs). However, so far, few datasets are available for specialized critical domains such as law and the available ones are often small and only in English.

- **[On Efficient and Statistical Quality Estimation for Data Annotation](https://aclanthology.org/2024.acl-long.837/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Annotated datasets are an essential ingredient to train, evaluate, compare and productionalize supervised machine learning models. It is therefore imperative that annotations are of high quality.

- **[SPZ: A Semantic Perturbation-based Data Augmentation Method with Zonal-Mixing for Alzheimer’s Disease Detection](https://aclanthology.org/2024.acl-long.823/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Alzheimer’s Disease (AD), characterized by significant cognitive and functional impairment, necessitates the development of early detection techniques. Traditional diagnostic practices, such as cognitive assessments and biomarker analysis, are often invasive and costly.

- **[GeniL: A Multilingual Dataset on Generalizing Language](https://openreview.net/forum?id=kLH4ccaL21)** — *COLM 2024 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Generative language models are increasingly transforming our digital ecosystem, but they often inherit societal biases learned from their training data, for instance stereotypes associating certain attributes with specific identity groups. While whether and how these biases are mitigated may depend on the specific use cases, being able to effectively detect instances of stereotype perpetuation is a crucial first step.

- **[GPQA: A Graduate-Level Google-Proof Q&A Benchmark](https://openreview.net/forum?id=Ti67584b98)** — *COLM 2024 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** We present GPQA, a challenging dataset of 448 multiple-choice questions written by domain experts in biology, physics, and chemistry. We ensure that the questions are high-quality and extremely difficult: experts who have or are pursuing PhDs in the corresponding domains reach 65\% accuracy (74\% when discounting clear mistakes the experts identified in retrospect), while highly skilled non-expert validators only reach 34\%...

- **[Top Leaderboard Ranking = Top Coding Proficiency, Always? EvoEval: Evolving Coding Benchmarks via LLM](https://openreview.net/forum?id=zZa7Ke7WAJ)** — *COLM 2024 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Large language models (LLMs) have become the go-to choice for code generation tasks, with an exponential increase in the training, development, and usage of LLMs specifically for code generation. To evaluate the ability of LLMs on code, both academic and industry practitioners rely on popular handcrafted benchmarks.

- **[What the Harm? Quantifying the Tangible Impact of Gender Bias in Machine Translation with a Human-centered Study](https://aclanthology.org/2024.emnlp-main.1002/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Gender bias in machine translation (MT) is recognized as an issue that can harm people and society. And yet, advancements in the field rarely involve people, the final MT users, or inform how they might be impacted by biased technologies.

- **[AGIEval: A Human-Centric Benchmark for Evaluating Foundation Models](https://aclanthology.org/2024.findings-naacl.149/)** — *NAACL 2024 · Findings*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Assessing foundation models’ abilities for human-level tasks is crucial for Artificial General Intelligence (AGI) development.Traditional benchmarks, which rely on artificial datasets, may not accurately represent these capabilities. In this paper, we introduce AGIEval, a novel bilingual benchmark designed to assess foundation models in the context of human-centric standardized exams, such as college entrance exams, law school...

- **[Effective Long-Context Scaling of Foundation Models](https://aclanthology.org/2024.naacl-long.260/)** — *NAACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** We present an effective recipe to train strong long-context LLMs that are capable of utilizing massive context windows of up to 32,000 tokens. Our models are built through continual pretraining from Llama 2 checkpoints with longer text sequences and on a dataset where long texts are upsampled.

- **[GPTScore: Evaluate as You Desire](https://aclanthology.org/2024.naacl-long.365/)** — *NAACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Generative Artificial Intelligence (AI) has enabled the development of sophisticated models that are capable of producing high-caliber text, images, and other outputs through the utilization of large pre-trained models.Nevertheless, assessing the quality of the generation is an even more arduous task than the generation itself, and this issue has not been given adequate consideration recently.This paper proposes a novel evaluation...

- **[ChaosBench: A Multi-Channel, Physics-Based Benchmark for Subseasonal-to-Seasonal Climate Prediction](https://openreview.net/forum?id=s1K5Z5QPog)** — *NeurIPS 2024 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Accurate prediction of climate in the subseasonal-to-seasonal scale is crucial for disaster preparedness and robust decision making amidst climate change. Yet, forecasting beyond the weather timescale is challenging because it deals with problems other than initial condition, including boundary interaction, butterfly effect, and our inherent lack of physical understanding.

## Graph Learning

- **[Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness](https://openreview.net/forum?id=HSKaGOi7Ar)** — *ICLR 2024 · Oral*
  - **Topic:** Graph learning and network analysis
  - **Summary:** Designing expressive Graph Neural Networks (GNNs) is a fundamental topic in the graph learning community. So far, GNN expressiveness has been primarily assessed via the Weisfeiler-Lehman (WL) hierarchy.

## Other AI Research

- **[Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models: Characterization and Learning](https://openreview.net/forum?id=b8TlYh6PN6)** — *ICLR 2026 · Oral*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Causal discovery with latent variables is a fundamental task. Yet most existing methods rely on strong structural assumptions, such as enforcing specific indicator patterns for latents or restricting how they can interact with others.

- **[Probabilistic Kernel Function for Fast Angle Testing](https://openreview.net/forum?id=nCsF3Bsn2n)** — *ICLR 2026 · Oral*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** We propose two probabilistic kernel functions for angle testing, which can be used to accelerate vector-based similarity search.

- **[A Bitter Lesson for Data Filtering](https://openreview.net/forum?id=1bGfOCtPWO)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** We investigate data filtering for large model pretraining via new scaling studies that target the high compute, data-scarce regime. In spite of an apparently common belief that filtering data to include only high-quality information is essential, our experiments suggest that with enough compute, the best data filter is no data filter.

- **[Typology-Guided Adaptation in Multilingual Models](https://aclanthology.org/2025.acl-long.1059/)** — *ACL 2025 · Long*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Multilingual models often treat language diversity as a problem of data imbalance, overlooking structural variation. We introduce the *Morphological Index* (MoI), a typologically grounded metric that quantifies how strongly a language relies on surface morphology for noun classification.

- **[Almost linear time differentially private release of synthetic graphs](https://openreview.net/forum?id=UWNfWtCXCZ)** — *AISTATS 2025 · Oral*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** In this paper, we give an almost linear time and space algorithms to sample from an exponential mechanism with an $\ell_1$-score function defined over an exponentially large non-convex set. As a direct result, on input an $n$ vertex $m$ edges graph $G$, we present the first $\widetilde{O}(m)$ time and $O(m)$ space algorithms for differentially privately outputting an $n$ vertex $O(m)$ edges synthetic graph that approximates all the...

- **[Position: The Categorization of Race in ML is a Flawed Premise](https://openreview.net/forum?id=eI8KegpPyX)** — *ICML 2025 · Spotlight*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** This position paper critiques the reliance on rigid racial taxonomies in machine learning, exposing their U.S.-centric nature and lack of global applicability—particularly in Europe, where race categories are not commonly used. These classifications oversimplify racial identity, erasing the experiences of mixed-race individuals and reinforcing outdated essentialist views that contradict the social construction of race.

- **[Position: Machine Learning Conferences Should Establish a "Refutations and Critiques" Track](https://openreview.net/forum?id=DS1XSAPvKs)** — *NeurIPS 2025 · Oral*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Science progresses by iteratively advancing and correcting humanity's understanding of the world. In machine learning (ML) research, rapid advancements have led to an explosion of publications, but have also led to misleading, incorrect, flawed or perhaps even fraudulent studies being accepted and sometimes highlighted at ML conferences due to the fallibility of peer review.

- **[Prohibiting Generative AI in any Form of Weapon Control](https://openreview.net/forum?id=uEY7kQsiZz)** — *NeurIPS 2025 · Poster*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** This position paper argues that the use of generative artificial intelligence (GenAI) to control, direct, guide or govern any weapon, either in situ or remotely, should be prohibited by government agencies and non-governmental organizations. Such a moratorium should exist until hallucinations can be successfully modeled and predicted.

- **[We Should Chart an Atlas of All the World's Models](https://openreview.net/forum?id=BzFMBNqg7R)** — *NeurIPS 2025 · Poster*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Public model repositories now contain millions of models, yet most remain undocumented and effectively lost: their capabilities, provenance, and constraints cannot be reliably determined. As a result, the field wastes training time and compute, propagates hidden biases, faces intellectual-property risks, and misses opportunities for model reuse and transfer.

- **[NounAtlas: Filling the Gap in Nominal Semantic Role Labeling](https://aclanthology.org/2024.acl-long.857/)** — *ACL 2024 · Long*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Despite significant advances in Semantic Role Labeling (SRL), much work in this field has been carried out with a focus on verbal predicates, with the research on nominal SRL lagging behind. In many contexts, however, nominal predicates are often as informative as verbal ones, thus needing proper treatment.

- **[Semisupervised Neural Proto-Language Reconstruction](https://aclanthology.org/2024.acl-long.788/)** — *ACL 2024 · Long*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Existing work implementing comparative reconstruction of ancestral languages (proto-languages) has usually required full supervision. However, historical reconstruction models are only of practical value if they can be trained with a limited amount of labeled data.

- **[Spectrally Transformed Kernel Regression](https://openreview.net/forum?id=OeQE9zsztS)** — *ICLR 2024 · Spotlight*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Unlabeled data is a key component of modern machine learning. In general, the role of unlabeled data is to impose a form of smoothness, usually from the similarity information encoded in a base kernel, such as the ϵ-neighbor kernel or the adjacency matrix of a graph.

- **[Knowledge Distillation in Federated Learning: A Practical Guide](https://www.ijcai.org/proceedings/2024/905)** — *IJCAI 2024 · Poster*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Federated Learning (FL) enables the training of Deep Learning models without centrally collecting possibly sensitive raw data. The most used algorithms for FL are parameter-averaging based schemes (e.g., Federated Averaging) that, however, have well known limits, i.e., model homogeneity, high communication cost, poor performance in presence of heterogeneous data distributions.

## Sources and updates

- Data sources, selection rules, known gaps, and direct-source maintenance notes: [SOURCES.md](SOURCES.md).
- The scheduled GitHub Actions workflow refreshes source records and regenerates this README daily. Review-score changes are stored with observation time and review phase so the internal ranking follows rebuttal updates.
