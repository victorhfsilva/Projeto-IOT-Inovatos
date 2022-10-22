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
    print(f"Received Web Data: {data}.")
    return data

def send_i2c_data_loop(ip: str, port: int):
    while True:
        data = received_web_data(ip, port)
        if data == "On":
            bus.write_byte(DEVICE_ADDR, 0x1)
        elif data == "Off":
            bus.write_byte(DEVICE_ADDR, 0x0)
        else:
            raise ValueError("Invalid data.")
        time.sleep(0.5)

def run_web_server(web_server):
    web_server.run_web_server()

def receive_i2c_data():
    data = bus.read_byte(DEVICE_ADDR)
    print(f"Received I2C Data: {data}.")
    return data

def decide_web_data_to_send():
    data = receive_i2c_data()
    if data == 0x1:
        return "On"
    else:
        return "Off"

def loop(receiving_ip: str, sending_port: int, receiving_port):
    while True:
        # Send Web Data
        data = decide_web_data_to_send()
        web_server = WebServer(data, sending_port)
        send_web_process = multiprocessing.Process(target=lambda: run_web_server(web_server), daemon=True)
        send_web_process.start()
        time.sleep(1)
        # Initialize I2C process
        send_i2c_process = multiprocessing.Process(target=lambda: send_i2c_data_loop(receiving_ip, receiving_port), daemon=True)
        send_i2c_process.start()
        time.sleep(0.5)
        # Terminate processes
        send_web_process.terminate()
        send_i2c_process.terminate()

receiving_ip = "192.168.100.29"
sending_port = 49153
receiving_port = 49152
loop(receiving_ip, sending_port, receiving_port)
