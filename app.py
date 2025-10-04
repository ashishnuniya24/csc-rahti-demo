#!/usr/bin/env python3
from flask import Flask, jsonify
import os
import logging
import socket
import platform
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Rahti App - Ashish Nuniya</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f0f2f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #3366cc; text-align: center; }
            button { padding: 12px 24px; margin: 10px; background: #3366cc; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
            button:hover { background: #254e9e; }
            .api-section { background: #f8f9fa; padding: 20px; margin: 20px 0; border-radius: 8px; border-left: 4px solid #3366cc; }
            .success { color: #28a745; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 My CSC Rahti Application</h1>
            <p><strong>Student:</strong> Ashish Nuniya</p>
            <p><strong>Course:</strong> CSC Cloud Computing - Week 4 Assignment</p>
            
            <div class="api-section">
                <h2>🎯 Assignment Requirements</h2>
                <ul>
                    <li>✅ Deployed on CSC Rahti</li>
                    <li>✅ REST API returning student name</li>
                    <li>✅ Frontend with API link</li>
                    <li>✅ Personalized application</li>
                </ul>
            </div>

            <div class="api-section">
                <h2>🔧 API Testing</h2>
                <button onclick="getName()">Test Name API</button>
                <button onclick="getInfo()">Test Info API</button>
                <div id="result" style="margin-top: 15px;"></div>
            </div>

            <div class="api-section">
                <h2>🌐 API Endpoints</h2>
                <ul>
                    <li><a href="/api/name" target="_blank">/api/name</a> - Returns my name as JSON</li>
                    <li><a href="/api/data" target="_blank">/api/data</a> - Returns sample data</li>
                    <li><a href="/health" target="_blank">/health</a> - Health check</li>
                </ul>
            </div>
        </div>

        <script>
            function getName() {
                fetch('/api/name')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('result').innerHTML = 
                            `<p class="success">✅ Name from API: <strong>${data.name}</strong></p>`;
                    })
                    .catch(error => {
                        document.getElementById('result').innerHTML = 
                            `<p style="color: red;">❌ Error fetching name: ${error}</p>`;
                    });
            }

            function getInfo() {
                fetch('/api/data')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('result').innerHTML = 
                            `<p class="success">✅ Data API Response:</p>
                             <pre>${JSON.stringify(data, null, 2)}</pre>`;
                    })
                    .catch(error => {
                        document.getElementById('result').innerHTML = 
                            `<p style="color: red;">❌ Error fetching data: ${error}</p>`;
                    });
            }
        </script>
    </body>
    </html>
    """

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'hostname': socket.gethostname()
    })

@app.route('/api/data')
def api_data():
    data = {
        'message': 'Welcome to CSC Rahti Demo Application!',
        'student': 'Ashish Nuniya',
        'data': [
            {'id': 1, 'name': 'First Item', 'value': 42},
            {'id': 2, 'name': 'Second Item', 'value': 84},
            {'id': 3, 'name': 'Third Item', 'value': 126}
        ],
        'timestamp': datetime.now().isoformat(),
        'server': socket.gethostname()
    }
    return jsonify(data)

@app.route('/api/name')
def get_name():
    return jsonify({"name": "Ashish Nuniya"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    logger.info(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port)