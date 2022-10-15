import smbus
import time
import multiprocessing

from webserver import WebServer
from data import Data

DEVICE_ADDR = 0x04
bus = smbus.SMBus(0)

def received_web_data(ip: str, port: int) -> str:
    data_object = Data(ip, port)
    data = data_object.data
    return data

def send_i2c_data_loop(ip: str, port: int):
    while True:
        data = received_web_data(ip, port)
        if data == "On":
            bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
        elif data == "Off":
            bus.write_byte_data(DEVICE_ADDR, 0x00, 0x00)
        else:
            raise ValueError("Invalid data.")
        time.sleep(0.5)

def run_web_server(web_server):
    web_server.run_web_server()

def send_web_data(port: int):
    data = decide_web_data_to_send()
    web_server = WebServer(data, port)
    process = multiprocessing.Process(target=lambda: run_web_server(web_server), daemon=True)
    process.start()
    time.sleep(1)
    return process

def receive_i2c_data():
    data = bus.read_byte_data(DEVICE_ADDR, 0x00)
    return data

def decide_web_data_to_send():
    data = receive_i2c_data()
    if data == 0x01:
        return "On"
    elif data == 0x00:
        return "Off"
    else:
        raise ValueError("Invalid Data")

def send_web_data_loop(port: int):
    while True:
        web_send_process = send_web_data(port)
        time.sleep(1)
        web_send_process.terminate()

ip = "192.168.100.3"
port = 49153
send_i2c_process = multiprocessing.Process(target=lambda: send_i2c_data_loop(ip,port), daemon=True)
send_web_process = multiprocessing.Process(target=lambda: send_web_data_loop(port), daemon=True)
send_i2c_process.start()
send_web_process.start()