+++
date = "2017-03-07T17:12:30+01:00"
description = ""
taxonomies = "blogging"
title = "Our paper: Large-scale virtual screening on public cloud resources with Apache Spark, got published in the Journal of Cheminformatics"
+++

# Abstract

## Background
Structure-based virtual screening is an in-silico method to screen a target receptor against a virtual molecular library. Applying docking-based screening to large molecular libraries can be computationally expensive, however it constitutes a trivially parallelizable task. Most of the available parallel implementations are based on message passing interface, relying on low failure rate hardware and fast network connection. Google's MapReduce revolutionized large-scale analysis, enabling the processing of massive datasets on commodity hardware and cloud resources, providing transparent scalability and fault tolerance at the software level. Open source implementations of MapReduce include Apache Hadoop and the more recent Apache Spark.

## Results
We developed a method to run existing docking-based screening software on distributed cloud resources, utilizing the MapReduce approach. We benchmarked our method, which is implemented in Apache Spark, docking a publicly available target receptor against ~2.2 M compounds. The performance experiments show a good parallel efficiency (87%) when running in a public cloud environment.

## Conclusion
Our method enables parallel Structure-based virtual screening on public cloud resources or commodity computer clusters. The degree of scalability that we achieve allows for trying out our method on relatively small libraries first and then to scale to larger libraries. Our implementation is named Spark-VS and it is freely available as open source from GitHub (https://github.com/mcapuccini/spark-vs).

Link: http://jcheminf.springeropen.com/articles/10.1186/s13321-017-0204-4
