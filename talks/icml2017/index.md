---
layout: default
title: "Machine Learning for Data Exploration"
---

Learning Continuous Semantic Representations of Symbolic Expressions 
=====

Slides, papers, code for Charles Sutton's talk at the<br/>
International Conference on Machine Learning (ICML) 2017<br/>
Syndey, Australia, August 2017

## Citation

[Learning Continuous Semantic Representations of Symbolic Expressions](http://arxiv.org/abs/1611.01423). Miltiadis Allamanis, Pankajan Chanthirasegaran, Pushmeet Kohli and Charles Sutton. In Interational Conference on Machine Learning (ICML). 2017.
<p>
   [ <a href="http://arxiv.org/abs/1611.01423">.pdf</a>
     | <a href="javascript:toggle('biballamanis17symbolic', 'bib_link_allamanis17symbolic', 'bib')"  id="bib_link_allamanis17symbolic">bib</a>
 ] 
</p>
<div style="display:none;" id="biballamanis17symbolic"><pre class="bibtex">@inproceedings{allamanis17symbolic,
  author = {Allamanis, Miltiadis and Chanthirasegaran, Pankajan and Kohli, Pushmeet and Sutton, Charles},
  booktitle = {Interational Conference on Machine Learning (ICML)},
  journal = {CoRR},
  title = {Learning Continuous Semantic Representations of Symbolic Expressions},
  year = {2017}
}
</pre></div>


## TL;CE (too long; checked email)

* We want to understand how much of symbolic reasoning we can fit into continuous vectors.
* Turns out this is hard. So, we'll stick to simple expressions, polynomials and boolean formulae.
* Goal: Train a neural network that maps a symbolic expression to a vector
* Loss for training: 
* Makes sense to use a tree structured recurrent neural networks (a la Socher et al). This assigns a vector representation to each subtree of the expression tree. 
* But that doesn't work. To make it work, you need a couple of tricks:
    * Have multiple network layers with a resnet type connection at each node in the tree
	* Use a denoising autoencoder to regularize the triples of (parent, left child, right child) representation
	* We motivate this via an analogy to logical unification, but you can decide whether you believe in this analogy or not.
* Works way better than LSTMs or recurrent neural networks

## Formal Abstract

Combining abstract, symbolic reasoning with continuous neural
reasoning is a grand challenge of representation learning. As a step
in this direction, we propose a new architecture, called neural
equivalence networks, for the problem of learning continuous semantic
representations of algebraic and logical expressions. These networks
are trained to represent semantic equivalence, even of expressions
that are syntactically very different. The challenge is that semantic
representations must be computed in a syntax-directed manner, because
semantics is compositional, but at the same time, small changes in
syntax can lead to very large changes in semantics, which can be
difficult for continuous neural architectures. We perform an
exhaustive evaluation on the task of checking equivalence on a highly
diverse class of symbolic algebraic and boolean expression types,
showing that our model significantly outperforms existing
architectures.


## Slides

[Slides as pdf](semvec-icml2017.pdf)

## Visualizations and Data

We have another web page that contains our 
[data sets and an interactive visualizaton](http://groups.inf.ed.ac.uk/cup/semvec/)
of our learned representations.

## Code

 * Implementation of eqnets on Github: [https://github.com/mast-group/eqnet](https://github.com/mast-group/eqnet)
 
## Why am I doing this?

I've written a bit about the philosophy of these pages on my [talks page](../).
