# IEL Checkpoint - External API Runtime & Basic CRUD

## Objective

Learn how Python backends communicate with external services, consume JSON APIs, traverse nested data structures, and combine persistence with HTTP endpoints.

---

## Completed

### HTTP Runtime

Understands:

```text
Browser
↓
HTTP Request
↓
Flask Runtime
↓
Route Lookup
↓
Callback Function
↓
Response
↓
Browser
```

Can use:

- Flask
- Route registration
- Route parameters
- GET requests
- Request inspection
- Response generation

---

### External API Runtime

Understands:

```text
Browser
↓
Flask
↓
External API
↓
Flask
↓
Browser
```

Can use:

- requests.get()
- Response objects
- status_code
- response.json()
- API consumption
- Error handling

Understands:

```python
response = requests.get(...)
```

creates an outbound HTTP request from Flask to another server.

---

### JSON Inspection

Can inspect unknown JSON structures using:

```python
print(data)
print(type(data))
```

Understands:

```text
Receive JSON
↓
Inspect Shape
↓
Understand Structure
```

---

### JSON Traversal

Can navigate nested structures such as:

```python
data["types"][0]["type"]["name"]
```

Understands traversal through:

```text
dict
↓
list
↓
dict
↓
dict
↓
value
```

Can identify:

- dict access
- list indexing
- nested traversal

---

### Runtime Type Awareness

Can distinguish:

```text
Response Object
≠
Python Dict

Dict
≠
List

List Index
≠
Business ID
```

Understands importance of:

```python
type(variable)
```

during debugging.

---

### Reusable Functions

Learned function extraction:

Before:

```python
requests.get(...)
response.json(...)
```

repeated across multiple routes.

After:

```python
def get_pokemon(name):
```

shared across endpoints.

Understands:

```text
Duplicate Logic
↓
Extraction
↓
Reusable Function
```

---

### Persistence Runtime

Can load and save JSON files.

Understands:

```text
Disk
↓
Load
↓
RAM
↓
Modify
↓
Save
↓
Disk
```

Can use:

- json.load()
- json.dump()
- with open()

---

### Basic CRUD

Implemented:

- Read users
- Add users
- Delete users

Understands:

```text
Load State
↓
Search
↓
Match
↓
Mutate
↓
Save State
```

Can perform:

- List traversal
- Dict access
- Conditional matching
- State mutation

---

### Projects Completed

#### IEL Project 01

```text
pokemon-api-proxy
```

Concepts:

- External API Runtime
- JSON Inspection
- JSON Traversal
- Reusable Functions

---

#### IEL Project 02

```text
quote-api
```

Concepts:

- Repeated API Consumption
- JSON Shape Recognition
- Runtime Generalization

---

#### IEL Project 03

```text
json-user-crud
```

Concepts:

- Persistence Runtime
- CRUD Operations
- State Mutation
- Search & Delete Logic

---

## Current Capability

Can build:

- Stateful terminal applications
- Persistent JSON systems
- Flask backends
- External API consumers
- Multi-endpoint applications
- Basic CRUD APIs

Can reason about:

```text
Browser
↓
Flask
↓
External Service
↓
JSON
↓
Python Objects
↓
Response
```

and

```text
Browser
↓
Flask
↓
JSON File
↓
State Mutation
↓
Persistence
```

---

## Next Node

POST Runtime

Goals:

- request.form
- request.json
- JSON body
- POST endpoints
- State creation via requests
- REST mental model

Target Runtime:

```text
Client
↓
POST
↓
Flask
↓
Validate
↓
Modify State
↓
Save
↓
Response
```