from flask import Flask, render_template_string
import os
import platform
import datetime
import shutil

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud Server &bull; Personal Storage</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 20px;
        }
        .card {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 14px;
            padding: 40px;
            max-width: 640px;
            width: 100%;
            box-shadow: 0 12px 35px rgba(0,0,0,0.6);
            text-align: center;
        }
        .badge {
            display: inline-block;
            background-color: #238636;
            color: #ffffff;
            font-weight: 600;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            margin-bottom: 20px;
            letter-spacing: 0.5px;
        }
        h1 {
            font-size: 2.1rem;
            color: #f0f6fc;
            margin-bottom: 12px;
        }
        p {
            color: #8b949e;
            line-height: 1.6;
            margin-bottom: 25px;
        }
        .btn-storage {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: linear-gradient(135deg, #1f6feb, #238636);
            color: #ffffff;
            font-weight: 600;
            font-size: 1.05rem;
            padding: 14px 28px;
            border-radius: 8px;
            text-decoration: none;
            transition: all 0.2s ease;
            box-shadow: 0 4px 15px rgba(31, 111, 235, 0.4);
            margin-bottom: 30px;
        }
        .btn-storage:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(31, 111, 235, 0.6);
            opacity: 0.95;
        }
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
            text-align: left;
            border-top: 1px solid #21262d;
            padding-top: 25px;
        }
        .info-item {
            background: #0d1117;
            padding: 14px 16px;
            border-radius: 8px;
            border: 1px solid #30363d;
        }
        .info-item span {
            font-size: 0.75rem;
            color: #8b949e;
            text-transform: uppercase;
            display: block;
            margin-bottom: 4px;
            letter-spacing: 0.5px;
        }
        .info-item strong {
            font-size: 0.95rem;
            color: #58a6ff;
            word-break: break-all;
        }
        .storage-card {
            grid-column: span 2;
            text-align: center;
            padding: 20px 16px !important;
            background: linear-gradient(180deg, rgba(35, 134, 54, 0.12) 0%, #0d1117 100%);
            border: 1px solid rgba(35, 134, 54, 0.45);
        }
        .storage-stat {
            color: #3fb950 !important;
            font-size: 1.0rem !important;
            font-weight: 800 !important;
            line-height: 1.1;
            display: block;
            margin-top: 6px;
            letter-spacing: -0.5px;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">&#x25CF; CLOUD SERVER ACTIVE</div>
        <h1>Personal Cloud Storage</h1>
        <p>Your headless Linux server is online, secure, and ready for file management and remote access.</p>
        
        <a href="http://192.168.1.226:8080" target="_blank" class="btn-storage">
            📁 Open File Manager
        </a>

        <div class="info-grid">
            <div class="info-item storage-card">
                <span>Free Cloud Storage</span>
                <strong class="storage-stat">{{ free_storage }} Free</strong>
            </div>
            <div class="info-item">
                <span>File Manager Port</span>
                <strong>8080 (FileBrowser)</strong>
            </div>
            <div class="info-item">
                <span>Hostname</span>
                <strong>{{ hostname }}</strong>
            </div>
            <div class="info-item">
                <span>Architecture</span>
                <strong>{{ arch }}</strong>
            </div>
            <div class="info-item">
                <span>Network Tunnel</span>
                <strong>Cloudflare Edge</strong>
            </div>
            <div class="info-item" style="grid-column: span 2;">
                <span>Server Time</span>
                <strong>{{ server_time }}</strong>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    total, used, free = shutil.disk_usage("/")
    free_gb = f"{free // (1024**3)} GB"
    return render_template_string(
        HTML_TEMPLATE,
        hostname=os.uname().nodename,
        arch=platform.machine(),
        free_storage=free_gb,
        server_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

