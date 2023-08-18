import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

ssid = 'Experimentelles Atomlabor 2GHz'
password = 'mia0882171228'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def start():
    try:
        ip = connect()
    except KeyboardInterrupt:
        machine.reset()
start()
