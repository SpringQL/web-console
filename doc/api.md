# SpringQS Web Console API Document

## `GET /pipeline`

Shows Pipeline View.

## `POST /pipeline`

Updates pipeline for Pipeline View.

### Example

```bash
curl -L -X POST -H "Content-Type: application/json" -d @example/healthy-in-vehicle.json http://localhost:8050/pipeline
```

### Request Body Parameters

#### top-level object

- `"streams:"` (Array of Object): _Stream_'s.
- `"pumps:"` (Array of Object): _Pump_'s.

#### _Stream_ object

- `"id:"` (String): Stream name.
- `"type:"` (String): One of:
  - `"source-stream"`
  - `"stream"`
  - `"sink-stream"`
- `"stream-def:"` (String): `CREATE (SOURCE|SINK) STREAM` statement.

#### _Pump_ object

- `"id:"` (String): Pump name.
- `"pump-def:"` (String): `CREATE PUMP` statement.
- `"state:"` (String): One of:
  - `"stopped"`
  - `"started-operational"`
  - `"started-jammed"`: Sub-graph in which this pump is included gets jammed. Scheduler may prioritize this sub-graph.
  - `"started-critical"`: Sub-graph in which this pump is included consumes too much memory. Scheduler may prioritize this sub-graph but rows may be lost from this pump's queue.
- `"queues:"` (Array of Object): _Queue_'s.

#### _Queue_ object

- `"upstream-id:"` (String): Upstream's stream name.
- `"downstream-id:"` (String): Downstream's stream name.
- `"num-rows":` (Number): Number of rows in queue.
- `"memory-usage-kilobytes":` (Number): How much memory is used by queue [KB].
- `"num-rows-lost-so-far":` (Number): Number of rows lost so far.
