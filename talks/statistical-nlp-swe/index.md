---
layout: default
title: "Statistical Analysis of Computer Program Text"
---

Statistical Analysis of Computer Program Text
=====

Slides, papers, code for Charles Sutton's talk at<br/>
Amazon, Edinburgh, Wed 26 April 2017


## Abstract

Billions of lines of source code have been written, many of which are freely available on the Internet. This code contains a wealth of implicit knowledge about how to write software that is easy to read, avoids common bugs, and uses popular libraries effectively.

We want to extract this implicit knowledge by analyzing source code text. To do this, we employ the same tools from machine learning and natural language processing that have been applied successfully to natural language text. After all, source code is also a means of human communication.

We present three new software engineering tools inspired by this insight:

Naturalize, a system that learns local coding conventions. It proposes revisions to names and to formatting so as to make code more consistent. A version that uses word embeddings has shown promise toward naming methods and classes.

Data mining methods have been widely applied to summarize the patterns about how programmers invoke libraries and APIs. We present a new method for mining market basket data, based on a simple generative probabilistic model, that resolves fundamental statistical pathologies that lurk in popular current data mining techniques.

HAGGIS, a system that learns local recurring syntactic patterns, which
we call idioms. HAGGIS accomplishes this using a nonparametric
Bayesian tree substitution grammar, and is delicious with whisky
sauce.

## Slides

[Slides as pdf](2017-nlpswe.pdf)

## Papers

The papers that the talk is based on. Please see bibliographies for
works by others:


[Learning Natural Coding Conventions](http://homepages.inf.ed.ac.uk/csutton/publications/naturalize.pdf).
Miltiadis Allamanis, Earl T Barr, Christian Bird and Charles Sutton. In Foundations of Software Engineering
(FSE). 2014.

[Mining Idioms from Source Code](http://homepages.inf.ed.ac.uk/csutton/publications/idioms.pdf).
Miltos Allamanis and Charles Sutton.
In Foundations of Software Engineering
(FSE). 2014.

[Parameter-Free Probabilistic API Mining across GitHub](http://homepages.inf.ed.ac.uk/csutton/publications/fse2016.pdf). Jaroslav Fowkes
and Charles Sutton. In Foundations of Software Engineering
(FSE). 2016.

[Autofolding for Source Code Summarization.](http://arxiv.org/abs/1403.4503)
Jaroslav Fowkes, Razvan Ranca, Miltiadis Allamanis, Mirella Lapata and Charles Sutton. Transactions on Software Engineering. In press. 2017.

## Code

The code and papers are available on github:

* [Naturalize](http://groups.inf.ed.ac.uk/naturalize/)
* [Idiom mining](https://github.com/mast-group/codemining-treelm)
* [Probabilistic API Miner](https://github.com/mast-group/api-mining)
* [TASSAL](https://github.com/mast-group/tassal) for code summarization

For more about our work in this area, please see our [MAST group web page](http://mast-group.github.io/).

## Why am I doing this?

I've written a bit about the philosophy of these pages on my [talks page](../).
