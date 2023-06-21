#!/bin/bash

cd src/server

docker build -t back_end . > trash.txt 2>&1
docker run -d --name backEnd back_end > trash.txt

docker exec backEnd pytest -s

docker stop backEnd > trash.txt
docker rm backEnd > trash.txt

rm trash.txt

cd ../..