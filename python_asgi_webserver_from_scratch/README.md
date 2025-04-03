### Start server
```
python -m kaza.main
```

### Send request
```
python kaza/client.py
```

### Curl request with JSON data payload
```
curl -X POST 'http://localhost:8000/greet' \
  --header 'Content-Type: application/json' \
  --data-raw '{"name": "Charlie", "age": 38}'
```

