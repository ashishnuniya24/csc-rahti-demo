from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>My Rahti App</title></head>
    <body>
        <h1>Welcome to My CSC Rahti Application</h1>
        <p><strong>Student:</strong> Ashish Nuniya</p>
        
        <h2>API Testing:</h2>
        <button onclick="getName()">Get My Name via API</button>
        <div id="result"></div>
        
        <h2>API Endpoints:</h2>
        <ul>
            <li><a href="/api/name">/api/name</a> - Returns my name</li>
            <li><a href="/api/data">/api/data</a> - Returns data</li>
            <li><a href="/health">/health</a> - Health check</li>
        </ul>

        <script>
            function getName() {
                fetch('/api/name')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('result').innerHTML = 
                            '<h3 style="color: green;">Name: ' + data.name + '</h3>';
                    });
            }
        </script>
    </body>
    </html>
    """

@app.route('/api/name')
def get_name():
    return jsonify({"name": "Ashish Nuniya"})

@app.route('/api/data')
def api_data():
    return jsonify({
        'message': 'Welcome!',
        'student': 'Ashish Nuniya',
        'course': 'CSC Cloud Computing'
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
