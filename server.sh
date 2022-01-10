#!/bin/bash

set -x 

docker-compose up -d
docker exec -it rmi-nameserver python3 server.py