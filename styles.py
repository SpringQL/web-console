# This file is part of https://github.com/SpringQL/web-console which is licensed under MIT OR Apache-2.0. See file LICENSE-MIT or LICENSE-APACHE for full license details.

def main():
    return {
        'display': 'flex',
        'flex-wrap': 'wrap',
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
