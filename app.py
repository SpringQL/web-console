# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

import dash
from flask import Flask, request

from redis_client import redis_client

from pipeline import Pipeline

server = Flask(__name__)


@server.route("/pipeline", methods=['POST'])
def update_pipeline():
    pipeline_view = request.get_json()
    pipeline = Pipeline(pipeline_view)
    j = pipeline.to_cytoscape_elements_json()
    redis_client.set('pipeline', j)
    return ''


app = dash.Dash(__name__, server=server, url_base_pathname='/pipeline/')
