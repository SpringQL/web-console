import json


class TaskGraph:
    def __init__(self, task_graph_view):
        cytoscape_elements = self._to_cytoscape_elements(task_graph_view)
        self._cytoscape_elements_json = json.dumps(cytoscape_elements)

    def _to_cytoscape_elements(self, task_graph_view):
        tasks = task_graph_view['tasks']
        queues = task_graph_view['queues']

        cyto_nodes = []
        for task in tasks:
            cyto_node = CytoNode(task)
            cyto_nodes.append(cyto_node.to_cytoscape_element())

        cyto_nodes.append(CytoNode.host_app())

        cyto_edges = []
        for queue in queues:
            cyto_edge = CytoEdge(queue)
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
    def __init__(self, task_view):
        self.id = task_view['id']
        self.avg_gain_bytes_per_sec = float(
            task_view['avg-gain-bytes-per-sec'])

        type = task_view['type']
        self.classes = type

        #self.task_label = f'{self.id[:10]}\n{self.avg_gain_bytes_per_sec:.2g}B/s'
        self.task_label = f'{self.id[:20]}..\n({self.avg_gain_bytes_per_sec:,.1f}B/s)'

    def to_cytoscape_element(self):
        return {
            'data': {
                'id': self.id,
                'avg_gain_bytes_per_sec': self.avg_gain_bytes_per_sec,
                'node_label': self.task_label,
            },
            'classes': self.classes,
        }

    @classmethod
    def host_app(cls):
        return {
            'data': {
                'id': 'host-app',
            },
            'classes': 'host-app',
        }


class CytoEdge:
    def __init__(self, queue_view):
        self.source = queue_view['upstream-task-id']
        self.target = queue_view['downstream-task-id']
        if not self.target:
            self.target = 'host-app'
            self.classes = 'in-memory-queue'

        if queue_view['row-queue']:
            q = queue_view['row-queue']
            self.queue_label = f'{q["num-rows"]}rows\n{q["total-bytes"] * 1e-3:.2g}KB'
            if not hasattr(self, 'classes'):
                self.classes = 'row-queue'
        elif queue_view['window-queue']:
            q = queue_view['window-queue']
            self.queue_label = f'{q["num-rows-waiting"]}rows(wait)\n{q["total-bytes"] * 1e-3:.2g}KB'
            self.classes = 'window-queue'

    def to_cytoscape_element(self):
        return {
            'data': {
                'source': self.source,
                'target': self.target,
                'queue_label': self.queue_label,
            },
            'classes': self.classes,
        }
