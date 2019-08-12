FROM ubuntu 
LABEL "OWNER"="Srinivas"
RUN apt-get update -y && apt-get install apache2 -y && apt-get install iputils-ping
EXPOSE 80
CMD ["ping","-t","google.com"]