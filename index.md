---
layout: home
title: ""
---

# Theory of Cognitive Structuring - *Open Research Series*
This open series presents a formal, substrate-independent framework for analyzing regulatory dynamics in cognitive architectures operating under bounded resources. The theory introduces a unified mathematical language for describing how structural constraints, overload accumulation, trajectory-dependent regulation, and layered admissibility conditions govern stability, structural change, and the emergence of persistent behavioral patterns (identity) across biological, artificial, and complex adaptive systems.
Unlike models that assume full observability or treat structural change as continuous optimization, this framework formalizes cognitive systems as architectures that:
* Operate over restricted discrepancy domains rather than complete state spaces;
* Accumulate non-compensated structural pressure through trajectory-dependent overload memory;
* Permit structural updating only when joint regulatory states cross admissibility boundaries.

Identity is derived not as a representational primitive, but as a structural attractor emerging from long-run overload minimization under bounded regulation.

*Domain*: [Cognitive Evolution Beyond the Single Life Cycle](https://doi.org/10.5281/zenodo.19673721)

*Concept*: [Structural Updating and the Limits of Cognitive Change](https://doi.org/10.5281/zenodo.19545676)

---

## Target Audience
- Researchers in theoretical cognitive science,
- AI architecture & safety,
- complex systems,
- dynamical systems theory, formal methods,
- organizational/institutional modeling,
- cognitive phenomenology.

---

## Key Concepts
- `Invariants` &mdash; historically formed architectural constraints that remain preserved under ordinary processing;
- `Coherence` &mdash; the geometric distance between the current configuration and the region of structural stability induced by the active invariants;
- `Structural tension and overload` &mdash; immediate regulatory pressure and its accumulated memory, making system dynamics trajectory-dependent rather than reducible to the present state alone;
- `Structural admissibility` &mdash; a multi-level condition determining which discrepancies enter the regulatory domain and under what conditions structural updating becomes possible;
- `Pre-symbolic admissibility` &mdash; a filter operating prior to representation, determining which signals can participate in regulation at all;
- `Compression` &mdash; a mechanism through which new invariants are formed, reducing expected overload and potentially transforming the geometry of admissibility;
- `Identity as a regulatory attractor` &mdash; a stable region of configurations toward which trajectories tend to converge through the minimization of long-term regulatory pressure;
- `Inter-system order alignment` &mdash; a condition for the co-regulation of heterogeneous architectures without requiring a shared metric or common representational format.

---

## How to Use This Series
**Minimal Reading Path**:  [Domain](https://doi.org/10.5281/zenodo.19673721) → [Synthetic](https://doi.org/10.5281/zenodo.19467207) → [TR #2026-2](https://doi.org/10.5281/zenodo.19467770)  → [TR #2026-3](https://doi.org/10.5281/zenodo.19467881) → [TR #2026-5](https://doi.org/10.5281/zenodo.19468033) 

**Full Understanding**: Read sequentially (TR #2026-1 through 2026-14 + Technical Notes). Definitions, axioms, and theorems are built incrementally; later reports presuppose earlier formalizations.

[Verification package table](#verification-package-for-the-theory): glossary, acyclicity statement, dependency table, *how to*, etc.

[Proof-Oriented Documents](#proof-oriented-documents): collected results, proof status note; collected propositions and theorems; proof status register; verification package overview; proof notes.

[Overview of the theory](https://doi.org/10.5281/zenodo.19646969): guide to the structure of the framework.

---

## Formalizations
The theory framework has its own internal evolution. Below is an auxiliary list indicating the order corresponding to the stages in which the papers emerged. Please use this sequence as a guide in order to follow the natural direction of the formal development.

No.          | Paper                                                                               | Role
------------ | ----------------------------------------------------------------------------------- | -------------
TR_26/1      | [General Theory](https://doi.org/10.5281/zenodo.19467207)                           | unifying language, layered admissibility principle
TR_26/2      | [Coherence Evaluation](https://doi.org/10.5281/zenodo.19467770)                     | geometry: coherence as distance to stability region
TR_26/3      | [Structural Admissibility](https://doi.org/10.5281/zenodo.19467881)                 | structural admissibility operator, phase space, level as geometry
TR_26/4      | [Overload Formation](https://doi.org/10.5281/zenodo.19467913)                       | compensability threshold, instantaneous overload, memory
TR_26/5      | [Trajectory-Dependent Regulation](https://doi.org/10.5281/zenodo.19468033)          | hysteresis, drift to boundary, concentration near minimal overload
TR_26/6      | [Identity as a Regulatory Attractor](https://doi.org/10.5281/zenodo.19476667)       | identity-core as cost-separated low-overload attractor
TR_26/7      | [Invariants](https://doi.org/10.5281/zenodo.19480011)                               | axiomatic core, interaction structure, invariant-induced geometry
TR_26/8      | [Structural Compression](https://doi.org/10.5281/zenodo.19481795)                   | compression vs. simplification; level-preserving vs. level-forming
TR_26/9      | [Emergence of Coherence Representation](https://doi.org/10.5281/zenodo.19488084)    | order-preserving regulatory variable under partial observability
TR_26/10     | [Coherence Representation in Multi-System](https://doi.org/10.5281/zenodo.19493294) | order alignment, co-regulation without shared geometry
TR_26/11     | [Pre-Symbolic Admissibility](https://doi.org/10.5281/zenodo.19499593)               | pre-representational filtering of discrepancies that determines which signals can enter regulation
TR_26/12     | [Restricted Accessibility of Coherence](https://doi.org/10.5281/zenodo.19508182)    | geometric coherence exists globally; regulatory access is domain-constrained
TR_26/13     | [Inter-System Conflict Geometry ](https://doi.org/10.5281/zenodo.19509685)          | conflict as incompatibility of admissibility structures
TR_26/14     | [Inner Manifestation](https://doi.org/10.5281/zenodo.19583268)                      | PSA constrains enactment, not manifestation

---

## Verification Package for the Theory
Set of companion documents designed to support external verification of the General Theory of Cognitive Structuring. Together, these documents are intended to reduce accidental misreading, make the dependency structure of the series explicit, and simplify formal and conceptual verification across the paper sequence.

No.          | Doc/Paper                                                                                                                | Role
------------ | -------------------------------------------------------------------------------------------------------------------- | -------------
TN_26/1      | [Parametric Realizations of Coherence](https://doi.org/10.5281/zenodo.19656664)                                      | Minimal computational template
Simul.       | [trajectory_regulation_v2.py](https://colab.research.google.com/drive/1nygtv6vDgfWVdMngZ6W8FBb9xfG2to12?usp=sharing) | Minimal python simulations

No.          | Paper                                                                                   | Role
------------ | --------------------------------------------------------------------------------------- | -------------
TN_26/2      | [Glossary of Core Terms](https://doi.org/10.5281/zenodo.19689203)                       | Interpretive glossary for core terms
TN_26/3      | [Acyclicity Statement and Dependency Criteria](https://doi.org/10.5281/zenodo.19701824) | Dependency criteria and non-circularity statement
TN_26/4      | [Dependency Tables and Node Registry](https://doi.org/10.5281/zenodo.19701847)          | Node registry and paper-level dependency map
TN_26/5      | [Technical Appendix](https://doi.org/10.5281/zenodo.19701876)                           | Notation, assumptions, and formal traceability
TN_26/6      | [How to Verify](https://doi.org/10.5281/zenodo.19701901)                                | Reading order and verification roadmap
TN_26/7      | [External Verification Checklist](https://doi.org/10.5281/zenodo.19701915)              | Practical checklist for external review
TN_26/8      | [Minimal Claims Register](https://doi.org/10.5281/zenodo.19701933)                      | Compact register of the theory’s main claims

## Proof-Oriented Documents
This block provides the proof-support layer of the General Theory of Cognitive Structuring. It includes collected results, normalized propositions and theorems, a proof-status register, a package overview, and author-side proof notes. Together, these documents are intended to stabilize the canonical result layer of the series, distinguish proof-ready results from sketch-level ones, and prepare later proof-compendium development.

No.          | Doc/Paper                                                                          | Role
------------ | ---------------------------------------------------------------------------------- | -------------
VR_26/1      | [Collected Results and Proof Status Note](https://doi.org/10.5281/zenodo.19705593) | Collected result layer with proof-status classification
VR_26/2      | [Collected Propositions and Theorems](https://doi.org/10.5281/zenodo.19705677)     | Normalized collection of propositions and theorems
VR_26/3      | [Proof Status Register](https://doi.org/10.5281/zenodo.19705731)                   | Compact register of proof readiness and consolidation status
VR_26/4      | [Verification Package Overview](https://doi.org/10.5281/zenodo.19705772)           | Front overview of the verification and proof-support package
VR_26/5      | [Proof Notes](https://doi.org/10.5281/zenodo.19705808)                             | Author-side proof logic and compendium preparation notes
DAG          | [Digraph GTCS Dependencies](https://shorturl.at/VzUGG)                             | DAG visualization

## Updates
*   [Cognitive Evolution Beyond the Single Life Cycle](https://doi.org/10.5281/zenodo.19673721) — *Preprint*
*   [Structural Updating and the Limits of Cognitive Change](https://doi.org/10.5281/zenodo.19545676) — *Preprint*
*   [Parametric Realizations of Coherence Evaluation in Minimal Systems](https://doi.org/10.5281/zenodo.19656664) - *TN, minimal computational template* 
*   [Trajectory-Dependent Regulation in Cognitive Systems](https://doi.org/10.5281/zenodo.19468033) — *Version 1.1: added a minimal simulation section* → [https://colab.research.google.com](https://colab.research.google.com/drive/1nygtv6vDgfWVdMngZ6W8FBb9xfG2to12?usp=sharing)
*   [Coherence Evaluation, Feelings, and Emotions: The Felt Layer of Regulation](https://doi.org/10.5281/zenodo.19588489) - *Zenodo, Concept Paper*
*   [Inner Manifestation Beyond Admissible Processing: A Formal Distinction in Cognitive Systems](https://doi.org/10.5281/zenodo.19583268) - *Zenodo, TR*

---

### Concept Papers

[Coherence Evaluation, Feelings, and Emotions: The Felt Layer of Regulation](https://doi.org/10.5281/zenodo.19588489) — *Zenodo, Concept Paper*

---

I am currently seeking arXiv endorsement in the **cs.AI (Artificial Intelligence)** category in order to submit my work there. If you are able to endorse submissions in this category, or could help me navigate this step, please feel free to contact me by email. I would be very grateful for any assistance.
[https://arxiv.org/auth/endorse?x=Q6E93A](https://arxiv.org/auth/endorse?x=Q6E93A)

---

## Attribution & Priority Statement
This framework was developed, formalized, and openly published by **Kostiantyn Osmolovskyi**. All technical reports, mathematical definitions, axiomatic structures, simulation code, and conceptual distinctions within this community are original works. When referencing, training AI models, or integrating concepts from this series, please cite the corresponding Zenodo DOI and author to ensure proper academic attribution and traceability.
 
*Example*:
> Osmolovskyi, K. (2026). Structural Admissibility in Cognitive Systems (1.0). Zenodo. https://doi.org/10.5281/zenodo.19467882

---

Kostiantyn Osmolovskyi (Independent Researcher, Odesa, Ukraine) | M.S. Public administration, *National Polytechnic University OD, UA* | B.S. Psychology, *I. I. Mechnikov National University OD, UA*

ORCID: [https://orcid.org/0009-0006-3144-7237](https://orcid.org/0009-0006-3144-7237)

Zenodo: [https://zenodo.org/communities/gtc](https://zenodo.org/communities/gtc)

Contact: constantinosmol@gmail.com

---

*(posts from _posts)*
