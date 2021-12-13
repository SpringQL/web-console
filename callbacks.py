# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

from dash.dependencies import Input, Output, State
import json

from app import app
from redis_client import redis_client


@app.callback(Output('stream-name', 'children'),
              Input('cytoscape-pipeline', 'selectedNodeData'))
def updateStreamName(nodes):
    if not nodes:
        return "(no stream selected)"

    node = nodes[0]
    return node['id']


@app.callback(Output('stream-def-content', 'children'),
              Input('cytoscape-pipeline', 'selectedNodeData'))
def updateStreamDefContent(nodes):
    if not nodes:
        return ""

    node = nodes[0]
    return node['stream_def']


@app.callback(Output('stream-upstream-content', 'children'),
              Input('cytoscape-pipeline', 'selectedNodeData'))
def updateStreamUpstreamContent(nodes):
    if not nodes:
        return ""

    node = nodes[0]
    return node['stream_upstream_pump_def']


@app.callback(Output('cytoscape-pipeline', 'elements'),
              Input('btn-update-pipeline', 'n_clicks_timestamp'))
def updateElements(_btn):
    j = redis_client.get('pipeline')
    if not j:
        j = '{}'
    return json.loads(j)
