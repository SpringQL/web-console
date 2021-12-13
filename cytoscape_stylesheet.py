# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

CYTOSCAPE_STYLESHEET = [
    {
        'selector': 'node',
        'style': {
            'label': 'data(id)',
            'shape': 'rectangle',
            'border-width': '2px',
            "background-color": "#fff",
            "text-background-color": "#fff",
            "text-background-opacity": "0.5",
            "text-valign": "center",
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
            'target-arrow-color': '#333',
            "arrow-scale": 2.5,
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

    {
        'selector': 'edge[pump_state ^= "stopped"]',
        'style': {
            'line-color': '#c0c0c0',
        }
    },
    {
        'selector': 'edge[pump_state ^= "started-operational"]',
        'style': {
            'line-color': '#50cc50',
        }
    },
    {
        'selector': 'edge[pump_state ^= "started-jammed"]',
        'style': {
            'line-color': '#e0e020',
        }
    },
    {
        'selector': 'edge[pump_state ^= "started-critical"]',
        'style': {
            'line-color': '#ff5050',
        }
    },
]
