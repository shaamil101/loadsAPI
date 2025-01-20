import csv
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/loads/<reference_number>', methods=['GET'])
def query(value):
    with open("loads.csv", mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['reference_number'] == value:
                return jsonify({"status": "success", "data": data[reference_number]}), 200
    return jsonify({"status": "error", "message": "Reference number not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)