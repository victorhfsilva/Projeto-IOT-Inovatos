from webserver import WebServer
import multiprocessing
import time


def run_web_server(web_server):
    web_server.run_web_server()

def send_data(data: str, port: int):
    web_server = WebServer(data, port)
    process = multiprocessing.Process(target=lambda: run_web_server(web_server), daemon=True)
    process.start()
    time.sleep(1)
    return process

send_data("On", 49153)
