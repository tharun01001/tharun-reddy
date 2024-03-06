from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['jsondata']  # Change 'mydatabase' to your database name
collection = db['json']  # Change 'mycollection' to your collection name

# Define your API endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    # Query MongoDB collection for data
    data = list(collection.find({}, {"_id": 0 }))  # Exclude _id field
    return jsonify(data)

@app.route('/api/piedata', methods=['GET'])
def get_piedata():
    # Query MongoDB collection for data
    data = list(collection.find({}, {"topic":1,"intensity":1,"_id": 0 }))  # Exclude _id field
    return jsonify(data)

@app.route('/api/heatdata', methods=['GET'])
def get_heatdata():
    # Query MongoDB collection for data
    data = list(collection.find({}, {"start_year":1,"intensity":1,"_id": 0 }))  # Exclude _id field
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
