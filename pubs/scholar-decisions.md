# Google Scholar sync: decisions

Scholar profile: https://scholar.google.com/citations?user=hYtGXD0AAAAJ

When syncing, compare every Scholar item against `papers.bib` (fuzzy title match)
**and** against the "Skipped" list below. Only ask Charles about items in neither.
Add new decisions here so the review never has to be redone.

## Rules

- Add real papers (conference, journal, arXiv preprint) that Charles is an author of.
- Workshop papers and tech reports: skip if a full paper on the same work exists,
  **unless** the item has more than ~10 citations on Scholar.
- Skip non-papers: patents, Dagstuhl reports, proceedings front matter, lecture
  notes, datasets, committee messages.
- Big model reports: list on the publications page, never in Selected Publications
  (`top-cited.txt`).
- An arXiv link is enough; no need to store PDFs.
- Get author names from arXiv (Semantic Scholar mangles some, e.g. "Ken-Sen Shi").
  DBLP and Google Scholar detail pages block scripts; use arXiv, Semantic Scholar,
  Crossref and the proceedings sites (papers.nips.cc, proceedings.mlr.press).

## Skipped (Scholar title → reason)

Last full review: 2026-11-14 (202 Scholar items, 26 papers added).

| Scholar title | Reason |
|---|---|
| Modified Family-Vicsek Scaling and Probability Distributions for Brownian Castle Interfaces | Not Charles (a different C. Sutton); removed from Scholar profile |
| Machine learning and multimedia content generation for energy demand reduction (SustainIT 2012) | Charles's call: leave off |
| Type inference as optimization (AIPLANS workshop 2021) | Workshop, 3 cites; full version is OptTyper |
| Data cleaning using probabilistic models of integrity constraints (NIPS 2016 workshop) | Workshop, 4 cites |
| Expectation Propagation in Factor Graphs: A Tutorial | Unpublished tutorial, 1 cite |
| Fast inference and learning with sparse belief propagation (2005) | Tagged `exclude` in old database.bib; superseded by pal06sparse |
| A Bayesian blackboard for information fusion (Fusion 2004) | Charles's call: excluded despite 30 cites (doesn't like it) |
| Feature bagging: Preventing weight undertraining... (UMass TR IR-402, 2005) | Superseded by sutton06reducing; Charles's call: excluded despite 34 cites |
| Image Analysis by Prompting of Machine-Learned Models Using Chain of Thought | Patent |
| Tuning generative models using latent-variable inference | Patent |
| Generating learned representations of digital circuit designs | Patent |
| Prompting Machine-Learned Models Using Chains of Thought | Patent |
| Using Chains of Thought to Prompt Machine-Learned Models Pre-Trained on Diversified Objectives | Patent |
| Learning and Using Property Signatures for Computer Programs | Patent |
| Programming Language Processing (Dagstuhl Seminar 23062) / Dagstuhl Reports | Not a paper |
| Programming with "Big Code" (Dagstuhl Seminar 15472) | Not a paper |
| Proceedings of the 6th ACM SIGPLAN International Symposium on Machine Programming (MAPS'22) | Proceedings front matter |
| Proceedings of the Workshop on Computationally Hard Problems and Joint Inference... (2006) | Proceedings front matter |
| Message from the MSR 2021 Mining Challenge Track Co-Chairs | Not a paper |
| IAML: Dimensionality Reduction; IRDS: Data Mining Process; Introduction to Research in Data Science; Probabilistic Machine Learning | Lecture notes |
| GitHub Java Corpus | Dataset |
| IDEAL household energy dataset (Edinburgh DataShare) | Dataset; the paper is pullinger2021-jg |
| Learning generative models of mid-level structure in natural images (Heess thesis) | Student's thesis, not Charles's paper |
| Compact Explanations of Why Malware is Bad (AI4FM 2015) | Workshop, removed 2026-11-14; superseded by chen16robust / chen16wisec |
| Verifying Anti-Security Policies Learnt from Android Malware Families (2015) | Workshop, removed 2026-11-14; superseded by chen16robust / chen16wisec |
| Amortized inference for latent feature models using variational Russian roulette (NeurIPS 2018 workshop) | Workshop, 1 cite, removed 2026-11-14; superseded by xu2019russian |
| Graph Representations of Python Programs via Source-level Static Analysis | Duplicate of bieber2022python |
| Performance Management of Web Applications in the Cloud; Mining Interesting Itemsets using Submodular Optimization; Adaptive MCMC Methods for Bayesian CRFs; Attacking SpamBayes | Untitled-venue Scholar duplicates of existing entries |

Scholar also lists duplicates/variants of papers already in `papers.bib` under
different titles (e.g. "Houdini" = houdini, "Compressing LSTMs into CNNs" =
geras16blendingws, "Open-vocabulary models for source code" = karampatsis20big_code,
queueing-network papers = sutton10qnet / sutton10aistats). Those are fine to ignore.
