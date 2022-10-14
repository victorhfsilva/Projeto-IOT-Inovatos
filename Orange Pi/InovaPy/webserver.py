from flask import Flask

class WebServer:

    def __init__(self, data: str, port: int):
        self.data = data
        self.port = port
        self.__assert_data_is_correct()

    def __assert_data_is_correct(self):
        assert isinstance(self.data, str), "Data isn't a String."
        assert isinstance(self.port, int), "Port isn't an Integer."
        assert 49152 <= self.port <= 65535, "Port isn't a Dynamic Port."

    def run_web_server(self):
        app = Flask(__name__)

        @app.route('/data')
        def index():
            return self.data

        app.run(debug = True, host = '0.0.0.0', port = self.port, use_reloader = False)
