---
layout: home
title: ""
---

# Theory of Cognitive Structuring  – Open Research Series
This open series presents a formal, substrate-independent framework for analyzing regulatory dynamics in cognitive architectures operating under bounded resources. The theory introduces a unified mathematical language for describing how structural constraints, overload accumulation, trajectory-dependent regulation, and layered admissibility conditions govern stability, structural change, and the emergence of persistent behavioral patterns (identity) across biological, artificial, and complex adaptive systems.
Unlike models that assume full observability or treat structural change as continuous optimization, this framework formalizes cognitive systems as architectures that:
* Operate over restricted discrepancy domains rather than complete state spaces;
* Accumulate non-compensated structural pressure through trajectory-dependent overload memory;
* Permit structural updating only when joint regulatory states cross admissibility boundaries.

Identity is derived not as a representational primitive, but as a structural attractor emerging from long-run overload minimization under bounded regulation.

---

### Key Concepts
- `Invariants` &mdash; historically formed architectural constraints that remain preserved under ordinary processing;
- `Coherence` &mdash; the geometric distance between the current configuration and the region of structural stability induced by the active invariants;
- `Structural tension and overload` &mdash; immediate regulatory pressure and its accumulated memory, making system dynamics trajectory-dependent rather than reducible to the present state alone;
- `Structural admissibility` &mdash; a multi-level condition determining which discrepancies enter the regulatory domain and under what conditions structural updating becomes possible;
- `Pre-symbolic admissibility` &mdash; a filter operating prior to representation, determining which signals can participate in regulation at all;
- `Compression` &mdash; a mechanism through which new invariants are formed, reducing expected overload and potentially transforming the geometry of admissibility;
- `Identity as a regulatory attractor` &mdash; a stable region of configurations toward which trajectories tend to converge through the minimization of long-term regulatory pressure;
- `Inter-system order alignment` &mdash; a condition for the co-regulation of heterogeneous architectures without requiring a shared metric or common representational format.

---

