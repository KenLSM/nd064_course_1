import logging
from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def status():
    app.logger.info(datetime.now().strftime("%c") + "," +
                    "/status" + "endpoint was reached")
    return {"result": "OK - healthy"}


@app.route("/metrics")
def metrics():
    app.logger.info(datetime.now().strftime("%c") + "," +
                    "/metrics" + "endpoint was reached")
    return {"data": {"UserCount": 140, "UserCountActive": 23}}


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    logging.basicConfig(filename="app.log", level=logging.DEBUG)
