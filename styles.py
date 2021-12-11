# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

def main():
    return {
        'display': 'flex',
        'width': '1200px',
        'margin': 'auto',
        'background-color': '#f0f0f0',
    }


def left_pane():
    return {
        'left': '0',
        'width': 'calc(40.0% - 10px)',
        'margin': '0 5px',
        'background-color': '#fff',
    }


def right_pane():
    return {
        'left': 'calc(40.0%)',
        'width': 'calc(60.0% - 10px)',
        'margin': '0 5px',
        'background-color': '#fff',
    }
