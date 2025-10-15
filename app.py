from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>SudoR2spr Repository</title>
    <link rel="icon" type="image/x-icon" href="https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png" />
    <style>
        body {
            background-color: #212529; /* bg-dark */
            color: #dc3545; /* text-red */
            font-family: monospace, monospace;
            text-align: center;
            padding-top: 50px;
        }
        .card {
            text-decoration: none;
            color: inherit;
            display: inline-block;
            padding: 20px;
            border: 1px solid #dc3545;
            border-radius: 8px;
            background-color: #2c3034;
            box-shadow: 0 0 10px #dc3545;
            white-space: pre; /* preserve whitespace if needed */
        }
        footer {
            margin-top: 100px;
            padding: 20px;
            background-color: #212529;
            color: white;
        }
        footer img {
            vertical-align: middle;
            margin: 0 10px;
            border-radius: 50%;
        }
    }
    </style>
</head>

<body>
    <a href="https://github.com/DemonArmyBot" class="card">
<pre>
▗▄▄▄ ▗▄▄▄▖▗▖  ▗▖ ▗▄▖ ▗▖  ▗▖ ▗▄▖ ▗▄▄▖ ▗▖  ▗▖▗▖  ▗▖
▐▌  █▐▌   ▐▛▚▞▜▌▐▌ ▐▌▐▛▚▖▐▌▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌ ▝▚▞▘ 
▐▌  █▐▛▀▀▘▐▌  ▐▌▐▌ ▐▌▐▌ ▝▜▌▐▛▀▜▌▐▛▀▚▖▐▌  ▐▌  ▐▌  
▐▙▄▄▀▐▙▄▄▖▐▌  ▐▌▝▚▄▞▘▐▌  ▐▌▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌  ▐▌

                <b>v2.0.0</b>
</pre>
    </a>

    <footer>
        <img loading="lazy" src="https://i.ibb.co/FkF67ZyP/devil-anime-girl.jpg" width="50" height="50" alt="Logo" />
        Powered By DemonArmy
        <img loading="lazy" src="https://i.ibb.co/FkF67ZyP/devil-anime-girl.jpg" width="50" height="50" alt="Logo" />
        <div class="footer__copyright">
            <p>© 2024 Video Downloader. All rights reserved.</p>
        </div>
    </footer>
</body>

</html>
"""

# Pinger function to prevent sleeping (e.g., on free hosts like Render or Railway)
def pinger(url, interval=600):  # Ping every 10 minutes
    while True:
        try:
            requests.get(url)
            print(f"Pinged {url} to keep alive.")
        except Exception as e:
            print(f"Ping failed: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    # Assuming this will be deployed on a platform like Render; get the port from env
    import os
    port = int(os.environ.get('PORT', 5000))
    
    # Start the pinger in a background thread
    # Replace 'https://your-app-name.onrender.com' with your actual deployed URL
    deployed_url = 'https://your-app-name.onrender.com'  # <<< UPDATE THIS!
    threading.Thread(target=pinger, args=(deployed_url,), daemon=True).start()
    
    app.run(host='0.0.0.0', port=port)