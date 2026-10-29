import csv
import datetime
import paho.mqtt.client as mqttClient
now = datetime.datetime.now()

def on_connect(client, userdata, flags, rc, proterties):
    if rc == 0:
        print("connected to broker")
        global Connected
        Connected = True
    else:
        print("connection failed")

def on_message(client, userdata, message):
    print("Message resiver: " + str(message.payload))
    
    with open('data.csv', 'a', newline ='') as csvfile:
        writer = csv.writer(csvfile, dialect= 'unix', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, escapechar="\n")
        writer.writerow([str(now.time())] + [str(message.payload)] + ['\n'])

Connected = False


broker_address= "10.42.0.1"
port = 1883
user = "uberputer"
password = "liamangle"

client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION2)
client.username_pw_set(user, password=password)
client.on_connect= on_connect
client.on_message= on_message
client.connect(broker_address, port, 60)
client.subscribe("outTopic")
client.loop_forever(retry_first_connection=True)



