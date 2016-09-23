#!/bin/bash
hugo
docker build -t farmbio/pharmb.io .
