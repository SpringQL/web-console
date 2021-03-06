import json


class Pipeline:
    def __init__(self, pipeline_view):
        cytoscape_elements = self._to_cytoscape_elements(pipeline_view)
        self._cytoscape_elements_json = json.dumps(cytoscape_elements)

    def _to_cytoscape_elements(self, pipeline_view):
        streams = pipeline_view['streams']
        pumps = pipeline_view['pumps']

        cyto_nodes = []
        for stream in streams:
            upstream_pump = self._find_upstream_pump(stream, pumps)
            cyto_node = CytoNode(stream, upstream_pump)
            cyto_nodes.append(cyto_node.to_cytoscape_element())

        cyto_edges = []
        for pump in pumps:
            s_insert = pump['insert-stream-id']
            for s_select in pump['select-stream-ids']:
                cyto_edge = CytoEdge(s_select, s_insert)
                cyto_edges.append(cyto_edge.to_cytoscape_element())

        return cyto_nodes + cyto_edges

    def _find_upstream_pump(self, stream_view, pumps_view):
        upstream_pump_view = None
        for pump_view in pumps_view:
            upstream_id = pump_view['insert-stream-id']
            if upstream_id == stream_view['id']:
                upstream_pump_view = pump_view
                break
        return upstream_pump_view

    def to_cytoscape_elements_json(self):
        return self._cytoscape_elements_json


class CytoNode:
    def __init__(self, stream_view, upstream_pump_view):
        self.id = stream_view['id']
        self.stream_def = stream_view['stream-def']

        type = stream_view['type']
        if type == 'source-stream':
            self.classes = 'source-stream'
        elif type == 'stream':
            self.classes = 'stream'
        elif type == 'sink-stream':
            self.classes = 'sink-stream'
        else:
            raise Exception('Invalid type')

        if type != 'source-stream':
            assert upstream_pump_view, f'stream (not a source) must have a upstream pump: {stream_view}'
            self.stream_upstream_pump_def = upstream_pump_view['pump-def']
        else:
            self.stream_upstream_pump_def = None

    def to_cytoscape_element(self):
        return {
            'data': {
                'id': self.id,
                'stream_def': self.stream_def,
                'stream_upstream_pump_def': self.stream_upstream_pump_def,
                'node_label': self.id,
            },
            'classes': self.classes,
        }


class CytoEdge:
    def __init__(self, stream_select, stream_insert):
        self.source = stream_select
        self.target = stream_insert

    def to_cytoscape_element(self):
        return {
            'data': {
                'source': self.source,
                'target': self.target,
            },
            'classes': 'pump-edge',
        }
