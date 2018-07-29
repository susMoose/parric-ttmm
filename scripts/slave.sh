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
  lnarmour/parric:jenkins-slave-eclipse-1.0 \
  -url http://jenkins:8080 \
  -workDir "/home/jenkins/slave" \
  $secret \
  slave

sleep 10

docker exec -d slave Xvfb :1 -screen 0 1024x768x24
docker exec -d slave /home/jenkins/eclipse/eclimd -b

if [[ -n $(docker ps -f name=slave -q) ]]; then
   printf "SUCCESS : Created 'slave' successfully.\n"
else
   printf "ERROR : Couldn't create 'slave'. See 'docker logs slave'.\n\n"
   exit 1
fi
