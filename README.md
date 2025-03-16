# digantara-backend-assignment


# Algorithm API Service

A Flask-based RESTful API service that implements three common algorithms:
- Binary Search
- Quick Sort
- Breadth-First Search (BFS)

## Setup

1. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install required packages:
   ```
   pip install flask
   ```

3. Run the application:
   ```
   python app.py
   ```

The server will start on http://127.0.0.1:5000/

## API Endpoints

### 1. Binary Search

**Endpoint:** `/api/binary-search`
**Method:** POST
**Payload:**
```json
{
  "array": [1, 3, 5, 7, 9, 11, 13],
  "target": 7
}
```
**Response:**
```json
{
  "status": "success",
  "original_array": [1, 3, 5, 7, 9, 11, 13],
  "sorted_array": [1, 3, 5, 7, 9, 11, 13],
  "target": 7,
  "found": true,
  "position": 3,
  "execution_time_ms": 0.123
}
```

### 2. Quick Sort

**Endpoint:** `/api/quick-sort`
**Method:** POST
**Payload:**
```json
{
  "array": [9, 3, 7, 1, 5, 13, 11]
}
```
**Response:**
```json
{
  "status": "success",
  "original_array": [9, 3, 7, 1, 5, 13, 11],
  "sorted_array": [1, 3, 5, 7, 9, 11, 13],
  "execution_time_ms": 0.456
}
```

### 3. Breadth-First Search (BFS)

**Endpoint:** `/api/bfs`
**Method:** POST
**Payload:**
```json
{
  "graph": {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
  },
  "start_node": "A"
}
```
**Response:**
```json
{
  "status": "success",
  "graph": {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
  },
  "start_node": "A",
  "traversal_path": ["A", "B", "C", "D", "E", "F"],
  "execution_time_ms": 0.789
}
```

## Logging

All API requests and responses are logged in two places:
1. Application logs: `logs/app.log`
2. Transaction logs: `logs/transactions.log`

Each log entry contains:
- Timestamp
- Algorithm used
- Request payload
- Response data
- Execution time (in milliseconds)