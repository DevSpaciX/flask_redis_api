from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(app, title='My Redis API', version='1.0', description='A simple Redis API', default_label='Redis routers',
          default='Redis', prefix='/redis')

redis_model = api.model('KeyValue', {
    'key': fields.String(required=True, description='The key'),
    'value': fields.String(required=True, description='The value')
})

store = {}


@api.route('/set')
class SetKey(Resource):
    @api.expect(redis_model)
    def post(self):
        """Set a key-value pair"""
        data = api.payload
        key = data['key']
        value = data['value']
        store[key] = value
        return {key: value}, 201


@api.route('/get/<string:key>')
class GetKey(Resource):
    def get(self, key):
        """Get the value for a given key"""
        if key in store:
            return {key: store[key]}
        api.abort(404, "Key not found")


@api.route('/exists/<string:key>')
class ExistsKey(Resource):
    def get(self, key):
        """Check if a key exists"""
        serialized_key = key
        return {'exists': serialized_key in store}


@api.route('/del/<string:key>')
class DelKey(Resource):
    def delete(self, key):
        """Delete a key"""
        if key in store:
            del store[key]
            return {'deleted': key}
        api.abort(404, "Key not found")


@api.route('/incrby/<string:key>/<string:increment>')
class IncrByKey(Resource):
    def post(self, key, increment):
        """Increment the value of a key by a given increment"""

        if key not in store:
            return api.abort(404, "Key not found")

        try:

            store[key] = increment
            return {key: increment}, 200
        except ValueError:
            return api.abort(400, "Current value is not an integer")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
