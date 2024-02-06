#Pulling base ubuntu image from docker hub
FROM ubuntu:latest

#Installing required packages
RUN apt-get update -y; apt-get install fortune-mod cowsay netcat -y

#Creating application folder inside a container
RUN mkdir /opt/wisecow

#Copying wisecow file from local machine to the container
COPY ./wisecow.sh /opt/wisecow

#creating link file for cowsay and fortune in /usr/bin to make those available in path variable.
RUN ln -s /usr/games/cowsay /usr/bin/cowsay ; ln -s /usr/games/fortune /usr/bin/fortune

#EXPOSING default port 4499
EXPOSE 4499

#Executing wisecow.sh
CMD ["sh","/opt/wisecow/wisecow.sh"]


