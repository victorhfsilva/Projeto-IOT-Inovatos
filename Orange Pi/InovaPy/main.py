import smbus
from data import Data
from webserver import WebServer
import threading
import time

def run_web_server(web_server):
    web_server.run_web_server()

def receive_data(ip: str, port: int) -> str:
    data_object = Data(ip, port)
    data = data_object.data
    return data

threads = [0, 0]
def send_data(data: str, port: int, index: int):
    assert isinstance(index, int)
    web_server = WebServer("On", port)
    threads[index] = threading.Thread(target=lambda: run_web_server(web_server), daemon=True)
    threads[index].start()
    time.sleep(1)

send_data("On", 49153, 0)
print(receive_data("192.168.100.3", 49153))
send_data("Off", 49154, 1)
print(receive_data("192.168.100.3", 49154))


# DEVICE_ADDR = 0x04
# bus = smbus.SMBus(0)
# bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)




