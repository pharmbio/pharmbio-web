+++
title = "Two papers accepted for COPA2019 and published in PMLR"
description = "TBC"
date = "2019-08-20T01:14:00+01:00"
taxonomies = "blogging"
teaser_image = "/img/thumbs/copa-pmlr-thumb.png"
+++

<a href="https://pharmb.io/publication/2019-split-knowledge-transfer-learning-under-privileged-information/" target="_blank"><img src="/img/copa2019-split-kt-lupi.png" style="float: right; width: 37%; margin: 0 0 1em 2em; clear: both; box-shadow: 2px 2px 12px rgb(0,0,0,0.25);"/></a>

We are very proud to announce that we this year had 2 papers accepted to the [8th Symposium on Conformal and Probabilistic Prediction with Applications](http://clrc.rhul.ac.uk/copa2019)! Ola Spjuth will present the papers in Golden Sands, Bulgaria on 9-11 sept 2019.

<br>


#### Paper 1: Split Knowledge Transfer in Learning Under Privileged Information Framework

Gauraha, N., Söderdahl, F. and Spjuth, O.. <br>
Split Knowledge Transfer in Learning Under Privileged Information Framework.<br>
*Proceedings of Machine Learning Research (PMLR)*. 105, 43-52. (2019).<br>
URL: [https://proceedings.mlr.press/v105/gauraha19a.html](https://proceedings.mlr.press/v105/gauraha19a.html)



**ABSTRACT**

Learning Under Privileged Information (LUPI) enables the inclusion of additional (privileged) information when training machine learning models, data that is not available when making predictions. The methodology has been successfully applied to a diverse set of problems from various fields. SVM+ was the first realization of the LUPI paradigm which showed fast convergence but did not scale well. To address the scalability issue, knowledge transfer approaches were proposed to estimate privileged information from standard features in order to construct improved decision rules. Most available knowledge transfer methods use regression techniques and the same data for approximating the privileged features as for learning the transfer function. Inspired by the cross-validation approach, we propose to partition the training data into K folds and use each fold for learning a transfer function and the remaining folds for approximations of privileged features—we refer to this as split knowledge transfer. We evaluate the method using four different experimental setups comprising one synthetic and three real datasets. The results indicate that our approach leads to improved accuracy as compared to LUPI with standard knowledge transfer.

<br>

#### Paper 2: Combining Prediction Intervals on Multi-Source Non-Disclosed Regression Datasets

<a href="https://pharmb.io/publication/2019-combining-prediction-intervals-multi-source-non-disclosed-regression-datasets/" target="_blank"><img src="/img/copa2019-combining-multisource-intervals.png" style="float: right; width: 37%; margin: 1em 0 1em 2em; clear: both; box-shadow: 2px 2px 12px rgb(0,0,0,0.25);"/></a>

Spjuth O., Brännström R.C., Carlsson L. and Gauraha, N.<br>
Combining Prediction Intervals on Multi-Source Non-Disclosed Regression Datasets.<br>
*Proceedings of Machine Learning Research (PMLR)*. 105, 53-65. (2019).<br>
URL: [https://proceedings.mlr.press/v105/spjuth19a.html](https://proceedings.mlr.press/v105/spjuth19a.html)

**ABSTRACT**

Conformal Prediction is a framework that produces prediction intervals based on the output from a machine learning algorithm. In this paper we explore the case when training data is made up of multiple parts available in different sources that cannot be pooled. We here consider the regression case and propose a method where a conformal predictor is trained on each data source independently, and where the prediction intervals are then combined into a single interval. We call the approach Non-Disclosed Conformal Prediction (NDCP), and we evaluate it on a regression dataset from the UCI machine learning repository using support vector regression as the underlying machine learning algorithm, with varying number of data sources and sizes. The results show that the proposed method produces conservatively valid prediction intervals, and while we cannot retain the same efficiency as when all data is used, efficiency is improved through the proposed approach as compared to predicting using a single arbitrarily chosen source.