from data import Data
import time
import smbus

def receive_data(ip: str, port: int) -> str:
    data_object = Data(ip, port)
    data = data_object.data
    return data

DEVICE_ADDR = 0x04
bus = smbus.SMBus(0)

while True:
    data = receive_data("192.168.100.3", 49153)
    if data == "On":
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
    else:
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
    time(0.5)
