from flask import Flask
import os
import ssl

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


if __name__ == "__main__":
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    certfile = os.path.realpath('private.crt')
    keyfile = os.path.realpath('private.key')
    ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile, password='wlwjdrhk')
    app.run(host="0.0.0.0", port=4443, ssl_context=ssl_context)
