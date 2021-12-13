# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

from dash.dependencies import Input, Output, State

from app import app


@app.callback(Output('stream-name', 'children'),
              Input('cytoscape-pipeline', 'selectedNodeData'))
def updateStreamName(nodes):
    if nodes is None:
        return "(no stream selected)"

    stream = nodes[0]
    return stream['label']


@app.callback(Output('stream-def-content', 'children'),
              Input('cytoscape-pipeline', 'selectedNodeData'))
def updateStreamDefContent(nodes):
    if nodes is None:
        return ""

    stream = nodes[0]
    return stream['stream-def']


@app.callback(Output('stream-upstream-content', 'children'),
              Input('cytoscape-pipeline', 'selectedNodeData'))
def updateStreamUpstreamContent(nodes):
    if nodes is None:
        return ""

    stream = nodes[0]
    return stream['stream-upstream']


@app.callback(Output('cytoscape-pipeline', 'elements'),
              Input('btn-update-pipeline', 'n_clicks_timestamp'))
def updateElements(btn_add, btn_remove, elements):
    # TODO redis get j
    # return loads(j)
    pass
