FROM ubuntu

RUN apt-get update \
    DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata \
    apt-get -y install apache2 \
    apt-get -y install mysql-server \
    apt-get -y install php \
    service apache2 start \
    service mysql start 

CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"] 
