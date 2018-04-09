---
layout: default
title: "Machine Learning for Data Exploration"
---

Adventures in Neurosymbolic Learning
=====

Slides, papers, code for talk by Charles Sutton


## TL;CE (too long; checked email)

Symbolic AI and differentiable AI ought to be complementary. Symbolic notation can abstractly represent a large set of states that may be perceptually very different. Differentiable AI seems fundamentally better suited for all kinds of pattern recognition tasks. In differentiable AI, gradient descent is inherently a local search, whereas symbolic search can quickly make large jumps within the search space. One could argue that combining these two types of approaches is one of the grand challenges of AI.

I'll talk about two different approaches that we have developed that to combine neural and symbolic methods. At some hugely vague level of abstraction they could be considered dual to each other.

First, we explore the direction of learning continuous vectors that represent symbols. The goal is to develop a deep network that assigns continuous representations of symbolic expressions, based on their meanings. Expressions with similar semantics should have similar continuous representations, even if their syntactic representation is very different. This is an tricky problem because you want the continuous semantics to reflect the syntax (because of compositionality) but not too much (because if you do that, you've only learned syntax). The hope is that this can enable the use of pattern recognition methods to speed up symbolic search. We accomplish this by adding several modern bells-and-whistles to tree-based recursive neural networks.

Second, the dual direction is to use symbols to represent deep networks. One of the most distressing gaps in our knowledge of machine learning is that we don't know how to engineer systems that get better at learning over time. This challenge is sometimes called lifelong learning. Recent work (Gaunt et al, ICML 2017) has proposed tackling lifelong learning by building up neural libraries of networks that can be reused. We aim to show that symbolic program synthesis methods from the programming languages literature are a natural way to learn and combine neural libraries. We focus on *functional* differentiable programs. Modern deep architectures can be represented very compactly by functional programs, so program synthesis selects neural functions to transfer and selects the deep architecture at the same time. Essentially, this can be thought of as program synthesis for a functional subset of chainer/pytorch/eager-mode Tensorflow.

Also I'll try to spend a little bit of time on a new dimensionality reduction method to interpret the predictions of deep models, just because I quite like it.


## Slides

[Slides as pdf](adventures-neurosymbolic.pdf)


## Papers

[Interpreting Deep Classifiers by Visual Distillation of Dark Knowledge](https://arxiv.org/abs/1803.04042).
Kai Xu, Dae-Hoon Park, Yi Chang, Charles Sutton.
arXiv 1803.04042

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

[Synthesis of Differentiable Functional Programs for Lifelong Learning](https://arxiv.org/abs/1804.00218).
Lazar Valkov, Dipak Chaudhari, Akash Srivastava, Charles Sutton, and Swarat Chaudhuri.
arXiv 1804.00218

## Visualizations and Data

We have another web page that contains our
[data sets and an interactive visualizaton](http://groups.inf.ed.ac.uk/cup/semvec/)
of our learned representations.

## Code

 * Implementation of eqnets on Github: [https://github.com/mast-group/eqnet](https://github.com/mast-group/eqnet)

## Image credits

 * Learning curve [https://en.wikipedia.org/wiki/Learning_curve#/media/File:Alanf777_Lcd_fig02.png](https://en.wikipedia.org/wiki/Learning_curve#/media/File:Alanf777_Lcd_fig02.png)

## Why am I doing this?

I've written a bit about the philosophy of these pages on my [talks page](../).
