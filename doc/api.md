# SpringQS Web Console API Document

## `GET /pipeline`

Shows Pipeline View.

## `POST /pipeline`

Updates pipeline for Pipeline View.

### Example

```bash
curl -X POST -H "Content-Type: application/json" -d @example/healthy-in-vehicle.json http://localhost:8050/pipeline
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
- `"stream-upstream-pump-def:"` (optional String): Upstream's `CREATE PUMP` statement. `null` for source streams.

#### _Pump_ object

- `"id:"` (String): Pump name.
- `"upstream-id:"` (String): Upstream's stream name.
- `"downstream-id:"` (String): Downstream's stream name.
- `"state:"` (String): One of:
  - `"stopped"`
  - `"started-operational"`
  - `"started-jammed"`: Sub-graph in which this pump is included gets jammed.
  - `"started-critical"`: Rows in this pump's queue may be lost for severe memory usage.
- `"queue:"` (Object): _Queue_.

#### _Queue_ object

- `"num-rows":` (Number): Number of rows in queue.
- `"memory-usage-killobytes":` (Number): How much memory is used by queue [KB].
- `"num-rows-lost-so-far":` (Number): Number of rows lost so far.
