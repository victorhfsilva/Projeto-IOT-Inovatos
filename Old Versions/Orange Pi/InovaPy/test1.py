from data import Data
from webserver import WebServer
import time
import threading

def run_web_server(web_server):
        web_server.run_web_server()

# Sending first data
web_server1 = WebServer("On", 49153)
thread1 = threading.Thread(target = lambda : run_web_server(web_server1), daemon = True)
thread1.start()
time.sleep(1)

# Receiving first data
ip = "192.168.100.3"
first_data_object = Data(ip, 49153)
first_data = first_data_object.data
print(first_data)
time.sleep(1)

# Sending second data
web_server2 = WebServer("Off", 49152)
thread2 = threading.Thread(target = lambda : run_web_server(web_server2), daemon = True)
thread2.start()
time.sleep(1)

# Receiving second data
second_data_object = Data(ip, 49152)
second_data = second_data_object.data
print(second_data)
