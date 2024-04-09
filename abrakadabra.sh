#!/bin/bash
docker rm -f some-mysql
docker rm -f some-app
docker rm -f some-nginx

docker image rm doc-app
docker image rm doc-mysql

docker build -t  doc-app -f Dockerfile-app .
docker build -t  doc-mysql -f Dockerfile-mysql .
docker pull nginx
docker puul mysql

docker network create backend
docker network create frontend


docker run -d --name some-mysql --network backend  -v ./dump.sql:/docker-entrypoint-initdb.d/dump.sql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=orgabay  mysql:latest


#docker run -d --name some-mysql -e MYSQL_ROOT_PASSWORD_FILE=root -e MYSQL_DATABASE=orgabay --network backend -v mysql-vol:/var/lib/mysql  doc-mysql 
# -v ./mysql-vol:/vol

docker run -d --name some-app --network backend --network frontend -p 5000:5000 -v ./app-vol:/vol doc-app

docker run -d --name some-nginx --network frontend -p 80:80 -v ./default.conf:/etc/nginx/conf.d/default.conf -v ./nginx-vol:/vol nginx

# -v./mysql-dump:/docker-entrypoint-initdb.d
# docker run -d --name some-mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=orgabay -v mysql-vol:/var/lib/mysql -v ./vol:/vol doc-mysql 


