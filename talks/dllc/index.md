---
layout: default
title: "Deep Learning, Language, and Code"
---

# Deep Learning, Language, and Code: From Methodology to Applications and Back

Slides, papers, code for talk by Charles Sutton

## Slides

[Slides as pdf](dllc.pdf)

## TL;CE (too long; checked email)

There are three main sections to the talk:

* CRAIC: Learning to identify uninformative comments
    * We want to help developers to write better comments
    by steering them away from comments that don't add any value
    * Lots of software development authorities admonish against comments
      that word-for-word repeat the code.
    * How to detect these? Here is where deep learning comes in.
    * Sequence-to-sequence model predicts comment sentence from code
    * Basically, if my deep learning method can predict your comment,
    then probably your comment wasn't very good.
    * Good agreement with human judgments. Also we find Javadoc comments
    are much easier to predict!
* VEEGAN:
    * Deep generative models are great new tools for distributions over complicated manifolds.
    * We want to fix the problem of to mode collapse, which happens when a model,
    like a generative adversarial network (GANs) only learns to produce a few modes of the true distribution.
    * We address this by adding a cyclic consistency. GANs map random noise
    to data. We add a reconstructor like in an autoencoder which maps data to noise.
    Cyclic consistency means if you map noise --> data --> noise, you should
    get the same noise distribution that you started with.
    * The training objective has an interesting variational interpretation.
    The generator of the GAN becomes the approximating distribution
    in the variational argument.
    * There were lots of autoencoder + GAN papers happening at around the same
    time as ours. A nice bit about ours is that unlike a standard autoencoder,
     VEEGAN does not require specifying a loss function over the data, but rather only over the representations, which are standard normal by assumption.
* Continuous Representations of Symbolic Expressions
   * Speculative motivation: How much of symbolic logical reasoning
      can we reproduce using neural perceptual learning?
    * Out step: Let's map symbolic expressions to continuous semantics
    We want the semantics to retain information about equivalence
    * Tree-based networks seem natural here, but they tend to key on syntactic similarity rather than semantic
    * Our method is called <em>equivalence networks</em> (EqNets)
    * We add a regularization term, <em>subexpression forcing,</em> that requires that child semantics be predictable from parents and siblings. This is inpsired by what happens in symbolic logics via, e.g., unification.
    * Sequence-to-sequence, tree neural networks, etc., do not work well for this problem, but subexpression forcing gives a big improvement.
* Houdini (brief mention)

## Papers

Deep Learning to Detect Redundant Method Comments.
Annie Louis, Santanu Dash, Earl T Barr, and Charles Sutton.
2018

[VEEGAN: Reducing Mode Collapse in GANs using Implicit Variational Learning.](https://arxiv.org/abs/1705.07761) Akash Srivastava, Lazar Valkov, Chris Russell, Michael Gutmann and Charles Sutton. Advances in Neural Information Processing Systems (NIPS) 2017.

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

* *VEEGAN*: [Code and data for VEEGAN]()

* *Eqnets*: We have another web page that contains our
[data sets and an interactive visualizaton](http://groups.inf.ed.ac.uk/cup/semvec/)
of our learned representations.

 * *Eqnets*: Implementation of eqnets on Github: [https://github.com/mast-group/eqnet](https://github.com/mast-group/eqnet)

## Why am I doing this?

I've written a bit about the philosophy of these pages on my [talks page](../).
