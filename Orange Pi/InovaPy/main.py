from webserver import WebServer
import requests
import threading
import time

stop_thread = False

def print_server_text():
    r = requests.get(f"http://192.168.100.3:{port}/data")
    text = r.text
    print(text)

def run_web_server(wp):
    wp.run_web_server()
    time.sleep(3)

port = 49153
data = "A"
wp1 = WebServer(data, port)

server_thread = threading.Thread(target = lambda : run_web_server(wp1), daemon = True)
server_thread.start()
time.sleep(2)
print_server_text()
data = "B"
wp1 = WebServer(data, port)
server_thread = threading.Thread(target = lambda : run_web_server(wp1), daemon = True)
server_thread.start()
time.sleep(2)
print_server_text()