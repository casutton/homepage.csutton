---
layout: default
title: "Machine Learning for Data Exploration and Generation"
---

Machine Learning for Data Exploration and Generation
=====

Slides, papers, code for talk by Charles Sutton


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

Topic modelling has proven to be a highly useful family of methods for data exploration,
but it still requires a large amount of specialized effort to develop a new topic model for
a specific data analysis scenario. I'll present new results on highly scalable inference for latent Dirichlet
allocation based on recently proposed deep learning methods for probabilistic models.

Finally, deep generative models provide powerful tools for distributions over complicated manifolds, such as those of natural images. But many of these methods, including generative adversarial networks (GANs), can be difficult to train, in part because they are prone to mode collapse, which means that they characterize only a few modes of the true distribution. To address this, we introduce VEEGAN, which features a reconstructor network, reversing the action of the generator by mapping from data to noise. Our training objective retains the original asymptotic consistency guarantee of GANs, and can be interpreted as a novel autoencoder loss over the noise. In sharp contrast to a traditional autoencoder over data points, VEEGAN does not require specifying a loss function over the data, but rather only over the representations, which are standard normal by assumption.

## Slides

[Slides as pdf](edintelligence-2017.pdf)

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

[Autoencoding Variational Inference For Topic Models](https://openreview.net/forum?id=BybtVK9lg&noteId=BybtVK9lg). Akash Srivastava and Charles Sutton. International
Conference on Learning Representations, 2017.

[VEEGAN: Reducing Mode Collapse in GANs using Implicit Variational Learning.](https://arxiv.org/abs/1705.07761) Akash Srivastava, Lazar Valkov, Chris Russell, Michael Gutmann and Charles Sutton. Arxiv pre-print. 2017.

## Code

 * Itemset mining: [https://github.com/mast-group/itemset-mining](https://github.com/mast-group/itemset-mining)
 * Sequence mining: [https://github.com/mast-group/sequence-mining](https://github.com/mast-group/sequence-mining)
 * API mining: [https://github.com/mast-group/api-mining](https://github.com/mast-group/api-mining)
 * Neural inference for topic modelling: [https://github.com/akashgit/Neural-Variational-Inference-for-Topic-Models](https://github.com/akashgit/Neural-Variational-Inference-for-Topic-Models)
 
## When/Where

I gave this talk at the EdIntelligence student group in Edinburgh on 14 June 2017.

## Why am I doing this?

I've written a bit about the philosophy of these pages on my [talks page](../).
