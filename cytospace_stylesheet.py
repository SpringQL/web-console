CYTOSPACE_STYLESHEET = [
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
]
