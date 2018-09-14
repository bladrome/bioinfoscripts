#!/bin/bash
sudo apt install docker.io
sudo service docker start

echo "{ \"registry-mirrors\": [\"https://registry.docker-cn.com\"] }"  > /etc/docker/daemon.json

sudo docker pull meren/anvio

mkdir simulationVdata
git clone https://github.com/merenlab/reads-for-assembly.git
mv reads-for-assembly simulationVdata
simulationVdata=$(readlink -f simulationVdata)
sudo docker run -d -v $simulationVdata:/simulationVdata -it meren/anvio:latest #apt update
containerid=$(sudo docker ps -a | head -n 2 | tail -n 1 | cut -d ' ' -f 1)
sudo docker container attach $containerid
sudo docker exec -it $containerid apt update
sudo docker exec -it $containerid apt install -y vim
