# My Redis API

A simple REST API built with Flask and Flask-RESTx that mimics basic Redis key-value operations. This API allows users to set, retrieve, check existence, delete, and increment values associated with keys.

## Features

- **Set a Key-Value Pair**: Add or update a value for a specified key.
- **Get the Value for a Key**: Retrieve the value associated with a given key.
- **Check if a Key Exists**: Verify if a particular key is present in the store.
- **Delete a Key**: Remove a key and its value from the store.
- **Increment Key Value**: Increment the integer value of a specified key.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/redis-api.git
   cd flask_redis_api
   ```

2. **Run the docker container

   ```bash
   docker build -t flask-redis-app .
   docker run -p 5001:5001 flask-redis-app
   ```

3. You can test the api via curl requests in .sh file : )

Documentation

<img width="1492" alt="image" src="https://github.com/user-attachments/assets/b13db75a-ad84-46b1-ab8a-52ca42572007">


