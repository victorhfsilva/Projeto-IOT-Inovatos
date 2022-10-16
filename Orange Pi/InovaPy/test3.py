import time
import multiprocessing
from webserver import WebServer
from data import Data

def received_web_data(ip: str, port: int) -> str:
    data_object = Data(ip, port)
    data = data_object.data
    return data

def send_i2c_data_loop(ip: str, port: int):
    while True:
        data = received_web_data(ip, port)
        if data == "On":
            print("I2C Status: On")
        elif data == "Off":
            print("I2C Status: Off")
        else:
            raise ValueError("Invalid data.")
        time.sleep(0.5)

def run_web_server(web_server):
    web_server.run_web_server()

def receive_i2c_data():
    data = 0x01
    return data

def decide_web_data_to_send():
    data = receive_i2c_data()
    if data == 0x01:
        return "On"
    elif data == 0x00:
        return "Off"
    else:
        raise ValueError("Invalid Data")

def loop(ip: str, port: int):
    while True:
        # Send Web Data
        data = decide_web_data_to_send()
        web_server = WebServer(data, port)
        send_web_process = multiprocessing.Process(target=lambda: run_web_server(web_server), daemon=True)
        send_web_process.start()
        time.sleep(1)
        # Initialize I2C process
        send_i2c_process = multiprocessing.Process(target=lambda: send_i2c_data_loop(ip, port), daemon=True)
        send_i2c_process.start()
        time.sleep(0.5)
        # Terminate processes
        send_web_process.terminate()
        send_i2c_process.terminate()

ip = "192.168.100.3"
port = 49153
loop(ip, port)


