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
                'data': {'id': 'src_air_conditioner', 'label': 'src_air_conditioner'},
                'classes': 'source-stream',
            },
            {
                'data': {'id': 'air_conditioner', 'label': 'air_conditioner'},
                'classes': 'stream',
            },

            {
                'data': {'id': 'ac_engine_speed', 'label': 'ac_engine_speed'},
                'classes': 'stream',
            },

            {
                'data': {'id': 'sink_cockpit', 'label': 'sink_cockpit'},
                'classes': 'sink-stream',
            },

            {
                'data': {'id': 'sink_upload', 'label': 'sink_upload'},
                'classes': 'sink-stream',
            },

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

            {
                'data': {'id': 'stop_detection', 'label': 'stop_detection'},
                'classes': 'stream',
            },
            {
                'data': {'id': 'sink_stop_detection', 'label': 'sink_stop_detection'},
                'classes': 'sink-stream',
            },

            {
                'data': {'id': 'sink_health_check', 'label': 'sink_health_check'},
                'classes': 'sink-stream',
            },

            # edges
            {'data': {'source': 'src_air_conditioner', 'target': 'air_conditioner'}},
            {'data': {'source': 'air_conditioner', 'target': 'ac_engine_speed'}},
            {'data': {'source': 'ac_engine_speed', 'target': 'sink_cockpit'}},
            {'data': {'source': 'ac_engine_speed', 'target': 'sink_upload'}},

            {'data': {'source': 'src_engine', 'target': 'sampled_engine'}},

            {'data': {'source': 'src_vehicle_control', 'target': 'sampled_speed'}},
            {'data': {'source': 'sampled_speed', 'target': 'sampled_phy_speed'}},

            {'data': {'source': 'sampled_engine', 'target': 'engine_speed'}},
            {'data': {'source': 'sampled_phy_speed', 'target': 'engine_speed'}},

            {'data': {'source': 'engine_speed', 'target': 'sink_health_check'}},
            {'data': {'source': 'engine_speed', 'target': 'ac_engine_speed'}},

            {'data': {'source': 'sampled_phy_speed', 'target': 'stop_detection'}},
            {'data': {'source': 'stop_detection', 'target': 'sink_stop_detection'}},
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
