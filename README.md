# W251

## Working on the Jetson
### network = hw03
### Bridge for the containers
docker network create --driver bridge jetsonbridge

### Brocker Container docker on the Jetson
docker run --name mosquitto --network hw03 -p 1883:1883 -ti alpine sh
apk update && apk add mosquitto
#
/usr/sbin/mosquitto

### Forwarder container
apk update && apk add py-pip 
apk add mosquitto-clients
pip install paho-mqtt
forward.py python file

### Facedetect container

apt update

ENV DEBIAN_FRONTEND=noninteractive
apt install -y python-opencv python-pip vim-tiny mosquitto-clients libopencv-dev
pip install paho-mqtt
EXPOSE 1883
faces.py .





docker build -t broker -f Dockerfile.broker .
docker build -t forwarder -f Dockerfile.forwarder .
docker build -t facedetect -f Dockerfile.facedetect .
docker run -d --name broker -p 1883:1883 --network jetsonbridge broker
docker run -d --name forwarder --network jetsonbridge forwarder
docker run -d --name facedetect --privileged --network jetsonbridge facedetect


