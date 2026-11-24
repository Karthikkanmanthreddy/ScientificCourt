# ScientificCourt
## Evidence-Based Multi-Agent Debate System

**Course:** Generative AI  
**Team ID:** GenAI_DSC120A_05  
**Project Type:** Multi-Agent AI Application

### Team Members
1. Karthik Reddy Kanmanth
2. Saresh Guniganti
3. Sharath Kale

---

# 1. Problem Statement

Scientific research is continuously growing, making it increasingly difficult for individuals to evaluate scientific claims and distinguish reliable evidence from misleading or contradictory information.

Traditional fact-checking approaches often depend on a single system or reviewer, which may overlook contradictory research, limitations and alternative interpretations.

ScientificCourt aims to address this problem by developing an AI-powered multi-agent debate system that independently examines scientific claims using scientific evidence.

The application will use two opposing AI agents: a Supporter Agent and a Challenger Agent. A separate Judge Agent will evaluate their arguments against retrieved scientific evidence and produce a final verdict.

The system will prioritize evidence traceability, citation validity and transparent decision-making rather than relying solely on generated AI responses.

# 2. Project Objectives

The primary objectives are:

1. Develop an interactive scientific claim verification application.
2. Retrieve relevant scientific evidence from the SciFact dataset.
3. Implement independent Supporter and Challenger AI agents.
4. Develop an independent Judge Agent to evaluate competing arguments.
5. Generate evidence-supported verdicts.
6. Prevent fabricated scientific references.
7. Implement an abstention mechanism when evidence is insufficient.
8. Compare multi-agent performance against a single-agent baseline.
9. Evaluate accuracy, evidence quality, API costs and system limitations.

# 3. Intended Users

The application is intended for:

- Students researching scientific topics.
- Researchers exploring scientific claims.
- Educators evaluating scientific statements.
- Individuals interested in evidence-based information.
- Users who want to understand supporting and contradicting scientific evidence.

# 4. Proposed System Architecture

The system will consist of the following components:

1. User Interface
2. Claim Processing Module
3. Scientific Evidence Retrieval Module
4. Supporter Agent
5. Challenger Agent
6. Independent Judge Agent
7. Verdict Generation Module
8. Evaluation and Analytics Dashboard
9. Database and Debate History

### System Workflow

User submits a scientific claim.

↓

The claim is processed and relevant evidence is retrieved from SciFact.

↓

The retrieved evidence is provided to the Supporter and Challenger agents.

↓

The Supporter identifies evidence supporting the claim.

↓

The Challenger identifies contradictory evidence and limitations.

↓

Both agents exchange a limited response.

↓

The Judge independently evaluates the evidence and arguments.

↓

The system generates one of three verdicts:

- Supported
- Refuted
- Insufficient Evidence

↓

The application displays the verdict, evidence references, arguments and confidence information.

# 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive frontend |
| SciFact | Scientific claims and evidence dataset |
| Pandas | Data processing |
| Sentence Transformers | Semantic embeddings |
| FAISS | Similarity-based evidence retrieval |
| LLM API | AI agent reasoning |
| SQLite | Debate history and application data |
| GitHub | Version control and collaboration |

The final selection of models and APIs will consider affordability, performance and reproducibility.

# 6. Methodology

### 6.1 Dataset Preparation

We will use the SciFact dataset containing scientific claims, research abstracts and evidence annotations.

The dataset will be processed to prepare scientific text for retrieval and evaluation.

### 6.2 Evidence Retrieval

A semantic retrieval system will identify relevant scientific abstracts and passages for each submitted claim.

Retrieved passages will retain their source identifiers to support traceable citations.

### 6.3 Supporter Agent

The Supporter Agent will:

- Analyse the submitted claim.
- Examine retrieved scientific evidence.
- Identify supporting research.
- Explain its reasoning.
- Provide references to relevant evidence.

### 6.4 Challenger Agent

The Challenger Agent will:

- Independently analyse the claim.
- Identify contradictory research.
- Highlight limitations and missing context.
- Challenge unsupported arguments.
- Provide evidence references.

Each agent will have a limited opportunity to respond to the opposing argument.

### 6.5 Judge Agent

The Judge Agent will:

- Examine the original scientific evidence.
- Evaluate both agents' arguments.
- Identify unsupported statements.
- Determine whether the evidence supports or refutes the claim.
- Abstain when sufficient evidence is unavailable.

