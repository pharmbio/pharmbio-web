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

<img src="/img/infrastructure/cellab.png" width="800"/>

We have established an automated lab for cell profiling with a high-content microscope (ImageXpress XLS), a liquid handler robot (BioMek 4000), a plate incubator (Liconic STX44), plate hotel (Ambient), and a plate robot (PreciseFlex PF400) for automatic plate handling. Apart from the robotized equipment, we have access to a fully equipped cell- and biochemistry lab and a wide range of relevant cell lines.




### IT-infrastructure

<img src="/img/infrastructure/virtualinfra.png" width="800"/>

Computational equipment includes a networked storage system (240 TB), two local servers (20+24 cores, 160+160 GB RAM), and a local GPU cluster (10 Nvidia graphics cards) to run demanding Deep Learning analysis. We run an OpenStack instance for [external services](https://github.com/pharmbio/services/blob/master/README.md). We run an internal Kubernetes cluster for processing, also connected to the GPU cluster. Our entire virtual infrastructure is defined using Infrastructure-as-Code (IaC) and deployed via KubeNow, Rancher, Helm, and Ansible.

