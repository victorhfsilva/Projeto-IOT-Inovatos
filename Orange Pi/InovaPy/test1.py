from data import Data
from webserver import WebServer
import time
import threading

def run_web_server(web_server):
    web_server.run_web_server()

# Sending first data
port = 49153
data = "On"
web_server = WebServer(data, port)
server_thread = threading.Thread(target = lambda : run_web_server(web_server), daemon = True)
server_thread.start()

# Receiving first data
ip = "192.168.100.3"
first_data_object = Data(ip, port)
first_data = first_data_object.data
print(first_data)

# Sending second data
data = "Off"
web_server = WebServer(data, port)
server_thread = threading.Thread(target = lambda : run_web_server(web_server), daemon = True)
server_thread.start()

# Receiving second data
second_data_object = Data(ip, port)
second_data = first_data_object.data
print(second_data)
