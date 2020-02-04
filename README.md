# JSONPath demo

Demo of using [python-jsonpath-rw](https://github.com/kennknowles/python-jsonpath-rw) to access properties of an OpenAPI JSON object in [petstore.json](./petstore.json).

## Python demo

See [demo.py](./demo.py).

## Command-line examples

Get a single value at path `info.title`:

```bash
$ jsonpath.py 'info.title' petstore.json
Swagger Petstore
```

Get multiple values with `..` syntax:

```bash
$ jsonpath.py 'servers..url' petstore.json
http://petstore.swagger.io/v1
https://petstore.swagger.io/v1
```

Paths with special characters need to be escaped with single quotes:

```bash
$ jsonpath.py "paths.'/pets'" petstore.json
{'get': {'summary': 'List all pets', 'operationId': 'listPets', 'tags': ['pets'], 'parameters': [{'name': 'limit', 'in': 'query', 'description': 'How many items to return at one time (max 100)', 'required': False, 'schema': {'type': 'integer', 'format': 'int32'}}], 'responses': {'200': {'description': 'A paged array of pets', 'headers': {'x-next': {'description': 'A link to the next page of responses', 'schema': {'type': 'string'}}}, 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pets'}}}}, 'default': {'description': 'unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}}, 'post': {'summary': 'Create a pet', 'operationId': 'createPets', 'tags': ['pets'], 'responses': {'201': {'description': 'Null response'}, 'default': {'description': 'unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}}}
```

How to get a list of all operations (`['get', 'post']`) inside a given path? This is unfortunately not possible with pure JSONPath at the moment, as getting the keys of an object is [not supported](https://github.com/json-path/JsonPath/issues/439). Extracting the keys therefore requires extracting the keys from the full object in the client-side.

Get summaries of all operations in the OpenAPI specification:

```bash
$ jsonpath.py paths[*]..summary petstore.json
List all pets
Create a pet
Info for a specific pet
```
