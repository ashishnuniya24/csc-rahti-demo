from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! My name is Ashish Nuniya"

@app.route('/api/name')
def get_name():
    return jsonify({"name": "Ashish Nuniya"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)