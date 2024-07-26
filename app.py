from flask import Flask, send_file, render_template, request, jsonify
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topology', methods=['POST'])
def topology():
    try:
        branch_details = request.get_json()
        logging.debug(f"Received branch details: {branch_details}")
        img_base64 = base64.b64encode(img.read()).decode('utf-8')
        return jsonify(chart=img_base64)
    except Exception as e:
        logging.error(f"Error generating topology: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
