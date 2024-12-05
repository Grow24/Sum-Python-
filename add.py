from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/calculate', methods=['GET'])
def calculate_sum():
    data_type = request.args.get('dataType', '').lower()
    data_string = request.args.get('string', '')

    try:
        if data_type == 'single':
            # Parse the 'string' as a dictionary-like string
            params = eval(data_string)  # Use eval with caution; this assumes trusted input
            num1 = int(params.get('a', 0))
            num2 = int(params.get('b', 0))
            result = num1 + num2
            return jsonify({'sum': result})

        elif data_type == 'array':
            # Parse key-value pairs from the string
            params = {k: int(v) for k, v in [pair.split('=') for pair in data_string.split('&')]}
            num1 = params.get('a', 0)
            num2 = params.get('b', 0)
            result = num1 + num2
            return jsonify({'sum': result})

        elif data_type == 'json':
            # Parse JSON-like input from the string
            import json
            params = json.loads(data_string)
            num1 = int(params.get('a', 0))
            num2 = int(params.get('b', 0))
            result = num1 + num2
            return jsonify({'sum': result})

        elif data_type == 'object':
            # Similar to JSON; process the query string into a dictionary
            params = {k: int(v) for k, v in [pair.split('=') for pair in data_string.split('&')]}
            num1 = params.get('a', 0)
            num2 = params.get('b', 0)
            result = num1 + num2
            return jsonify({'sum': result})

        else:
            return jsonify({'error': 'Invalid dataType. Supported values: single, array, json, object.'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 400
        
if _name_ == '_main_':
    app.run(host='192.168.29.205', port=5000)