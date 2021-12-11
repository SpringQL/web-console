# Copyright (c) 2021 TOYOTA MOTOR CORPORATION. Licensed under MIT OR Apache-2.0.

CYTOSPACE_ELEMENTS = [
    # nodes
    {
        'data': {
            'id': 'src_air_conditioner', 'label': 'src_air_conditioner',
            'stream-def':
            '''CREATE SOURCE STREAM src_air_conditioner (
                 ts TIMESTAMP NOT NULL ROWTIME,
                 car_temperature FLOAT NOT NULL,
                 raw_out_temperature FLOAT NOT NULL
                ) SERVER NET_SERVER OPTIONS (
                  PROTOCOL 'TCP',
                  REMOTE_HOST '127.0.0.1,
                  REMOTE_PORT '19870'
                )
            ''',
            'stream-upstream': None,
        },
        'classes': 'source-stream',
    },
    {
        'data': {
            'id': 'air_conditioner', 'label': 'air_conditioner',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 
            '''CREATE PUMP pu_air_conditioner_phy_conversion AS
              INSERT INTO air_conditioner (ts, car_temperature, phy_out_temperature)
              SELECT ts, car_temperature, raw_out_temperature * 0.28
                FROM src_air_conditioner;
            ''',
        },
        'classes': 'stream',
    },

    {
        'data': {
            'id': 'ac_engine_speed', 'label': 'ac_engine_speed',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'stream',
    },

    {
        'data': {
            'id': 'sink_cockpit', 'label': 'sink_cockpit',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'sink-stream',
    },

    {
        'data': {
            'id': 'sink_upload', 'label': 'sink_upload',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'sink-stream',
    },

    {
        'data': {
            'id': 'src_engine', 'label': 'src_engine',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'source-stream',
    },
    {
        'data': {
            'id': 'sampled_engine', 'label': 'sampled_engine',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'stream',
    },

    {
        'data': {
            'id': 'src_vehicle_control', 'label': 'src_vehicle_control',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'source-stream',
    },
    {
        'data': {
            'id': 'sampled_speed', 'label': 'sampled_speed',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'stream',
    },
    {
        'data': {
            'id': 'sampled_phy_speed', 'label': 'sampled_phy_speed',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'stream',
    },

    {
        'data': {
            'id': 'engine_speed', 'label': 'engine_speed',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'stream',
    },

    {
        'data': {
            'id': 'stop_detection', 'label': 'stop_detection',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'stream',
    },
    {
        'data': {
            'id': 'sink_stop_detection', 'label': 'sink_stop_detection',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'sink-stream',
    },

    {
        'data': {
            'id': 'sink_health_check', 'label': 'sink_health_check',
            'stream-def': 'CREATE STREAM ...',
            'stream-upstream': 'CREATE PUMP ...',
        },
        'classes': 'sink-stream',
    },

    # edges
    {'data': {
        'source': 'src_air_conditioner', 'target': 'air_conditioner'},

     },
    {'data': {
        'source': 'air_conditioner', 'target': 'ac_engine_speed'},

     },
    {'data': {
        'source': 'ac_engine_speed', 'target': 'sink_cockpit'},

     },
    {'data': {
        'source': 'ac_engine_speed', 'target': 'sink_upload'},

     },

    {'data': {
        'source': 'src_engine', 'target': 'sampled_engine'},

     },

    {'data': {
        'source': 'src_vehicle_control', 'target': 'sampled_speed'},

     },
    {'data': {
        'source': 'sampled_speed', 'target': 'sampled_phy_speed'},

     },

    {'data': {
        'source': 'sampled_engine', 'target': 'engine_speed'},

     },
    {'data': {
        'source': 'sampled_phy_speed', 'target': 'engine_speed'},

     },

    {'data': {
        'source': 'engine_speed', 'target': 'sink_health_check'},

     },
    {'data': {
        'source': 'engine_speed', 'target': 'ac_engine_speed'},

     },

    {'data': {
        'source': 'sampled_phy_speed', 'target': 'stop_detection'},

     },
    {'data': {
        'source': 'stop_detection', 'target': 'sink_stop_detection'},
     },
]
