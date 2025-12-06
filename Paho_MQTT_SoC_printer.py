import paho.mqtt.client as mqtt
import time
import random
import json

# Logging callback
def on_log (client,userdata,level,buf):
    print("log: ",buf)

def on_connect(client, userdata, flags, rc):
    if(rc==0):
        print("Connected successfully")
    else:
        print("Bad connection, code: ",rc)

def on_disconnect(client, userdata, rc=0):
    print("Disconnected with code: ",rc)

broker="127.0.0.1"
client=mqtt.Client(client_id="python1")

# Assigning callbacks
client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_log=on_log

# Connecting to broker
print("Connecting to broker ", broker)
client.connect(broker, 1883, 60)
client.loop_start()
time.sleep(1)


snsr_rd=int(input('Enter the ammount of reads from your sensor:'))
for i in range(snsr_rd):
    # Insert your sensor reading code here, ex for simulated battery BMS message:
    SoC=random.random()*100
    # Create JSON payload
    payload={"SoC": SoC, "timestamp":time.time()}
    # Create JSON string
    json_payload=json.dumps(payload)
    #Publish to MQTT topics
    client.publish("Battery/json",json_payload)
    client.publish("Battery/SoC",str(payload["SoC"]))
    client.publish("Battery/time",str(payload["timestamp"]))
    time.sleep(1)

client.loop_stop()
client.disconnect()