---
layout: default
title: "Understanding and Interpreting Deep Learning"
---

Understanding and Interpreting Deep Learning
=====

Slides, papers, code for talk by Charles Sutton
at Huawei Shenzhen, December 2017

## Abstract

Deep learning has raised the state of the art throughout artificial intellgience,
including in computer vision, speech processing, and natural language processing.
However, a barrier to applying deep models more widely in practice is that it is difficult
for people to understand *why* a deep network is making the predictions that it does.
This makes it difficult to apply deep learning to mission critical applications
because without having a human understanding of the operation of the network,
it is difficult to offer a guarantee that the network will not make bad mistakes
in deployment.

In this talk, I will present our recent work in *deep generative models*,
which is a family of methods that combine deep methods with 
interpretable representations from probabilistic machine learning.
This yields methods that combine the power of deep learning methods for perceptual 
data with the engineering benefits of interpretable representations.
First, topic modelling has proven to be a highly useful family of methods for data exploration,
but it still requires a large amount of specialized effort to develop a new topic model for
a specific data analysis scenario. I'll present new results on highly scalable inference for latent Dirichlet
allocation based on recently proposed deep learning methods for probabilistic models.

Finally, deep generative models provide powerful tools for distributions over complicated manifolds, such as those of natural images. But many of these methods, including generative adversarial networks (GANs), can be difficult to train, in part because they are prone to mode collapse, which means that they characterize only a few modes of the true distribution. To address this, we introduce VEEGAN, which features a reconstructor network, reversing the action of the generator by mapping from data to noise. Our training objective retains the original asymptotic consistency guarantee of GANs, and can be interpreted as a novel autoencoder loss over the noise. In sharp contrast to a traditional autoencoder over data points, VEEGAN does not require specifying a loss function over the data, but rather only over the representations, which are standard normal by assumption.

## Slides

Slides will be added here in due course.

## Papers

For more details about this work, please see our papers:

[Autoencoding Variational Inference For Topic Models](https://openreview.net/forum?id=BybtVK9lg&noteId=BybtVK9lg). Akash Srivastava and Charles Sutton. International
Conference on Learning Representations (ICLR) 2017.

[VEEGAN: Reducing Mode Collapse in GANs using Implicit Variational Learning.](https://arxiv.org/abs/1705.07761) Akash Srivastava, Lazar Valkov, Chris Russell, Michael Gutmann and Charles Sutton. Advances in Neural Information Processing Systems (NIPS) 2017.

## Code


 * Neural inference for topic modelling: [https://github.com/akashgit/Neural-Variational-Inference-for-Topic-Models](https://github.com/akashgit/Neural-Variational-Inference-for-Topic-Models)

 * VEEGAN [https://akashgit.github.io/VEEGAN/](https://akashgit.github.io/VEEGAN/)

## Why am I doing this?

I've written a bit about the philosophy of these pages on my [talks page](../).