### How to Use This Series
**Minimal Reading Path**:  [Domain](https://doi.org/10.5281/zenodo.19673721) → [Synthetic](https://doi.org/10.5281/zenodo.19467207) → TR #2026-2  → TR #2026-3 → TR #2026-5 

**Full Understanding**: Read sequentially (TR #2026-1 through 2026-14 + Technical Notes). Definitions, axioms, and theorems are built incrementally; later reports presuppose earlier formalizations.

**Map of the series**: [Overview of the theory](https://doi.org/10.5281/zenodo.19646969)

**Minimal Python simulations** e.g., [trajectory_regulation_v2.py](https://colab.research.google.com/drive/1nygtv6vDgfWVdMngZ6W8FBb9xfG2to12?usp=sharing) accompany relevant reports to illustrate trajectory dependence and admissibility dynamics. Parameters are explicitly documented. Simulations are strictly illustrative and are not intended as exhaustive computational studies or empirical validations.

---

#### Updates
*   [Cognitive Evolution Beyond the Single Life Cycle](https://doi.org/10.5281/zenodo.19673721) — *Preprint*
*   [Parametric Realizations of Coherence Evaluation in Minimal Systems](https://doi.org/10.5281/zenodo.19656664) — *TN, minimal computational template* 
*   [Trajectory-Dependent Regulation in Cognitive Systems](https://doi.org/10.5281/zenodo.19468033) — *Version 1.1: added a minimal simulation section* → [https://colab.research.google.com](https://colab.research.google.com/drive/1nygtv6vDgfWVdMngZ6W8FBb9xfG2to12?usp=sharing)
*   [Coherence Evaluation, Feelings, and Emotions: The Felt Layer of Regulation](https://doi.org/10.5281/zenodo.19588489) — *Zenodo, Concept Paper*
*   [Inner Manifestation Beyond Admissible Processing: A Formal Distinction in Cognitive Systems](https://doi.org/10.5281/zenodo.19583268) — *Zenodo, TR*


---

###Formalizations
The theory framework has its own internal evolution. Below is an auxiliary list indicating the order corresponding to the stages in which the papers emerged. Please use this sequence as a guide in order to follow the natural direction of the formal development.

No.          | Paper                                    | Role
------------ | ---------------------------------------- | -------------
TR_26\1      | General Theory                           | unifying language, layered admissibility principle
TR_26\2      | Coherence Evaluation                     | geometry: coherence as distance to stability region
TR_26\3      | Structural Admissibility                 | structural admissibility operator, phase space, level as geometry
TR_26\4      | Overload Formation                       | compensability threshold, instantaneous overload, memory
TR_26\5      | Trajectory-Dependent Regulation          | hysteresis, drift to boundary, concentration near minimal overload
TR_26\6      | Identity as a Regulatory Attractor       | identity-core as cost-separated low-overload attractor
TR_26\7      | Invariants                               | axiomatic core, interaction structure, invariant-induced geometry
TR_26\8      | Structural Compression                   | compression vs. simplification; level-preserving vs. level-forming
TR_26\9      | Emergence of Coherence Representation    | order-preserving regulatory variable under partial observability
TR_26\10     | Coherence Representation in Multi-System | order alignment, co-regulation without shared geometry
TR_26\11     | Pre-Symbolic Admissibility               | pre-representational filtering of discrepancies that determines which signals can enter regulation
TR_26\12     | Restricted Accessibility of Coherence    | geometric coherence exists globally; regulatory access is domain-constrained
TR_26\13     | Inter-System Conflict Geometry           | conflict as incompatibility of admissibility structures
TR_26\14     | Inner Manifestation                      | PSA constrains enactment, not manifestation
TN_26\1      | Parametric Realizations of Coherence     | minimal computational template

---

#### General theory of cognitive structuring and a series of formal theoretical papers

[The general theory framework](https://zenodo.org/communities/gtc/records) has its own internal evolution. Below is an auxiliary list indicating the order corresponding to the stages in which the papers emerged. Please use this sequence as a guide in order to follow the natural direction of the formal development.


| No. | Paper                                                          | Role in the series                                            | Main contribution                                                                                                                                                                         | Key concept                                            |
| --- | -------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| 1   | **[Structural Updating and the Limits of Cognitive Change](https://doi.org/10.5281/zenodo.19545676)**                     | Theoretical entry point to the series                         | Shows that access to processing should be distinguished from the availability of structural updating, and introduces admissibility of structural updating. | **Structural updating** |
| 2   | **[Coherence Evaluation in Cognitive Systems](https://doi.org/10.5281/zenodo.19467770)**                  | Geometric foundation of the series                            | Formalizes coherence as the relation between the current configuration and the region of stable processing                                                                                | **Coherence geometry**                                 |
| 3   | **[Structural Admissibility in Cognitive Systems](https://doi.org/10.5281/zenodo.19467881)**              | Formalization of the limit of structural updating             | Shows when structural updating becomes admissible under accumulated tension and architectural constraints                                                                                 | **Admissibility operator**                             |
| 4   | **[Overload Formation in Cognitive Processing](https://doi.org/10.5281/zenodo.19467913)**                 | Formalization of regulatory overload                          | Explains how non-compensable tension becomes accumulated overload                                                                                                                         | **Overload**                                           |
| 5   | **[Trajectory-Dependent Regulation in Cognitive Systems](https://doi.org/10.5281/zenodo.19468033)**       | Introduction of the historical dependence of regulation       | Demonstrates that the regulatory state depends not only on the current point, but also on the path by which it was reached                                                                | **Trajectory dependence**                              |
| 6   | **[Identity as a Regulatory Attractor](https://doi.org/10.5281/zenodo.19476667)**                         | Introduction of a stable core of regulation                   | Shows identity as a stable regulatory configuration rather than a content-based description                                                                                               | **Identity as a regulatory attractor**                 |
| 7   | **[Invariants in Cognitive Architectures](https://doi.org/10.5281/zenodo.19480011)**                      | Formalization of stable architectural constraints             | Defines invariants as what stabilizes admissible forms of further processing                                                                                                              | **Invariants**                                         |
| 8   | **[Structural Compression in Cognitive Architectures](https://doi.org/10.5281/zenodo.19481795)**          | Mechanism of stable structure formation                       | Shows how recurrent regulatorily significant relations are compressed into compact architectural formations                                                                               | **Structural compression**                             |
| 9   | **[Emergence of Coherence Representation](https://doi.org/10.5281/zenodo.19488084)**                      | Transition from geometry to an internal regulatory variable   | Explains how an internal variable arises from locally available signals and makes regulation possible without direct access to full coherence geometry                                    | **Coherence representation**                           |
| 10  | **[Coherence Representation in Multi-System Regulation](https://doi.org/10.5281/zenodo.19493294)**        | Transition to inter-system regulation                         | Shows how systems can relate regulatory states not through shared geometry but through alignment of regulatory significance order                                                         | **Inter-system order alignment**                       |
| 11  | **[Pre-Symbolic Admissibility in Cognitive Systems](https://doi.org/10.5281/zenodo.19499593)**            | Earliest layer of regulatory selection                        | Formalizes which local discrepancies are admitted to further regulatory processing before representation and before structural updating                                                   | **Pre-symbolic admissibility**                         |
| 12  | **[Restricted Accessibility of Coherence in Cognitive Systems](https://doi.org/10.5281/zenodo.19508182)** | Distinction between geometric coherence and its accessibility | Shows that coherence may be geometrically defined without being regulatorily accessible to the system                                                                                     | **Restricted accessibility of coherence**              |
| 13  | **[Inter-System Conflict Geometry in Cognitive Systems](https://doi.org/10.5281/zenodo.19509685)**        | Formalization of conflict at the inter-system level           | Defines conflict not as disagreement, but as the absence of a shared admissible discrepancy structure sufficient for coordinated regulation                                               | **Conflict geometry**                                  |
| 14  | **[General Theory of Cognitive Structuring](https://doi.org/10.5281/zenodo.19467207)**                    | Synthetic work of the series                                  | Integrates the separate formalizations into a unified theory of stability, constraints, trajectories, invariants, representations, and conflict                                           | **General theory of cognitive structuring**            |


---

#### Branch
[Inner Manifestation Beyond Admissible Processing: A Formal Distinction in Cognitive Systems](https://doi.org/10.5281/zenodo.19583268) — *Zenodo, TR*


---

#### Concept Papers
[Cognitive Evolution Beyond the Single Life Cycle](https://doi.org/10.5281/zenodo.19673721) — *Preprint*

[Coherence Evaluation, Feelings, and Emotions: The Felt Layer of Regulation](https://doi.org/10.5281/zenodo.19588489) — *Zenodo, Concept Paper*

---
I am currently seeking arXiv endorsement in the **cs.AI (Artificial Intelligence)** category in order to submit my work there. If you are able to endorse submissions in this category, or could help me navigate this step, please feel free to contact me by email. I would be very grateful for any assistance.
[https://arxiv.org/auth/endorse?x=Q6E93A](https://arxiv.org/auth/endorse?x=Q6E93A)



#### Links
[Email](mailto:constantinosmol@gmail.com)    [ORCID](https://orcid.org/0009-0006-3144-7237)   [Zenobo](https://zenodo.org/communities/gtc/records)

---

##### Blog
*(posts from _posts)*
