# W251

The homework assignment required the creation of 3 containers in the JEtson and two containers on the IBM cloud. I was unable to accomplish the goal of storing captured images in the VM, however I did learn an extravegant amount throughout the process. Below are the containers required for this assignment. 

## Working on the Jetson
 network = jetsonbridge
### Bridge for the containers
docker network create --driver bridge jetsonbridge

### Brocker Container docker on the Jetson
docker run --name mosquitto --network hw03 -p 1883:1883 -ti alpine sh

apk update && apk add mosquitto

/usr/sbin/mosquitto

### Forwarder container
docker run -d --name forwarder --network jetsonbridge forwarder

apk update && apk add py-pip 

apk add mosquitto-clients

pip install paho-mqtt

forward.py python file


### Facedetect container
docker run -d --name broker -p 1883:1883 --network jetsonbridge broke

apt update

ENV DEBIAN_FRONTEND=noninteractive

apt install -y python-opencv python-pip vim-tiny mosquitto-clients libopencv-dev

pip install paho-mqtt

EXPOSE 1883

faces.py .


### Three containers in the Jetson
CONTAINER ID        IMAGE               COMMAND       

7b1ec6f18b22        facedetect          "/bin/sh -c 'python …"  

097ec86ebad1        forwarder           "/bin/sh -c 'python …"   

1740a8d47cc1        broker              "/bin/sh -c /usr/sbi…"   

## In the IBM Virtual Mahine
### Create a network cloudbridge
docker network create --driver bridge cloudbridge


### Cloudbroker container

docker run -d --name cloudbroker -p 1883:1883 --network cloudbridge cloudbroker

RUN apk update && apk add mosquitto

docker run -d --name readandsave -v /mnt/hw3bucket:/data --network cloudbridge readandsave

### Read and Save the image container
docker run -d --name readandsave -v /mnt/hw3bucket:/data --network cloudbridge readandsave



### Two containers in the IBM VM
CONTAINER ID        IMAGE               COMMAND     

c9c5f62b9f11        readandsave         "/bin/sh -c 'python …"  

328ce21d4c3d        cloudbroker         "/bin/sh -c /usr/sbi…"   


