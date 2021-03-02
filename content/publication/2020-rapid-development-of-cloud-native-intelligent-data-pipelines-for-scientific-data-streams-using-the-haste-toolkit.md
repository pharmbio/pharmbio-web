+++
title = "Rapid development of cloud-native intelligent data pipelines for scientific data streams using the HASTE Toolkit"
date = 2021-02-24T14:49:00+02:00
doi = ""
url_html = "https://www.biorxiv.org/content/10.1101/2020.09.13.274779v1"
journal = "Gigascience"
author = "Blamey B, Toor S, Dahlö M, Wieslander H, Harrison PJ, Sintorn IM, Sabirsh A, Wählby C, Spjuth O, Hellander A"
volume = "Accepted"
number = ""
art_number = ""
preprint = false
year = "2021"
keywords = ""
document_bibtex_type = ""
abstract = "This paper introduces the HASTE Toolkit, a cloud-native software toolkit capable of partitioning data streams in order to prioritize usage of limited resources. This in turn enables more efficient data-intensive experiments. We propose a model that introduces automated, autonomous decision making in data pipelines, such that a stream of data can be partitioned into a tiered or ordered data hierarchy. Importantly, the partitioning is online and based on data content rather than a priori metadata. At the core of the model are interestingness functions and policies. Interestingness functions assign a quantitative measure of interestingness to a single data object in the stream, an interestingness score. Based on this score, a policy guides decisions on how to prioritize computational resource usage for a given object. The HASTE Toolkit is a collection of tools to adapt data stream processing to this pipeline model. The result is smart data pipelines capable of effective or even optimal use of e.g. storage, compute and network bandwidth, to support experiments involving rapid processing of scientific data characterized by large individual data object sizes. We demonstrate the proposed model and our toolkit through two microscopy imaging case studies, each with their own interestingness functions, policies, and data hierarchies. The first deals with a high content screening experiment, where images are analyzed in an on-premise container cloud with the goal of prioritizing the images for storage and subsequent computation. The second considers edge processing of images for upload into the public cloud for a real-time control loop for a transmission electron microscope."
# --- Pharmb.io custom fields ---
short_summary = ""
users = ["olas"]
projects = [""]
# --- Tentative URL fields ---
url_repo_data = ""
url_repo_paper = ""
url_repo_code = ""
url_repo_notebook = ""
url_tutorial = ""
+++
