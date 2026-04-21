---
layout: home
title: General Theory of Cognitive Structuring
description: Formal framework for regulatory dynamics in cognitive architectures under bounded resources.
keywords: cognitive architecture, regulatory dynamics, structural admissibility, invariant-based modeling, coherence geometry, overload memory, trajectory dependence, pre-symbolic filtering, structural compression, identity as attractor, multi-system regulation, order alignment, partial observability, bounded rationality, theoretical cognitive science, AI safety, complex systems, dynamical systems, hysteresis, formal methods, open science
---

**Author:** [Kostiantyn Osmolovskyi](https://orcid.org/0009-0006-3144-7237)  
**Affiliation:** Independent Researcher, Ukraine  
**Contact:** [constantinosmol@gmail.com](mailto:constantinosmol@gmail.com)  
**Zenodo Community:** [https://zenodo.org/communities/gtc](https://zenodo.org/communities/gtc)

---

## Overview

This open series presents a formal, substrate-independent framework for analyzing regulatory dynamics in cognitive architectures operating under bounded resources. The theory introduces a unified mathematical language for describing how structural constraints, overload accumulation, trajectory-dependent regulation, and layered admissibility conditions govern stability, structural change, and the emergence of persistent behavioral patterns (identity) across biological, artificial, and complex adaptive systems.

Core distinction: **geometric coherence ≠ regulatory accessibility ≠ structural updating**.

---

## Minimal Reading Path

For first-time readers:

1. [2026-1: General Theory of Cognitive Structuring](https://doi.org/10.5281/zenodo.xxxxxxx) — unifying language, layered admissibility
2. [2026-2: Coherence Evaluation](https://doi.org/10.5281/zenodo.xxxxxxx) — geometry: coherence as distance to stability region
3. [2026-3: Structural Admissibility](https://doi.org/10.5281/zenodo.xxxxxxx) — operator A(·), phase space (T, L)
4. [2026-5: Trajectory-Dependent Regulation](https://doi.org/10.5281/zenodo.xxxxxxx) — hysteresis, drift to boundary, concentration near minimal overload

Full corpus: read sequentially 2026-1 → 2026-14. Definitions and axioms are built incrementally.

---

## Key Concepts

- `Invariants`: historically constituted architectural constraints
- `Coherence`: geometric distance to invariant-induced stability region
- `Structural tension`: instantaneous regulatory pressure (K + C)
- `Overload memory`: trajectory-dependent accumulation of non-compensated tension
- `Pre-symbolic admissibility`: filter determining which discrepancies enter regulatory processing
- `Coherence representation`: internal regulatory variable constructed from admissible signals
- `Structural compression`: mechanism for invariant formation that reduces expected overload
- `Identity as attractor`: persistent low-overload region emerging from bounded regulation
- `Order alignment`: condition for multi-system co-regulation without shared geometry

---

## Code & Reproducibility

Minimal Python simulations accompany relevant reports to illustrate core mechanisms (e.g., trajectory dependence). Parameters are explicitly documented. Simulations are strictly illustrative, not exhaustive computational studies.

- [`assets/trajectory_regulation_v2.py`](assets/trajectory_regulation_v2.py) — minimal demo of trajectory-dependent regulation

```bash
pip install numpy matplotlib
python assets/trajectory_regulation_v2.py
