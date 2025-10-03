from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/api/name')
def get_name():
    return jsonify({"name": "Ashish Nuniya"})

if __name__ == '__main__':
    print("Starting test server...")
    app.run(host='0.0.0.0', port=5000, debug=True)