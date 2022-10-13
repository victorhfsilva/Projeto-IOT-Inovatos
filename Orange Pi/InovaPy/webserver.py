from flask import Flask

class WebServer:

    def __init__(self, data: str, port: int):
        self.data = data
        self.port = port
        self.__assert_data_is_correct()

    def __assert_data_is_correct(self):
        assert isinstance(self.data, str)
        assert isinstance(self.port, int)
        # Allow only dynamic ports
        assert 49152 <= self.port <= 65535

    def run_web_server(self):
        app = Flask(__name__)

        @app.route('/data')
        def index():
            return self.data

        app.run(debug = True, host = '0.0.0.0', port = self.port, use_reloader = False)
