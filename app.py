# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

import dash
from flask import Flask, request

server = Flask(__name__)


@server.route("/pipeline", methods=['POST'])
def update_pipeline():
    print(request)
    j = request.get_json()
    return j


app = dash.Dash(__name__, server=server, url_base_pathname='/pipeline/')
