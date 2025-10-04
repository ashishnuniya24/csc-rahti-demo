from flask import Flask, jsonify
from datetime import datetime
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Rahti App - Ashish Nuniya</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            .container {
                max-width: 1000px;
                margin: 0 auto;
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            }
            .header {
                text-align: center;
                margin-bottom: 40px;
            }
            h1 {
                color: #333;
                font-size: 2.5em;
                margin-bottom: 10px;
                background: linear-gradient(135deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .student-info {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 30px;
                border-left: 5px solid #667eea;
            }
            .api-section {
                background: #f8f9fa;
                padding: 25px;
                margin: 25px 0;
                border-radius: 10px;
                border: 1px solid #e9ecef;
            }
            button {
                padding: 12px 24px;
                margin: 10px 5px;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
                font-weight: 600;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
            .result {
                margin-top: 20px;
                padding: 15px;
                border-radius: 8px;
                background: white;
                border: 1px solid #dee2e6;
            }
            .endpoints {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 15px;
                margin-top: 15px;
            }
            .endpoint-card {
                background: white;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #e9ecef;
                text-align: center;
            }
            .endpoint-card a {
                color: #667eea;
                text-decoration: none;
                font-weight: 600;
            }
            .endpoint-card a:hover {
                text-decoration: underline;
            }
            .badge {
                display: inline-block;
                padding: 5px 10px;
                background: #28a745;
                color: white;
                border-radius: 20px;
                font-size: 0.8em;
                margin-left: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 CSC Rahti Application</h1>
                <p style="color: #666; font-size: 1.2em;">Cloud Computing - Week 4 Assignment</p>
            </div>

            <div class="student-info">
                <h2>👨‍🎓 Student Information</h2>
                <p><strong>Name:</strong> Ashish Nuniya</p>
                <p><strong>Course:</strong> CSC Cloud Computing</p>
                <p><strong>Assignment:</strong> Week 4 - Container Deployment</p>
                <p><strong>Platform:</strong> CSC Rahti OpenShift</p>
            </div>

            <div class="api-section">
                <h2>🔧 API Testing</h2>
                <p>Test the REST API endpoints:</p>
                <div>
                    <button onclick="testEndpoint('/api/name')">Test Name API</button>
                    <button onclick="testEndpoint('/api/info')">Test Info API</button>
                    <button onclick="testEndpoint('/health')">Test Health Check</button>
                </div>
                <div id="result" class="result">
                    <p style="color: #666; text-align: center;">Click a button to test API endpoints...</p>
                </div>
            </div>

            <div class="api-section">
                <h2>🌐 Available Endpoints</h2>
                <div class="endpoints">
                    <div class="endpoint-card">
                        <h3>Name API</h3>
                        <p><a href="/api/name" target="_blank">/api/name</a></p>
                        <p style="color: #666; font-size: 0.9em;">Returns student name as JSON</p>
                    </div>
                    <div class="endpoint-card">
                        <h3>Student Info</h3>
                        <p><a href="/api/info" target="_blank">/api/info</a></p>
                        <p style="color: #666; font-size: 0.9em;">Returns detailed student information</p>
                    </div>
                    <div class="endpoint-card">
                        <h3>Health Check</h3>
                        <p><a href="/health" target="_blank">/health</a></p>
                        <p style="color: #666; font-size: 0.9em;">Returns application health status</p>
                    </div>
                </div>
            </div>

            <div class="api-section">
                <h2>✅ Assignment Requirements</h2>
                <ul style="list-style: none; padding: 0;">
                    <li>✅ Deployed on CSC Rahti container platform</li>
                    <li>✅ REST API returning student name via /api/name</li>
                    <li>✅ Frontend with interactive API testing</li>
                    <li>✅ Personalized application with student information</li>
                    <li>✅ Git repository with source code</li>
                </ul>
            </div>
        </div>

        <script>
            async function testEndpoint(endpoint) {
                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = '<p style="color: #666;">Testing ' + endpoint + '...</p>';
                
                try {
                    const response = await fetch(endpoint);
                    const data = await response.json();
                    
                    resultDiv.innerHTML = `
                        <div style="color: #28a745;">
                            <h3>✅ Success - ${endpoint}</h3>
                            <pre style="background: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto;">${JSON.stringify(data, null, 2)}</pre>
                        </div>
                    `;
                } catch (error) {
                    resultDiv.innerHTML = `
                        <div style="color: #dc3545;">
                            <h3>❌ Error - ${endpoint}</h3>
                            <p>${error.message}</p>
                        </div>
                    `;
                }
            }
        </script>
    </body>
    </html>
    """

@app.route('/api/name')
def get_name():
    return jsonify({
        "name": "Ashish Nuniya",
        "timestamp": datetime.now().isoformat(),
        "endpoint": "/api/name"
    })

@app.route('/api/info')
def get_info():
    return jsonify({
        "student": {
            "name": "Ashish Nuniya",
            "course": "CSC Cloud Computing",
            "assignment": "Week 4 - Container Deployment"
        },
        "application": {
            "platform": "CSC Rahti OpenShift",
            "status": "Running",
            "hostname": socket.gethostname()
        },
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "CSC Rahti Demo Application",
        "student": "Ashish Nuniya",
        "timestamp": datetime.now().isoformat(),
        "uptime": "Running smoothly"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)