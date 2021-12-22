# SpringQS Web Console API Document

## `GET /pipeline`

Shows Pipeline View.

## `POST /pipeline`

Updates pipeline for Pipeline View.

### Example

```bash
curl -L -X POST -H "Content-Type: application/json" -d @example/pipeline-in-vehicle.json http://localhost:8050/pipeline
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
- `"select-stream-ids:"` (Array of String): Stream names to select from.
- `"insert-stream-id:"` (String): Stream name to insert into.

## `GET /task-graph`

Shows Task Graph View.

## `POST /task-graph`

Updates task graph for Task Graph View.

### Example

```bash
curl -L -X POST -H "Content-Type: application/json" -d @example/task-graph-in-vehicle.json http://localhost:8050/task-graph
```

### Request Body Parameters

#### top-level object

- `"tasks:"` (Array of Object): _Task_'s.
- `"queues:"` (Array of Object): _Queue_'s.

#### _Task_ object

- `"id:"` (String): Task name.
- `"type"` (String): One of:
  - `"source-task"`
  - `"pump-row-task"`
  - `"pump-window-task"`
  - `"sink-task"`
- `"avg-gain-bytes-per-sec:"` (Number): Memory gain throughput of this task.

#### _Queue_ object

- `"id:"` (String): Queue name.
- `"upstream-task-id:"` (String): Upstream's task name.
- `"downstream-task-id:"` (Optional string): Downstream's task name. In-memory queue sink should set null.
- `"row-queue:"` (Optional object): _RowQueue_. (Including for downstream of in-memory queue sink)
- `"window-queue:"` (Optional object): _WindowQueue_. (Pump-window-task's upstreams)

#### _RowQueue_ object

- `"num-rows":` (Number): Current number of rows in queue.
- `"total-bytes:"` (Number): How much memory is currently used by queue.
- `"num-rows-used-so-far":` (Number)
- `"num-rows-purged-so-far":` (Number)

#### _WindowQueue_ object

- `"num-open-windows:` (Number): Current number of open windows in queue.
- `"total-bytes:"` (Number): How much memory is currently used by queue.
- `"num-windows-used-so-far":` (Number)
- `"num-windows-purged-so-far":` (Number)
- `"num-rows-accepted-so-far":` (Number)
- `"num-rows-rejected-so-far":` (Number)
