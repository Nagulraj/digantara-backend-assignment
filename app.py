from flask import Flask, request, jsonify
import json
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
import os

from algorithms import binary_search, quick_sort, bfs

app = Flask(__name__)

if not os.path.exists('logs'):
    os.makedirs('logs')

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10000, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

# Add handlers to Flask logger
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

# Ensure we don't use the default Flask logging handlers
app.logger.propagate = False

# Create a separate log file for transactions
def log_transaction(algorithm, request_data, response_data, execution_time=None):
    """
    Logs transaction details to a text file
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = {
        'timestamp': timestamp,
        'algorithm': algorithm,
        'request': request_data,
        'response': response_data,
        'execution_time_ms': execution_time
    }

    app.logger.info(f"API Call: {algorithm} - Input: {json.dumps(request_data)} - Response: {json.dumps(response_data)} - Time: {execution_time}ms")

    with open('logs/transactions.log', 'a') as log_file:
        log_file.write(f"[{timestamp}] {algorithm} API CALL\n")
        log_file.write(f"Input: {json.dumps(request_data)}\n")
        log_file.write(f"Output: {json.dumps(response_data)}\n")
        log_file.write(f"Execution Time: {execution_time}ms\n")
        log_file.write("-" * 80 + "\n")

@app.route('/binary-search', methods=['POST'])
@app.route('/api/binary-search', methods=['POST'])
def binary_search_api():
    data = request.get_json()

    if not data or 'array' not in data or 'target' not in data:
        error_response = {
            'status': 'error',
            'message': 'Missing required fields: array and target required'
        }
        log_transaction('binary_search', data, error_response)
        return jsonify(error_response), 400

    sorted_array = sorted(data['array'])
    start_time = datetime.now()
    result = binary_search(sorted_array, data['target'])
    execution_time = (datetime.now() - start_time).total_seconds() * 1000

    response = {
        'status': 'success',
        'original_array': data['array'],
        'sorted_array': sorted_array,
        'target': data['target'],
        'found': result != -1,
        'position': result if result != -1 else None,
        'execution_time_ms': execution_time
    }

    log_transaction('binary_search', data, response, execution_time)
    
    return jsonify(response)

@app.route('/quick-sort', methods=['POST'])
@app.route('/api/quick-sort', methods=['POST'])
def quick_sort_api():
    data = request.get_json()

    if not data or 'array' not in data:
        error_response = {
            'status': 'error',
            'message': 'Missing required field: array'
        }
        log_transaction('quick_sort', data, error_response)
        return jsonify(error_response), 400

    start_time = datetime.now()
    sorted_array = quick_sort(data['array'].copy())
    execution_time = (datetime.now() - start_time).total_seconds() * 1000

    response = {
        'status': 'success',
        'original_array': data['array'],
        'sorted_array': sorted_array,
        'execution_time_ms': execution_time
    }

    log_transaction('quick_sort', data, response, execution_time)
    
    return jsonify(response)

@app.route('/bfs', methods=['POST'])
@app.route('/api/bfs', methods=['POST'])
def bfs_api():
    data = request.get_json()

    if not data or 'graph' not in data or 'start_node' not in data:
        error_response = {
            'status': 'error',
            'message': 'Missing required fields: graph and start_node required'
        }
        log_transaction('bfs', data, error_response)
        return jsonify(error_response), 400

    start_time = datetime.now()
    traversal_result = bfs(data['graph'], data['start_node'])
    execution_time = (datetime.now() - start_time).total_seconds() * 1000

    response = {
        'status': 'success',
        'graph': data['graph'],
        'start_node': data['start_node'],
        'traversal_path': traversal_result,
        'execution_time_ms': execution_time
    }

    log_transaction('bfs', data, response, execution_time)
    
    return jsonify(response)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'online',
        'message': 'Algorithm API is running',
        'endpoints': [
            '/binary-search',
            '/quick-sort', 
            '/bfs',
            '/api/binary-search',
            '/api/quick-sort',
            '/api/bfs'
        ]
    })

if __name__ == '__main__':

    startup_message = "Algorithm API Service started"
    app.logger.info(startup_message)
    
    with open('logs/transactions.log', 'a') as log_file:
        log_file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {startup_message}\n")
        log_file.write("-" * 80 + "\n")
    
    app.run(debug=True)