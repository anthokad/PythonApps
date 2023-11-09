from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'your_username'  # Change this to your desired username
app.config['BASIC_AUTH_PASSWORD'] = 'your_password'  # Change this to your desired password

basic_auth = BasicAuth(app)

@app.route('/hello', methods=['POST'])
@basic_auth.required
def hello():
    try:
        data = request.get_json()
        if 'persons' in data:
            persons = data['persons']
            response_data = []

            for person in persons:
                if 'name' in person and 'age' in person:
                    name = person['name']
                    age = person['age']
                    response_data.append({"message": f"Hello, {name}! You are {age} years old."})
                else:
                    return jsonify({"error": "Name or age not found in the person data"}), 400

            return jsonify(response_data)
        else:
            return jsonify({"error": "Persons array not found in JSON data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)