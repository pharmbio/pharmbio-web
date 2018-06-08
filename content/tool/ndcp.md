+++
date = "2016-11-01T15:31:37+01:00"
description = "Non-Disclosed Conformal Prediction - aggregate models without disclosing the datasets between parties."
maintenance_status = "inhouse"
taxonomies = ""
title = "NDCP"
url_documentation = ""
url_github = "https://github.com/pharmbio/nondisc-acp"
url_publication = ""
url_website = ""
weight = 0
+++

# NDCP: Non-Disclosed Conformal Prediction
Aggregated Conformal Prediction on non-disclosed dataset for ligand-based modeling

This is an implementation of Aggregated Conformal Prediction as described in Carlsson et al 2014 (https://link.springer.com/chapter/10.1007/978-3-662-44722-2_25) but in a distributed setting without disclosing data between the aggregated parties.

## Background
It is a common objective for different organizations to be able to contribute to improved predictive models, such as in pre-competitive alliances, but there is often problems with sharing internal data between the parties. One example is in the pharmaceutical industry, where predictions on existing data (such as measured assays of various hazard endpoints for chemical compounds) constitute valuable assets and it would be desirable for all companies to have as good predictive models as possible; but sharing data between companies is usually not so easy.

## Method
The idea of the method is that the different parties train an individual model of their local data, and make this available as a web service accepting a SMILES as input, and delivers results in form of p-values (one per each class in the classification case), and a prediction interval (in the regression case). No other information is transferred over the network, making the implementation preserve privacy completely. The results from the contributing parties is then merged as described in Carlsson et al 2014 (https://link.springer.com/chapter/10.1007/978-3-662-44722-2_25) to yield predictions with lower variance and improved efficiency.

## Usage
TBC

## Implementation
The implementation uses CPSign (http://cpsign-docs.genettasoft.com/) as the underlying modeling method. A license is required but these are generously provided by GenettaSoft.

