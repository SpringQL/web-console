# This file is part of https://github.com/SpringQL/web-console which is licensed under MIT OR Apache-2.0. See file LICENSE-MIT or LICENSE-APACHE for full license details.

import dash_cytoscape as cyto
from dash import html

from app import app

import callbacks as _
import styles
from cytoscape_stylesheet import CYTOSCAPE_STYLESHEET


app.layout = html.Main([
    html.Div([
        html.Div([
            html.H3('Task graph performance summary'),
        ], id='task-graph-summary', style=styles.left_pane()),

        html.Div([
            html.Button('Update Task Graph', id='btn-update-task-graph',
                        n_clicks_timestamp=0),

            cyto.Cytoscape(
                id='cytoscape-task-graph',
                layout={
                    'name': 'breadthfirst',
                    'roots': '.source-task'
                },
                style={'width': '100%', 'height': '800px'},
                stylesheet=CYTOSCAPE_STYLESHEET,
                elements={},
            ),
        ], id='task-graph-view', style=styles.right_pane()),
    ], style=styles.main()),
    html.Div([
        html.Div([
            html.H3(id='stream-name'),

            html.H4('Stream Definition', id='stream-def'),
            html.Pre(children=[
                html.Code(id='stream-def-content'),
            ]),

            html.H4('Upstream Pump Definition', id='stream-upstream'),
            html.Pre(children=[
                html.Code(id='stream-upstream-content')
            ]),
        ], id='stream-view', style=styles.left_pane()),

        html.Div([
            html.Button('Update Pipeline', id='btn-update-pipeline',
                        n_clicks_timestamp=0),

            cyto.Cytoscape(
                id='cytoscape-pipeline',
                layout={
                    'name': 'breadthfirst',
                    'roots': '.source-stream'
                },
                style={'width': '100%', 'height': '800px'},
                stylesheet=CYTOSCAPE_STYLESHEET,
                elements={},
            ),
        ], id='pipeline-view', style=styles.right_pane()),
    ], style=styles.main())
], style=styles.main())


if __name__ == '__main__':
    app.run_server(debug=True)
