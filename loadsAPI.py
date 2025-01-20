import csv
import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/loads/', methods=['GET'])
def query():
    reference_number = request.args.get('reference_number')
    if not reference_number:
        return jsonify({"status": "error", "message": "Missing reference number"}), 400
    with open("loads.csv", mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['reference_number'].lower() == reference_number.lower():
                return jsonify({"status": "success", "data": row}), 200
    return jsonify({"status": "error", "message": "Reference number not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)