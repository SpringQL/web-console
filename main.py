# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

import dash
import dash_cytoscape as cyto
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-two-nodes',
        layout={
            'name': 'breadthfirst',
            'roots': '#one'
        },
        style={'width': '100%', 'height': '800px'},
        elements=[
            {'data': {'id': 'one', 'label': 'Node 1'}},
            {'data': {'id': 'two', 'label': 'Node 2'}},
            {'data': {'source': 'one', 'target': 'two'}}
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
