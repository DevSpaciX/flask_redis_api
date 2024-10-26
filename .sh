# Set key-value
curl -X POST http://localhost:5000/set -H "Content-Type: application/json" -d '{"key": "mykey", "value": "myvalue"}'

# Get key
curl http://localhost:5000/get/mykey

# Check existence
curl http://localhost:5000/exists/mykey

# Delete key
curl -X DELETE http://localhost:5000/del/mykey

# Increment key by value
curl -X POST http://localhost:5000/incrby -H "Content-Type: application/json" -d '{"key": "mykey", "increment": 5}'
