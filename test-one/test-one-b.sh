#!/bin/bash
sudo docker build . -t reactdocker ;
sudo docker run -it -p 8080:80 --name reactdockerized reactdocker;