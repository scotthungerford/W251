import numpy as np
import math
import cv2

import paho.mqtt.client as mqtt
print('completed')
index = 0

HOST="159.8.241.4"
PORT=1883
TOPIC="cloudfaces"

path = '/data/' #map directory to  /mnt/hw3bucket

def on_connect(clnt, user, flags, rc):
    client.subscribe(TOPIC)
    print('subscribed to topic')
    print("connected with rc:" + str(rc))

def on_message(client, userdata, msg):
    global index
    global path
    f = np.frombuffer(msg.payload, dtype='uint8')
    img = cv2.imdecode(f, flags=1)
    name = 'face_%s.png'%str(index)
    index+=1
    cv2.imwrite(path+name, img)

client = mqtt.Client()
client.on_connect = on_connect
client.connect(HOST, PORT, 60)
client.on_message=on_message
client.loop_forever()
