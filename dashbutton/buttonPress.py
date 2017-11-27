from scapy.all import *
import requests
import json
import time
import Adafruit_DHT
# import logging

MAC_ADDRESS = 'XX:XX:XX:XX:XX:XX'
# logging.basicConfig(level=logging.INFO, filename="dashbutton.log")

def detect_button(pkt):
    if pkt.haslayer(ARP): # Needed for Raspberry Pi
            if pkt[ARP].op == 1: #who-has (request)
                if pkt[ARP].hwsrc == MAC_ADDRESS:
#                     logging.info("Button Pressed")
                    sendToIfttt()
                else:
                    print "ARP Probe from unknown device: " + pkt[ARP].hwsrc


def getEnv():
    sensor = Adafruit_DHT.DHT22
    pin = 26
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return "Temperature: {}, Humidity: {}".format(temperature, humidity)


def sendToIfttt():
    environment = getEnv()
    timestamp = time.strftime("%Y-%m-%d %H:%M")
    mac_addr = 'XX:XX:XX:XX:XX:XX'
    payload = {
                'value1': environment,
                'value2': timestamp,
                'value3': mac_addr
                }
    headers = {'content-type': 'application/json'}

    # Make the request to IFTTT
    requests.post("https://maker.ifttt.com/trigger/dash/with/key/YOURKEY", data=json.dumps(payload),headers=headers)


print sniff(prn=detect_button, filter="arp", store=0, count=0)
