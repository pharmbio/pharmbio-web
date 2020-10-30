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

<iframe width="560" height="315" src="https://www.youtube.com/embed/96UiejAA41A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br/>
*Video from our automated cell profiling laboratory.*

## Equipment
Our automated cell profiling lab consists of:

Our robotized lab for cell profiling comprises a fully contained environment with monitored climate control, humidity, and ventilation. Equipment includes:

- ImageXpress XLS automated high-content imaging microscope
- Holomonitor label-free phase imaging microscope
- BioMek 4000 liquid handling robot
- OpenTrons OT-2 liquid handling robot
- Liconic STX44 plate incubator
- Ambient plate hotel
- Three plate robots for automatic plate handling (PreciseFlex PF400, Universal Robots UR10e, Automata Eva)
- Biotek 405 LS microplate washer
- Biotek MultiFlo FX microplate dispenser
- ViaFlow 384 automated pipette

### Lab automation software

We are developing an Open Source Automated Robotic System for biological laboratories (AROS, https://github.com/pharmbio/aros) that can be used for research groups who would like to set up custom automated lab installations comprising multiple instruments. We welcome contributions to this project by all interested developers!



### IT-infrastructure

<img src="/img/infrastructure/virtualinfra.png" width="800"/>

Computational equipment includes a networked storage system (240 TB), two local servers (20+24 cores, 160+160 GB RAM), and a local GPU cluster (10 Nvidia graphics cards) to run demanding Deep Learning analysis. We run an OpenStack instance for [external services](https://github.com/pharmbio/services/blob/master/README.md). We run an internal Kubernetes cluster for processing, also connected to the GPU cluster. Our entire virtual infrastructure is defined using Infrastructure-as-Code (IaC) and deployed via [STACKn](https://github.com/scaleoutsystems/stackn), Rancher, Helm, and Ansible. All code for the virtual infrastructure is open source and [available from github](https://github.com/pharmbio).

