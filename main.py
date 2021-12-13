# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

import dash_cytoscape as cyto
from dash import html

from app import app

import callbacks as _
import styles
from cytoscape_stylesheet import CYTOSCAPE_STYLESHEET
from cytoscape_elements import CYTOSCAPE_ELEMENTS


app.layout = html.Main([
    html.Div([
        html.H3(id='stream-name'),

        html.H4('Stream Definition', id='stream-def'),
        html.Pre(children=[
            html.Code(id='stream-def-content'),
        ]),

        html.H4('Upstream Pump', id='stream-upstream'),
        html.Pre(children=[
            html.Code(id='stream-upstream-content')
        ]),
    ], id='stream-view', style=styles.left_pane()),

    html.Div([
        html.Button('Update Pipeline', id='btn-update-pipeline', n_clicks_timestamp=0),

        cyto.Cytoscape(
            id='cytoscape-pipeline',
            layout={
                'name': 'breadthfirst',
                'roots': '.source-stream'
            },
            style={'width': '100%', 'height': '800px'},
            stylesheet=CYTOSCAPE_STYLESHEET,
            elements=CYTOSCAPE_ELEMENTS,
        )
    ], id='pipeline-view', style=styles.right_pane()),
], style=styles.main())


if __name__ == '__main__':
    app.run_server(debug=True)
