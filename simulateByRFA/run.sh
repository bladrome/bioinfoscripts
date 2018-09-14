#!/bin/bash
sudo apt install docker.io
sudo service docker start

echo "{ \"registry-mirrors\": [\"https://registry.docker-cn.com\"] }"  > /etc/docker/daemon.json

sudo docker pull meren/anvio

mkdir simulationVdata
git clone https://github.com/merenlab/reads-for-assembly.git
mv reads-for-assembly simulationVdata
containerid=$(sudo docker run -d -it meren/anvio:latest)
sudo docker container attach $containerid
