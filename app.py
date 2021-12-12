# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

import dash
from flask import Flask

server = Flask(__name__)


@server.route("/hello")
def hello_world():
    return "Hello, World!"


app = dash.Dash(__name__, server=server, url_base_pathname='/pipeline/')
