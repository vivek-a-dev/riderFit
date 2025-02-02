from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Sample route data (for simplicity, you could expand it to be dynamic)
routes_data = [
    {
        'id': 1,
        'name': 'Route 1',
        'accidents': random.randint(0, 5),
        'safety_level': random.choice(['High', 'Medium', 'Low']),
    },
    {
        'id': 2,
        'name': 'Route 2',
        'accidents': random.randint(0, 5),
        'safety_level': random.choice(['High', 'Medium', 'Low']),
    }
]

@app.route('/api/routes/<int:route_id>', methods=['GET'])
def get_route_info(route_id):
    route = next((r for r in routes_data if r['id'] == route_id), None)
    if route:
        return jsonify(route)
    return jsonify({'error': 'Route not found'}), 404

@app.route('/api/check-ride', methods=['POST'])
def check_ride():
    data = request.json
    response = {}

    if data['vehicle_type'] == 'two_wheeler':
        response['helmet'] = 'Are you wearing a helmet?'
        response['co_pilot'] = 'Do you have a co-pilot?'
    elif data['vehicle_type'] == 'four_wheeler':
        response['seatbelt'] = 'Are you wearing a seatbelt?'

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
