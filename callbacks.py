# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

from dash.dependencies import Input, Output

from app import app

@app.callback(Output('stream-name', 'children'),
              Input('cytoscape-pipeline', 'selectedNodeData'))
def displaySelectedStream(stream_list):
    if stream_list is None:
        return "No stream selected."

    stream = stream_list[0]
    return stream['label']