### 6.6 Final Verdict

The system will generate:

- Supported
- Refuted
- Insufficient Evidence

The verdict will include an explanation, supporting evidence, contradictory evidence and confidence information.

# 7. Five End-to-End User Journeys

| No. | User Journey | Expected Outcome |
|---|---|---|
| 1 | Submit a scientific claim | Relevant scientific evidence is retrieved. |
| 2 | Start a scientific debate | Supporter and Challenger produce evidence-based arguments. |
| 3 | Evaluate a disputed claim | Judge generates a reasoned verdict. |
| 4 | Submit a claim with insufficient evidence | System abstains instead of generating an unsupported verdict. |
| 5 | Experience evidence retrieval failure | Application displays an error and provides a retry or recovery option. |

All five journeys will be tested using reproducible inputs and expected outcomes.

# 8. Evaluation Strategy

The application will be evaluated using at least 100 held-out SciFact claims.

The evaluation will include:

### Performance Metrics

- Claim classification accuracy.
- Evidence Precision, Recall and F1-score.
- Unsupported verdict rate.
- Evidence citation validity.
- Abstention performance.
- API token usage and cost.

### Baseline Comparison

We will compare:

1. Single-Agent Evidence-Based Verification.
2. Multi-Agent Debate System.

Both approaches will be evaluated using comparable claims and matched API budgets.

### Ablation Study

We will investigate the contribution of individual agents by removing:

- The Challenger Agent.
- The independent Judge/verification stage.

The results will help determine whether the multi-agent architecture provides measurable improvements.

### Additional Testing

We will also evaluate at least five misleading evidence cases and analyse system failures, limitations and performance trade-offs.

# 9. Development Milestones

| Phase | Milestone | Expected Deliverable |
|---|---|---|
| 1 | Project Setup | GitHub repository and proposal |
| 2 | Dataset Preparation | Processed SciFact dataset |
| 3 | Baseline Development | Single-agent verification |
| 4 | Multi-Agent Development | Supporter and Challenger |
| 5 | Judge Development | Evidence-based verdict generation |
| 6 | Application Integration | Working Streamlit application |
| 7 | Evaluation | Baseline comparison and ablation study |
| 8 | Final Delivery | Testing, documentation and presentation |

# 10. Team Responsibilities

Initial proposed responsibilities:

**Karthik Reddy Kanmanth**
- System architecture and overall integration.
- Scientific evidence retrieval.
- Application backend and workflow integration.

**Saresh Guniganti**
- Supporter Agent development.
- Challenger Agent development.
- Agent prompt design and evidence analysis.

**Sharath Kale**
- Judge Agent development.
- Evaluation framework and performance metrics.
- Testing and result analysis.

All three members will participate in integration, testing and final evaluation. Every member will understand the complete application and its architecture.

# 11. Risk Management

| Risk | Mitigation |
|---|---|
| Hallucinated scientific references | Restrict references to retrieved dataset records. |
| Insufficient evidence | Implement an abstention mechanism. |
| API costs | Limit debate rounds and token usage. |
| Poor retrieval quality | Evaluate semantic retrieval and improve ranking. |
| Agent disagreement | Use independent evidence-based verification. |
| Dataset limitations | Document coverage and evaluation limitations. |
| Application failures | Implement error handling and automated tests. |

# 12. GitHub and Development Management

The team will maintain a public GitHub repository containing:

- Project proposal.
- Source code.
- Dataset preparation scripts.
- Evaluation experiments.
- Automated tests.
- Architecture documentation.
- Weekly progress records.
- Final evaluation report.

The team will maintain a dated PROGRESS.md file and update it at least weekly.

The following development releases will be maintained:

- v0.1 – Feasibility and baseline.
- v0.2 – Integrated end-to-end workflow.
- v1.0 – Tested final application.

API keys and restricted dataset copies will not be committed to the repository.

# 13. Expected Outcomes

At the end of the project, we aim to deliver a complete interactive scientific claim verification platform.

The application will demonstrate how multiple AI agents can analyse scientific evidence from opposing perspectives and generate transparent, evidence-based conclusions.

The project will also provide a quantitative comparison between single-agent and multi-agent verification approaches, highlighting their strengths, weaknesses, costs and limitations.

The final application will be documented and published on GitHub as a portfolio-ready Generative AI project.

---

**Project Name:** ScientificCourt

**Tagline:** Where Science Meets Evidence.
