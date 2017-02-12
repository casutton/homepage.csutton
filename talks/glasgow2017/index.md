---
layout: default
title: "Machine Learning for Data Exploration"
---

Machine Learning for Data Exploration
=====

Slides, papers, code for Charles Sutton's talk at<br/>
University of Glasgow<br/>
Mon 23 January 2017


## Abstract

One of the first and most fundamental tasks in data mining is what we might call data understanding.
Given a dump of data, what's in it? If modern machine learning methods are effective at finding
patterns in data, then they should be effective at summarizing data sets so as to help
data analysts develop a high-level understanding of them.

I'll describe several different approaches to this problem. First I'll describe a new approach
to classic data mining problems, such as frequent itemset mining and frequent sequence mining,
using a new principled model from probabilistic machine learning. Essentially, this casts the problem
of pattern mining as one of structure learning in a probabilistic model. I'll describe an application
to summarizing the usage of software libraries on Github.

A second attack to this general problem is based on cluster analysis. A good clustering can help a data analyst
to explore and understand a data set, but what constitutes a good clustering may depend on domain-specific
and application-specific criteria. I'll describe a new framework for interactive clustering that allows
the analyst to examine a clustering and guide it in a way that is more useful for their information need.

Finally, topic modelling has proven to be a highly useful family of methods for data exploration,
but it still requires a large amount of specialized effort to develop a new topic model for
a specific data analysis scenario. I'll present new results on highly scalable inference for latent Dirichlet
allocation based on recently proposed deep learning methods for probabilistic models.

## Slides

[Slides as pdf](glasgow-ir-seminar-2017.pdf)

Image credits:
[Wikipedia](https://en.wikipedia.org/w/index.php?curid=8201514).

## Papers

The papers that the talk is based on. Please see bibliographies for
works by others:

[A Bayesian Network Model for Interesting Itemsets](http://homepages.inf.ed.ac.uk/csutton/publications/pkdd2016-iim.pdf).
Jaroslav Fowkes and Charles Sutton. In European Conference on Machine Learning and
Principles and Practice of Knowledge Discovery (ECML-PKDD). 2016.

[A Subsequence Interleaving Model for Sequential Pattern
Mining](http://homepages.inf.ed.ac.uk/csutton/publications/kdd2016-subsequence-interleaving.pdf).
Jaroslav Fowkes and Charles Sutton. In ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining. 2016.

[Parameter-Free Probabilistic API Mining across GitHub](http://homepages.inf.ed.ac.uk/csutton/publications/fse2016.pdf). Jaroslav Fowkes
and Charles Sutton. In Foundations of Software Engineering
(FSE). 2016.

[Clustering with a Reject Option: Interactive Clustering as Bayesian Prior Elicitation.](http://arxiv.org/abs/1602.06886) Akash Srivastava, James Zou, Ryan P. Adams and Charles Sutton. In Workshop on Human Interpretability in Machine Learning Workshop on Human Interpretability in Machine Learning (co-located with ICML). 2016.

[Neural Variational Inference For Topic Models](http://openreview.net/forum?id=B1vRTeqxg). Akash Srivastava and Charles Sutton. In Open Review submission. 2016.

## Code

 * Itemset mining: [https://github.com/mast-group/itemset-mining](https://github.com/mast-group/itemset-mining)
 * Sequence mining: [https://github.com/mast-group/sequence-mining](https://github.com/mast-group/sequence-mining)
 * API mining: [https://github.com/mast-group/api-mining](https://github.com/mast-group/api-mining)
 * Neural inference for topic modelling: [https://github.com/akashgit/Neural-Variational-Inference-for-Topic-Models](https://github.com/akashgit/Neural-Variational-Inference-for-Topic-Models)
 
## Why am I doing this?

I've written a bit about the philosophy of these pages on my [talks page](../).
