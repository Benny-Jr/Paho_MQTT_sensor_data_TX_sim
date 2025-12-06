# Paho_MQTT_sensor_data_TX_sim

This is an example code for transmitting sensor data in localhost using Paho MQTT. 
In order to simulate the receiving end, you need to install the Mosquitto broker and in CLI after entering the Mosquitto folder run 
mosquitto_sub -t <Topic/Subtopic> -h localhost
