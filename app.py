from flask import Flask, render_template_string
import os
import platform
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloudflare Tunnel &bull; Flask Server</title>
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
            border-radius: 12px;
            padding: 40px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
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
            font-size: 2rem;
            color: #f0f6fc;
            margin-bottom: 12px;
        }
        p {
            color: #8b949e;
            line-height: 1.6;
            margin-bottom: 25px;
        }
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            text-align: left;
            margin-top: 25px;
            border-top: 1px solid #21262d;
            padding-top: 25px;
        }
        .info-item {
            background: #0d1117;
            padding: 12px 16px;
            border-radius: 8px;
            border: 1px solid #30363d;
        }
        .info-item span {
            font-size: 0.75rem;
            color: #8b949e;
            text-transform: uppercase;
            display: block;
            margin-bottom: 4px;
        }
        .info-item strong {
            font-size: 0.95rem;
            color: #58a6ff;
            word-break: break-all;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">&#x25CF; SYSTEM OPERATIONAL</div>
        <h1>Flask &times; Cloudflare Tunnel</h1>
        <p>Your headless Linux server is live and routing traffic securely through Cloudflare without open router ports.</p>
        
        <div class="info-grid">
            <div class="info-item">
                <span>Hostname</span>
                <strong>{{ hostname }}</strong>
            </div>
            <div class="info-item">
                <span>Architecture</span>
                <strong>{{ arch }}</strong>
            </div>
            <div class="info-item">
                <span>Environment</span>
                <strong>Docker &amp; Gunicorn</strong>
            </div>
            <div class="info-item">
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
    return render_template_string(
        HTML_TEMPLATE,
        hostname=os.uname().nodename,
        arch=platform.machine(),
        server_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
