import smbus
from data import Data
from webserver import WebServer
import time
import multiprocessing

def run_web_server(web_server):
    web_server.run_web_server()

def receive_data(ip: str, port: int) -> str:
    data_object = Data(ip, port)
    data = data_object.data
    return data

# def send_data(data: str, port: int):
#     web_server = WebServer(data, port)
#     thread = threading.Thread(target=lambda: run_web_server(web_server), daemon=True)
#     thread.start()
#     time.sleep(1)

def send_data(data: str, port: int):
    web_server = WebServer(data, port)
    process = multiprocessing.Process(target=lambda: run_web_server(web_server), daemon=True)
    process.start()
    time.sleep(1)
    return process

process = send_data("On", 49153)
print(receive_data("192.168.100.3", 49153))
process.terminate()
process = send_data("Off", 49153)
print(receive_data("192.168.100.3", 49153))


# DEVICE_ADDR = 0x04
# bus = smbus.SMBus(0)
# bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)