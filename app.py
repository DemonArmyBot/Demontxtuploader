from flask import Flask
import threading
import time
import requests
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello_world():
    logger.info("Received request to root endpoint")
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>SudoR2spr Repository</title>
    <link rel="icon" type="image/x-icon" href="https://tinypic.host/images/2025/02/07/DeWaterMark.ai_1738952933236-1.png" />
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

# Improved pinger with shorter interval and retry logic
def pinger(url, interval=300, retries=3):  # Ping every 5 minutes
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                logger.info(f"Pinged {url} successfully (status: {response.status_code})")
                break
            else:
                logger.warning(f"Ping to {url} returned status: {response.status_code}, attempt {attempt}/{retries}")
        except Exception as e:
            logger.error(f"Ping failed, attempt {attempt}/{retries}: {e}")
            if attempt == retries:
                logger.error(f"All {retries} ping attempts failed for {url}")
        time.sleep(5)  # Short delay between retries
    time.sleep(interval)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    
    # REPLACE WITH YOUR ACTUAL DEPLOYED URL
    deployed_url = 'https://demontxtuploader.onrender.com'  # e.g., https://sudosr2spr.onrender.com
    
    # Start pinger in a daemon thread
    threading.Thread(target=pinger, args=(deployed_url,), daemon=True).start()
    
    # Log startup
    logger.info(f"Starting Flask app on port {port}")
    
    # For local testing, use Flask dev server; Gunicorn will be used in production via Render
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False for stability