# This file is part of https://github.com/SpringQL/web-console which is licensed under MIT OR Apache-2.0. See file LICENSE-MIT or LICENSE-APACHE for full license details.

import dash
from flask import Flask, request

from redis_client import redis_client

from pipeline import Pipeline
from task_graph import TaskGraph

server = Flask(__name__)


@server.route("/pipeline", methods=['POST'])
def update_pipeline():
    pipeline_view = request.get_json()
    pipeline = Pipeline(pipeline_view)
    j = pipeline.to_cytoscape_elements_json()
    redis_client.set('pipeline', j)
    return ''


@server.route("/task-graph", methods=['POST'])
def update_task_graph():
    task_graph_view = request.get_json()
    task_graph = TaskGraph(task_graph_view)
    j = task_graph.to_cytoscape_elements_json()
    redis_client.set('task-graph', j)
    return ''


app = dash.Dash(__name__, server=server, url_base_pathname='/pipeline/')
