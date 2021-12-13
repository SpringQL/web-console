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
            cyto_nodes.append(cyto_node)

        cyto_edges = []
        for pump in pumps:
            for queue in pump['queues']:
                cyto_edge = CytoEdge(queue)
                cyto_edges.append(cyto_edge)

    def _find_upstream_pump(self, stream_view, pumps_view):
        upstream_pump_view = None
        for pump_view in pumps_view:
            q0 = pump_view['queues'][0]
            upstream_id = q0['downstream-id']
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
            self.classes = 'sink-stream'
        elif type == 'sink-stream':
            self.classes = 'sink-stream'
        else:
            raise Exception('Invalid type')

        if type != 'source-stream':
            assert upstream_pump_view, f'stream (not a source) must have a upstream pump: {stream_view}'
            self.stream_upstream_pump_def = upstream_pump_view['pump-def']

    def to_cytoscape_element(self):
        return {
            'data': {
                'id': self.id,
                'stream_def': self.stream_def,
                'stream_upstream_pump_def': self.stream_upstream_pump_def,
            },
            'classes': self.classes,
        }


class CytoEdge:
    def __init__(self, queue_view):
        self.source = queue_view['upstream-id']
        self.target = queue_view['downstream-id']

        self.queue_label = f'{queue_view["num-rows"]}rows\n{queue_view["memory-usage-kilobytes"]}KB'
        if queue_view['num-rows-lost-so-far'] > 0:
            self.queue_label += f'\n{queue_view["num-rows-lost-so-far"]}rows lost'

    def to_cytoscape_element(self):
        return {
            'data': {
                'source': self.source,
                'target': self.target,
                'queue_label': self.queue_label,
            },
            'classes': 'queue',
        }
