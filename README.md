# AI Research Papers by Topic

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

- **[Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models: Characterization and Learning](https://openreview.net/forum?id=b8TlYh6PN6)** — *ICLR 2026 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Causal discovery with latent variables is a fundamental task.

- **[EDIT-Bench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits](https://openreview.net/forum?id=FtL9eEmU6v)** — *ICLR 2026 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We propose a new benchmark for evaluating an LLM's ability to perform code edits.

- **[From Markov to Laplace: How Mamba In-Context Learns Markov Chains](https://openreview.net/forum?id=kmK3WSCOCT)** — *ICLR 2026 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We uncover an interesting phenomenon where a single-layer Mamba represents the Bayes optimal Laplacian smoothing estimator when trained on Markov chains and we demonstrate it theoretically and empirically.

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
  - **Summary:** Current Large Language Models have achieved Olympiad-level logic, yet Vision-Language Models paradoxically falter on elementary spatial tasks like block counting.

- **[A Constrained Optimization Perspective of Unrolled Transformers](https://openreview.net/forum?id=aYe8j2jOmK)** — *ICML 2026 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce a constrained optimization framework for training transformers that behave like optimization descent algorithms.

- **[A Mechanistic Investigation of Theory of Mind in a Large Language Model](https://neurips.cc/virtual/2026/poster/148276)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models successfully solve classic theory-of-mind tasks adapted from cognitive science, but the mechanisms underlying this ability remain unclear.

- **[A Solvable Model of Chain-of-Thought in In-Context Learning](https://neurips.cc/virtual/2026/poster/154777)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Chain-of-thought (CoT) reasoning has become a widely used mechanism for eliciting multi-step reasoning in large language models by generating intermediate reasoning steps at inference time.

- **[Cobra: Extending Mamba to Multi-Modal Large Language Model for Efficient Inference](https://ojs.aaai.org/index.php/AAAI/article/view/33131)** — *AAAI 2025*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In recent years, applying multi-modal large language models (MLLMs) in various fields has achieved remarkable success.

- **[FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts](https://ojs.aaai.org/index.php/AAAI/article/view/34568)** — *AAAI 2025*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Vision-Language Models (LVLMs) signify a groundbreaking paradigm shift within the Artificial Intelligence (AI) community, extending beyond the capabilities of Large Language Models (LLMs) by assimilating additional modalities (e.g., images).

- **[LiDAR-LLM: Exploring the Potential of Large Language Models for 3D LiDAR Understanding](https://ojs.aaai.org/index.php/AAAI/article/view/33001)** — *AAAI 2025*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recently, Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) have shown promise in instruction following and image understanding.

- **[A New Formulation of Zipf’s Meaning-Frequency Law through Contextual Diversity](https://aclanthology.org/2025.acl-long.744/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This paper proposes formulating Zipf’s meaning-frequency law, the power law between word frequency and the number of meanings, as a relationship between word frequency and contextual diversity.

- **[A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive](https://aclanthology.org/2025.acl-long.1454/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are increasingly utilized in autonomous decision-making, where they sample options from vast action spaces.

- **[All That Glitters is Not Novel: Plagiarism in AI Generated Research](https://aclanthology.org/2025.acl-long.1249/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Automating scientific research is considered the final frontier of science.

- **[Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral](https://aclanthology.org/2025.acl-long.294/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Moral reasoning is a complex cognitive process shaped by individual experiences and cultural contexts and presents unique challenges for computational analysis.

- **[Between Circuits and Chomsky: Pre-pretraining on Formal Languages Imparts Linguistic Biases](https://aclanthology.org/2025.acl-long.478/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Pretraining language models on formal language can improve their acquisition of natural language.

- **[Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention](https://aclanthology.org/2025.acl-long.270/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have shown remarkable capabilities in natural language processing but exhibit significant performance gaps among different languages.

- **[Byte Latent Transformer: Patches Scale Better Than Tokens](https://aclanthology.org/2025.acl-long.453/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce the Byte Latent Transformer (BLT), a new byte-level LLM architecture that, for the first time, matches tokenization-based LLM performance at scale with significant improvements in inference efficiency and robustness.

- **[HALoGEN: Fantastic LLM Hallucinations and Where to Find Them](https://aclanthology.org/2025.acl-long.71/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Despite their impressive ability to generate high-quality and fluent text, generative large language models (LLMs) also produce hallucinations: statements that are misaligned with established world knowledge or provided input context.

- **[Language Models Resist Alignment: Evidence From Data Compression](https://aclanthology.org/2025.acl-long.1141/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) may exhibit unintended or undesirable behaviors.

- **[Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs](https://aclanthology.org/2025.acl-long.791/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We observe a novel phenomenon, *contextual entrainment*, across a wide range of language models (LMs) and prompt settings, providing a new mechanistic perspective on how LMs become distracted by “irrelevant” contextual information in the input prompt.

- **[LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts](https://aclanthology.org/2025.acl-long.1207/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Safety concerns in large language models (LLMs) have gained significant attention due to their exposure to potentially harmful data during pre-training.

- **[MaCP: Minimal yet Mighty Adaptation via Hierarchical Cosine Projection](https://aclanthology.org/2025.acl-long.1006/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We present a new adaptation method MaCP, Minimal yet Mighty adaptive Cosine Projection, that achieves exceptional performance while requiring minimal parameters and memory for fine-tuning large foundation models.Its general idea is to exploit the superior energy compaction...

- **[Mapping 1,000+ Language Models via the Log-Likelihood Vector](https://aclanthology.org/2025.acl-long.1584/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** To compare autoregressive language models at scale, we propose using log-likelihood vectors computed on a predefined text set as model features.

- **[Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models](https://aclanthology.org/2025.acl-long.533/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The composition of pre-training datasets for large language models (LLMs) remains largely undisclosed, hindering transparency and efforts to optimize data quality—a critical driver of model performance.

- **[MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Long Context Understanding (LCU) is a critical area for exploration in current large language models (LLMs).

- **[Palm: A Culturally Inclusive and Linguistically Diverse Dataset for Arabic LLMs](https://aclanthology.org/2025.acl-long.1579/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** As large language models (LLMs) become increasingly integrated into daily life, ensuring their cultural sensitivity and inclusivity is paramount.

- **[Past Meets Present: Creating Historical Analogy with Large Language Models](https://aclanthology.org/2025.acl-long.200/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Historical analogies, which compare known past events with contemporary but unfamiliar events, are important abilities that help people make decisions and understand the world.

- **[Pre3: Enabling Deterministic Pushdown Automata for Faster Structured LLM Generation](https://aclanthology.org/2025.acl-long.551/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Extensive LLM applications demand efficient structured generations, particularly for LR(1) grammars, to produce outputs in specified formats (e.g., JSON).

- **[Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](https://aclanthology.org/2025.acl-long.1356/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recently, scaling test-time compute on Large Language Models (LLM) has garnered wide attention.

- **[Revisiting Compositional Generalization Capability of Large Language Models Considering Instruction Following Ability](https://aclanthology.org/2025.acl-long.1508/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In generative commonsense reasoning tasks such as CommonGen, generative large language models (LLMs) compose sentences that include all given concepts.

- **[SubLIME: Subset Selection via Rank Correlation Prediction for Data-Efficient LLM Evaluation](https://aclanthology.org/2025.acl-long.1477/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The rapid expansion of Large Language Models (LLMs) and natural language processing datasets has made exhaustive benchmark evaluations computationally prohibitive.

- **[The AI Gap: How Socioeconomic Status Affects Language Technology Interactions](https://aclanthology.org/2025.acl-long.914/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Socioeconomic status (SES) fundamentally influences how people interact with each other and, more recently, with digital technologies like large language models (LLMs).

- **[Towards the Law of Capacity Gap in Distilling Language Models](https://aclanthology.org/2025.acl-long.1097/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language model (LM) distillation aims at distilling the knowledge in a large teacher LM to a small student one.

- **[Turning Trash into Treasure: Accelerating Inference of Large Language Models with Token Recycling](https://aclanthology.org/2025.acl-long.338/)** — *ACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The rapid growth in the parameters of LLMs has made inference latency a fundamental bottleneck.

- **[Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning](https://openreview.net/forum?id=dNW3RGW0gi)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Discovering efficient algorithms for solving complex problems has been an outstanding challenge in mathematics and computer science, requiring substantial human expertise over the years.

- **[Can LLM "Self-report"?: Evaluating the Validity of Self-report Scales in Measuring Personality Design in LLM-based Chatbots](https://openreview.net/forum?id=xqIwK9mNkj)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** A chatbot’s personality design is key to interaction quality.

- **[Can Performant LLMs Be Ethical? Quantifying the Impact of Web Crawling Opt-Outs](https://openreview.net/forum?id=a6QsOjr3wo)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The increasing adoption of web crawling opt-outs by copyright holders of online content raises critical questions about the impact of data compliance on large language model (LLM) performance.

- **[EvalTree: Profiling Language Model Weaknesses via Hierarchical Capability Trees](https://openreview.net/forum?id=aV2hQN9vkp)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** An ideal model evaluation should achieve two goals: identifying where the model fails and providing actionable improvement guidance.

- **[FineWeb2: One Pipeline to Scale Them All — Adapting Pre-Training Data Processing to Every Language](https://openreview.net/forum?id=jnRBe6zatP)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Pre-training state-of-the-art large language models (LLMs) requires vast amounts of clean and diverse text data.

- **[Fluid Language Model Benchmarking](https://openreview.net/forum?id=mxcCg9YRqj)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language model (LM) benchmarking faces several challenges: comprehensive evaluations are costly, benchmarks often fail to measure the intended capabilities, and evaluation quality can degrade due to labeling errors and benchmark saturation.

- **[Resona: Improving Context Copying in Linear Recurrence Models with Retrieval](https://openreview.net/forum?id=4mxQmpnawk)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recent shifts in the space of large language model (LLM) research have shown an increasing focus on novel architectures to compete with prototypical Transformer-based models that have long dominated this space.

- **[SuperBPE: Space Travel for Language Models](https://openreview.net/forum?id=lcDRvffeNP)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The assumption across nearly all language model (LM) tokenization schemes is that tokens should be subwords, i.e., contained within word boundaries.

- **[The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains](https://openreview.net/forum?id=9rwtezthwo)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Improvements in language models are often driven by increasing the quality of the data we train them on, which can be limiting when strong supervision is not readily available.

- **[Tulu 3: Pushing Frontiers in Open Language Model Post-Training](https://openreview.net/forum?id=i1uGbfHHpH)** — *COLM 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language model post-training is applied to refine behaviors and unlock new skills across a wide range of language models, but open recipes for applying these techniques lag behind proprietary ones.

- **[Insight-V: Exploring Long-Chain Visual Reasoning with Multimodal Large Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Dong_Insight-V_Exploring_Long-Chain_Visual_Reasoning_with_Multimodal_Large_Language_Models_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) demonstrate enhanced capabilities and reliability by reasoning more, evolving from Chain-of-Thought prompting to product-level solutions like OpenAI o1.

- **[3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding](https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** A 3D scene graph represents a compact scene model by capturing both the objects present and the semantic relationships between them, making it a promising structure for robotic applications.

- **[Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models](https://iclr.cc/virtual/2025/poster/28041)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language Model (LM) agents for cybersecurity that are capable of autonomously identifying vulnerabilities and executing exploits have potential to cause real-world impact.

- **[Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://iclr.cc/virtual/2025/poster/29377)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Hallucinations in large language models are a widespread problem, yet the mechanisms behind whether models will hallucinate are poorly understood, limiting our ability to solve this problem.

- **[OLMoE: Open Mixture-of-Experts Language Models](https://iclr.cc/virtual/2025/poster/27777)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce OLMoE, a fully open, state-of-the-art language model leveraging sparse Mixture-of-Experts (MoE).

- **[Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://iclr.cc/virtual/2025/poster/30572)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Aligning large language models (LLMs) with human preferences becomes a key component to obtaining state-of-the-art performance, but it yields a huge cost to construct a large human-annotated preference dataset.

- **[Test of Time: A Benchmark for Evaluating LLMs on Temporal Reasoning](https://iclr.cc/virtual/2025/poster/31040)** — *ICLR 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) have showcased remarkable reasoning capabilities, yet they remain susceptible to errors, particularly in temporal reasoning tasks involving complex temporal logic.

- **[Transformers Provably Solve Parity Efficiently with Chain of Thought](https://iclr.cc/virtual/2025/poster/28433)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This work provides the first theoretical analysis of training transformers to solve complex problems by recursively generating intermediate states, analogous to fine-tuning for chain-of-thought (CoT) reasoning.

- **[Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://iclr.cc/virtual/2025/poster/28810)** — *ICLR 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Catastrophic forgetting (CF) poses a significant challenge in machine learning, where a model forgets previously learned information upon learning new tasks.

- **[Position: Formal Mathematical Reasoning—A New Frontier in AI](https://icml.cc/virtual/2025/poster/40156)** — *ICML 2025 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** AI for Mathematics (AI4Math) is intellectually intriguing and is crucial for AI-driven system design and verification.

- **[Position: General Intelligence Requires Reward-based Pretraining](https://icml.cc/virtual/2025/poster/40143)** — *ICML 2025 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have demonstrated impressive real-world utility, exemplifying artificial useful intelligence (AUI).

- **[Position: Language model developers should report train-test overlap](https://icml.cc/virtual/2025/poster/40154)** — *ICML 2025 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language models are extensively evaluated, but correctly interpreting evaluation results requires knowledge of train-test overlap, which refers to the extent to which the language model is trained on the very data it is being tested on.

- **[Position: Principles of Animal Cognition to Improve LLM Evaluations](https://icml.cc/virtual/2025/poster/40117)** — *ICML 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** It has become increasingly challenging to understand and evaluate LLM capabilities as these models exhibit a broader range of behaviors.

- **[Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://icml.cc/virtual/2025/poster/40102)** — *ICML 2025 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The proliferation of LLM bias probes introduces three challenges: we lack (1) principled criteria for selecting appropriate probes, (2) a system for reconciling conflicting results across probes, and (3) formal frameworks for reasoning about when and why experimental findings...

- **[GPT-NER: Named Entity Recognition via Large Language Models](https://aclanthology.org/2025.findings-naacl.239/)** — *NAACL 2025 · Findings*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Despite the fact that large-scale Language Models (LLM) have achieved SOTA performances on a variety of NLP tasks, its performance on NER is still significantly below supervised baselines.

- **[GRAG: Graph Retrieval-Augmented Generation](https://aclanthology.org/2025.findings-naacl.232/)** — *NAACL 2025 · Findings*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Naive Retrieval-Augmented Generation (RAG) focuses on individual documents during retrieval and, as a result, falls short in handling networked documents which are very popular in many applications such as citation graphs, social media, and knowledge graphs.

- **[ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](https://aclanthology.org/2025.naacl-long.342/)** — *NAACL 2025 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The pace of scientific research, vital for improving human life, is complex, slow, and needs specialized expertise.

- **[Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://openreview.net/forum?id=4OsgYD7em5)** — *NeurIPS 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) has recently demonstrated notable success in enhancing the reasoning performance of large language models (LLMs), particularly in mathematics and programming tasks.

- **[Neither Valid nor Reliable? Investigating the Use of LLMs as Judges](https://openreview.net/forum?id=yqKfMr0yvY)** — *NeurIPS 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Evaluating natural language generation (NLG) systems remains a core challenge, further complicated by the rise of general-purpose large language models (LLMs).

- **[Prompting as Scientific Inquiry](https://openreview.net/forum?id=yZU8kdwafM)** — *NeurIPS 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Prompting is the primary method by which we study and control large language models.

- **[Simulating Society Requires Simulating Thought](https://openreview.net/forum?id=EvXWexakZX)** — *NeurIPS 2025 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Simulating society with large language models (LLMs), we argue, requires more than generating plausible behavior; it demands cognitively grounded reasoning that is structured, revisable, and traceable.

- **[Stop DDoS Attacking the Research Community with AI-Generated Survey Papers](https://openreview.net/forum?id=R5uuqCAPf8)** — *NeurIPS 2025 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Survey papers are foundational to the scholarly progress of research communities, offering structured overviews that guide both novices and experts across disciplines.

- **[Benchmarking Large Language Models in Retrieval-Augmented Generation](https://ojs.aaai.org/index.php/AAAI/article/view/29728)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Retrieval-Augmented Generation (RAG) is a promising approach for mitigating the hallucination of large language models (LLMs).

- **[Detecting and Preventing Hallucinations in Large Vision Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/29771)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Instruction tuned Large Vision Language Models (LVLMs) have significantly advanced in generalizing across a diverse set of multi-modal tasks, especially for Visual Question Answering (VQA).

- **[ExpeL: LLM Agents Are Experiential Learners](https://ojs.aaai.org/index.php/AAAI/article/view/29936)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The recent surge in research interest in applying large language models (LLMs) to decision-making tasks has flourished by leveraging the extensive world knowledge embedded in LLMs.

- **[From Statistical Relational to Neuro-Symbolic Artificial Intelligence](https://ojs.aaai.org/index.php/AAAI/article/view/30294)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The integration of learning and reasoning is one of the key challenges in artificial intelligence and machine learning today.

- **[Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/29720)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce Graph of Thoughts (GoT): a framework that advances prompting capabilities in large language models (LLMs) beyond those offered by paradigms such as Chain-of-Thought or Tree of Thoughts (ToT).

- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have drastically reshaped our interactions with artificial intelligence (AI) systems, showcasing impressive performance across an extensive array of tasks.

- **[Visual Adversarial Examples Jailbreak Aligned Large Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/30150)** — *AAAI 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Warning: this paper contains data, prompts, and model outputs that are offensive in nature.

- **[AI ‘News’ Content Farms Are Easy to Make and Hard to Detect: A Case Study in Italian](https://aclanthology.org/2024.acl-long.817/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are increasingly used as ‘content farm’ models (CFMs), to generate synthetic text that could pass for real news articles.

- **[Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model](https://aclanthology.org/2024.acl-long.845/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recent breakthroughs in large language models (LLMs) have centered around a handful of data-rich languages.

- **[Can Large Language Models be Good Emotional Supporter? Mitigating Preference Bias on Emotional Support Conversation](https://aclanthology.org/2024.acl-long.813/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Emotional Support Conversation (ESC) is a task aimed at alleviating individuals’ emotional distress through daily conversation.

- **[Causal Estimation of Memorisation Profiles](https://aclanthology.org/2024.acl-long.834/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Understanding memorisation in language models has practical and societal implications, e.g., studying models’ training dynamics or preventing copyright infringements.Prior work defines memorisation as the causal effect of training with an instance on the model’s ability to...

- **[Causal-Guided Active Learning for Debiasing Large Language Models](https://aclanthology.org/2024.acl-long.778/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Although achieving promising performance, recent analyses show that current generative large language models (LLMs) may still capture dataset biases and utilize them for generation, leading to poor generalizability and harmfulness of LLMs.

- **[CHECKWHY: Causal Fact Verification via Argument Structure](https://aclanthology.org/2024.acl-long.835/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** With the growing complexity of fact verification tasks, the concern with “thoughtful” reasoning capabilities is increasing.

- **[DIALECTBENCH: An NLP Benchmark for Dialects, Varieties, and Closely-Related Languages](https://aclanthology.org/2024.acl-long.777/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language technologies should be judged on their usefulness in real-world use cases.

- **[Discursive Socratic Questioning: Evaluating the Faithfulness of Language Models’ Understanding of Discourse Relations](https://aclanthology.org/2024.acl-long.341/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** While large language models have significantly enhanced the effectiveness of discourse relation classifications, it remains unclear whether their comprehension is faithful and reliable.

- **[Do Llamas Work in English? On the Latent Language of Multilingual Transformers](https://aclanthology.org/2024.acl-long.820/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We ask whether multilingual language models trained on unbalanced, English-dominated corpora use English as an internal pivot language—-a question of key importance for understanding how language models function and the origins of linguistic bias.

- **[Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research](https://aclanthology.org/2024.acl-long.840/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Information about pretraining corpora used to train the current best-performing language models is seldom discussed: commercial models rarely detail their data, and even open models are often released without accompanying training data or recipes to reproduce them.

- **[Don’t Hallucinate, Abstain: Identifying LLM Knowledge Gaps via Multi-LLM Collaboration](https://aclanthology.org/2024.acl-long.786/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Despite efforts to expand the knowledge of large language models (LLMs), knowledge gaps—missing or outdated information in LLMs—might always persist given the evolving nature of knowledge.

- **[G-DIG: Towards Gradient-based DIverse and hiGh-quality Instruction Data Selection for Machine Translation](https://aclanthology.org/2024.acl-long.821/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have demonstrated remarkable abilities in general scenarios.

- **[Getting Serious about Humor: Crafting Humor Datasets with Unfunny Large Language Models](https://aclanthology.org/2024.acl-short.76/)** — *ACL 2024 · Short*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Humor is a fundamental facet of human cognition and interaction.

- **[Greed is All You Need: An Evaluation of Tokenizer Inference Methods](https://aclanthology.org/2024.acl-short.73/)** — *ACL 2024 · Short*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** While subword tokenizers such as BPE and WordPiece are typically used to build vocabularies for NLP models, the method of decoding text into a sequence of tokens from these vocabularies is often left unspecified, or ill-suited to the method in which they were constructed.

- **[Having Beer after Prayer? Measuring Cultural Bias in Large Language Models](https://aclanthology.org/2024.acl-long.862/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** As the reach of large language models (LMs) expands globally, their ability to cater to diverse cultural contexts becomes crucial.

- **[How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs](https://aclanthology.org/2024.acl-long.773/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Most traditional AI safety research views models as machines and centers on algorithm-focused attacks developed by security experts.

- **[IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages](https://aclanthology.org/2024.acl-long.843/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Despite the considerable advancements in English LLMs, the progress in building comparable models for other languages has been hindered due to the scarcity of tailored resources.

- **[IRCoder: Intermediate Representations Make Language Models Robust Multilingual Code Generators](https://aclanthology.org/2024.acl-long.802/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Code generation has fast become one of the most popular applications of language models (LMs).

- **[L-Eval: Instituting Standardized Evaluation for Long Context Language Models](https://aclanthology.org/2024.acl-long.776/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recently, there has been growing interest in long-context scaling of large language models (LLMs).

- **[MAP’s not dead yet: Uncovering true language model modes by conditioning away degeneracy](https://aclanthology.org/2024.acl-long.855/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** It has been widely observed that exact or approximate MAP (mode-seeking) decoding from natural language generation (NLG) models consistently leads to degenerate outputs (Holtzman et al., 2019; Stahlberg and Byrne, 2019).

- **[Media Framing: A typology and Survey of Computational Approaches Across Disciplines](https://aclanthology.org/2024.acl-long.822/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Framing studies how individuals and societies make sense of the world, by communicating or representing complex issues through schema of interpretation.

- **[MIDGARD: Self-Consistency Using Minimum Description Length for Structured Commonsense Reasoning](https://aclanthology.org/2024.acl-long.380/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We study the task of conducting structured reasoning as generating a reasoning graph from natural language input using large language models (LLMs).

- **[Mission: Impossible Language Models](https://aclanthology.org/2024.acl-long.787/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Chomsky and others have very directly claimed that large language models (LLMs) are equally capable of learning languages that are possible and impossible for humans to learn.

- **[MultiPICo: Multilingual Perspectivist Irony Corpus](https://aclanthology.org/2024.acl-long.849/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recently, several scholars have contributed to the growth of a new theoretical framework in NLP called perspectivism.

- **[Must NLP be Extractive?](https://aclanthology.org/2024.acl-long.797/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** How do we roll out language technologies across a world with 7,000 languages?

- **[Natural Language Satisfiability: Exploring the Problem Distribution and Evaluating Transformer-based Language Models](https://aclanthology.org/2024.acl-long.815/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Efforts to apply transformer-based language models (TLMs) to the problem of reasoning in natural language have enjoyed ever-increasing success in recent years.

- **[OLMo: Accelerating the Science of Language Models](https://aclanthology.org/2024.acl-long.841/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language models (LMs) have become ubiquitous in both NLP research and in commercial product offerings.

- **[Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models](https://aclanthology.org/2024.acl-long.816/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Much recent work seeks to evaluate values and opinions in large language models (LLMs) using multiple-choice surveys and questionnaires.

- **[Quantized Side Tuning: Fast and Memory-Efficient Tuning of Quantized Large Language Models](https://aclanthology.org/2024.acl-long.1/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Finetuning large language models (LLMs) has been empirically effective on a variety of downstream tasks.

- **[RomanSetu: Efficiently unlocking multilingual capabilities of Large Language Models via Romanization](https://aclanthology.org/2024.acl-long.833/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This study addresses the challenge of extending Large Language Models (LLMs) to non-English languages, specifically those using non-Roman scripts.

- **[Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models](https://aclanthology.org/2024.acl-long.818/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This paper explores the impact of extending input lengths on the capabilities of Large Language Models (LLMs).

- **[Spiral of Silence: How is Large Language Model Killing Information Retrieval?—A Case Study on Open Domain Question Answering](https://aclanthology.org/2024.acl-long.798/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The practice of Retrieval-Augmented Generation (RAG), which integrates Large Language Models (LLMs) with retrieval systems, has become increasingly prevalent.

- **[Steering Llama 2 via Contrastive Activation Addition](https://aclanthology.org/2024.acl-long.828/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce Contrastive Activation Addition (CAA), a method for steering language models by modifying their activations during forward passes.

- **[The Earth is Flat because...: Investigating LLMs’ Belief towards Misinformation via Persuasive Conversation](https://aclanthology.org/2024.acl-long.858/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) encapsulate vast amounts of knowledge but still remain vulnerable to external misinformation.

- **[VariErr NLI: Separating Annotation Error from Human Label Variation](https://aclanthology.org/2024.acl-long.123/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Human label variation arises when annotators assign different labels to the same item for valid reasons, while annotation errors occur when labels are assigned for invalid reasons.

- **[Why are Sensitive Functions Hard for Transformers?](https://aclanthology.org/2024.acl-long.800/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Empirical studies have identified a range of learnability biases and limitations of transformers, such as a persistent difficulty in learning to compute simple formal languages such as PARITY, and a bias towards low-degree functions.

- **[Word Embeddings Are Steers for Language Models](https://aclanthology.org/2024.acl-long.864/)** — *ACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language models (LMs) automatically learn word embeddings during pre-training on language corpora.

- **[Mechanics of Next Token Prediction with Self-Attention](https://proceedings.mlr.press/v238/li24f.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Transformer-based language models are trained on large datasets to predict the next token given an input sequence.

- **[Multi-resolution Time-Series Transformer for Long-term Forecasting](https://proceedings.mlr.press/v238/zhang24l.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The performance of transformers for time-series forecasting has improved significantly.

- **[Quantifying Uncertainty in Natural Language Explanations of Large Language Models](https://proceedings.mlr.press/v238/harsha-tanneru24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are increasingly used as powerful tools for several high-stakes natural language processing (NLP) applications.

- **[Can Language Models Solve Olympiad Programming?](https://openreview.net/forum?id=kGa4fMtP9l)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Olympiad programming is one of the hardest reasoning challenges for humans, yet it has been understudied as a domain to benchmark language models (LMs).

- **[Dated Data: Tracing Knowledge Cutoffs in Large Language Models](https://openreview.net/forum?id=wS7PxDjy6m)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are often paired with a reported cutoff date, the time at which training data was gathered.

- **[Evaluating Cultural Adaptability of a Large Language Model via Simulation of Synthetic Personas](https://openreview.net/forum?id=S4ZOkV1AHl)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The success of Large Language Models (LLMs) in multicultural environments hinges on their ability to understand users' diverse cultural backgrounds.

- **[Information-Theoretic Distillation for Reference-less Summarization](https://openreview.net/forum?id=JXcXnJJSuL)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The current winning recipe for automatic summarization is using proprietary large-scale language models (LLMs) such as ChatGPT as is, or imitation learning from them as teacher models.

- **[Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://openreview.net/forum?id=tEYskw1VY2)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module.

- **[Measuring and Controlling Instruction (In)Stability in Language Model Dialogs](https://openreview.net/forum?id=60a1SAtH4e)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** System-prompting is a standard tool for customizing language-model chatbots, enabling them to follow a specific instruction.

- **[PolygloToxicityPrompts: Multilingual Evaluation of Neural Toxic Degeneration in Large Language Models](https://openreview.net/forum?id=ootI3ZO6TJ)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recent advances in large language models (LLMs) have led to their extensive global deployment, and ensuring their safety calls for comprehensive and multilingual toxicity evaluations.

- **[Will the Real Linda Please Stand up...to Large Language Models? Examining the Representativeness Heuristic in LLMs](https://openreview.net/forum?id=3GhOWfSLrD)** — *COLM 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Although large language models (LLMs) have demonstrated remarkable proficiency in modeling text and generating human-like text, they may exhibit biases acquired from training data in doing so.

- **[Environment Curriculum Generation via Large Language Models](https://openreview.net/forum?id=F0rWEID2gb)** — *CoRL 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recent work has demonstrated that a promising strategy for teaching robots a wide range of complex skills is by training them on a curriculum of progressively more challenging environments.

- **[PoliFormer: Scaling On-Policy RL with Transformers Results in Masterful Navigators](https://openreview.net/forum?id=KdVLK0Wo5z)** — *CoRL 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We present PoliFormer (Policy Transformer), an RGB-only indoor navigation agent trained end-to-end with reinforcement learning at scale that generalizes to the real-world without adaptation despite being trained purely in simulation.

- **[CogAgent: A Visual Language Model for GUI Agents](https://openaccess.thecvf.com/content/CVPR2024/html/Hong_CogAgent_A_Visual_Language_Model_for_GUI_Agents_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** People are spending an enormous amount of time on digital devices through graphical user interfaces (GUIs) e.g. computer or smartphone screens.

- **[Improved Baselines with Visual Instruction Tuning](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Improved_Baselines_with_Visual_Instruction_Tuning_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large multimodal models (LMM) have recently shown encouraging progress with visual instruction tuning.

- **[PointLLM: Empowering Large Language Models to Understand Point Clouds](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3601_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** "The unprecedented advancements in Large Language Models (LLMs) have shown a profound impact on natural language processing but are yet to fully embrace the realm of 3D understanding.

- **[A User-Centric Multi-Intent Benchmark for Evaluating Large Language Models](https://aclanthology.org/2024.emnlp-main.210/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) are essential tools that users employ across various scenarios, so evaluating their performance and guiding users in selecting the suitable service is important.

- **[Are Large Language Models Capable of Generating Human-Level Narratives?](https://aclanthology.org/2024.emnlp-main.978/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** As daily reliance on large language models (LLMs) grows, assessing their generation quality is crucial to understanding how they might impact on our communications.

- **[Backward Lens: Projecting Language Model Gradients into the Vocabulary Space](https://aclanthology.org/2024.emnlp-main.142/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Understanding how Transformer-based Language Models (LMs) learn and recall information is a key goal of the deep learning community.

- **[Do LLMs Plan Like Human Writers? Comparing Journalist Coverage of Press Releases with LLMs](https://aclanthology.org/2024.emnlp-main.1216/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Journalists engage in multiple steps in the news writing process that depend on human creativity, like exploring different “angles” (i.e. the specific perspectives a reporter takes).

- **[Finding Blind Spots in Evaluator LLMs with Interpretable Checklists](https://aclanthology.org/2024.emnlp-main.911/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are increasingly relied upon to evaluate text outputs of other LLMs, thereby influencing leaderboards and development decisions.

- **[Fishing for Magikarp: Automatically Detecting Under-trained Tokens in Large Language Models](https://aclanthology.org/2024.emnlp-main.649/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The disconnect between tokenizer creation and model training in language models allows for specific inputs, such as the infamous SolidGoldMagikarp token, to induce unwanted model behaviour.

- **[Formality is Favored: Unraveling the Learning Preferences of Large Language Models on Data with Conflicting Knowledge](https://aclanthology.org/2024.emnlp-main.304/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Having been trained on massive pretraining data, large language models have shown excellent performance on many knowledge-intensive tasks.

- **[GoldCoin: Grounding Large Language Models in Privacy Laws via Contextual Integrity Theory](https://aclanthology.org/2024.emnlp-main.195/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Privacy issues arise prominently during the inappropriate transmission of information between entities.

- **[KidLM: Advancing Language Models for Children – Early Insights and Future Directions](https://aclanthology.org/2024.emnlp-main.277/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recent studies highlight the potential of large language models in creating educational tools for children, yet significant challenges remain in maintaining key child-specific properties such as linguistic nuances, cognitive needs, and safety standards.

- **[Language Models Learn Rare Phenomena from Less Rare Phenomena: The Case of the Missing AANNs](https://aclanthology.org/2024.emnlp-main.53/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Language models learn rare syntactic phenomena, but the extent to which this is attributable to generalization vs. memorization is a major open question.

- **[Learning Planning-based Reasoning by Trajectories Collection and Process Reward Synthesizing](https://aclanthology.org/2024.emnlp-main.20/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have demonstrated significant potential in handling complex reasoning tasks through step-by-step rationale generation.

- **[Learning to Retrieve Iteratively for In-Context Learning](https://aclanthology.org/2024.emnlp-main.406/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We introduce iterative retrieval, a novel framework that empowers retrievers to make iterative decisions through policy optimization.

- **[Measuring Psychological Depth in Language Models](https://aclanthology.org/2024.emnlp-main.953/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Evaluations of creative stories generated by large language models (LLMs) often focus on objective properties of the text, such as its style, coherence, and diversity.

- **[OATH-Frames: Characterizing Online Attitudes Towards Homelessness with LLM Assistants](https://aclanthology.org/2024.emnlp-main.724/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Warning: Contents of this paper may be upsetting.Public attitudes towards key societal issues, expressed on online media, are of immense value in policy and reform efforts, yet challenging to understand at scale.

- **[Pretraining Data Detection for Large Language Models: A Divergence-based Calibration Method](https://aclanthology.org/2024.emnlp-main.300/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** As the scale of training corpora for large language models (LLMs) grows, model developers become increasingly reluctant to disclose details on their data.

- **[sign.mt: Real-Time Multilingual Sign Language Translation Application](https://aclanthology.org/2024.emnlp-demo.19/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** This paper presents sign.mt, an open-source application for real-time multilingual bi-directional translation between spoken and signed languages.

- **[STOP! Benchmarking Large Language Models with Sensitivity Testing on Offensive Progressions](https://aclanthology.org/2024.emnlp-main.243/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Mitigating explicit and implicit biases in Large Language Models (LLMs) has become a critical focus in the field of natural language processing.

- **[The Zeno’s Paradox of ‘Low-Resource’ Languages](https://aclanthology.org/2024.emnlp-main.983/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The disparity in the languages commonly studied in Natural Language Processing (NLP) is typically reflected by referring to languages as low vs high-resourced.

- **[Towards Cross-Cultural Machine Translation with Retrieval-Augmented Generation from Multilingual Knowledge Graphs](https://aclanthology.org/2024.emnlp-main.914/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Translating text that contains entity names is a challenging task, as cultural-related references can vary significantly across languages.

- **[Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving](https://aclanthology.org/2024.emnlp-main.172/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Natural language explanations represent a proxy for evaluating explanation-based and multi-step Natural Language Inference (NLI) models.

- **[When Is Multilinguality a Curse? Language Modeling for 250 High- and Low-Resource Languages](https://aclanthology.org/2024.emnlp-main.236/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Multilingual language models are widely used to extend NLP systems to low-resource languages.

- **[Which questions should I answer? Salience Prediction of Inquisitive Questions](https://aclanthology.org/2024.emnlp-main.1114/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Inquisitive questions — open-ended, curiosity-driven questions people ask as they read — are an integral part of discourse processing and comprehension.

- **[BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://iclr.cc/virtual/2024/poster/19359)** — *ICLR 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Summarizing book-length documents ($>$100K tokens) that exceed the context window size of large language models (LLMs) requires first breaking the input document into smaller chunks and then prompting an LLM to merge, update, and compress chunk-level summaries.

- **[The mechanistic basis of data dependence and abrupt learning in an in-context classification task](https://iclr.cc/virtual/2024/poster/18368)** — *ICLR 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Transformer models exhibit in-context learning: the ability to accurately predict the response to a novel query based on illustrative examples in the input sequence, which contrasts with traditional in-weights learning of query-output relationships.

- **[Understanding and Mitigating the Label Noise in Pre-training on Downstream Tasks](https://iclr.cc/virtual/2024/poster/18555)** — *ICLR 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Pre-training on large-scale datasets and then fine-tuning on downstream tasks have become a standard practice in deep learning.

- **[GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection](https://proceedings.mlr.press/v235/zhao24s.html)** — *ICML 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Training Large Language Models (LLMs) presents significant memory challenges, predominantly due to the growing size of weights and optimizer states.

- **[Nash Learning from Human Feedback](https://proceedings.mlr.press/v235/munos24a.html)** — *ICML 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Reinforcement learning from human feedback (RLHF) has emerged as the main paradigm for aligning large language models (LLMs) with human preferences.

- **[NExT-GPT: Any-to-Any Multimodal LLM](https://proceedings.mlr.press/v235/wu24e.html)** — *ICML 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** While recently Multimodal Large Language Models (MM-LLMs) have made exciting strides, they mostly fall prey to the limitation of only input-side multimodal understanding, without the ability to produce content in multiple modalities.

- **[Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modulo Frameworks](https://proceedings.mlr.press/v235/kambhampati24a.html)** — *ICML 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We argue that auto-regressive LLMs cannot, by themselves, do planning or self-verification (which is after all a form of reasoning), and shed some light on the reasons for misunderstandings in the literature.

- **[Unified Training of Universal Time Series Forecasting Transformers](https://proceedings.mlr.press/v235/woo24a.html)** — *ICML 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Deep learning for time series forecasting has traditionally operated within a one-model-per-dataset framework, limiting its potential to leverage the game-changing impact of large pre-trained models.

- **[VideoPoet: A Large Language Model for Zero-Shot Video Generation](https://proceedings.mlr.press/v235/kondratyuk24a.html)** — *ICML 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We present VideoPoet, a language model capable of synthesizing high-quality video from a large variety of conditioning signals.

- **[Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision](https://proceedings.mlr.press/v235/burns24b.html)** — *ICML 2024 · Oral*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Widely used alignment techniques, such as reinforcement learning from human feedback (RLHF), rely on the ability of humans to supervise model behavior---for example, to evaluate whether a model faithfully followed instructions or generated safe outputs.

- **[AutoTAMP: Autoregressive Task and Motion Planning with LLMs as Translators and Checkers](https://ieeexplore.ieee.org/document/10611163/)** — *ICRA 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** For effective human-robot interaction, robots need to understand, plan, and execute complex, long-horizon tasks described by natural language.

- **[Driving with LLMs: Fusing Object-Level Vector Modality for Explainable Autonomous Driving](https://ieeexplore.ieee.org/document/10611018/)** — *ICRA 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have shown promise in the autonomous driving sector, particularly in generalization and interpretability.

- **[LLM-Grounder: Open-Vocabulary 3D Visual Grounding with Large Language Model as an Agent](https://ieeexplore.ieee.org/document/10610443/)** — *ICRA 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** 3D visual grounding is a critical skill for household robots, enabling them to navigate, manipulate objects, and answer questions based on their environment.

- **[RoCo: Dialectic Multi-Robot Collaboration with Large Language Models](https://ieeexplore.ieee.org/document/10610855/)** — *ICRA 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** We propose a novel approach to multi-robot collaboration that harnesses the power of pre-trained large language models (LLMs) for both high-level communication and low-level path planning.

- **[A Survey of Graph Meets Large Language Model: Progress and Future Directions](https://www.ijcai.org/proceedings/2024/898)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Graph plays a significant role in representing and analyzing complex relationships in real-world applications such as citation networks, social networks, and biological data.

- **[Beyond the Limits: A Survey of Techniques to Extend the Context Length in Large Language Models](https://www.ijcai.org/proceedings/2024/917)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Recently, large language models (LLMs) have shown remarkable capabilities including understanding context, engaging in logical reasoning, and generating responses.

- **[Large Language Model Based Multi-agents: A Survey of Progress and Challenges](https://www.ijcai.org/proceedings/2024/890)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have achieved remarkable success across a wide array of tasks.

- **[Large Language Models Are Not Strong Abstract Reasoners](https://www.ijcai.org/proceedings/2024/693)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models have shown tremendous performance on a large variety of natural language processing tasks, ranging from text comprehension to common sense reasoning.

- **[Large Language Models for Time Series: A Survey](https://www.ijcai.org/proceedings/2024/921)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have seen significant use in domains such as natural language processing and computer vision.

- **[ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://www.ijcai.org/proceedings/2024/339)** — *IJCAI 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Screen user interfaces (UIs) and infographics, sharing similar visual language and design principles, play important roles in human communication and human-machine interaction.

- **[DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment](https://ieeexplore.ieee.org/document/10802284/)** — *IROS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) encode a vast amount of semantic knowledge and possess remarkable understanding and reasoning capabilities.

- **[LLM3: Large Language Model-based Task and Motion Planning with Motion Failure Reasoning](https://ieeexplore.ieee.org/document/10801328/)** — *IROS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Conventional Task and Motion Planning (TAMP) approaches rely on manually designed interfaces connecting symbolic task planning with continuous motion generation.

- **[SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models](https://ieeexplore.ieee.org/document/10802322/)** — *IROS 2024 · Poster*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In this work, we introduce SMART-LLM, an innovative framework designed for embodied multi-robot task planning.

- **[AnnoLLM: Making Large Language Models to Be Better Crowdsourced Annotators](https://aclanthology.org/2024.naacl-industry.15/)** — *NAACL 2024*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Many natural language processing (NLP) tasks rely on labeled data to train machine learning models with high performance.

- **[Large Language Models are Effective Text Rankers with Pairwise Ranking Prompting](https://aclanthology.org/2024.findings-naacl.97/)** — *NAACL 2024 · Findings*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Ranking documents using Large Language Models (LLMs) by directly feeding the query and candidate documents into the prompt is an interesting and practical problem.

- **[Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions](https://aclanthology.org/2024.findings-naacl.130/)** — *NAACL 2024 · Findings*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) have demonstrated remarkable capabilities in various NLP tasks.

- **[Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks](https://aclanthology.org/2024.naacl-long.102/)** — *NAACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** The impressive performance of recent language models across a wide range of tasks suggests that they possess a degree of abstract reasoning skills.

- **[Sentiment Analysis in the Era of Large Language Models: A Reality Check](https://aclanthology.org/2024.findings-naacl.246/)** — *NAACL 2024 · Findings*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Sentiment analysis (SA) has been a long-standing research area in natural language processing.

- **[Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration](https://aclanthology.org/2024.naacl-long.15/)** — *NAACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Human intelligence thrives on cognitive synergy, where collaboration among different minds yield superior outcomes compared to isolated individuals.

- **[XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models](https://aclanthology.org/2024.naacl-long.301/)** — *NAACL 2024 · Long*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Without proper safeguards, large language models will readily follow malicious instructions and generate toxic content.

- **[A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://neurips.cc/virtual/2024/poster/97687)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) have achieved impressive success on many benchmarks for mathematical reasoning.

- **[BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://neurips.cc/virtual/2024/poster/97462)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In recent years, the input context sizes of large language models (LLMs) have increased dramatically.

- **[Instruction Tuning Large Language Models to Understand Electronic Health Records](https://neurips.cc/virtual/2024/poster/97801)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large language models (LLMs) have shown impressive capabilities in solving a wide range of tasks based on human instructions.

- **[PrivAuditor: Benchmarking Data Protection Vulnerabilities in LLM Adaptation Techniques](https://neurips.cc/virtual/2024/poster/97662)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** Large Language Models (LLMs) are recognized for their potential to be an important building block toward achieving artificial general intelligence due to their unprecedented capability for solving diverse tasks.

- **[xLSTM: Extended Long Short-Term Memory](https://neurips.cc/virtual/2024/poster/96260)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Language modeling, reasoning, and NLP
  - **Summary:** In the 1990s, the constant error carousel and gating were introduced as the central ideas of the Long Short-Term Memory (LSTM).

## AI Agents and Tools

- **[DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents](https://openreview.net/forum?id=q1jd5DsPfx)** — *ICLR 2027 · Under review*
  - **Topic:** Agent red-teaming and safety
  - **Summary:** Introduces a red-teaming platform and automated attack agents for evaluating tool use, prompt injection, and other safety risks across reproducible agent environments.

- **[OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://openreview.net/forum?id=ddJW429f5j)** — *ICLR 2027 · Under review*
  - **Topic:** Long-horizon computer-use agents
  - **Summary:** Introduces 108 long-horizon computer-use workflows covering cross-source reasoning, dynamic interfaces, and hidden-state inference for evaluating real-world computer-use agents.

- **[Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments](https://openreview.net/forum?id=9gw03JpKK4)** — *ICLR 2026 · Oral*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Gaia2 evaluates LLM agents in asynchronous, dynamic environments with action-level verification, revealing fundamental trade-offs between reasoning, speed, and robustness.

- **[$\\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://openreview.net/forum?id=OC2z7iSQKa)** — *ICML 2026 · Spotlight*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Existing benchmarks for conversational AI agents simulate _single-control_ environments, where only the AI agent can use tools to interact with the world, while the user remains a passive information provider.

- **[R2E-Gym: Procedural Environment Generation and Hybrid Verifiers for Scaling Open-Weights SWE Agents](https://openreview.net/forum?id=7evvwwdo3z)** — *COLM 2025 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Improving open-source models on real-world SWE tasks (solving GITHUB issues) faces two key challenges: 1) scalable curation of execution environments to train these models, and, 2) optimal scaling of test-time compute.

- **[Position: AI Agents Need Authenticated Delegation](https://icml.cc/virtual/2025/poster/40172)** — *ICML 2025 · Oral*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** The rapid deployment of autonomous AI agents creates urgent challenges in the areas of authorization, accountability, and access control in task delegation.

- **[Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://icml.cc/virtual/2025/poster/40177)** — *ICML 2025 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Self-improving agents aim to continuously acquire new capabilities with minimal supervision.

- **[EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](https://aclanthology.org/2025.naacl-long.44/)** — *NAACL 2025 · Long*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** There has been a rising interest in utilizing tools in applications of autonomous agents based on large language models (LLMs) to address intricate real-world tasks.

- **[Simulating Classroom Education with LLM-Empowered Agents](https://aclanthology.org/2025.naacl-long.520/)** — *NAACL 2025 · Long*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Large language models (LLMs) have been applied across various intelligent educational tasks to assist teaching.

- **[UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26/)** — *NAACL 2025 · Long*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** We introduce UFO, a UI-Fcused agent designed to fulfill user requests tailored to Windows OS applications by observing and analyzing the GUI and control information of these applications.

- **[Embracing Trustworthy Brain-Agent Collaboration as Paradigm Extension for Intelligent Assistive Technologies](https://openreview.net/forum?id=VZnOKzQ5qW)** — *NeurIPS 2025 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Brain-Computer Interfaces (BCIs) offer a direct communication pathway between the human brain and external devices, holding significant promise for individuals with severe neurological impairments.

- **[AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://aclanthology.org/2024.acl-long.850/)** — *ACL 2024 · Long*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Autonomous agents that address day-to-day digital tasks (e.g., ordering groceries for a household), must not only operate multiple apps (e.g., notes, messaging, shopping app) via APIs, but also generate rich code with complex control flow in an iterative manner based on their...

- **[EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities](https://aclanthology.org/2024.acl-long.829/)** — *ACL 2024 · Long*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** The advent of artificial intelligence has led to a growing emphasis on data-driven modeling in macroeconomics, with agent-based modeling (ABM) emerging as a prominent bottom-up simulation paradigm.

- **[OpenOmni: A Collaborative Open Source Tool for Building Future-Ready Multimodal Conversational Agents](https://aclanthology.org/2024.emnlp-demo.5/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Multimodal conversational agents are highly desirable because they offer natural and human-like interaction.However, there is a lack of comprehensive end-to-end solutions to support collaborative development and benchmarking.While proprietary systems like GPT-4o and Gemini...

- **[SUPER: Evaluating Agents on Setting Up and Executing Tasks from Research Repositories](https://aclanthology.org/2024.emnlp-main.702/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Given that Large Language Models (LLMs) have made significant progress in writing code, can they now be used to autonomously reproduce results from research repositories?

- **[TravelPlanner: A Benchmark for Real-World Planning with Language Agents](https://proceedings.mlr.press/v235/xie24j.html)** — *ICML 2024 · Spotlight*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Planning has been part of the core pursuit for artificial intelligence since its conception, but earlier AI agents mostly focused on constrained settings because many of the cognitive substrates necessary for human-level planning have been lacking.

- **[AutoAgents: A Framework for Automatic Agent Generation](https://www.ijcai.org/proceedings/2024/3)** — *IJCAI 2024 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** Large language models (LLMs) have enabled remarkable advances in automated task-solving with multi-agent systems.

- **[Scalable Multi-Agent Reinforcement Learning for Warehouse Logistics with Robotic and Human Co-Workers](https://ieeexplore.ieee.org/document/10802813/)** — *IROS 2024 · Poster*
  - **Topic:** Agents, tool use, and planning
  - **Summary:** We consider a warehouse in which dozens of mobile robots and human pickers work together to collect and deliver items within the warehouse.

## AI for Science and Biology

- **[Co-folding with a Soup of Representations](https://arxiv.org/abs/2609.15552)** — *ICLR 2027 · Under review*
  - **Topic:** Protein and biomolecular structure prediction
  - **Summary:** Combines pair representations from multiple co-folding models to predict protein and other biomolecular complex structures without retraining the underlying models.

- **[Language-Enhanced Representation Learning for Single-Cell Transcriptomics](https://arxiv.org/abs/2503.09427)** — *ICLR 2026*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** Single-cell RNA sequencing (scRNA-seq) offers detailed insights into cellular heterogeneity.

- **[A Call to Lagrangian Action: Learning Population Mechanics from Temporal Snapshots](https://arxiv.org/abs/2605.08550)** — *ICML 2026 · Spotlight*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** The population dynamics of molecules, cells, and organisms are governed by a number of unknown internal and external forces.

- **[Learning stochastic dynamics from snapshots through regularized unbalanced optimal transport](https://iclr.cc/virtual/2025/poster/28822)** — *ICLR 2025 · Oral*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** Reconstructing dynamics using samples from sparsely time-resolved snapshots is an important problem in both natural sciences and machine learning.

- **[Huatuo-26M, a Large-scale Chinese Medical QA Dataset](https://aclanthology.org/2025.findings-naacl.211/)** — *NAACL 2025 · Findings*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** Large Language Models infuse newfound vigor into the advancement of the medical domain, yet the scarcity of data poses a significant bottleneck hindering community progress.

- **[Fool Me Once? Contrasting Textual and Visual Explanations in a Clinical Decision-Support Setting](https://aclanthology.org/2024.emnlp-main.1051/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Protein, molecule, and biological modeling
  - **Summary:** The growing capabilities of AI models are leading to their wider use, including in safety-critical domains.

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
  - **Summary:** Most current paradigms in visual mechanistic interpretability (MI) remain confined to interpreting internal units of the vision model via heuristic methods (e.g., top-$K$ activation retrieval or optimization with regularization).

- **[3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model](https://neurips.cc/virtual/2026/poster/155977)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Feed-forward 3D reconstruction models have demonstrated strong generalization under large-scale pre-training, yet they struggle in long-tail scenarios such as low-light reconstruction, joint human-scene reconstruction, and test-time adaptation.

- **[A multi-scale information geometry reveals the structure of mutual information in neural populations](https://neurips.cc/virtual/2026/poster/154781)** — *NeurIPS 2026 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Understanding how neural population responses represent sensory information is a central problem in systems neuroscience.

- **[AdaCodec: A Predictive Visual Code for Video MLLMs](https://neurips.cc/virtual/2026/poster/148821)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Video is temporally redundant: adjacent frames usually share most objects, background, and layout.

- **[AdapToPASS: Ambiguity-aware Adaptive Spherical Transformer for Panoramic Semantic Segmentation](https://neurips.cc/virtual/2026/poster/151962)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Spherical Transformers have emerged as a promising framework for panoramic semantic segmentation (PASS) by operating directly on spherical geometry and alleviating projection-induced distortions.

- **[EfficientVMamba: Atrous Selective Scan for Light Weight Visual Mamba](https://ojs.aaai.org/index.php/AAAI/article/view/32690)** — *AAAI 2025*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Prior efforts in light-weight model development mainly centered on CNN and Transformer-based designs yet faced persistent challenges.

- **[IMAGDressing-v1: Customizable Virtual Dressing](https://ojs.aaai.org/index.php/AAAI/article/view/32729)** — *AAAI 2025*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Existing virtual try-on (VTON) methods provide only limited user control over garment attributes and generally overlook essential factors such as face, pose, and scene context.

- **[Point Cloud Mamba: Point Cloud Learning via State Space Model](https://ojs.aaai.org/index.php/AAAI/article/view/33098)** — *AAAI 2025*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Recently, state space models have exhibited strong global modeling capabilities and linear computational complexity in contrast to transformers.

- **[Segment Any 3D Gaussians](https://ojs.aaai.org/index.php/AAAI/article/view/32193)** — *AAAI 2025*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** This paper presents SAGA (Segment Any 3D GAussians), a highly efficient 3D promptable segmentation method based on 3D Gaussian Splatting (3D-GS).

- **[U-KAN Makes Strong Backbone for Medical Image Segmentation and Generation](https://ojs.aaai.org/index.php/AAAI/article/view/32491)** — *AAAI 2025*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** U-Net has become a cornerstone in various visual applications such as image segmentation and diffusion probability models.

- **[DepthCrafter: Generating Consistent Long Depth Sequences for Open-world Videos](https://openaccess.thecvf.com/content/CVPR2025/html/Hu_DepthCrafter_Generating_Consistent_Long_Depth_Sequences_for_Open-world_Videos_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Estimating video depth in open-world scenarios is challenging due to the diversity of videos in appearance, content motion, camera movement, and length.

- **[Identity-Preserving Text-to-Video Generation by Frequency Decomposition](https://openaccess.thecvf.com/content/CVPR2025/html/Yuan_Identity-Preserving_Text-to-Video_Generation_by_Frequency_Decomposition_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Identity-preserving text-to-video (IPT2V) generation aims to create high-fidelity videos with consistent human identity.

- **[MoSca: Dynamic Gaussian Fusion from Casual Videos via 4D Motion Scaffolds](https://openaccess.thecvf.com/content/CVPR2025/html/Lei_MoSca_Dynamic_Gaussian_Fusion_from_Casual_Videos_via_4D_Motion_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We introduce 4D Motion Scaffolds (MoSca), a modern 4D reconstruction system designed to reconstruct and synthesize novel views of dynamic scenes from monocular videos captured casually in the wild.

- **[Structured 3D Latents for Scalable and Versatile 3D Generation](https://openaccess.thecvf.com/content/CVPR2025/html/Xiang_Structured_3D_Latents_for_Scalable_and_Versatile_3D_Generation_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We introduce a novel 3D generation method for versatile and high-quality 3D asset creation.The cornerstone is a unified Structured LATent (SLAT) representation which allows decoding to different output formats, such as Radiance Fields, 3D Gaussians, and meshes.

- **[UniReal: Universal Image Generation and Editing via Learning Real-world Dynamics](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_UniReal_Universal_Image_Generation_and_Editing_via_Learning_Real-world_Dynamics_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We introduce UniReal, a unified framework designed to address various image generation and editing tasks.

- **[Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis](https://openaccess.thecvf.com/content/CVPR2025/html/Fu_Video-MME_The_First-Ever_Comprehensive_Evaluation_Benchmark_of_Multi-modal_LLMs_in_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** In the quest for artificial general intelligence, Multi-modal Large Language Models (MLLMs) have emerged as a focal point in recent advancements.

- **[WonderWorld: Interactive 3D Scene Generation from a Single Image](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_WonderWorld_Interactive_3D_Scene_Generation_from_a_Single_Image_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We present WonderWorld, a novel framework for interactive 3D scene generation that enables users to interactively specify scene contents and layout and see the created scenes in low latency.

- **["Principal Components" Enable A New Language of Images](https://openaccess.thecvf.com/content/ICCV2025/html/Wen_Principal_Components_Enable_A_New_Language_of_Images_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We introduce a novel visual tokenization framework that embeds a provable PCA-like structure into the latent token space.

- **[2D Gaussian Splatting-based Sparse-view Transparent Object Depth Reconstruction via Physics Simulation for Scene Update](https://openaccess.thecvf.com/content/ICCV2025/html/Kim_2D_Gaussian_Splatting-based_Sparse-view_Transparent_Object_Depth_Reconstruction_via_Physics_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Understanding the 3D geometry of transparent objects from RGB images is challenging due to their inherent physical properties, such as reflection and refraction.

- **[2HandedAfforder: Learning Precise Actionable Bimanual Affordances from Human Videos](https://openaccess.thecvf.com/content/ICCV2025/html/Heidinger_2HandedAfforder_Learning_Precise_Actionable_Bimanual_Affordances_from_Human_Videos_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** When interacting with objects, humans effectively reason about which regions of objects are viable for an intended action, i.e., the affordance regions of the object.

- **[3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Vision-language navigation (VLN) requires an agent to traverse complex 3D environments based on natural language instructions, necessitating a thorough scene understanding.

- **[3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial Camouflage Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Lou_3D_Gaussian_Splatting_Driven_Multi-View_Robust_Physical_Adversarial_Camouflage_Generation_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Physical adversarial attack methods expose the vulnerabilities of deep neural networks and pose a significant threat to safety-critical scenarios such as autonomous driving.

- **[3D Mesh Editing using Masked LRMs](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_3D_Mesh_Editing_using_Masked_LRMs_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We present a novel approach to mesh shape editing, building on recent progress in 3D reconstruction from multi-view images.

- **[3D Test-time Adaptation via Graph Spectral Driven Point Shift](https://openaccess.thecvf.com/content/ICCV2025/html/Wei_3D_Test-time_Adaptation_via_Graph_Spectral_Driven_Point_Shift_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** While test-time adaptation (TTA) methods effectively address domain shifts by dynamically adapting pre-trained models to target domain data during online inference, their application to 3D point clouds is hindered by their irregular and unordered structure.

- **[3D-MOOD: Lifting 2D to 3D for Monocular Open-Set Object Detection](https://openaccess.thecvf.com/content/ICCV2025/html/Yang_3D-MOOD_Lifting_2D_to_3D_for_Monocular_Open-Set_Object_Detection_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Monocular 3D object detection is valuable for various applications such as robotics and AR/VR.

- **[SAM 2: Segment Anything in Images and Videos](https://iclr.cc/virtual/2025/poster/30219)** — *ICLR 2025 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We present Segment Anything Model 2 (SAM 2), a foundation model towards solving promptable visual segmentation in images and videos.

- **[Stop the Nonconsensual Use of Nude Images in Research](https://openreview.net/forum?id=Ev5xwr3vWh)** — *NeurIPS 2025 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** In order to train, test, and evaluate nudity detection models, machine learning researchers typically rely on nude images scraped from the Internet.

- **[T2I-Adapter: Learning Adapters to Dig Out More Controllable Ability for Text-to-Image Diffusion Models](https://ojs.aaai.org/index.php/AAAI/article/view/28226)** — *AAAI 2024*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** The incredible generative ability of large-scale text-to-image (T2I) models has demonstrated strong power of learning complex structures and meaningful semantics.

- **[Learning to Manipulate Anywhere: A Visual Generalizable Framework For Reinforcement Learning](https://openreview.net/forum?id=jart4nhCQr)** — *CoRL 2024 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Can we endow visuomotor robots with generalization capabilities to operate in diverse open-world scenarios?

- **[Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding](https://openaccess.thecvf.com/content/CVPR2024/html/Jin_Chat-UniVi_Unified_Visual_Representation_Empowers_Large_Language_Models_with_Image_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Large language models have demonstrated impressive universal capabilities across a wide range of open-ended tasks and have extended their utility to encompass multimodal conversations.

- **[Gaussian Splatting SLAM](https://openaccess.thecvf.com/content/CVPR2024/html/Matsuki_Gaussian_Splatting_SLAM_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We present the first application of 3D Gaussian Splatting in monocular SLAM the most fundamental but the hardest setup for Visual SLAM.

- **[GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting](https://openaccess.thecvf.com/content/CVPR2024/html/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** In this paper we introduce GS-SLAM that first utilizes 3D Gaussian representation in the Simultaneous Localization and Mapping (SLAM) system.

- **[Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding](https://openaccess.thecvf.com/content/CVPR2024/html/Leng_Mitigating_Object_Hallucinations_in_Large_Vision-Language_Models_through_Visual_Contrastive_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Large Vision-Language Models (LVLMs) have advanced considerably intertwining visual recognition and language understanding to generate content that is not only coherent but also contextually attuned.

- **[Monkey: Image Resolution and Text Label Are Important Things for Large Multi-modal Models](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Monkey_Image_Resolution_and_Text_Label_Are_Important_Things_for_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Large Multimodal Models (LMMs) have shown promise in vision-language tasks but struggle with high-resolution input and detailed scene understanding.

- **[MVBench: A Comprehensive Multi-modal Video Understanding Benchmark](https://openaccess.thecvf.com/content/CVPR2024/html/Li_MVBench_A_Comprehensive_Multi-modal_Video_Understanding_Benchmark_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** With the rapid development of Multi-modal Large Language Models (MLLMs) a number of diagnostic benchmarks have recently emerged to evaluate the comprehension capabilities of these models.

- **[Scaffold-GS: Structured 3D Gaussians for View-Adaptive Rendering](https://openaccess.thecvf.com/content/CVPR2024/html/Lu_Scaffold-GS_Structured_3D_Gaussians_for_View-Adaptive_Rendering_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Summary unavailable in the public source record.

- **[VBench: Comprehensive Benchmark Suite for Video Generative Models](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_VBench_Comprehensive_Benchmark_Suite_for_Video_Generative_Models_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Video generation has witnessed significant advancements yet evaluating these models remains a challenge.

- **[Wonder3D: Single Image to 3D using Cross-Domain Diffusion](https://openaccess.thecvf.com/content/CVPR2024/html/Long_Wonder3D_Single_Image_to_3D_using_Cross-Domain_Diffusion_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** In this work we introduce Wonder3D a novel method for generating high-fidelity textured meshes from single-view images with remarkable efficiency.

- **[An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10478_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "In this study, we identify the inefficient attention phenomena in Large Vision-Language Models (LVLMs), notably within prominent models like LLaVA-1.5, QwenVL-Chat, and Video-LLaVA.

- **[DriveLM: Driving with Graph Visual Question Answering](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6870_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "We study how vision-language models (VLMs) trained on web-scale data can be integrated into end-to-end driving systems to boost generalization and enable interactivity with human users.

- **[DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6298_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "Animating a still image offers an engaging visual experience.

- **[Grounding Image Matching in 3D with MASt3R](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9080_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "Image Matching is a core component of all best-performing algorithms and pipelines in 3D vision.

- **[LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/465_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "3D content creation has achieved significant progress in terms of both quality and speed.

- **[MotionDirector: Motion Customization of Text-to-Video Diffusion Models](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7327_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "Large-scale pre-trained diffusion models have exhibited remarkable capabilities in diverse video generations.

- **[MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3187_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "We introduce , an efficient model that, given sparse multi-view images as input, predicts clean feed-forward 3D Gaussians.

- **[SV3D: Novel Multi-view Synthesis and 3D Generation from a Single Image using Latent Video Diffusion](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/150_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** "We present Stable Video 3D (SV3D) — a latent video diffusion model for high-resolution, image-to-multi-view generation of orbital videos around a 3D object.

- **[An image speaks a thousand words, but can everyone listen? On image transcreation for cultural relevance](https://aclanthology.org/2024.emnlp-main.573/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Given the rise of multimedia content, human translators increasingly focus on culturally adapting not only words but also other modalities such as images to convey the same meaning.

- **[Threshold-driven Pruning with Segmented Maximum Term Weights for Approximate Cluster-based Sparse Retrieval](https://aclanthology.org/2024.emnlp-main.1101/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** This paper revisits dynamic pruning through rank score thresholding in cluster-based sparse retrieval to skip the index partially at cluster and document levels during inference.

- **[Words Worth a Thousand Pictures: Measuring and Understanding Perceptual Variability in Text-to-Image Generation](https://aclanthology.org/2024.emnlp-main.311/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Diffusion models are the state of the art in text-to-image generation, but their perceptual variability remains understudied.

- **[DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation](https://iclr.cc/virtual/2024/poster/18512)** — *ICLR 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Recent advances in 3D content creation mostly leverage optimization-based 3D generation via score distillation sampling (SDS).

- **[LRM: Large Reconstruction Model for Single Image to 3D](https://iclr.cc/virtual/2024/poster/17635)** — *ICLR 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We propose the first Large Reconstruction Model (LRM) that predicts the 3D model of an object from a single input image within just 5 seconds.

- **[Real3D-Portrait: One-shot Realistic 3D Talking Portrait Synthesis](https://iclr.cc/virtual/2024/poster/19369)** — *ICLR 2024 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** One-shot 3D talking portrait generation aims to reconstruct a 3D avatar from an unseen image, and then animate it with a reference video or audio to generate a talking portrait video.

- **[SyncDreamer: Generating Multiview-consistent Images from a Single-view Image](https://iclr.cc/virtual/2024/poster/18828)** — *ICLR 2024 · Spotlight*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** In this paper, we present a novel diffusion model called SyncDreamer that generates multiview-consistent images from a single-view image.

- **[DoRA: Weight-Decomposed Low-Rank Adaptation](https://proceedings.mlr.press/v235/liu24bn.html)** — *ICML 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Among the widely used parameter-efficient fine-tuning (PEFT) methods, LoRA and its variants have gained considerable popularity because of avoiding additional inference costs.

- **[Genie: Generative Interactive Environments](https://proceedings.mlr.press/v235/bruce24a.html)** — *ICML 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** We introduce Genie, the first *generative interactive environment* trained in an unsupervised manner from unlabelled Internet videos.

- **[Scaling Rectified Flow Transformers for High-Resolution Image Synthesis](https://proceedings.mlr.press/v235/esser24a.html)** — *ICML 2024 · Oral*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Diffusion models create data from noise by inverting the forward paths of data towards noise and have emerged as a powerful generative modeling technique for high-dimensional, perceptual data such as images and videos.

- **[ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://ieeexplore.ieee.org/document/10610243/)** — *ICRA 2024 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** For robots to perform a wide variety of tasks, they require a 3D representation of the world that is semantically rich, yet compact and efficient for task-driven perception and planning.

- **[ProtoPFormer: Concentrating on Prototypical Parts in Vision Transformers for Interpretable Image Recognition](https://www.ijcai.org/proceedings/2024/168)** — *IJCAI 2024 · Poster*
  - **Topic:** Vision, video, and 3D graphics
  - **Summary:** Prototypical part network (ProtoPNet) and its variants have drawn wide attention and been applied to various tasks due to their inherent self-explanatory property.

## Speech and Audio

- **[Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition](https://openreview.net/forum?id=sSbEEHNEsL)** — *ICLR 2026 · Poster*
  - **Topic:** Speech, audio, and music
  - **Summary:** Unified Speech Recognition (USR) has emerged as a semi-supervised framework for training a single model for audio, visual, and audiovisual speech recognition, achieving state-of-the-art results on in-distribution benchmarks.

- **[HateDay: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter](https://aclanthology.org/2025.acl-long.115/)** — *ACL 2025 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** To address the global challenge of online hate speech, prior research has developed detection models to flag such content on social media.

- **[IndicSynth: A Large-Scale Multilingual Synthetic Speech Dataset for Low-Resource Indian Languages](https://aclanthology.org/2025.acl-long.1070/)** — *ACL 2025 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** Recent advances in synthetic speech generation technology have facilitated the generation of high-quality synthetic (fake) speech that emulates human voices.

- **[Toward Automatic Discovery of a Canine Phonetic Alphabet](https://aclanthology.org/2025.acl-long.451/)** — *ACL 2025 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** Dogs communicate intelligently but little is known about the phonetic properties of their vocalization communication.

- **[AudioGPT: Understanding and Generating Speech, Music, Sound, and Talking Head](https://ojs.aaai.org/index.php/AAAI/article/view/30570)** — *AAAI 2024*
  - **Topic:** Speech, audio, and music
  - **Summary:** Large language models (LLMs) have exhibited remarkable capabilities across a variety of domains and tasks, challenging our understanding of learning and cognition.

- **[Language Complexity and Speech Recognition Accuracy: Orthographic Complexity Hurts, Phonological Complexity Doesn’t](https://aclanthology.org/2024.acl-long.827/)** — *ACL 2024 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** We investigate what linguistic factors affect the performance of Automatic Speech Recognition (ASR) models.

- **[Let’s Go Real Talk: Spoken Dialogue Model for Face-to-Face Conversation](https://aclanthology.org/2024.acl-long.860/)** — *ACL 2024 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** In this paper, we introduce a novel Face-to-Face spoken dialogue model.

- **[Speech Translation with Speech Foundation Models and Large Language Models: What is There and What is Missing?](https://aclanthology.org/2024.acl-long.789/)** — *ACL 2024 · Long*
  - **Topic:** Speech, audio, and music
  - **Summary:** The field of natural language processing (NLP) has recently witnessed a transformative shift with the emergence of foundation models, particularly Large Language Models (LLMs) that have revolutionized text-based NLP.

- **[Towards Robust Speech Representation Learning for Thousands of Languages](https://aclanthology.org/2024.emnlp-main.570/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Speech, audio, and music
  - **Summary:** Self-supervised learning (SSL) has helped extend speech technologies to more languages by reducing the need for labeled data.

- **[Twists, Humps, and Pebbles: Multilingual Speech Recognition Models Exhibit Gender Performance Gaps](https://aclanthology.org/2024.emnlp-main.1188/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Speech, audio, and music
  - **Summary:** Current automatic speech recognition (ASR) models are designed to be used across many languages and tasks without substantial changes.

- **[NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models](https://proceedings.mlr.press/v235/ju24b.html)** — *ICML 2024 · Oral*
  - **Topic:** Speech, audio, and music
  - **Summary:** While recent large-scale text-to-speech (TTS) models have achieved significant progress, they still fall shorts in speech quality, similarity, and prosody.

- **[GTSinger: A Global Multi-Technique Singing Corpus with Realistic Music Scores for All Singing Tasks](https://neurips.cc/virtual/2024/poster/97428)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Speech, audio, and music
  - **Summary:** The scarcity of high-quality and multi-task singing datasets significantly hinders the development of diverse controllable and personalized singing tasks, as existing singing datasets suffer from low quality, limited diversity of languages and singers, absence of...

## Multimodal Learning

- **[Generative Universal Verifier as Multimodal Meta-Reasoner](https://openreview.net/forum?id=DM0Y0oL33T)** — *ICLR 2026 · Oral*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** We introduce *Generative Universal Verifier*, a novel concept and plugin designed for next-generation multimodal reasoning in vision-language models and unified multimodal models, providing the fundamental capability of reflection and refinement on visual outcomes during the...

- **[$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](https://openreview.net/forum?id=vlhoswksBO)** — *CoRL 2025 · Oral*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab.

- **[Multimodal Autoregressive Pre-training of Large Vision Encoders](https://openaccess.thecvf.com/content/CVPR2025/html/Fini_Multimodal_Autoregressive_Pre-training_of_Large_Vision_Encoders_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** We introduce a novel method for pre-training of large-scale vision encoders.

- **[2.5 Years in Class: A Multimodal Textbook for Vision-Language Pretraining](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_2.5_Years_in_Class_A_Multimodal_Textbook_for_Vision-Language_Pretraining_ICCV_2025_paper.html)** — *ICCV 2025 · Poster*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** Compared to image-text pair data, interleaved corpora enable Vision-Language Models (VLMs) to understand the world more naturally like humans.

- **[LMMs-Eval: Reality Check on the Evaluation of Large Multimodal Models](https://aclanthology.org/2025.findings-naacl.51/)** — *NAACL 2025 · Findings*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** The advances of large foundation models necessitate wide-coverage, low-cost, and zero-contamination benchmarks.

- **[CaMML: Context-Aware Multimodal Learner for Large Models](https://aclanthology.org/2024.acl-long.223/)** — *ACL 2024 · Long*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** In this work, we introduce Context-Aware MultiModal Learner (CaMML), for tuning large multimodal models (LMMs).

- **[MMToM-QA: Multimodal Theory of Mind Question Answering](https://aclanthology.org/2024.acl-long.851/)** — *ACL 2024 · Long*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** Theory of Mind (ToM), the ability to understand people’s mental states, is an essential ingredient for developing machines with human-level social intelligence.

- **[OpenVLA: An Open-Source Vision-Language-Action Model](https://openreview.net/forum?id=ZMnD6QZAE6)** — *CoRL 2024 · Poster*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** Large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new behaviors from scratch, we can fine-tune such vision-language-action (VLA)...

- **[mPLUG-Owl2: Revolutionizing Multi-modal Large Language Model with Modality Collaboration](https://openaccess.thecvf.com/content/CVPR2024/html/Ye_mPLUG-Owl2_Revolutionizing_Multi-modal_Large_Language_Model_with_Modality_Collaboration_CVPR_2024_paper.html)** — *CVPR 2024 · Highlight*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** Multi-modal Large Language Models (MLLMs) have demonstrated impressive instruction abilities across various open-ended tasks.

- **[MMBENCH: Is Your Multi-Modal Model an All-around Player?](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/959_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Multimodal learning and fusion
  - **Summary:** "Large vision-language models (VLMs) have recently achieved remarkable progress, exhibiting impressive multimodal perception and reasoning abilities.

## Robotics and Embodied AI

- **[Embodied Navigation Foundation Model](https://openreview.net/forum?id=kkBOIsrCXh)** — *ICLR 2026 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We propose a cross-task and cross-embodiment navigation foundation model.

- **[Language Prompt for Autonomous Driving](https://ojs.aaai.org/index.php/AAAI/article/view/32902)** — *AAAI 2025*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** A new trend in the computer vision community is to capture objects of interest following flexible human command represented by a natural language prompt.

- **[AirExo-2: Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons](https://openreview.net/forum?id=ksOrtEgIC0)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Scaling up robotic imitation learning for real-world applications requires efficient and scalable demonstration collection methods.

- **[ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes](https://openreview.net/forum?id=4XKKUifQ9c)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions.

- **[DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration](https://openreview.net/forum?id=Tl7girqoLi)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Imitation learning has shown great promise in robotic manipulation, but the policy’s execution is often unsatisfactorily slow due to commonly tardy demonstrations collected by human operators.

- **[DexSkin: High-Coverage Conformable Robotic Skin for Learning Contact-Rich Manipulation](https://openreview.net/forum?id=CNPCSuwxJw)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Human skin provides a rich tactile sensing stream, localizing intentional and unintentional contact events over a large and contoured region.

- **[DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation](https://openreview.net/forum?id=XrgRvBklWu)** — *CoRL 2025 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We present DexUMI - a data collection and policy learning framework that uses the human hand as the natural interface to transfer dexterous manipulation skills to various robot hands.

- **[Emerging Risks from Embodied AI Require Urgent Policy Action](https://openreview.net/forum?id=fXiPp3qvrW)** — *NeurIPS 2025 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** The field of embodied AI (EAI) is rapidly advancing.

- **[A Language Agent for Autonomous Driving](https://openreview.net/forum?id=UPE6WYE8vg)** — *COLM 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Human-level driving is an ultimate goal of autonomous driving.

- **[D$^3$RoMa: Disparity Diffusion-based Depth Sensing for Material-Agnostic Robotic Manipulation](https://openreview.net/forum?id=7E3JAys1xO)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Depth sensing is an important problem for 3D vision-based robotics.

- **[HumanPlus: Humanoid Shadowing and Imitation from Humans](https://openreview.net/forum?id=WnSl42M9Z4)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** One of the key arguments for building robots that have similar form factors to human beings is that we can leverage the massive human data for training.Yet, doing so has remained challenging in practice due to the complexities in humanoid perception and control, lingering...

- **[Learning to Open and Traverse Doors with a Legged Manipulator](https://openreview.net/forum?id=VoC3wF6fbh)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Using doors is a longstanding challenge in robotics and is of significant practical interest in giving robots greater access to human-centric spaces.

- **[Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild](https://openreview.net/forum?id=vBj5oC60Lk)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Recent works have proposed a number of general-purpose robotic foundation models that can control a variety of robotic platforms to perform a range of different tasks, including in the domains of navigation and manipulation.

- **[OCCAM: Online Continuous Controller Adaptation with Meta-Learned Models](https://openreview.net/forum?id=xeFKtSXPMd)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Control tuning and adaptation present a significant challenge to the usage of robots in diverse environments.

- **[Play to the Score: Stage-Guided Dynamic Multi-Sensory Fusion for Robotic Manipulation](https://openreview.net/forum?id=N5IS6DzBmL)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Humans possess a remarkable talent for flexibly alternating to different senses when interacting with the environment.

- **[Reinforcement Learning with Foundation Priors: Let Embodied Agent Efficiently Learn on Its Own](https://openreview.net/forum?id=dsxmR6lYlg)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Reinforcement learning (RL) is a promising approach for solving robotic manipulation tasks.

- **[Robotic Control via Embodied Chain-of-Thought Reasoning](https://openreview.net/forum?id=S70MgnIA0v)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** A key limitation of learned robot control policies is their inability to generalize outside their training data.

- **[Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation](https://openreview.net/forum?id=AuJnXGq3AL)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Modern machine learning systems rely on large datasets to attain broad generalization, and this often poses a challenge in robotic learning, where each robotic platform and task might have only a small dataset.

- **[Visual Whole-Body Control for Legged Loco-Manipulation](https://openreview.net/forum?id=cT2N3p1AcE)** — *CoRL 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We study the problem of mobile manipulation using legged robots equipped with an arm, namely legged loco-manipulation.

- **[Thin-Shell Object Manipulations With Differentiable Physics Simulations](https://iclr.cc/virtual/2024/poster/18881)** — *ICLR 2024 · Spotlight*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** In this work, we aim to teach robots to manipulate various thin-shell materials.

- **[Extreme Parkour with Legged Robots](https://ieeexplore.ieee.org/document/10610200/)** — *ICRA 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Humans can perform parkour by traversing obstacles in a highly dynamic fashion requiring precise eye-muscle coordination and movement.

- **[NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://ieeexplore.ieee.org/document/10610665/)** — *ICRA 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Robotic learning for navigation in unfamiliar environments needs to provide policies for both task-oriented navigation (i.e., reaching a goal that the robot has located), and task-agnostic exploration (i.e., searching for a goal in a novel setting).

- **[Open X-Embodiment: Robotic Learning Datasets and RT-X Models : Open X-Embodiment Collaboration0](https://ieeexplore.ieee.org/document/10611477/)** — *ICRA 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Large, high-capacity models trained on diverse datasets have shown remarkable successes on efficiently tackling downstream applications.

- **[Physically Grounded Vision-Language Models for Robotic Manipulation](https://ieeexplore.ieee.org/document/10610090/)** — *ICRA 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Recent advances in vision-language models (VLMs) have led to improved performance on tasks such as visual question answering and image captioning.

- **[RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking](https://ieeexplore.ieee.org/document/10611293/)** — *ICRA 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** The grand aim of having a single robot that can manipulate arbitrary objects in diverse settings is at odds with the paucity of robotics datasets.

- **[CoPa: General Robotic Manipulation through Spatial Constraints of Parts with Foundation Models](https://ieeexplore.ieee.org/document/10801352/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Foundation models pre-trained on web-scale data are shown to encapsulate extensive world knowledge beneficial for robotic manipulation in the form of task planning.

- **[Extended Tree Search for Robot Task and Motion Planning](https://ieeexplore.ieee.org/document/10802552/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Integrated Task and Motion Planning (TAMP) offers opportunities for achieving generalized autonomy in robots but also poses challenges.

- **[GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators](https://ieeexplore.ieee.org/document/10801581/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Humans can teleoperate robots to accomplish complex manipulation tasks.

- **[Learning Agile Locomotion on Risky Terrains](https://ieeexplore.ieee.org/document/10801909/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Quadruped robots have shown remarkable mobility on various terrains through reinforcement learning.

- **[Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](https://ieeexplore.ieee.org/document/10801984/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We present Human to Humanoid (H2O), a reinforcement learning (RL) based framework that enables real-time whole-body teleoperation of a full-sized humanoid robot with only an RGB camera.

- **[Whole-body Humanoid Robot Locomotion with Human Reference](https://ieeexplore.ieee.org/document/10801451/)** — *IROS 2024 · Poster*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** Recently, humanoid robots have made significant advances in their ability to perform challenging tasks due to the deployment of Reinforcement Learning (RL), however, the inherent complexity of humanoid robots, including the difficulty of designing complicated reward functions...

- **[Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making](https://neurips.cc/virtual/2024/poster/97552)** — *NeurIPS 2024 · Oral*
  - **Topic:** Robotics, control, and embodied learning
  - **Summary:** We aim to evaluate Large Language Models (LLMs) for embodied decision making.

## Reinforcement Learning and Decision-Making

- **[Learning While Scheduling Jobs under Context-Dependent Service Rates: An Anytime Rate-Optimal Algorithm](https://openreview.net/forum?id=ZZ2jyq4qFC)** — *ICLR 2027 · Under review*
  - **Topic:** Contextual bandits and job scheduling
  - **Summary:** Studies online learning and job scheduling when service rates are unknown. It proposes WISE, an anytime algorithm with queue-regret guarantees that does not require a known time horizon.

- **[Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data](https://openreview.net/forum?id=oBXfPyi47m)** — *ICLR 2026 · Poster*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** Leveraging offline data is a promising way to improve the sample efficiency of online reinforcement learning (RL).

- **[A Causal Decomposition Approach for Fair Contextual Multi-Armed Bandits](https://openreview.net/forum?id=kHEL0GD175)** — *ICML 2026 · Spotlight*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** Counterfactual reasoning is one of the fundamental facets of human cognition, involved in various tasks such as explanation, credit assignment, blame, and responsibility.

- **[Adaptive Stepsizes for Eligibility Traces in Deep Reinforcement Learning](https://neurips.cc/virtual/2026/poster/153394)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** Modern deep reinforcement learning algorithms often store past sensory observations in a buffer for later replay and learning.

- **[Corruption Robust Offline Reinforcement Learning with Human Feedback](https://openreview.net/forum?id=AM5VTtoexY)** — *AISTATS 2025 · Oral*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** We study data corruption robustness for reinforcement learning with human feedback (RLHF) in an offline setting.

- **[Distributional Counterfactual Explanations With Optimal Transport](https://openreview.net/forum?id=cGnnwEm2gu)** — *AISTATS 2025 · Oral*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** Counterfactual explanations (CE) are the de facto method for providing insights into black-box decision-making models by identifying alternative inputs that lead to different outcomes.

- **[Understanding R1-Zero-Like Training: A Critical Perspective](https://openreview.net/forum?id=5PAF7PAY2Y)** — *COLM 2025 · Poster*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** DeepSeek-R1-Zero has shown that reinforcement learning (RL) at scale can directly enhance the reasoning capabilities of LLMs without supervised fine-tuning.

- **[FACET: Force-Adaptive Control via Impedance Reference Tracking for Legged Robots](https://openreview.net/forum?id=EcOGafgvuC)** — *CoRL 2025 · Oral*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** Reinforcement learning (RL) has made significant strides in legged robot control, enabling locomotion across diverse terrains and complex loco-manipulation capabilities.

- **[Generative Flow Networks as Entropy-Regularized RL](https://proceedings.mlr.press/v238/tiapkin24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** The recently proposed generative flow networks (GFlowNets) are a method of training a policy to sample compositional discrete objects with probabilities proportional to a given reward via a sequence of actions.

- **[Privileged Sensing Scaffolds Reinforcement Learning](https://iclr.cc/virtual/2024/poster/19090)** — *ICLR 2024 · Spotlight*
  - **Topic:** Reinforcement learning, bandits, and decisions
  - **Summary:** We need to look at our shoelaces as we first learn to tie them but having mastered this skill, can do it from touch alone.

## Generative Models and World Models

- **[WBench: A Comprehensive Multi-turn Benchmark for Interactive World Model Evaluation](https://openreview.net/forum?id=PQdqz0vaG5)** — *ICLR 2027 · Under review*
  - **Topic:** Interactive world-model evaluation
  - **Summary:** Introduces a benchmark with 289 cases and 1,058 interaction turns for evaluating video quality, instruction following, consistency, and physical plausibility in interactive world models.

- **[La-Proteina: Atomistic Protein Generation via Partially Latent Flow Matching](https://openreview.net/forum?id=RDerF20JYT)** — *ICLR 2026 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** We introduce a partially latent flow matching model for atomistic protein design.

- **[A Kinetic Energy Perspective of Flow Matching](https://openreview.net/forum?id=d6IyHrX48y)** — *ICML 2026 · Spotlight*
  - **Topic:** Generative modeling and world models
  - **Summary:** Flow-based generative models can be viewed through a physics lens: sampling transports a particle from noise to data by integrating a learned velocity field, and each sample corresponds to a trajectory with its own dynamical effort.

- **[Fast Controlled Generation from Language Models with Adaptive Weighted Rejection Sampling](https://openreview.net/forum?id=3BmPSFAdq3)** — *COLM 2025 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** The dominant approach to generating from language models subject to some constraint is locally constrained decoding (LCD), incrementally sampling tokens at each time step such that the constraint is never violated.

- **[Belief-Conditioned One-Step Diffusion: Real-Time Trajectory Planning with Just-Enough Sensing](https://openreview.net/forum?id=t2asRJv2SD)** — *CoRL 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Robots equipped with rich sensor suites can localize reliably in partially-observable environments---but powering every sensor continuously is wasteful and often infeasible.

- **[Cross-Sensor Touch Generation](https://openreview.net/forum?id=oGcC8nMOit)** — *CoRL 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Today's visuo-tactile sensors come in many shapes and sizes, making it challenging to develop general-purpose tactile representations.

- **[3DTopia-XL: Scaling High-quality 3D Asset Generation via Primitive Diffusion](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_3DTopia-XL_Scaling_High-quality_3D_Asset_Generation_via_Primitive_Diffusion_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Generative modeling and world models
  - **Summary:** The increasing demand for high-quality 3D assets across various industries necessitates efficient and automated 3D content creation.

- **[DiffusionDrive: Truncated Diffusion Model for End-to-End Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_DiffusionDrive_Truncated_Diffusion_Model_for_End-to-End_Autonomous_Driving_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Generative modeling and world models
  - **Summary:** Recently, the diffusion model has emerged as a powerful generative technique for robotic policy learning, capable of modeling multi-mode action distributions.

- **[Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think](https://iclr.cc/virtual/2025/poster/30467)** — *ICLR 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Recent studies have shown that the denoising process in (generative) diffusion models can induce meaningful (discriminative) representations inside the model, though the quality of these representations still lags behind those learned through recent self-supervised learning...

- **[Scaling In-the-Wild Training for Diffusion-based Illumination Harmonization and Editing by Imposing Consistent Light Transport](https://iclr.cc/virtual/2025/poster/28002)** — *ICLR 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Diffusion-based image generators are becoming unique methods for illumination harmonization and editing.

- **[Simplifying, Stabilizing and Scaling Continuous-time Consistency Models](https://iclr.cc/virtual/2025/poster/29963)** — *ICLR 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Consistency models (CMs) are a powerful class of diffusion-based generative models optimized for fast sampling.

- **[NeurIPS should lead scientific consensus on AI policy](https://openreview.net/forum?id=a4oXTW1PW2)** — *NeurIPS 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Designing wise AI policy is a grand challenge for society.

- **[Real-Time Hyper-Personalized Generative AI Should Be Regulated to Prevent the Rise of "Digital Heroin"](https://openreview.net/forum?id=1IpHkK5Q8F)** — *NeurIPS 2025 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** This position paper argues that real-time generative AI has the potential to become the next wave of addictive digital media, creating a new class of digital content akin to ``digital heroin'' with severe implications for mental health and youth development.

- **[Deciphering Oracle Bone Language with Diffusion Models](https://aclanthology.org/2024.acl-long.831/)** — *ACL 2024 · Long*
  - **Topic:** Generative modeling and world models
  - **Summary:** Originating from China’s Shang Dynasty approximately 3,000 years ago, the Oracle Bone Script (OBS) is a cornerstone in the annals of linguistic history, predating many established writing systems.

- **[Adaptivity of Diffusion Models to Manifold Structures](https://proceedings.mlr.press/v238/tang24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** Empirical studies have demonstrated the effectiveness of (score-based) diffusion models in generating high-dimensional data, such as texts and images, which typically exhibit a low-dimensional manifold nature.

- **[Generating and Imputing Tabular Data via Diffusion and Flow-based Gradient-Boosted Trees](https://proceedings.mlr.press/v238/jolicoeur-martineau24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** Tabular data is hard to acquire and is subject to missing values.

- **[Simulation-Free Schrödinger Bridges via Score and Flow Matching](https://proceedings.mlr.press/v238/tong24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** We present simulation-free score and flow matching ([SF]$^2$M), a simulation-free objective for inferring stochastic dynamics given unpaired samples drawn from arbitrary source and target distributions.

- **[Theoretically Grounded Loss Functions and Algorithms for Score-Based Multi-Class Abstention](https://proceedings.mlr.press/v238/mao24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** Learning with abstention is a key scenario where the learner can abstain from making a prediction at some cost.

- **[Does Collaborative Human–LM Dialogue Generation Help Information Extraction from Human–Human Dialogues?](https://openreview.net/forum?id=uILyEJGKWw)** — *COLM 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** The capabilities of pretrained language models (LMs) have opened opportunities to explore new application areas, but applications involving human-human interaction are limited by the fact that most data is protected from public release for privacy reasons.

- **[EquiGraspFlow: SE(3)-Equivariant 6-DoF Grasp Pose Generative Flows](https://openreview.net/forum?id=5lSkn5v4LK)** — *CoRL 2024 · Poster*
  - **Topic:** Generative modeling and world models
  - **Summary:** Traditional methods for synthesizing 6-DoF grasp poses from 3D observations often rely on geometric heuristics, resulting in poor generalizability, limited grasp options, and higher failure rates.

- **[Adversarial Diffusion Distillation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/11557_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** "We introduce Adversarial Diffusion Distillation (ADD), a novel training approach that efficiently samples large-scale foundational image diffusion models in just 1–4 steps while maintaining high image quality.

- **[CoGen: Learning from Feedback with Coupled Comprehension and Generation](https://aclanthology.org/2024.emnlp-main.721/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Generative modeling and world models
  - **Summary:** Systems with both language comprehension and generation capabilities can benefit from the tight connection between the two.

- **[Generalization in diffusion models arises from geometry-adaptive harmonic representations](https://iclr.cc/virtual/2024/poster/19264)** — *ICLR 2024 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Deep neural networks (DNNs) trained for image denoising are able to generate high-quality samples with score-based reverse diffusion algorithms.

- **[Monte Carlo guided Denoising Diffusion models for Bayesian linear inverse problems.](https://iclr.cc/virtual/2024/poster/17864)** — *ICLR 2024 · Oral*
  - **Topic:** Generative modeling and world models
  - **Summary:** Ill-posed linear inverse problems arise frequently in various applications, from computational photography to medical imaging.

- **[SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis](https://iclr.cc/virtual/2024/poster/18250)** — *ICLR 2024 · Spotlight*
  - **Topic:** Generative modeling and world models
  - **Summary:** We present Stable Diffusion XL (SDXL), a latent diffusion model for text-to-image synthesis.

- **[Probablistic Emulation of a Global Climate Model with Spherical DYffusion](https://neurips.cc/virtual/2024/poster/95762)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Generative modeling and world models
  - **Summary:** Data-driven deep learning models are transforming global weather forecasting.

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

- **[A Graph Foundation Model for Unified Clustering](https://neurips.cc/virtual/2026/poster/154668)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Representation learning and clustering
  - **Summary:** Graph clustering is a fundamental task for understanding graph-structured data without labels, yet classical end-to-end methods require retraining on each dataset, limiting their generalization ability.

- **[SatCLIP: Global, General-Purpose Location Embeddings with Satellite Imagery](https://ojs.aaai.org/index.php/AAAI/article/view/32457)** — *AAAI 2025*
  - **Topic:** Representation learning and clustering
  - **Summary:** Geographic information is essential for modeling tasks in fields ranging from ecology to epidemiology.

- **[I0T: Embedding Standardization Method Towards Zero Modality Gap](https://aclanthology.org/2025.acl-long.1319/)** — *ACL 2025 · Long*
  - **Topic:** Representation learning and clustering
  - **Summary:** Contrastive Language-Image Pretraining (CLIP) enables zero-shot inference in downstream tasks such as image-text retrieval and classification.

- **[Divide, Discover, Deploy: Factorized Skill Learning with Symmetry and Style Priors](https://openreview.net/forum?id=Ddb8w8FVV9)** — *CoRL 2025 · Oral*
  - **Topic:** Representation learning and clustering
  - **Summary:** Unsupervised Skill Discovery (USD) allows agents to autonomously learn diverse behaviors without task-specific rewards.

- **[Artificial Kuramoto Oscillatory Neurons](https://iclr.cc/virtual/2025/poster/28387)** — *ICLR 2025 · Oral*
  - **Topic:** Representation learning and clustering
  - **Summary:** It has long been known in both neuroscience and AI that ``binding'' between neurons leads to a form of competitive learning where representations are compressed in order to represent more abstract concepts in deeper layers of the network.

- **[Position: Deep Learning is Not So Mysterious or Different](https://icml.cc/virtual/2025/poster/40178)** — *ICML 2025 · Spotlight*
  - **Topic:** Representation learning and clustering
  - **Summary:** Deep neural networks are often seen as different from other model classes by defying conventional notions of generalization.

- **[Tree-Averaging Algorithms for Ensemble-Based Unsupervised Discontinuous Constituency Parsing](https://aclanthology.org/2024.acl-long.808/)** — *ACL 2024 · Long*
  - **Topic:** Representation learning and clustering
  - **Summary:** We address unsupervised discontinuous constituency parsing, where we observe a high variance in the performance of the only previous model in the literature.

- **[Exploitation of a Latent Mechanism in Graph Contrastive Learning: Representation Scattering](https://neurips.cc/virtual/2024/poster/95196)** — *NeurIPS 2024 · Oral*
  - **Topic:** Representation learning and clustering
  - **Summary:** Graph Contrastive Learning (GCL) has emerged as a powerful approach for generating graph representations without the need for manual annotation.

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
  - **Summary:** We introduce a GPU-friendly algorithm for computing the polar decomposition of a matrix to low accuracy that is optimal in its class.

- **[(Doubly) Exponential Lower Bounds for Follow the Regularized Leader in Potential Games](https://openreview.net/forum?id=l6KZJO7w48)** — *ICML 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** Follow the regularized leader (FTRL) is the premier algorithm for online optimization.

- **[A Fully First-Order Layer for Differentiable Optimization](https://openreview.net/forum?id=jJur8Fq7IK)** — *ICML 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** Differentiable optimization studies how to embed a mathematical program as a differentiable layer in machine learning pipelines.

- **[A Noise Sensitivity Exponent Controls Large Statistical-to-Computational Gaps in Single- and Multi-Index Models](https://openreview.net/forum?id=KHhO311xZ2)** — *ICML 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** Understanding when learning is statistically possible yet computationally hard is a central challenge in high-dimensional statistics.

- **[(Strongly) Replicable Distribution Testers imply High Probability Distribution Testers](https://neurips.cc/virtual/2026/poster/150921)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** We study connections between the sample cost of replicability, which requires an algorithm to produce consistent outputs in different runs, and the sample complexity in the high success probability regime for distribution testing algorithms.

- **[A Near-optimal SQ Lower Bound for Smoothed Agnostic Learning of Boolean Halfspaces](https://neurips.cc/virtual/2026/poster/150497)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** We study the complexity of smoothed agnostic learning of halfspaces on $\{\pm 1\}^n$ under uniform marginals in the model of \citet{KM25} where each input coordinate is independently flipped with probability $\sigma \in (0, {1}/{2})$.

- **[A Theoretical Analysis of Test-Driven Code Generation](https://neurips.cc/virtual/2026/poster/149483)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** Code assistants are increasingly utilized in test-driven software development, yet the theoretical mechanisms behind their environment-interaction strategies remain underexplored.

- **[A Novel Convex Gaussian Min Max Theorem for Repeated Features](https://openreview.net/forum?id=T2FJaLgM4r)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** The Convex Gaussian Min-Max Theorem (CGMT) allows for the study of min-max optimization problems over bilinear Gaussian forms by instead considering an alternative optimization problem whose statistical properties are tied to that of the primary optimization.

- **[A Random Matrix Theory Perspective on the Spectrum of Learned Features and Asymptotic Generalization Capabilities](https://openreview.net/forum?id=3K7rKkU7Ri)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** A key property of neural networks is their capacity of adapting to data during training.

- **[A Robust Kernel Statistical Test of Invariance: Detecting Subtle Asymmetries](https://openreview.net/forum?id=uPgGW67dSX)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** While invariances naturally arise in almost any type of real-world data, no efficient and robust test exists for detecting them in observational data under arbitrarily given group actions.

- **[Additive Model Boosting: New Insights and Path(ologie)s](https://openreview.net/forum?id=p4CHBlYxYj)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** Additive models (AMs) have sparked a lot of interest in machine learning recently, allowing the incorporation of interpretable structures into a wide range of model classes.

- **[Causal discovery in mixed additive noise models](https://openreview.net/forum?id=1YNxc4j8sd)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** Uncovering causal relationships in datasets that include both categorical and continuous variables is a challenging problem.

- **[Cubic regularized subspace Newton for non-convex optimization](https://openreview.net/forum?id=FI1Q9Bi4rH)** — *AISTATS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** This paper addresses the optimization problem of minimizing non-convex continuous functions, a problem highly relevant in high-dimensional machine learning scenarios, particularly those involving over-parameterization.

- **[LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://iclr.cc/virtual/2025/poster/29397)** — *ICLR 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** Low-rank adaption (LoRA) is a widely used parameter-efficient finetuning method for LLM that reduces memory requirements.

- **[Position: Algebra Unveils Deep Learning - An Invitation to Neuroalgebraic Geometry](https://icml.cc/virtual/2025/poster/40106)** — *ICML 2025 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** In this position paper, we promote the study of function spaces parameterized by machine learning models through the lens of algebraic geometry.

- **[Position: Constants are Critical in Regret Bounds for Reinforcement Learning](https://icml.cc/virtual/2025/poster/40179)** — *ICML 2025 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** Mainstream research in theoretical RL is currently focused on designing online learning algorithms with regret bounds that match the corresponding regret lower bound up to multiplicative constants (and, sometimes, logarithmic terms).

- **[Learning Linear Attention in Polynomial Time](https://openreview.net/forum?id=QN0E0KX2LM)** — *NeurIPS 2025 · Oral*
  - **Topic:** Learning theory and optimization
  - **Summary:** Previous research has explored the expressivity of Transformer models in simulating Boolean circuits or Turing machines.

- **[Rigor in AI: Doing Rigorous AI Work Requires a Broader, Responsible AI-Informed Conception of Rigor](https://openreview.net/forum?id=USqNoPVhxx)** — *NeurIPS 2025 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** In AI research and practice, rigor remains largely understood in terms of methodological rigor---such as whether mathematical, statistical, or computational methods are correctly applied.

- **[COKE: A Cognitive Knowledge Graph for Machine Theory of Mind](https://aclanthology.org/2024.acl-long.848/)** — *ACL 2024 · Long*
  - **Topic:** Learning theory and optimization
  - **Summary:** Theory of mind (ToM) refers to humans’ ability to understand and infer the desires, beliefs, and intentions of others.

- **[A General Theoretical Paradigm to Understand Learning from Human Preferences](https://proceedings.mlr.press/v238/gheshlaghi-azar24a.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** The prevalent deployment of learning from human preferences through reinforcement learning (RLHF) relies on two important approximations: the first assumes that pairwise preferences can be substituted with pointwise rewards.

- **[Identifying Spurious Biases Early in Training through the Lens of Simplicity Bias](https://proceedings.mlr.press/v238/yang24c.html)** — *AISTATS 2024 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** Neural networks trained with (stochastic) gradient descent have an inductive bias towards learning simpler solutions.

- **[A Survey on Deep Learning for Theorem Proving](https://openreview.net/forum?id=zlw6AHwukB)** — *COLM 2024 · Poster*
  - **Topic:** Learning theory and optimization
  - **Summary:** Theorem proving is a fundamental aspect of mathematics, spanning from informal reasoning in natural language to rigorous derivations in formal systems.

- **[DEM: Distribution Edited Model for Training with Mixed Data Distributions](https://aclanthology.org/2024.emnlp-main.1074/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Learning theory and optimization
  - **Summary:** Training with mixed data distributions is a common and important part of creating multi-task and instruction-following models.

- **[Spectrally Transformed Kernel Regression](https://iclr.cc/virtual/2024/poster/18734)** — *ICLR 2024 · Spotlight*
  - **Topic:** Learning theory and optimization
  - **Summary:** Unlabeled data is a key component of modern machine learning.

## Trustworthy AI and Safety

- **[Allocation-Dependent Distortion for Fair Clustering Ensembles](https://openreview.net/forum?id=V84yBc0EgP)** — *ICLR 2027 · Under review*
  - **Topic:** Fair clustering
  - **Summary:** Studies how fair clustering ensembles should account for the allocation of protected groups across clusters. It introduces an allocation-dependent distortion objective and analyzes its relationship to group disparities.

- **[Training Honesty Adapters To Detect Deception In LLMs](https://openreview.net/forum?id=gpt1K3Ia4D)** — *ICLR 2027 · Under review*
  - **Topic:** Deception detection in language models
  - **Summary:** Trains LoRA honesty adapters on on-policy dialogue to detect deception, reporting improved detection of unseen models over several probing baselines.

- **[A Dirac-Frenkel-Onsager Principle: Instantaneous Residual Minimization with Gauge Momentum for Nonlinear Parametrizations of PDE Solutions](https://openreview.net/forum?id=aDPbUSUCwh)** — *ICML 2026 · Spotlight*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Dirac-Frenkel instantaneous residual minimization evolves nonlinear parametrizations of PDE solutions in time, but ill-conditioning can render the parameter dynamics non-unique.

- **[A Factorized Low-Rank RNN Framework for Uncovering Independent Neural Latent Dynamics and Connectivity](https://openreview.net/forum?id=QvIbmX9jBr)** — *ICML 2026 · Spotlight*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Low-rank recurrent neural networks (lrRNNs) are a class of models that uncover low-dimensional latent dynamics underlying neural population activity.

- **[Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities for Downstream Task Scaling Law](https://aclanthology.org/2025.acl-long.1157/)** — *ACL 2025 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Scaling law builds the relationship between training computation and validation loss, enabling researchers to effectively predict the loss trending of models across different levels of computation.

- **[Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs](https://aclanthology.org/2025.acl-long.341/)** — *ACL 2025 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Algorithmic fairness has conventionally adopted the mathematically convenient perspective of racial color-blindness (i.e., difference unaware treatment).

- **[LaTIM: Measuring Latent Token-to-Token Interactions in Mamba Models](https://aclanthology.org/2025.acl-long.1194/)** — *ACL 2025 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** State space models (SSMs), such as Mamba, have emerged as an efficient alternative to transformers for long-context sequence modeling.

- **[Balls-and-Bins Sampling for DP-SGD](https://openreview.net/forum?id=RwJTeddgRD)** — *AISTATS 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** We introduce the _Balls-and-Bins_ sampling for differentially private (DP) optimization methods such as DP-SGD.

- **[Safety Alignment Should be Made More Than Just a Few Tokens Deep](https://iclr.cc/virtual/2025/poster/30893)** — *ICLR 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** The safety alignment of current Large Language Models (LLMs) is vulnerable.

- **[Position: AI Safety should prioritize the Future of Work](https://icml.cc/virtual/2025/poster/40166)** — *ICML 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Current efforts in AI safety prioritize filtering harmful content, preventing manipulation of human behavior, and eliminating existential risks in cybersecurity or biosecurity.

- **[Position: Generative AI Regulation Can Learn from Social Media Regulation](https://icml.cc/virtual/2025/poster/40119)** — *ICML 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** There is strong agreement that generative AI should be regulated, but strong disagreement on how to approach regulation.

- **[Position: Humanity Faces Existential Risk from Gradual Disempowerment](https://icml.cc/virtual/2025/poster/40107)** — *ICML 2025 · Poster*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** This paper examines the systemic risks posed by incremental advancements in artificial intelligence, developing the concept of `gradual disempowerment', in contrast to the abrupt takeover scenarios commonly discussed in AI safety.

- **[Position: The Categorization of Race in ML is a Flawed Premise](https://icml.cc/virtual/2025/poster/40122)** — *ICML 2025 · Spotlight*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** This position paper critiques the reliance on rigid racial taxonomies in machine learning, exposing their U.S.-centric nature and lack of global applicability—particularly in Europe, where race categories are not commonly used.

- **[Machine Unlearning Doesn't Do What You Think: Lessons for Generative AI Policy and Research](https://openreview.net/forum?id=mfd6GRW4Az)** — *NeurIPS 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** "Machine unlearning" is a popular proposed solution for mitigating the existence of content in an AI model that is problematic for legal or moral reasons, including privacy, copyright, safety, and more.

- **[More effort is needed to protect pedestrian privacy in the era of AI](https://openreview.net/forum?id=rdeCalg68L)** — *NeurIPS 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** In the era of artificial intelligence (AI), pedestrian privacy is increasingly at risk.

- **[Position: Bridge the Gaps between Machine Unlearning and AI Regulation](https://openreview.net/forum?id=0ngi2StMwC)** — *NeurIPS 2025 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** The "right to be forgotten" and the data privacy laws that encode it have motivated machine unlearning since its earliest days.

- **[Position: Towards Bidirectional Human-AI Alignment](https://openreview.net/forum?id=PgA9rZoMY8)** — *NeurIPS 2025 · Poster*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Recent advances in general-purpose AI underscore the urgent need to align AI systems with human goals and values.

- **[Prohibiting Generative AI in any Form of Weapon Control](https://openreview.net/forum?id=uEY7kQsiZz)** — *NeurIPS 2025 · Poster*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** This position paper argues that the use of generative artificial intelligence (GenAI) to control, direct, guide or govern any weapon, either in situ or remotely, should be prohibited by government agencies and non-governmental organizations.

- **[Preference Ranking Optimization for Human Alignment](https://ojs.aaai.org/index.php/AAAI/article/view/29865)** — *AAAI 2024*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Large language models (LLMs) often contain misleading content, emphasizing the need to align them with human values to ensure secure AI systems.

- **[CausalGym: Benchmarking causal interpretability methods on linguistic tasks](https://aclanthology.org/2024.acl-long.785/)** — *ACL 2024 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Language models (LMs) have proven to be powerful tools for psycholinguistic research, but most prior work has focused on purely behavioural measures (e.g., surprisal comparisons).

- **[Emulated Disalignment: Safety Alignment for Large Language Models May Backfire!](https://aclanthology.org/2024.acl-long.842/)** — *ACL 2024 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Large language models (LLMs) undergo safety alignment to ensure safe conversations with humans.

- **[PsySafe: A Comprehensive Framework for Psychological-based Attack, Defense, and Evaluation of Multi-agent System Safety](https://aclanthology.org/2024.acl-long.812/)** — *ACL 2024 · Long*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Multi-agent systems, when enhanced with Large Language Models (LLMs), exhibit profound capabilities in collective intelligence.

- **[AI-generated text boundary detection with RoFT](https://openreview.net/forum?id=kzzwTrt04Z)** — *COLM 2024 · Poster*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Due to the rapid development of large language models, people increasingly often encounter texts that may start as written by a human but continue as machine-generated.

- **[Meta Continual Learning Revisited: Implicitly Enhancing Online Hessian Approximation via Variance Reduction](https://iclr.cc/virtual/2024/poster/18552)** — *ICLR 2024 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Regularization-based methods have so far been among the *de facto* choices for continual learning.

- **[Continual Learning with Pre-Trained Models: A Survey](https://www.ijcai.org/proceedings/2024/924)** — *IJCAI 2024 · Poster*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Nowadays, real-world applications often face streaming data, which requires the learning system to absorb new knowledge as data evolves.

- **[The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models](https://neurips.cc/virtual/2024/poster/97804)** — *NeurIPS 2024 · Oral*
  - **Topic:** Safety, privacy, fairness, and robustness
  - **Summary:** Human feedback is central to the alignment of Large Language Models (LLMs).

## AI Systems and Efficiency

- **[Feedback-driven recurrent quantum neural network universality](https://openreview.net/forum?id=248ysaRatx)** — *ICLR 2026 · Poster*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** The paper proves quantitative universal approximation results for learning state-space systems using recurrent quantum neural networks.

- **[Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126/)** — *ACL 2025 · Long*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** Long-context modeling is crucial for next-generation language models, yet the high computational cost of standard attention mechanisms poses significant computational challenges.

- **[Certifiably Quantisation-Robust training and inference of Neural Networks](https://openreview.net/forum?id=qtppWP3gXl)** — *AISTATS 2025 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** We tackle the problem of computing guarantees for the robustness of neural networks against quantisation of their inputs, parameters and activation values.

- **[Entropic Matching for Expectation Propagation of Markov Jump Processes](https://openreview.net/forum?id=23yqeRmadg)** — *AISTATS 2025 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** We propose a novel, tractable latent state inference scheme for Markov jump processes, for which exact inference is often intractable.

- **[PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling](https://openreview.net/forum?id=ayi7qezU87)** — *COLM 2025 · Poster*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** In this study, we investigate whether attention-based information flow inside large language models (LLMs) is aggregated through noticeable patterns for long context processing.

- **[Timestep Embedding Tells: It's Time to Cache for Video Diffusion Model](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Timestep_Embedding_Tells_Its_Time_to_Cache_for_Video_Diffusion_CVPR_2025_paper.html)** — *CVPR 2025 · Highlight*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** As a fundamental backbone for video generation, diffusion models are challenged by low inference speed due to the sequential nature of denoising.Previous methods speed up the models by caching and reusing model outputs at uniformly selected timesteps.However, such a strategy...

- **[Military AI Needs Technically-Informed Regulation to Safeguard AI Research and its Applications](https://openreview.net/forum?id=gXTFLbGUQp)** — *NeurIPS 2025 · Poster*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** Military weapon systems and command-and-control infrastructure augmented by artificial intelligence (AI) have seen rapid development and deployment in recent years.

- **[Position: If Innovation in AI systematically Violates Fundamental Rights, Is It Innovation at All?](https://openreview.net/forum?id=PFRandBfSz)** — *NeurIPS 2025 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** Artificial intelligence (AI) now permeates critical infrastructures and decisionmaking systems where failures produce social, economic, and democratic harm.

- **[MobileNetV4: Universal Models for the Mobile Ecosystem](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5647_ECCV_2024_paper.php)** — *ECCV 2024 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** "We present the latest generation of MobileNets: MobileNetV4 (MNv4).

- **[Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs](https://iclr.cc/virtual/2024/poster/17575)** — *ICLR 2024 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** In this study, we introduce adaptive KV cache compression, a plug-and-play method that reduces the memory footprint of generative inference for Large Language Models (LLMs).

- **[Convolutional Differentiable Logic Gate Networks](https://neurips.cc/virtual/2024/poster/96650)** — *NeurIPS 2024 · Oral*
  - **Topic:** Inference, training, and infrastructure
  - **Summary:** With the increasing inference cost of machine learning models, there is a growing interest in models with fast and efficient inference.

## Datasets and Evaluation

- **[BIRD-INTERACT: Re-imagining Text-to-SQL Evaluation via Lens of Dynamic Interactions](https://openreview.net/forum?id=nHrYBGujps)** — *ICLR 2026 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Large language models (LLMs) have demonstrated remarkable performance on single-turn text-to-SQL tasks, but real-world database applications predominantly require multi-turn interactions to handle ambiguous queries, execution errors, and evolving user requirements.

- **[AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset](https://aclanthology.org/2025.acl-long.96/)** — *ACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Recent advancements in large language model (LLM) performance on medical multiplechoice question (MCQ) benchmarks have stimulated interest from healthcare providers and patients globally.

- **[Beyond N-Grams: Rethinking Evaluation Metrics and Strategies for Multilingual Abstractive Summarization](https://aclanthology.org/2025.acl-long.932/)** — *ACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Automatic N-gram based metrics such as ROUGE are widely used for evaluating generative tasks such as summarization.

- **[BRIGHTER: BRIdging the Gap in Human-Annotated Textual Emotion Recognition Datasets for 28 Languages](https://aclanthology.org/2025.acl-long.436/)** — *ACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** People worldwide use language in subtle and complex ways to express emotions.

- **[From Real to Synthetic: Synthesizing Millions of Diversified and Complicated User Instructions with Attributed Grounding](https://aclanthology.org/2025.acl-long.517/)** — *ACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** The pursuit of diverse, complex, and large-scale instruction data is crucial for automatically aligning large language models (LLMs).

- **[PARME: Parallel Corpora for Low-Resourced Middle Eastern Languages](https://aclanthology.org/2025.acl-long.1451/)** — *ACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** The Middle East is characterized by remarkable linguistic diversity, with over 400 million inhabitants speaking more than 60 languages across multiple language families.

- **[Déjà Vu: Multilingual LLM Evaluation through the Lens of Machine Translation Evaluation](https://openreview.net/forum?id=yxzVanFoij)** — *COLM 2025 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Generation capabilities and language coverage of multilingual large language models (mLLMs) are advancing rapidly.

- **[Data Retrieval with Importance Weights for Few-Shot Imitation Learning](https://openreview.net/forum?id=wnWYoetLhC)** — *CoRL 2025 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** While large-scale robot datasets have propelled recent progress in imitation learning, learning from smaller task specific datasets remains critical for deployment in new environments and unseen tasks.

- **[Fabrica: Dual-Arm Assembly of General Multi-Part Objects via Integrated Planning and Learning](https://openreview.net/forum?id=aSUNzvEJIf)** — *CoRL 2025 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Multi-part assembly poses significant challenges for robotic systems to execute long-horizon, contact-rich manipulation with generalization across complex geometries.

- **[BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://iclr.cc/virtual/2025/poster/29245)** — *ICLR 2025 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Task automation has been greatly empowered by the recent advances in Large Language Models (LLMs) via Python code, where the tasks range from software engineering development to general-purpose reasoning.

- **[Position: AI Competitions Provide the Gold Standard for Empirical Rigor in GenAI Evaluation](https://icml.cc/virtual/2025/poster/40139)** — *ICML 2025 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** In this position paper, we observe that empirical evaluation in Generative AI is at a crisis point since traditional ML evaluation and benchmarking strategies are insufficient to meet the needs of evaluating modern GenAI models and systems.

- **[Position: Human Baselines in Model Evaluations Need Rigor and Transparency (With Recommendations & Reporting Checklist)](https://icml.cc/virtual/2025/poster/40115)** — *ICML 2025 · Spotlight*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** **In this position paper, we argue that human baselines in foundation model evaluations must be more rigorous and more transparent to enable meaningful comparisons of human vs.

- **[Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://icml.cc/virtual/2025/poster/40129)** — *ICML 2025 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Medical large language models (LLMs) research often makes bold claims, from encoding clinical knowledge to reasoning like a physician.

- **[In-Context Learning with Long-Context Models: An In-Depth Exploration](https://aclanthology.org/2025.naacl-long.605/)** — *NAACL 2025 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** As model context lengths continue to increase, the number of demonstrations that can be provided in-context approaches the size of entire training datasets.

- **[RewardBench: Evaluating Reward Models for Language Modeling](https://aclanthology.org/2025.findings-naacl.96/)** — *NAACL 2025 · Findings*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Reward models (RMs) are at the crux of successfully using RLHF to align pretrained models to human preferences, yet there has been relatively little study that focuses on evaluation of those models.

- **[Fostering the Ecosystem of AI for Social Impact Requires Expanding and Strengthening Evaluation Standards](https://openreview.net/forum?id=dl5pvd5IgW)** — *NeurIPS 2025 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** There has been increasing research interest in AI/ML for social impact, and correspondingly more publication venues refining review criteria for practice-driven AI/ML research.

- **[Measuring Fingerprints of Web-filtered Text Datasets and Fingerprint Propagation Through Training](https://openreview.net/forum?id=iKwHwCaddB)** — *NeurIPS 2025 · Spotlight*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** We investigate fingerprints in pretraining datasets for large language models (LLMs) through dataset classification experiments.

- **[COSMIC: Mutual Information for Task-Agnostic Summarization Evaluation](https://aclanthology.org/2024.acl-long.686/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Assessing the quality of summarizers poses significant challenges—gold summaries are hard to obtain and their suitability depends on the use context of the summarization system.

- **[Distributional Inclusion Hypothesis and Quantifications: Probing for Hypernymy in Functional Distributional Semantics](https://aclanthology.org/2024.acl-long.784/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Functional Distributional Semantics (FDS) models the meaning of words by truth-conditional functions.

- **[Estimating the Level of Dialectness Predicts Inter-annotator Agreement in Multi-dialect Arabic Datasets](https://aclanthology.org/2024.acl-short.70/)** — *ACL 2024 · Short*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** On annotating multi-dialect Arabic datasets, it is common to randomly assign the samples across a pool of native Arabic speakers.

- **[Latxa: An Open Language Model and Evaluation Suite for Basque](https://aclanthology.org/2024.acl-long.799/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** We introduce Latxa, a family of large language models for Basque ranging from 7 to 70 billion parameters.

- **[M4LE: A Multi-Ability Multi-Range Multi-Task Multi-Domain Long-Context Evaluation Benchmark for Large Language Models](https://aclanthology.org/2024.acl-long.832/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Managing long sequences has become an important and necessary feature for large language models (LLMs).

- **[MultiLegalPile: A 689GB Multilingual Legal Corpus](https://aclanthology.org/2024.acl-long.805/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Large, high-quality datasets are crucial for training Large Language Models (LLMs).

- **[On Efficient and Statistical Quality Estimation for Data Annotation](https://aclanthology.org/2024.acl-long.837/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Annotated datasets are an essential ingredient to train, evaluate, compare and productionalize supervised machine learning models.

- **[SPZ: A Semantic Perturbation-based Data Augmentation Method with Zonal-Mixing for Alzheimer’s Disease Detection](https://aclanthology.org/2024.acl-long.823/)** — *ACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Alzheimer’s Disease (AD), characterized by significant cognitive and functional impairment, necessitates the development of early detection techniques.

- **[GeniL: A Multilingual Dataset on Generalizing Language](https://openreview.net/forum?id=kLH4ccaL21)** — *COLM 2024 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Generative language models are increasingly transforming our digital ecosystem, but they often inherit societal biases learned from their training data, for instance stereotypes associating certain attributes with specific identity groups.

- **[GPQA: A Graduate-Level Google-Proof Q&A Benchmark](https://openreview.net/forum?id=Ti67584b98)** — *COLM 2024 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** We present GPQA, a challenging dataset of 448 multiple-choice questions written by domain experts in biology, physics, and chemistry.

- **[Top Leaderboard Ranking = Top Coding Proficiency, Always? EvoEval: Evolving Coding Benchmarks via LLM](https://openreview.net/forum?id=zZa7Ke7WAJ)** — *COLM 2024 · Poster*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Large language models (LLMs) have become the go-to choice for code generation tasks, with an exponential increase in the training, development, and usage of LLMs specifically for code generation.

- **[What the Harm? Quantifying the Tangible Impact of Gender Bias in Machine Translation with a Human-centered Study](https://aclanthology.org/2024.emnlp-main.1002/)** — *EMNLP 2024 · Award recipient*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Gender bias in machine translation (MT) is recognized as an issue that can harm people and society.

- **[AGIEval: A Human-Centric Benchmark for Evaluating Foundation Models](https://aclanthology.org/2024.findings-naacl.149/)** — *NAACL 2024 · Findings*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Assessing foundation models’ abilities for human-level tasks is crucial for Artificial General Intelligence (AGI) development.Traditional benchmarks, which rely on artificial datasets, may not accurately represent these capabilities.

- **[Effective Long-Context Scaling of Foundation Models](https://aclanthology.org/2024.naacl-long.260/)** — *NAACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** We present an effective recipe to train strong long-context LLMs that are capable of utilizing massive context windows of up to 32,000 tokens.

- **[GPTScore: Evaluate as You Desire](https://aclanthology.org/2024.naacl-long.365/)** — *NAACL 2024 · Long*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Generative Artificial Intelligence (AI) has enabled the development of sophisticated models that are capable of producing high-caliber text, images, and other outputs through the utilization of large pre-trained models.Nevertheless, assessing the quality of the generation is...

- **[ChaosBench: A Multi-Channel, Physics-Based Benchmark for Subseasonal-to-Seasonal Climate Prediction](https://neurips.cc/virtual/2024/poster/97481)** — *NeurIPS 2024 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Accurate prediction of climate in the subseasonal-to-seasonal scale is crucial for disaster preparedness and robust decision making amidst climate change.

- **[CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://neurips.cc/virtual/2024/poster/97798)** — *NeurIPS 2024 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Visual Question Answering~(VQA) is an important task in multimodal AI, which requires models to understand and reason on knowledge present in visual and textual data.

- **[Dataset and Lessons Learned from the 2024 SaTML LLM Capture-the-Flag Competition](https://neurips.cc/virtual/2024/poster/97654)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Large language model systems face significant security risks from maliciously crafted messages that aim to overwrite the system's original instructions or leak private data.

- **[GAIA: Rethinking Action Quality Assessment for AI-Generated Videos](https://neurips.cc/virtual/2024/poster/97817)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Assessing action quality is both imperative and challenging due to its significant impact on the quality of AI-generated videos, further complicated by the inherently ambiguous nature of actions within AI-generated video (AIGV).

- **[LINGOLY: A Benchmark of Olympiad-Level Linguistic Reasoning Puzzles in Low Resource and Extinct Languages](https://neurips.cc/virtual/2024/poster/97604)** — *NeurIPS 2024 · Oral*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** In this paper, we present the LingOly benchmark, a novel benchmark for advanced reasoning abilities in large language models.

- **[SpreadsheetBench: Towards Challenging Real World Spreadsheet Manipulation](https://neurips.cc/virtual/2024/poster/97753)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** We introduce SpreadsheetBench, a challenging spreadsheet manipulation benchmark exclusively derived from real-world scenarios, designed to immerse current large language models (LLMs) in the actual workflow of spreadsheet users.

- **[WikiDBs: A Large-Scale Corpus Of Relational Databases From Wikidata](https://neurips.cc/virtual/2024/poster/97622)** — *NeurIPS 2024 · Spotlight*
  - **Topic:** Datasets, benchmarks, and evaluation
  - **Summary:** Deep learning on tabular data, and particularly tabular representation learning, has recently gained growing interest.

## Graph Learning

- **[Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness](https://iclr.cc/virtual/2024/poster/18994)** — *ICLR 2024 · Oral*
  - **Topic:** Graph learning and network analysis
  - **Summary:** Designing expressive Graph Neural Networks (GNNs) is a fundamental topic in the graph learning community.

## Other AI Research

- **[Probabilistic Kernel Function for Fast Angle Testing](https://openreview.net/forum?id=nCsF3Bsn2n)** — *ICLR 2026 · Oral*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** We propose two probabilistic kernel functions for angle testing, which can be used to accelerate vector-based similarity search.

- **[A Bitter Lesson for Data Filtering](https://neurips.cc/virtual/2026/poster/155947)** — *NeurIPS 2026 · Spotlight*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** We investigate data filtering for large model pretraining via new scaling studies that target the high compute, data-scarce regime.

- **[Typology-Guided Adaptation in Multilingual Models](https://aclanthology.org/2025.acl-long.1059/)** — *ACL 2025 · Long*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Multilingual models often treat language diversity as a problem of data imbalance, overlooking structural variation.

- **[Almost linear time differentially private release of synthetic graphs](https://openreview.net/forum?id=UWNfWtCXCZ)** — *AISTATS 2025 · Oral*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** In this paper, we give an almost linear time and space algorithms to sample from an exponential mechanism with an $\ell_1$-score function defined over an exponentially large non-convex set.

- **[Position: Machine Learning Conferences Should Establish a "Refutations and Critiques" Track](https://openreview.net/forum?id=DS1XSAPvKs)** — *NeurIPS 2025 · Oral*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Science progresses by iteratively advancing and correcting humanity's understanding of the world.

- **[We Should Chart an Atlas of All the World's Models](https://openreview.net/forum?id=BzFMBNqg7R)** — *NeurIPS 2025 · Poster*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Public model repositories now contain millions of models, yet most remain undocumented and effectively lost: their capabilities, provenance, and constraints cannot be reliably determined.

- **[NounAtlas: Filling the Gap in Nominal Semantic Role Labeling](https://aclanthology.org/2024.acl-long.857/)** — *ACL 2024 · Long*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Despite significant advances in Semantic Role Labeling (SRL), much work in this field has been carried out with a focus on verbal predicates, with the research on nominal SRL lagging behind.

- **[Semisupervised Neural Proto-Language Reconstruction](https://aclanthology.org/2024.acl-long.788/)** — *ACL 2024 · Long*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Existing work implementing comparative reconstruction of ancestral languages (proto-languages) has usually required full supervision.

- **[Knowledge Distillation in Federated Learning: A Practical Guide](https://www.ijcai.org/proceedings/2024/905)** — *IJCAI 2024 · Poster*
  - **Topic:** Machine learning and artificial intelligence
  - **Summary:** Federated Learning (FL) enables the training of Deep Learning models without centrally collecting possibly sensitive raw data.

## Sources and updates

- Data sources, selection rules, known gaps, and direct-source maintenance notes: [SOURCES.md](SOURCES.md).
- The scheduled GitHub Actions workflow refreshes source records and regenerates this README daily. Review-score changes are stored with observation time and review phase so the internal ranking follows rebuttal updates.
