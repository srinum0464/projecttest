FROM ubuntu 
LABEL "OWNER"="Srinivas"
RUN apt-get update -y && apt-get install apache2 -y && apt-get install iputils-ping -y
ADD https://raw.githubusercontent.com/srinum0464/projecttest/ansible/index.html /var/www/html/
EXPOSE 80
WORKDIR /usr/local
VOLUME [ "/var/www/html/" ]
RUN chmod 777 /var/www/html/index.html 
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]