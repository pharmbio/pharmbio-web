+++
title = "Laeeq Ahmed successfully defended his PhD thesis: 'Scalable Analysis of Large Datasets in Life Sciences'"
description = "TBC"
date = "2019-12-03T13:00:00+01:00"
taxonomies = "blogging"
teaser_image = "/img/laeeqthesis/laeeq-thumb.png"
+++



<img style="float: right; width: 150px;" src="/img/laeeqthesis/laeeq-thumb.png">

<img src="/img/laeeqthesis/laeeq-book.png" style="float: right; width: 37%; margin: 1em 0 1em 2em; clear: both; box-shadow: 2px 2px 12px rgb(0,0,0,0.25);"/>


Today, [Laeeq Ahmed](/people/laeeq) who is affiliated with the group successfully defended his thesis, titled:<br>
_"[Scalable Analysis of Large Datasets in Life Sciences](urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-261683)"_

 We congratulate Laeeq for his success and wish him well in his future career! Laeeq is already working as Data Scientist at Scania.



- **Supervisor:** [Prof. Erwin Laure](https://www.kth.se/profile/erwinl), Royal Institute of Technology, Stockholm
- **Co-Supervisor:** [Assoc Prof. Ola Spjuth](/people/olas), Uppsala University
- **Co-supervisor:** [Dr Åke Edlund](https://www.linkedin.com/in/aaked), Chief Domain Architect, Analytics BI & AI at Telia.


## Thesis abstract

We are experiencing a deluge of data in all fields of scientific and business research, particularly in the life sciences, due to the development of better instrumentation and the rapid advancements that have occurred in information technology in recent times. There are major challenges when it comes to handling such large amounts of data. These range from the practicalities of managing these large volumes of data, to understanding the meaning and practical implications of the data.

In this thesis, I present parallel methods to efficiently manage, process, analyse and visualize large sets of data from several life sciences fields at a rapid rate, while building and utilizing various machine learning techniques in a novel way. Most of the work is centred on applying the latest Big Data Analytics frameworks for creating efficient virtual screening strategies while working with large datasets. Virtual screening is a method in cheminformatics used for Drug discovery by searching large libraries of molecule structures. I also present a method for the analysis of large Electroencephalography data in real time. Electroencephalography is one of the main techniques used to measure the brain electrical activity.

First, I evaluate the suitability of Spark, a parallel framework for large datasets, for performing parallel ligand-based virtual screening. As a case study, I classify molecular library using prebuilt classification models to filter out the active molecules. I also demonstrate a strategy to create cloud-ready pipelines for structure-based virtual screening. The major advantages of this strategy are increased productivity and high throughput. In this work, I show that Spark can be applied to virtual screening, and that it is, in general, an appropriate solution for large-scale parallel pipelining. Moreover, I illustrate how Big Data analytics are valuable in working with life sciences datasets.

Secondly, I present a method to further reduce the overall time of the structured-based virtual screening strategy using machine learning and a conformal-prediction-based iterative modelling strategy. The idea is to only dock those molecules that have a better than average chance of being an inhibitor when searching for molecules that could potentially be used as drugs. Using machine learning models from this work, I built a web service to predict the target profile of multiple compounds against ready-made models for a list of targets where 3D structures are available. These target predictions can be used to understand off-target effects, for example in the early stages of drug discovery projects.

Thirdly, I present a method to detect seizures in long term Electroencephalography readings - this method works in real time taking the ongoing readings in as live data streams. The method involves tackling the challenges of real-time decision-making, storing large datasets in memory and updating the prediction model with newly produced data at a rapid rate. The resulting algorithm not only classifies seizures in real time, it also learns the threshold in real time. I also present a new feature "top-k amplitude measure" for classifying which parts of the data correspond to seizures. Furthermore, this feature helps to reduce the amount of data that needs to be processed in the subsequent steps.

- [Fulltext is available in DiVA](urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-261683)

## Papers in thesis

**Paper 1:** [Using Iterative MapReduce for Parallel Virtual Screening](http://localhost:1313/publication/2013-mapreduce-vs/)<br>
Laeeq Ahmed, Ake Edlund, Erwin Laure and Ola Spjuth<br>
In Cloud Computing Technology and Science (CloudCom), 2013 IEEE 5th International Conference on (Vol. 2, pp. 27- 32)

**Paper 2:** [Large-scale virtual screening on public cloud resources with Apache Spark](http://localhost:1313/publication/2017-virtual-screening-spark/)<br>
Marco Capuccini, Laeeq Ahmed, Wesley Schaal, Erwin Laure and Ola Spjuth<br>
Journal of cheminformatics, 9(1), 15.

**Paper 3:** [Efficient iterative virtual screening with Apache Spark and conformal prediction](http://localhost:1313/publication/2018-iterative-virtual-screening-spark-conformal-prediction/)<br>
Laeeq Ahmed, Valentin Georgiev, Marco Capuccini, Salman Toor, Wesley Schaal, Erwin Laure and Ola Spjuth<br>
Journal of cheminformatics, 10(1), 8.

**Paper 4:** Predicting Target Profiles with Confidence as a Service using Docking Scores<br>
Laeeq Ahmed, Hiba Alogheli, Staffan Arvidsson, Arvid Berg, Jonathan Alvarsson, Wesley Schaal, Erwin Laure and Ola Spjuth<br>
Manuscript submitted

**Paper 5:** [Parallel Real Time Seizure Detection in Large EEG Data](http://www.scitepress.org/DigitalLibrary/Link.aspx?doi=10.5220/0005875502140222)<br>
Laeeq Ahmed, Ake Edlund, Erwin Laure, and Stephen Whitmarsh<br>
In Proceedings of the International Conference on Internet of Things and Big Data, 214-222, 2016, Rome, Italy



## Faculty Opponent

- [Professor Vincent Breton](https://www.linkedin.com/in/vincent-breton-88880b5?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BW%2FQkvHi1S9ColwwLsBhGPg%3D%3D), Research Director Vincent Breton, French National Center for Scientific Research

## Examination committee

- [Dr. Samuel Flores](https://www.su.se/english/profiles/sflor-1.341350), Department of Biochemistry and Biophysics, Stockholm University, Sweden
- [Dr. Jessica Lindvall](https://nbis.se/about/staff/jessica-lindvall/), National Bioinformatics Infrastructure Sweden (NBIS)
- [Prof. Panagiotis Papapetrou](https://papapetrou.blogs.dsv.su.se/), Department of Computer and Systems Sciences, Stockholm University, Sweden



<img src="/img/laeeqthesis/IMG_0998.jpeg">

<img src="/img/laeeqthesis/IMG_1004.jpeg">

<img src="/img/laeeqthesis/IMG_1015.jpeg">

<img src="/img/laeeqthesis/IMG_1021.jpeg">

