# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

CYTOSPACE_STYLESHEET = [
    {
        'selector': 'node',
        'style': {
            'label': 'data(id)',
            'shape': 'rectangle',
            "text-background-color": "#fff",
            "text-background-opacity": "0.5",
            "text-valign": "center",
        }
    },
    {
        'selector': 'node.source-stream',
        'style': {
            'shape': 'triangle',
        }
    },
    {
        'selector': 'node.sink-stream',
        'style': {
            'shape': 'diamond',
        }
    },
    {
        'selector': 'edge',
        'style': {
            'curve-style': 'bezier',  # The default curve style does not work with certain arrows
            'target-arrow-shape': 'triangle',
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
