---
layout: default
title: "Learning for Programs"
---

# Learning for Programs: Connecting code, statistics, semantics, and language

Slides, papers, code for talk by Charles Sutton

## Slides

[Slides as pdf](learning4code.pdf)

## Abstract


Billions of lines of source code have been written, many of which are freely available on the Internet. This code contains a wealth of implicit knowledge about how to write software that is easy to read, uses popular libraries effectively, and avoids common bugs. There has been a recent trend in applying machine learning to find patterns in large codebases, which can then be used to inform various applications in software engineering and programming languages.

The first wave of applications in the area of machine learning for code primarily represented code at the token level, e.g., learning statistical dependencies between names that are used together in an expression.  But code does not appear alone in a vacuum, but appears with other artifacts like documentation, and has semantics that are well-understood. Both of these resources provide information that can be used to develop more advanced tools for program analysis. I will describe two methods in this vein: one that aims to help developers improve documentation using a model of comments and code, and one that aims to identify local semantic patterns in software, such as for-loops that implement map and reduce operations, by combining program abstractions with a nonparametric Bayesian analysis.

Finally, I'll discuss a new application of "learning for code"  back into machine learning itself. Lifelong learning is the challenge of engineering learning systems that improve their ability to learn over time by being exposed to a variety of different learning tasks. Recent work (Gaunt et al, ICML 2017) has proposed tackling lifelong learning by building up neural libraries of networks that can be reused. We show that neural libraries can be naturally represented using functional programming and symbolic program synthesis. Modern deep architectures can be represented very compactly by functional programs, so program synthesis selects neural functions to transfer and selects the deep architecture at the same time. Essentially, this can be thought of as program synthesis for a functional subset of chainer/pytorch/eager-mode Tensorflow.

## Papers

[Mining Semantic Loop Idioms from Big Code](http://groups.inf.ed.ac.uk/cup/semantic-idioms/).
Miltiadis Allamanis, Earl T. Barr, Chris Bird, Premkumar Devanbu, Mark Marron,  and Charles Sutton.
Web site contains link to technical report and data.

Deep Learning to Detect Redundant Method Comments.
Annie Louis, Santanu Dash, Earl T Barr, and Charles Sutton.
2018

[Synthesis of Differentiable Functional Programs for Lifelong Learning](https://arxiv.org/abs/1804.00218).
Lazar Valkov, Dipak Chaudhari, Akash Srivastava, Charles Sutton, and Swarat Chaudhuri.
arXiv 1804.00218

## Visualizations and Data

* *VEEGAN*: [Code and data for VEEGAN](https://akashgit.github.io/VEEGAN/)
* *Eqnets*: We have another web page that contains our
[data sets and an interactive visualizaton](http://groups.inf.ed.ac.uk/cup/semvec/)
of our learned representations.
 * *Eqnets*: Implementation of eqnets on Github: [https://github.com/mast-group/eqnet](https://github.com/mast-group/eqnet)

## Why am I doing this?

I've written a bit about the philosophy of these pages on my [talks page](../).
