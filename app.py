from flask import Flask, jsonify, render_template_string
import os
import platform
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSC Rahti Demo Application</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        
        .header {
            background: #2c3e50;
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.2em;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        .content {
            padding: 30px;
        }
        
        .section {
            margin-bottom: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        
        .section h2 {
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 1.4em;
        }
        
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 10px;
        }
        
        .info-item {
            background: white;
            padding: 15px;
            border-radius: 6px;
            border: 1px solid #e9ecef;
        }
        
        .info-item strong {
            color: #2c3e50;
            display: block;
            margin-bottom: 5px;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }
        
        .feature {
            background: white;
            padding: 12px;
            border-radius: 6px;
            border: 1px solid #e9ecef;
        }
        
        .feature:before {
            content: "✓";
            color: #28a745;
            font-weight: bold;
            margin-right: 8px;
        }
        
        .api-section {
            text-align: center;
            background: #e8f4fd;
            border-left-color: #2196F3;
        }
        
        .api-button {
            display: inline-block;
            background: #2196F3;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 6px;
            font-weight: bold;
            margin-top: 10px;
            border: none;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .api-button:hover {
            background: #1976D2;
        }
        
        .links {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .link {
            color: #667eea;
            text-decoration: none;
            padding: 8px 16px;
            border: 1px solid #667eea;
            border-radius: 6px;
            transition: all 0.3s;
        }
        
        .link:hover {
            background: #667eea;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>CSC Rahti Demo Application</h1>
            <p>Welcome! This is a demo application for CSC's Rahti container platform.</p>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>System Information</h2>
                <div class="info-grid">
                    <div class="info-item">
                        <strong>Server:</strong> {{ server_hostname }}
                    </div>
                    <div class="info-item">
                        <strong>Platform:</strong> {{ platform_info }}
                    </div>
                    <div class="info-item">
                        <strong>Python Version:</strong> {{ python_version }}
                    </div>
                    <div class="info-item">
                        <strong>Timestamp:</strong> {{ current_time }}
                    </div>
                    <div class="info-item">
                        <strong>Port:</strong> {{ port }}
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>Rahti Features</h2>
                <div class="features">
                    <div class="feature">OpenShift/OKD-based platform</div>
                    <div class="feature">Automatic scaling</div>
                    <div class="feature">Rolling updates</div>
                    <div class="feature">Health checks</div>
                    <div class="feature">Persistent storage</div>
                    <div class="feature">Load balancing</div>
                    <div class="feature">HTTPS support</div>
                    <div class="feature">CI/CD integration</div>
                </div>
            </div>
            
            <div class="section api-section">
                <h2>API Demo</h2>
                <p>Test the application's API endpoint:</p>
                <div>
                    <button class="api-button" onclick="fetchAPI('/api/name')">Fetch API Data</button>
                </div>
                <div id="api-result" style="margin-top: 20px; padding: 15px; background: white; border-radius: 6px; min-height: 50px; text-align: left;">
                    <p style="color: #666; text-align: center;">API results will appear here...</p>
                </div>
            </div>
            
            <div class="section">
                <h2>Useful Links</h2>
                <div class="links">
                    <a href="/health" class="link">Health Check</a>
                    <a href="/api/info" class="link">System Information (JSON)</a>
                    <a href="/api/name" class="link">API Data Fetch</a>
                </div>
            </div>
        </div>
    </div>

    <script>
        async function fetchAPI(endpoint) {
            const resultDiv = document.getElementById('api-result');
            resultDiv.innerHTML = '<p style="color: #666;">Testing ' + endpoint + '...</p>';
            
            try {
                const response = await fetch(endpoint);
                const data = await response.json();
                
                resultDiv.innerHTML = `
                    <div style="color: #28a745;">
                        <h3>Success - ${endpoint}</h3>
                        <pre style="background: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto;">${JSON.stringify(data, null, 2)}</pre>
                    </div>
                `;
            } catch (error) {
                resultDiv.innerHTML = `
                    <div style="color: #dc3545;">
                        <h3>Error - ${endpoint}</h3>
                        <p>${error.message}</p>
                    </div>
                `;
            }
        }
    </script>
</body>
</html>
    ''', 
    server_hostname=socket.gethostname(),
    platform_info=platform.platform(),
    python_version=platform.python_version(),
    current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    port=os.environ.get('PORT', 8080)
    )

@app.route('/api/name')
def get_name():
    return jsonify({
        "name": "Ashish Nuniya",
        "course": "CSC Cloud Computing",
        "assignment": "Week 4",
        "timestamp": datetime.now().isoformat(),
        "server": socket.gethostname()
    })

@app.route('/api/info')
def get_info():
    return jsonify({
        "system_info": {
            "platform": platform.platform(),
            "python_version": platform.python_version(),
            "hostname": socket.gethostname()
        },
        "application": {
            "name": "CSC Rahti Demo",
            "student": "Ashish Nuniya",
            "status": "Running"
        },
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "CSC Rahti Demo Application",
        "student": "Ashish Nuniya",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)