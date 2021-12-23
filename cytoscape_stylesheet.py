# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

CYTOSCAPE_STYLESHEET = [
    {
        'selector': 'node',
        'style': {
            'label': 'data(node_label)',
            'shape': 'rectangle',
            'border-width': '2px',
            "background-color": "#fff",
            "text-background-color": "#fff",
            "text-background-opacity": "0.5",
            "text-valign": "center",
            "text-wrap": "wrap",
            "text-max-width": '8em',
        }
    },
    {
        'selector': 'node:selected',
        'style': {
            "background-color": "#00f",
        }
    },
    {
        'selector': 'node.source-stream',
        'style': {
            'shape': 'rhomboid',
        }
    },
    {
        'selector': 'node.source-task',
        'style': {
            'shape': 'rhomboid',
        }
    },
    {
        'selector': 'node.sink-stream',
        'style': {
            'shape': 'diamond',
        }
    },
    {
        'selector': 'node.sink-task',
        'style': {
            'shape': 'diamond',
        }
    },
    {
        'selector': 'node.host-app',
        'style': {
            'shape': 'vee',
        }
    },
    {
        'selector': 'edge',
        'style': {
            'width': '2px',
            'curve-style': 'bezier',  # The default curve style does not work with certain arrows
            'target-arrow-shape': 'triangle',
            'target-arrow-color': '#333',
            "arrow-scale": 2.5,
        }
    },
    {
        'selector': 'edge.in-memory-queue',
        'style': {
            'line-style': 'dashed',
        }
    },
    {
        'selector': 'edge.window-queue',
        'style': {
            'width': '5px',
        }
    },
    {
        'selector': 'edge[queue_label]',
        'style': {
            "label": "data(queue_label)",
            "text-rotation": "autorotate",
            "text-wrap": "wrap",
            "text-background-color": "#fff",
            "text-background-opacity": "0.5",
        }
    },
]
