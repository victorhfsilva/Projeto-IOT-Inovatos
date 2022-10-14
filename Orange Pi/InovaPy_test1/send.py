from webserver import WebServer
import threading
import time

def send_data(data: str, port: int):
    web_server = WebServer("On", port)
    thread = threading.Thread(target=lambda: run_web_server(web_server), daemon=True)
    thread.start()
    time.sleep(20)

send_data("On", 49153)
