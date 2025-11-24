---
date: "2016-09-22T10:39:24+02:00"
title: "Infrastructure"
menu:
  main:
    weight: -200
---

Infrastructure
========

### Automatic Cell Profiling Laboratory

<!--iframe width="560" height="315" src="https://www.youtube.com/embed/96UiejAA41A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe-->



<img src="/img/infra/robot-lab-UR.png" width="800"/>
<br/>
Our workcell for Cell Painting.
<br/>
<br/>

<img src="/img/infra/robot-lab-squid.png" width="800"/>
<br/>
Our workcell for imaging, both widefield (we have multiple Cephla Squid microscopes) and confocal (Nikon).
<br/>
<br/>


<img src="/img/infra/robot-lab-maak.png" width="800"/>
<br/>
Our experimental setting for autonomous drug perturbations.
<br/>
<br/>

<img src="/img/infra/cp-cells.png" width="800"/>
<br/>
Image of U2OS cells after cell painting. Our capacity is 20,000 experiments per week corresponding to ca 200,000 images.
<br/>
<br/>






### Lab automation software

We are developing an Open Source Automated Robotic System for biological laboratories (https://github.com/pharmbio/robotlab) that can be used for research groups who would like to set up custom automated lab installations comprising multiple instruments. We welcome contributions to this project by all interested developers!



### IT-infrastructure

<!--img src="/img/infrastructure/virtualinfra.png" width="800"/-->

Computational equipment includes networked storage (440 TB), CPU (128 cores, 160+160 GB RAM), 2 GPU clusters (10+4 Nvidia graphics cards) to run demanding Deep Learning analysis. We run a local Kubernetes cluster for provisioning pods to our team members and collaborators. Our entire virtual infrastructure is defined using Infrastructure-as-Code and [available from github](https://github.com/pharmbio).

