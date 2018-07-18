#!/bin/bash

secret=$1

if [[ -z $secret ]]; then
   printf "ERROR : Must specify slave secret.\n"
   printf "USAGE : slave.sh <secret>\n\n"
   exit 1
fi

docker run \
  --network jenkins-nw \
  --name slave \
  -d \
  lnarmour/parric:jenkins-slave \
  -url http://jenkins:8080 \
  -workDir "/home/jenkins/slave" \
  $secret \
  slave

sleep 3

if [[ -n $(docker ps -f name=slave -q) ]]; then
   printf "SUCCESS : Created 'slave' successfully.\n"
else
   printf "ERROR : Couldn't create 'slave'. See 'docker logs slave'.\n\n"
   exit 1
fi
