import requests
import re

class Data:

    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.__assert_data_is_correct()
        self.data = self.request_data()


    def __assert_data_is_correct(self):
        assert isinstance(self.ip, str), "IP isn't a String."
        assert re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", self.ip), "Ip doesn't match IP format."
        assert isinstance(self.port, int), "Port isn't an Integer."
        assert 49152 <= self.port <= 65535, "Port isn't a Dynamic Port."

    def request_data(self) -> str:
        address = "http://" + self.ip + ":" + str(self.port) + "/data"
        r = requests.get(address)
        data = r.text
        return data

