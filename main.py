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
            'roots': '.source-stream'
        },
        style={'width': '100%', 'height': '800px'},
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'label': 'data(id)'
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'curve-style': 'bezier',  # The default curve style does not work with certain arrows
                    'target-arrow-shape': 'triangle',
                }
            },
        ],
        elements=[
            # nodes
            {
                'data': {'id': 'src_engine', 'label': 'src_engine'},
                'classes': 'source-stream',
            },
            {
                'data': {'id': 'sampled_engine', 'label': 'sampled_engine'},
                'classes': 'stream',
            },

            {
                'data': {'id': 'src_vehicle_control', 'label': 'src_vehicle_control'},
                'classes': 'source-stream',
            },
            {
                'data': {'id': 'sampled_speed', 'label': 'sampled_speed'},
                'classes': 'stream',
            },
            {
                'data': {'id': 'sampled_phy_speed', 'label': 'sampled_phy_speed'},
                'classes': 'stream',
            },

            {
                'data': {'id': 'engine_speed', 'label': 'engine_speed'},
                'classes': 'stream',
            },

            # edges
            {'data': {'source': 'src_engine', 'target': 'sampled_engine'}},

            {'data': {'source': 'src_vehicle_control', 'target': 'sampled_speed'}},
            {'data': {'source': 'sampled_speed', 'target': 'sampled_phy_speed'}},

            {'data': {'source': 'sampled_engine', 'target': 'engine_speed'}},
            {'data': {'source': 'sampled_phy_speed', 'target': 'engine_speed'}},
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
