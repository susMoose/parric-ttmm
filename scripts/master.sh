#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "ERROR : This script must be run as root"
   exit 1
fi

type docker >/dev/null 2>&1 || echo >&2 "ERROR : Can't find 'docker', aborting."

# create docker network so containers can talk to eachother by container name.
network_name=jenkins-nw
network_id=$(docker network ls -f name=$network_name -q)
if [[ -z "$network_id" ]]; then
   docker network create $network_name
fi

# get docker images
docker pull lnarmour/parric:jenkins-master
docker pull lnarmour/parric:jenkins-slave

# start the jenkins master container
# - mounts the $HOME/jenkins as jenkins_home inside container so container can
#   be restarted without losing any configuration
# - the docker.sock is needed to let jenkins master talk to host docker daemon
#   to start up additonal containers (e.g. additional build agents)
docker run \
  -u root \
  --rm \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v /opt/jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --network jenkins-nw \
  --name jenkins \
  lnarmour/parric:jenkins-master

sleep 3

if [[ -n $(docker ps -f name=jenkins -q) ]]; then
   printf "SUCCESS : Created 'jenkins' successfully.\n"
   printf "SUCCESS : Available at 'http://ci-parric.ddns.net:8080'.\n"
else
   printf "ERROR : Couldn't create 'jenkins' master. See 'docker logs jenkins'.\n\n"
   exit 1
fi
